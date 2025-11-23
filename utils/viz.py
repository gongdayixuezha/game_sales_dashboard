import plotly.express as px
import plotly.graph_objects as go
import altair as alt
import streamlit as st
import pandas as pd
from utils.lang import get_text

# 新增1：堆叠面积图（各地区销售额趋势）
def stacked_area_chart(df):
    """各地区销售额堆叠面积图（显示区域占比趋势）"""
    # 按年份和地区分组
    yearly_region = df.groupby("Year").agg(
        NA_Sales=("NA_Sales", "sum"),
        EU_Sales=("EU_Sales", "sum"),
        JP_Sales=("JP_Sales", "sum"),
        Other_Sales=("Global_Sales", lambda x: x.sum() - df.loc[x.index, "NA_Sales"].sum() - df.loc[x.index, "EU_Sales"].sum() - df.loc[x.index, "JP_Sales"].sum())
    ).reset_index()
    yearly_region = yearly_region.sort_values("Year")
    
    fig = go.Figure()
    # 北美
    fig.add_trace(go.Scatter(
        x=yearly_region["Year"], y=yearly_region["NA_Sales"],
        name=get_text("North America"), stackgroup="one", mode="lines",
        line=dict(width=0.5), fill='tozeroy', fillcolor="#3498db"
    ))
    # 欧洲
    fig.add_trace(go.Scatter(
        x=yearly_region["Year"], y=yearly_region["EU_Sales"],
        name=get_text("Europe"), stackgroup="one", mode="lines",
        line=dict(width=0.5), fill='tozeroy', fillcolor="#e74c3c"
    ))
    # 日本
    fig.add_trace(go.Scatter(
        x=yearly_region["Year"], y=yearly_region["JP_Sales"],
        name=get_text("Japan"), stackgroup="one", mode="lines",
        line=dict(width=0.5), fill='tozeroy', fillcolor="#2ecc71"
    ))
    # 其他地区
    fig.add_trace(go.Scatter(
        x=yearly_region["Year"], y=yearly_region["Other_Sales"],
        name=get_text("Other"), stackgroup="one", mode="lines",
        line=dict(width=0.5), fill='tozeroy', fillcolor="#9b59b6"
    ))
    
    fig.update_layout(
        title=f"{get_text('regional_sales_trend')}（堆叠面积图）",
        xaxis_title=get_text("year"),
        yaxis_title=get_text("sales_million"),
        height=400,
        hovermode="x unified",
        legend_title=get_text("region")
    )
    return fig

# 新增2：交互式散点图（游戏数量vs平均销售额）
def scatter_game_count_vs_avg_sales(df):
    """按类型分组的散点图：游戏数量 vs 平均销售额"""
    # 按类型分组计算指标
    genre_metrics = df.groupby("Genre").agg(
        Game_Count=("Name", "count"),
        Avg_Sales=("Global_Sales", "mean"),
        Total_Sales=("Global_Sales", "sum")
    ).reset_index()
    
    fig = px.scatter(
        genre_metrics,
        x="Game_Count",
        y="Avg_Sales",
        size="Total_Sales",  # 气泡大小=总销售额
        color="Genre",
        hover_name="Genre",
        title=get_text("genre_game_count_vs_avg_sales"),
        labels={
            "Game_Count": get_text("game_count"),
            "Avg_Sales": get_text("avg_sales_million"),
            "Total_Sales": get_text("total_sales_million")
        },
        size_max=60,
        template="plotly_white"
    )
    fig.update_layout(
        height=450,
        xaxis_title=get_text("game_count"),
        yaxis_title=get_text("avg_sales_million"),
        legend_title=get_text("genre")
    )
    return fig

# 新增3：雷达图（Top3发行商区域表现）
def radar_chart_top_publishers(df):
    """Top3发行商的各地区销售额雷达图"""
    # 获取Top3发行商
    top3_publishers = df.groupby("Publisher")["Global_Sales"].sum().nlargest(3).index.tolist()
    if len(top3_publishers) < 3:
        return None  # 数据不足时返回None
    
    # 计算各发行商的地区销售额占比
    radar_data = []
    regions = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    region_labels = [get_text("North America"), get_text("Europe"), get_text("Japan"), get_text("Other")]
    
    for publisher in top3_publishers:
        pub_df = df[df["Publisher"] == publisher]
        total = pub_df["Global_Sales"].sum()
        if total == 0:
            continue
        # 计算各地区占比
        na_pct = (pub_df["NA_Sales"].sum() / total) * 100
        eu_pct = (pub_df["EU_Sales"].sum() / total) * 100
        jp_pct = (pub_df["JP_Sales"].sum() / total) * 100
        other_pct = 100 - na_pct - eu_pct - jp_pct
        radar_data.append({
            "Publisher": publisher,
            get_text("North America"): na_pct,
            get_text("Europe"): eu_pct,
            get_text("Japan"): jp_pct,
            get_text("Other"): other_pct
        })
    
    if not radar_data:
        return None
    
    fig = px.line_polar(
        pd.DataFrame(radar_data),
        r=[d[region] for d in radar_data for region in region_labels],
        theta=region_labels * len(radar_data),
        color=[d["Publisher"] for d in radar_data for _ in region_labels],
        line_close=True,
        title=get_text("top3_publisher_region_performance"),
        template="plotly_white"
    )
    fig.update_traces(fill="toself", opacity=0.6)
    fig.update_layout(
        height=450,
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], title=get_text("sales_pct"))
        ),
        legend_title=get_text("publisher")
    )
    return fig

