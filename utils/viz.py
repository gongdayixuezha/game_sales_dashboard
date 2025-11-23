import plotly.express as px
import plotly.graph_objects as go
import altair as alt
import streamlit as st

def line_chart_timeseries(data):
    """时间序列趋势图：年度销售额与游戏数量"""
    fig = go.Figure()
    # 销售额折线（左轴）
    fig.add_trace(go.Scatter(
        x=data["Year"], y=data["Global_Sales"],
        name="全球销售额（百万）",
        yaxis="y1",
        line=dict(color="#1f77b4", width=2),
        hovertemplate="年份：%{x}<br>销售额：%{y:.2f}M"
    ))
    # 游戏数量柱状图（右轴）
    fig.add_trace(go.Bar(
        x=data["Year"], y=data["Game_Count"],
        name="发布游戏数量",
        yaxis="y2",
        marker=dict(color="#ff7f0e", opacity=0.6),
        hovertemplate="年份：%{x}<br>游戏数量：%{y}"
    ))
    fig.update_layout(
        title="全球游戏销售额与发布数量趋势（1980s-2010s）",
        xaxis_title="年份",
        yaxis=dict(title="销售额（百万）", side="left", range=[0, data["Global_Sales"].max()*1.1]),
        yaxis2=dict(title="游戏数量", side="right", overlaying="y", range=[0, data["Game_Count"].max()*1.1]),
        legend=dict(x=0.01, y=0.99, xanchor="left"),
        height=400
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
        title="各地区游戏类型销售额对比",
        labels={"Sales": "销售额（百万）", "Genre": "游戏类型"},
        color_discrete_map={"North America": "#1f77b4", "Europe": "#ff7f0e", "Japan": "#2ca02c"},
        hover_data={"Sales": ":,.2f"}
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        height=400,
        legend_title="地区"
    )
    return fig

def bar_chart_publisher(data):
    """发行商销售额排名图（Top 20）"""
    fig = px.bar(
        data,
        y="Publisher",
        x="Global_Sales",
        orientation="h",
        title="全球销售额 Top 20 发行商",
        labels={"Global_Sales": "全球销售额（百万）", "Publisher": "发行商"},
        color="Global_Sales",
        color_continuous_scale=px.colors.sequential.Viridis,
        hover_data={"Global_Sales": ":,.2f", "Game_Count": ":,"}
    )
    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=500,
        coloraxis_showscale=False
    )
    return fig

def altair_platform_small_multiples(data):
    """平台销售小多图（按年代分组）"""
    # 筛选有明确年代的平台（排除 Unknown）
    data = data[data["Decade"] != "Unknown"]
    
    # 修复核心：将 height/width 移到子图的 properties 中，FacetChart 不支持直接设置
    subchart = alt.Chart(data).mark_bar().encode(
        x=alt.X("Platform", sort="-y", title="游戏平台"),
        y=alt.Y("Global_Sales", title="销售额（百万）"),
        color=alt.Color("Platform", legend=None),
        tooltip=[
            alt.Tooltip("Platform", title="游戏平台"),
            alt.Tooltip("Global_Sales", title="销售额", format=",.2f")
        ]
    ).properties(
        height=200,  # 子图高度（每个分栏的高度）
        width=150    # 子图宽度（每个分栏的宽度）
    )
    
    # 外层分栏图表：只配置标题、分栏间距等，不设置 height/width
    chart = subchart.facet(
        column=alt.Column("Decade", title="年代"),
    ).properties(
        title="各年代主流游戏平台销售额"  # 仅保留标题配置
    ).configure_facet(
        spacing=15  # 分栏之间的间距
    ).configure_title(
        anchor="middle",
        fontSize=16
    ).configure_axis(
        labelAngle=-45,
        labelFontSize=10,
        titleFontSize=12
    )
    return chart