import streamlit as st
from utils.viz import (
    line_chart_timeseries, bar_chart_region_genre,
    bar_chart_publisher, altair_platform_small_multiples
)

def show_deep_dives(tables):
    timeseries = tables["timeseries"]
    region_genre = tables["region_genre"]
    publisher_rank = tables["publisher_rank"]
    platform_sales = tables["platform_sales"]

    # 1. 时间趋势分析
    st.markdown("## 1. 时间趋势：行业发展脉络")
    # 年份筛选器
    min_year = timeseries["Year"].min()
    max_year = timeseries["Year"].max()
    year_range = st.slider("选择年份范围", min_value=int(min_year), max_value=int(max_year), value=(1990, 2010))
    filtered_timeseries = timeseries[(timeseries["Year"] >= year_range[0]) & (timeseries["Year"] <= year_range[1])]
    # 修复：use_container_width=True → width='stretch'
    st.plotly_chart(line_chart_timeseries(filtered_timeseries), width='stretch')

    # 2. 区域偏好分析
    st.markdown("## 2. 区域偏好：各市场游戏类型差异")
    regions = st.multiselect("选择区域", ["North America", "Europe", "Japan"], default=["North America", "Europe", "Japan"])
    # 修复：use_container_width=True → width='stretch'
    st.plotly_chart(bar_chart_region_genre(region_genre, regions), width='stretch')

    # 3. 发行商排名分析
    st.markdown("## 3. 市场竞争：头部发行商格局")
    # 修复：use_container_width=True → width='stretch'
    st.plotly_chart(bar_chart_publisher(publisher_rank), width='stretch')

    # 4. 平台演变：各年代主流载体
    st.markdown("## 4. 平台演变：各年代主流游戏平台")
    # 修复：use_container_width=True → width='stretch'
    st.altair_chart(altair_platform_small_multiples(platform_sales), width='stretch')