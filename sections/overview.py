import streamlit as st

def show_overview(tables):
    timeseries = tables["timeseries"]
    publisher_rank = tables["publisher_rank"]

    # KPI 指标行
    st.markdown("## 核心销售指标")
    col1, col2, col3, col4 = st.columns(4)
    total_sales = timeseries["Global_Sales"].sum()
    total_games = timeseries["Game_Count"].sum()
    top_publisher = publisher_rank.iloc[0]["Publisher"]
    top_publisher_sales = publisher_rank.iloc[0]["Global_Sales"]

    col1.metric("全球总销售额", f"{total_sales:.2f}M", help="所有记录的全球销售额总和")
    col2.metric("游戏总数", f"{total_games:,}", help="清洗后的有效游戏记录数")
    col3.metric("头部发行商", top_publisher, help="全球销售额最高的发行商")
    col4.metric("头部发行商销售额", f"{top_publisher_sales:.2f}M", help="头部发行商的全球销售总额")

    # 关键趋势预览
    st.markdown("## 关键趋势预览")
    st.markdown("### 销售黄金期：2000-2010 年")
    golden_age = timeseries[(timeseries["Year"] >= 2000) & (timeseries["Year"] <= 2010)]
    golden_sales = golden_age["Global_Sales"].sum()
    golden_pct = (golden_sales / total_sales) * 100
    st.success(f"2000-2010 年全球销售额达 {golden_sales:.2f}M，占总销售额的 {golden_pct:.1f}%，为行业黄金发展期")