# 新增4：动态气泡图（类型-年份-销售额-游戏数量）
def bubble_chart_genre_year(df):
    """气泡图：年份×类型×销售额×游戏数量（支持动态播放）"""
    # 筛选有效年份（1980-2015）
    df_bubble = df.dropna(subset=["Year"]).copy()
    df_bubble["Year"] = df_bubble["Year"].astype(int)
    df_bubble = df_bubble[(df_bubble["Year"] >= 1980) & (df_bubble["Year"] <= 2015)]
    
    # 按年份和类型分组
    bubble_data = df_bubble.groupby(["Year", "Genre"]).agg(
        Total_Sales=("Global_Sales", "sum"),
        Game_Count=("Name", "count")
    ).reset_index()
    
    # 只保留销售额前10的类型（避免图表杂乱）
    top_genres = df_bubble.groupby("Genre")["Global_Sales"].sum().nlargest(10).index
    bubble_data = bubble_data[bubble_data["Genre"].isin(top_genres)]
    
    fig = px.scatter(
        bubble_data,
        x="Year",
        y="Total_Sales",
        size="Game_Count",
        color="Genre",
        hover_name="Genre",
        animation_frame="Year",  # 动态播放年份
        animation_group="Genre",
        title=get_text("genre_year_sales_bubble_chart"),
        labels={
            "Total_Sales": get_text("total_sales_million"),
            "Game_Count": get_text("game_count"),
            "Year": get_text("year")
        },
        size_max=50,
        range_x=[1979, 2016],
        range_y=[0, bubble_data["Total_Sales"].max() * 1.1],
        template="plotly_white"
    )
    fig.update_layout(
        height=500,
        xaxis_title=get_text("year"),
        yaxis_title=get_text("total_sales_million"),
        legend_title=get_text("genre")
    )
    return fig

def line_chart_timeseries(data):
    """时间序列趋势图：年度销售额与游戏数量"""
    fig = go.Figure()
    # 销售额折线（左轴）
    fig.add_trace(go.Scatter(
        x=data["Year"], y=data["Global_Sales"],
        name=f"{get_text('global_sales')}（百万）",
        yaxis="y1",
        line=dict(color="#3498db", width=2),
        hovertemplate=f"{get_text('year')}：%{{x}}<br>{get_text('sales')}：%{{y:.2f}}M"
    ))
    # 游戏数量柱状图（右轴）
    fig.add_trace(go.Bar(
        x=data["Year"], y=data["Game_Count"],
        name=get_text("game_count"),
        yaxis="y2",
        marker=dict(color="#e74c3c", opacity=0.6),
        hovertemplate=f"{get_text('year')}：%{{x}}<br>{get_text('game_count')}：%{{y}}"
    ))
    fig.update_layout(
        title=f"{get_text('global_sales')}与{get_text('game_count')}趋势（1980s-2010s）",
        xaxis_title=get_text("year"),
        yaxis=dict(title=get_text("sales_million"), side="left", range=[0, data["Global_Sales"].max()*1.1]),
        yaxis2=dict(title=get_text("game_count"), side="right", overlaying="y", range=[0, data["Game_Count"].max()*1.1]),
        legend=dict(x=0.01, y=0.99, xanchor="left"),
        height=400,
        plot_bgcolor="white"
    )
    return fig

def bar_chart_region_genre(data, selected_regions=None):
    """区域-类型销售额对比图"""
    if selected_regions:
        data = data[data["Region"].isin(selected_regions)]
    fig = px.bar(
        data,
        x="Genre",
        y="Sales",
        color="Region",
        barmode="group",
        title=f"{get_text('region')}{get_text('genre')}{get_text('sales')}对比",
        labels={"Sales": get_text("sales_million"), "Genre": get_text("genre"), "Region": get_text("region")},
        color_discrete_map={"North America": "#3498db", "Europe": "#e74c3c", "Japan": "#2ca02c"},
        hover_data={"Sales": ":,.2f"}
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        height=400,
        legend_title=get_text("region"),
        plot_bgcolor="white"
    )
    return fig

