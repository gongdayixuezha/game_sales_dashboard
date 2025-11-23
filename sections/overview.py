import streamlit as st
import plotly.express as px
import pandas as pd
from utils.lang import get_text

def show_overview(tables):
    df_clean = st.session_state.get("df_clean")
    selected_decade = st.session_state.get("selected_decade", ["1990", "2000", "2010"])
    
    # ---------------------- 核心修复1：数据校验与字段名兼容 ----------------------
    # 1. 确保df_clean存在且非空
    if df_clean is None or len(df_clean) == 0:
        st.warning("⚠️ 未获取到有效数据，请检查数据集是否正确加载")
        return
    
    # 2. 兼容常见字段名（用户可根据实际数据集修改，这里覆盖主流格式）
    # 定义字段名映射（key：目标字段，value：可能的实际字段名列表）
    field_mapping = {
        "global_sales": ["Global_Sales", "global_sales", "Global Sales", "global sales"],
        "na_sales": ["NA_Sales", "na_sales", "North_America_Sales", "north_america_sales", "NA Sales"],
        "eu_sales": ["EU_Sales", "eu_sales", "Europe_Sales", "europe_sales", "EU Sales"],
        "jp_sales": ["JP_Sales", "jp_sales", "Japan_Sales", "japan_sales", "JP Sales"],
        "year": ["Year", "year", "Release_Year", "release_year"],
        "platform": ["Platform", "platform"],
        "genre": ["Genre", "genre"],
        "publisher": ["Publisher", "publisher"]
    }
    
    # 匹配实际字段名（返回第一个存在的字段名，无则返回None）
    def get_actual_field(df, target_fields):
        for field in target_fields:
            if field in df.columns:
                return field
        return None
    
    # 校验关键字段是否存在
    global_sales_field = get_actual_field(df_clean, field_mapping["global_sales"])
    na_sales_field = get_actual_field(df_clean, field_mapping["na_sales"])
    eu_sales_field = get_actual_field(df_clean, field_mapping["eu_sales"])
    jp_sales_field = get_actual_field(df_clean, field_mapping["jp_sales"])
    year_field = get_actual_field(df_clean, field_mapping["year"])
    
    # 若关键字段缺失，提示用户
    missing_fields = []
    if not global_sales_field:
        missing_fields.append("全球销售额字段（如 Global_Sales）")
    if not na_sales_field:
        missing_fields.append("北美销售额字段（如 NA_Sales）")
    if not eu_sales_field:
        missing_fields.append("欧洲销售额字段（如 EU_Sales）")
    if not jp_sales_field:
        missing_fields.append("日本销售额字段（如 JP_Sales）")
    if not year_field:
        missing_fields.append("年份字段（如 Year）")
    
    if missing_fields:
        st.error(f"⚠️ 数据集缺少关键字段：{', '.join(missing_fields)}，请检查数据集格式或修改代码中的字段名映射")
        return
    
    # ---------------------- 核心修复2：简化筛选逻辑（用Year直接筛选，不依赖Decade） ----------------------
    # 转换Year字段为整数，过滤无效值
    df_clean[year_field] = pd.to_numeric(df_clean[year_field], errors="coerce")  # 非数值转为NaN
    df_valid = df_clean.dropna(subset=[year_field, global_sales_field])  # 过滤年份和销售额为空的记录
    df_valid = df_valid[df_valid[global_sales_field] > 0]  # 过滤销售额为0的记录
    
    # 将selected_decade（如["1990", "2000"]）转为年份范围（1990-1999，2000-2009）
    year_ranges = []
    for decade in selected_decade:
        if decade.isdigit() and len(decade) == 4:
            start_year = int(decade)
            end_year = start_year + 9
            year_ranges.append((start_year, end_year))
    
    # 筛选年份在选中年代范围内的数据
    if year_ranges:
        mask = pd.Series(False, index=df_valid.index)
        for start, end in year_ranges:
            mask |= (df_valid[year_field] >= start) & (df_valid[year_field] <= end)
        filtered_df = df_valid[mask]
    else:
        filtered_df = df_valid  # 若年代筛选无效，使用全量有效数据
    
    # 调试输出（帮助用户确认筛选结果，可后续删除）
    st.write(f"📊 调试信息：有效数据总行数={len(df_valid)}，筛选后行数={len(filtered_df)}")
    st.write(f"字段名映射：全球销售额={global_sales_field}，北美={na_sales_field}，欧洲={eu_sales_field}，日本={jp_sales_field}")
    st.write(f"年代筛选范围：{year_ranges}")
    
    # ---------------------- 核心修复3：重新计算指标（确保字段名正确） ----------------------
    # 核心指标（基于筛选后的有效数据）
    total_sales = filtered_df[global_sales_field].sum() if len(filtered_df) > 0 else 0
    total_games = len(filtered_df) if len(filtered_df) > 0 else 0
    active_platforms = filtered_df[get_actual_field(df_clean, field_mapping["platform"])].nunique() if len(filtered_df) > 0 else 0
    
    # 地区销售额（使用匹配到的字段名）
    na_sales = filtered_df[na_sales_field].sum() if len(filtered_df) > 0 else 0
    eu_sales = filtered_df[eu_sales_field].sum() if len(filtered_df) > 0 else 0
    jp_sales = filtered_df[jp_sales_field].sum() if len(filtered_df) > 0 else 0
    other_sales = total_sales - na_sales - eu_sales - jp_sales  # 其他地区=全球-三大地区
    other_sales = max(other_sales, 0)  # 避免负数（数据误差）
    
    # 地区占比（避免除0错误）
    na_sales_pct = (na_sales / total_sales * 100) if total_sales > 0 else 0
    eu_sales_pct = (eu_sales / total_sales * 100) if total_sales > 0 else 0
    jp_sales_pct = (jp_sales / total_sales * 100) if total_sales > 0 else 0
    other_sales_pct = (other_sales / total_sales * 100) if total_sales > 0 else 0
    
    # 头部发行商和热门类型
    publisher_field = get_actual_field(df_clean, field_mapping["publisher"])
    genre_field = get_actual_field(df_clean, field_mapping["genre"])
    
    if len(filtered_df) > 0:
        # 头部发行商
        top_publisher = filtered_df.groupby(publisher_field)[global_sales_field].sum().nlargest(1).index[0]
        top_publisher_sales = filtered_df.groupby(publisher_field)[global_sales_field].sum().nlargest(1).values[0]
        # 热门类型
        top_genre = filtered_df.groupby(genre_field)[global_sales_field].sum().nlargest(1).index[0]
        top_genre_sales = filtered_df.groupby(genre_field)[global_sales_field].sum().nlargest(1).values[0]
    else:
        top_publisher = "N/A"
        top_publisher_sales = 0
        top_genre = "N/A"
        top_genre_sales = 0
    
    # 近5年增长率（动态指标）
    growth_delta = "无数据"
    growth_color = "gray"
    if len(filtered_df) > 0:
        recent_years = filtered_df.dropna(subset=[year_field])
        if len(recent_years) >= 5:
            yearly_sales = recent_years.groupby(year_field)[global_sales_field].sum().reset_index()
            yearly_sales = yearly_sales.sort_values(year_field)
            last_5_years = yearly_sales.tail(5)
            if last_5_years.iloc[0][global_sales_field] > 0:
                growth_rate = ((last_5_years.iloc[-1][global_sales_field] - last_5_years.iloc[0][global_sales_field]) / last_5_years.iloc[0][global_sales_field]) * 100
                growth_delta = f"{growth_rate:.1f}%"
                growth_color = "green" if growth_rate > 0 else "red"
    
    # ---------------------- 页面渲染（保持原有样式，仅替换变量） ----------------------
    # 第一行：核心KPI（4列）
    st.markdown(f"<div class='section-title'>{get_text('core_kpi_title')}</div>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class='kpi-card' style='border-left-color: #3498db;'>
            <h5 style='margin: 0; color: #666;'>{get_text('total_global_sales')}</h5>
            <h2 style='margin: 10px 0; color: #3498db;'>{total_sales:.2f}M</h2>
            <p style='margin: 0; color: {growth_color};'>{growth_delta} {get_text('vs_5y_ago')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='kpi-card' style='border-left-color: #e74c3c;'>
            <h5 style='margin: 0; color: #666;'>{get_text('total_games')}</h5>
            <h2 style='margin: 10px 0; color: #e74c3c;'>{total_games:,}</h2>
            <p style='margin: 0; color: #666;'>{get_text('active_platforms')}：{active_platforms}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='kpi-card' style='border-left-color: #2ecc71;'>
            <h5 style='margin: 0; color: #666;'>{get_text('top_publisher')}</h5>
            <h4 style='margin: 10px 0; color: #2ecc71;'>{top_publisher}</h4>
            <p style='margin: 0; color: #666;'>{get_text('sales')}：{top_publisher_sales:.2f}M</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='kpi-card' style='border-left-color: #f39c12;'>
            <h5 style='margin: 0; color: #666;'>{get_text('top_genre')}</h5>
            <h4 style='margin: 10px 0; color: #f39c12;'>{top_genre}</h4>
            <p style='margin: 0; color: #666;'>{get_text('sales')}：{top_genre_sales:.2f}M</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 第二行：区域占比 + 近期趋势（2列）
    st.markdown(f"<div class='section-title'>{get_text('region_trend_title')}</div>", unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    
    with col5:
        # 地区销售占比（确保有数据的地区才显示）
        region_data = pd.DataFrame({
            "区域": [get_text("North America"), get_text("Europe"), get_text("Japan"), get_text("Other")],
            "销售额占比": [na_sales_pct, eu_sales_pct, jp_sales_pct, other_sales_pct],
            "销售额（M）": [na_sales, eu_sales, jp_sales, other_sales],
            "颜色": ["#3498db", "#e74c3c", "#2ecc71", "#9b59b6"]
        })
        # 过滤占比小于0.1%的地区（避免图表杂乱）
        region_data = region_data[region_data["销售额占比"] >= 0.1]
        
        fig_region = px.pie(
            region_data,
            values="销售额占比",
            names="区域",
            color="颜色",
            color_discrete_map=dict(zip(region_data["区域"], region_data["颜色"])),
            title=get_text("regional_sales_share"),
            hole=0.4  # 环形图
        )
        fig_region.update_traces(
            hoverinfo="label+percent+value",
            textinfo="label+percent",
            textfont_size=12
        )
        st.plotly_chart(fig_region, width='stretch')
    
    with col6:
        # 近10年销售趋势
        if len(filtered_df) > 0:
            recent_10y_df = filtered_df.dropna(subset=[year_field])
            if len(recent_10y_df) > 0:
                recent_10y = recent_10y_df.groupby(year_field)[global_sales_field].sum().reset_index()
                recent_10y = recent_10y.nlargest(10, year_field).sort_values(year_field)  # 取最近10年
                fig_trend = px.line(
                    recent_10y,
                    x=year_field,
                    y=global_sales_field,
                    title=get_text("recent_10y_trend"),
                    labels={global_sales_field: get_text("sales_million")},
                    color_discrete_sequence=["#3498db"],
                    markers=True
                )
                fig_trend.update_layout(
                    height=300,
                    xaxis_title=get_text("year"),
                    yaxis_title=get_text("sales_million"),
                    hovermode="x unified"
                )
                st.plotly_chart(fig_trend, width='stretch')
            else:
                st.info(get_text("no_data_in_range"))
        else:
            st.info(get_text("no_data_warning"))
    
    # 第三行：Top类型 + Top平台（2列）
    st.markdown(f"<div class='section-title'>{get_text('top_ranking_title')}</div>", unsafe_allow_html=True)
    col7, col8 = st.columns(2)
    
    with col7:
        # Top5游戏类型
        if len(filtered_df) > 0:
            top5_genre = filtered_df.groupby(genre_field)[global_sales_field].sum().nlargest(5).reset_index()
            top5_genre.rename(columns={genre_field: get_text("genre"), global_sales_field: get_text("sales_million")}, inplace=True)
            fig_genre = px.bar(
                top5_genre,
                y=get_text("genre"),
                x=get_text("sales_million"),
                orientation="h",
                title=get_text("top5_genre_sales"),
                color_discrete_sequence=["#f39c12"]
            )
            fig_genre.update_layout(height=300)
            st.plotly_chart(fig_genre, width='stretch')
        else:
            st.info(get_text("no_data_warning"))
    
    with col8:
        # Top5平台
        if len(filtered_df) > 0:
            platform_field = get_actual_field(df_clean, field_mapping["platform"])
            top5_platform = filtered_df.groupby(platform_field)[global_sales_field].sum().nlargest(5).reset_index()
            top5_platform.rename(columns={platform_field: get_text("platform"), global_sales_field: get_text("sales_million")}, inplace=True)
            fig_platform = px.bar(
                top5_platform,
                y=get_text("platform"),
                x=get_text("sales_million"),
                orientation="h",
                title=get_text("top5_platform_sales"),
                color_discrete_sequence=["#9b59b6"]
            )
            fig_platform.update_layout(height=300)
            st.plotly_chart(fig_platform, width='stretch')
        else:
            st.info(get_text("no_data_warning"))
    
    # 数据质量提示（折叠面板）
    with st.expander(get_text("data_quality_detail"), expanded=False):
        data_quality = tables.get("data_quality", {})
        st.markdown(f"""
        <div class='card'>
            <p>• {get_text('original_records')}：{data_quality.get('Total_Records', 'N/A')}</p>
            <p>• {get_text('cleaned_records')}：{data_quality.get('Cleaned_Records', 'N/A')}</p>
            <p>• {get_text('missing_year_pct')}：{data_quality.get('Missing_Year_Pct', 'N/A')}</p>
            <p>• {get_text('duplicate_records')}：{data_quality.get('Duplicate_Records', 'N/A')}</p>
            <p>• {get_text('max_sales_single')}：{data_quality.get('Max_Global_Sales', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)