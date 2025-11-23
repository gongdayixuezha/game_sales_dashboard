import streamlit as st
import pandas as pd 
from utils.viz import (
    line_chart_timeseries, bar_chart_region_genre, bar_chart_publisher,
    altair_platform_small_multiples, heatmap_genre_platform,
    histogram_sales_distribution, top_games_table,
    stacked_area_chart, scatter_game_count_vs_avg_sales,  # 新增图表
    radar_chart_top_publishers, bubble_chart_genre_year   # 新增图表
)
from utils.lang import get_text

def show_deep_dives(tables):
    # 直接使用清洗后的完整数据集，避免依赖tables中的timeseries
    df_clean = st.session_state.get("df_clean")
    selected_decade = st.session_state.get("selected_decade", ["1990", "2000", "2010"])
    unknown_text = get_text("Unknown")
    
    # 筛选年代数据（统一基于df_clean，避免多重过滤）
    if unknown_text not in selected_decade and "Unknown" not in selected_decade:
        filtered_df_clean = df_clean[df_clean["Decade"].isin(selected_decade)]
    else:
        filtered_df_clean = df_clean
    
    # 过滤有效数据（移除Year为空、销售额为0的记录）
    filtered_df_clean = filtered_df_clean.dropna(subset=["Year"])
    filtered_df_clean = filtered_df_clean[filtered_df_clean["Global_Sales"] > 0]
    filtered_df_clean["Year"] = filtered_df_clean["Year"].astype(int)
    
    # ---------------------- 1. 时间趋势分析----------------------
    st.markdown(f"<div class='section-title'>{get_text('time_trend_title')}</div>", unsafe_allow_html=True)
    
    with st.container():
        # 异常处理：如果筛选后无数据，显示提示
        if len(filtered_df_clean) == 0:
            st.warning(get_text("no_data_warning"))
        else:
            # 基于筛选后的完整数据重新生成时间序列（避免依赖tables["timeseries"]）
            timeseries_data = filtered_df_clean.groupby("Year").agg(
                Global_Sales=("Global_Sales", "sum"),
                Game_Count=("Name", "count")
            ).reset_index().sort_values("Year")
            
            col1, col2 = st.columns([3, 1])
            with col1:
                min_year = timeseries_data["Year"].min()
                max_year = timeseries_data["Year"].max()
                
                # 安全默认值（确保在有效范围内）
                default_start = max(1990, min_year)
                default_end = min(2010, max_year)
                if default_start > default_end:
                    default_start, default_end = min_year, max_year
                
                year_range = st.slider(
                    get_text("select_year_range"),
                    min_value=int(min_year),
                    max_value=int(max_year),
                    value=(default_start, default_end),
                    key="year_slider"
                )
                # 按滑块筛选时间范围
                filtered_timeseries_range = timeseries_data[
                    (timeseries_data["Year"] >= year_range[0]) & (timeseries_data["Year"] <= year_range[1])
                ]
            with col2:
                st.markdown("<div class='filter-container'>", unsafe_allow_html=True)
                st.markdown(f"<h5>{get_text('display_options')}</h5>", unsafe_allow_html=True)
                show_sales = st.checkbox(get_text("show_sales"), value=True)
                show_count = st.checkbox(get_text("show_count"), value=True)
                st.markdown("</div>", unsafe_allow_html=True)
            
            # 显示时间趋势图
            if len(filtered_timeseries_range) == 0:
                st.info(get_text("no_data_in_range"))
            else:
                fig_trend = line_chart_timeseries(filtered_timeseries_range)
                if not show_sales:
                    fig_trend.data[0].visible = False
                if not show_count:
                    fig_trend.data[1].visible = False
                st.plotly_chart(fig_trend, width='stretch')
        
        st.markdown(f"<div class='section-title'>{get_text('regional_sales_trend')}</div>", unsafe_allow_html=True)
        if len(filtered_df_clean) > 0:
            fig_area = stacked_area_chart(filtered_df_clean)
            st.plotly_chart(fig_area, width='stretch')
        else:
            st.info(get_text("no_data_warning"))
    
    # ---------------------- 2. 区域偏好分析 ----------------------
    st.markdown(f"<div class='section-title'>{get_text('region_preference_title')}</div>", unsafe_allow_html=True)
    with st.container():
        regions = st.multiselect(
            get_text("select_regions"),
            ["North America", "Europe", "Japan"],
            default=["North America", "Europe", "Japan"],
            key="region_multiselect"
        )
        # 生成区域-类型数据（基于筛选后的df_clean）
        region_genre_data = []
        for region in regions:
            if region == "North America":
                genre_sales = filtered_df_clean.groupby(["Genre", "Decade"])["NA_Sales"].sum().reset_index()
            elif region == "Europe":
                genre_sales = filtered_df_clean.groupby(["Genre", "Decade"])["EU_Sales"].sum().reset_index()
            elif region == "Japan":
                genre_sales = filtered_df_clean.groupby(["Genre", "Decade"])["JP_Sales"].sum().reset_index()
            else:
                continue
            genre_sales["Region"] = region
            genre_sales.rename(columns={genre_sales.columns[2]: "Sales"}, inplace=True)
            region_genre_data.append(genre_sales)
        
        if region_genre_data:
            region_genre_combined = pd.concat(region_genre_data, ignore_index=True)
            st.plotly_chart(bar_chart_region_genre(region_genre_combined, regions), width='stretch')
        else:
            st.info(get_text("no_region_data"))
    
    # ---------------------- 3. 发行商排名分析 ----------------------
    st.markdown(f"<div class='section-title'>{get_text('publisher_competition_title')}</div>", unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            top_n = st.slider(
                get_text("select_topn_publisher"),
                min_value=5,
                max_value=30,
                value=20,
                step=5,
                key="publisher_topn_slider"
            )
            # 基于筛选后的df_clean重新计算发行商排名
            publisher_rank = filtered_df_clean.groupby("Publisher").agg(
                Global_Sales=("Global_Sales", "sum"),
                Game_Count=("Name", "count")
            ).reset_index().sort_values("Global_Sales", ascending=False)
            filtered_publisher = publisher_rank.head(top_n)
        with col2:
            if len(filtered_publisher) == 0:
                st.info(get_text("no_publisher_data"))
            else:
                st.plotly_chart(bar_chart_publisher(filtered_publisher), width='stretch')
        
        # 新增：Top3发行商雷达图
        st.markdown(f"<div class='section-title'>{get_text('top3_publisher_region_performance')}</div>", unsafe_allow_html=True)
        radar_fig = radar_chart_top_publishers(filtered_df_clean)
        if radar_fig:
            st.plotly_chart(radar_fig, width='stretch')
        else:
            st.info(get_text("no_data_for_heatmap"))
    
    # ---------------------- 4. 类型-平台热力图 ----------------------
    st.markdown(f"<div class='section-title'>{get_text('genre_platform_title')}</div>", unsafe_allow_html=True)
    if len(filtered_df_clean) == 0:
        st.info(get_text("no_data_for_heatmap"))
    else:
        st.plotly_chart(heatmap_genre_platform(filtered_df_clean, selected_decade), width='stretch')
    
    # ---------------------- 5. 销售额分布直方图 ----------------------
    st.markdown(f"<div class='section-title'>{get_text('sales_distribution_title')}</div>", unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            bin_count = st.slider(
                get_text("adjust_bin_count"),
                min_value=10,
                max_value=50,
                value=30,
                step=5,
                key="bin_slider"
            )
        with col2:
            sales_data_valid = filtered_df_clean[filtered_df_clean["Global_Sales"] > 0]
            if len(sales_data_valid) == 0:
                st.info(get_text("no_valid_sales_data"))
            else:
                st.plotly_chart(histogram_sales_distribution(sales_data_valid, bin_count), width='stretch')
    
    # ---------------------- 6. Top游戏交互式表格 ----------------------
    st.markdown(f"<div class='section-title'>{get_text('top_games_detail_title')}</div>", unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            top_n_games = st.slider(
                get_text("select_topn_games"),
                min_value=10,
                max_value=50,
                value=20,
                step=10,
                key="games_topn_slider"
            )
        with col2:
            if len(filtered_df_clean) == 0:
                st.info(get_text("no_game_data"))
            else:
                top_games = top_games_table(filtered_df_clean, top_n_games)
                st.dataframe(
                    top_games,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        get_text("table_global_sales"): st.column_config.NumberColumn(format="%.2f"),
                        get_text("table_na_sales"): st.column_config.NumberColumn(format="%.2f"),
                        get_text("table_eu_sales"): st.column_config.NumberColumn(format="%.2f"),
                        get_text("table_jp_sales"): st.column_config.NumberColumn(format="%.2f")
                    }
                )
    
    # ---------------------- 7. 平台演变小多图 ----------------------
    st.markdown(f"<div class='section-title'>{get_text('platform_evolution_title')}</div>", unsafe_allow_html=True)
    platform_sales_valid = filtered_df_clean.groupby(["Platform", "Decade"])["Global_Sales"].sum().reset_index()
    platform_sales_valid = platform_sales_valid[platform_sales_valid["Decade"] != unknown_text]
    if len(platform_sales_valid) == 0:
        st.info(get_text("no_platform_data"))
    else:
        st.altair_chart(altair_platform_small_multiples(platform_sales_valid), width='stretch')
    
    # ---------------------- 新增8：散点图（游戏数量vs平均销售额）----------------------
    st.markdown(f"<div class='section-title'>{get_text('genre_game_count_vs_avg_sales')}</div>", unsafe_allow_html=True)
    if len(filtered_df_clean) > 0:
        scatter_fig = scatter_game_count_vs_avg_sales(filtered_df_clean)
        st.plotly_chart(scatter_fig, width='stretch')
    else:
        st.info(get_text("no_data_warning"))
    
    # ---------------------- 新增9：动态气泡图（类型-年份-销售额）----------------------
    st.markdown(f"<div class='section-title'>{get_text('genre_year_sales_bubble_chart')}</div>", unsafe_allow_html=True)
    if len(filtered_df_clean) > 0:
        bubble_fig = bubble_chart_genre_year(filtered_df_clean)
        st.plotly_chart(bubble_fig, width='stretch')
    else:
        st.info(get_text("no_data_warning"))