def bar_chart_publisher(data):
    """发行商销售额排名图（Top 20）"""
    fig = px.bar(
        data,
        y="Publisher",
        x="Global_Sales",
        orientation="h",
        title=f"{get_text('global_sales')} Top 20 {get_text('publisher')}",
        labels={"Global_Sales": get_text("sales_million"), "Publisher": get_text("publisher")},
        color="Global_Sales",
        color_continuous_scale=px.colors.sequential.Viridis,
        hover_data={"Global_Sales": ":,.2f", "Game_Count": ":,"},
        template="plotly_white"
    )
    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=500,
        coloraxis_showscale=False,
        plot_bgcolor="white"
    )
    return fig

def altair_platform_small_multiples(data):
    """平台销售小多图（按年代分组）"""
    data = data[data["Decade"] != get_text("Unknown")]
    subchart = alt.Chart(data).mark_bar().encode(
        x=alt.X("Platform", sort="-y", title=get_text("platform")),
        y=alt.Y("Global_Sales", title=get_text("sales_million")),
        color=alt.Color("Platform", legend=None),
        tooltip=[
            alt.Tooltip("Platform", title=get_text("platform")),
            alt.Tooltip("Global_Sales", title=get_text("sales"), format=",.2f")
        ]
    ).properties(
        height=200,
        width=150
    )
    chart = subchart.facet(
        column=alt.Column("Decade", title=get_text("decade")),
    ).properties(
        title=get_text("platform_evolution_title")
    ).configure_facet(
        spacing=15
    ).configure_title(
        anchor="middle",
        fontSize=16,
        color="#2c3e50"
    ).configure_axis(
        labelAngle=-45,
        labelFontSize=10,
        titleFontSize=12,
        titleColor="#2c3e50"
    ).configure_view(
        stroke="transparent"
    )
    return chart

def heatmap_genre_platform(data, selected_decade=None):
    """游戏类型-平台销售额热力图"""
    if selected_decade and get_text("Unknown") not in selected_decade and "Unknown" not in selected_decade:
        data = data[data["Decade"].isin(selected_decade)]
    # 按类型和平台分组计算销售额
    heatmap_data = data.groupby(["Genre", "Platform"])["Global_Sales"].sum().reset_index()
    # 筛选销售额前10的平台，避免图表过密
    top_platforms = data.groupby("Platform")["Global_Sales"].sum().nlargest(10).index
    heatmap_data = heatmap_data[heatmap_data["Platform"].isin(top_platforms)]
    
    fig = px.density_heatmap(
        heatmap_data,
        x="Platform",
        y="Genre",
        z="Global_Sales",
        title=get_text("genre_platform_heatmap"),
        labels={"Global_Sales": get_text("sales_million"), "Platform": get_text("platform"), "Genre": get_text("genre")},
        color_continuous_scale=px.colors.sequential.YlOrRd,
        hover_data={"Global_Sales": ":,.2f"}
    )
    fig.update_layout(
        height=450,
        xaxis_tickangle=-45,
        plot_bgcolor="white"
    )
    return fig

def histogram_sales_distribution(data, bin_count=30):
    """游戏销售额分布直方图"""
    # 筛选有效销售额（排除0）
    sales_data = data[data["Global_Sales"] > 0]["Global_Sales"]
    fig = px.histogram(
        x=sales_data,
        title=get_text("sales_distribution"),
        labels={"x": get_text("sales_million"), "count": get_text("game_count")},
        nbins=bin_count,
        color_discrete_sequence=["#9b59b6"],
        opacity=0.7,
        marginal="box"  # 新增箱线图边际，展示统计信息
    )
    fig.update_layout(
        height=400,
        plot_bgcolor="white",
        xaxis_title=get_text("sales_million"),
        yaxis_title=get_text("game_count")
    )
    return fig

def top_games_table(data, top_n=20):
    """Top N 游戏详情表格（支持排序和筛选）"""
    top_games = data.nlargest(top_n, "Global_Sales")[
        ["Rank", "Name", "Platform", "Year", "Genre", "Publisher", "NA_Sales", "EU_Sales", "JP_Sales", "Global_Sales"]
    ]
    # 格式化数值列
    numeric_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Global_Sales"]
    for col in numeric_cols:
        top_games[col] = top_games[col].round(2)
    # 重命名列名，更友好（动态语言）
    top_games.rename(columns={
        "Rank": get_text("table_rank"),
        "Name": get_text("table_name"),
        "Platform": get_text("table_platform"),
        "Year": get_text("table_year"),
        "Genre": get_text("table_genre"),
        "Publisher": get_text("table_publisher"),
        "NA_Sales": get_text("table_na_sales"),
        "EU_Sales": get_text("table_eu_sales"),
        "JP_Sales": get_text("table_jp_sales"),
        "Global_Sales": get_text("table_global_sales")
    }, inplace=True)
    return top_games