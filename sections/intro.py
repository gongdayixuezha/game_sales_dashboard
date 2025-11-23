import streamlit as st

def show_intro():
    st.markdown("""
    # 全球电子游戏销售数据叙事
    ## 背景与目标
    电子游戏行业已成为全球娱乐产业的支柱，2023 年全球市场规模超 2000 亿美元。本仪表盘基于 1980s-2010s 全球游戏销售数据集，探索行业发展趋势、区域偏好差异和市场竞争格局，为游戏发行商、开发者和投资者提供数据驱动的决策参考。

    ## 数据集说明
    - **来源**：Video Game Sales Dataset（开放数据集）
    - **规模**：16,598 条游戏销售记录
    - **核心字段**：游戏名称、平台、发行年份、类型、发行商、各地区销售额（北美、欧洲、日本、其他地区）、全球销售额
    - **单位**：销售额以百万美元计

    ## 分析框架
    1. 全局概览：核心销售指标与整体趋势
    2. 深度分析：时间趋势、区域偏好、发行商/平台排名
    3. 洞察启示：市场机会与策略建议
    """)

    # 数据质量提示
    st.markdown("### 数据质量说明")
    data_quality = st.session_state.get("data_quality", {})
    st.info(f"""
    - 原始记录数：{data_quality.get('Total_Records', 'N/A')}
    - 清洗后记录数：{data_quality.get('Cleaned_Records', 'N/A')}
    - 年份缺失比例：{data_quality.get('Missing_Year_Pct', 'N/A')}
    - 重复记录数：{data_quality.get('Duplicate_Records', 'N/A')}
    - 单款游戏最高销售额：{data_quality.get('Max_Global_Sales', 'N/A')}
    """)