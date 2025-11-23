import streamlit as st
from utils.io import load_data
from utils.prep import make_tables
from sections.intro import show_intro
from sections.overview import show_overview
from sections.deep_dives import show_deep_dives
from sections.conclusions import show_conclusions

# 页面配置
st.set_page_config(
    page_title="全球游戏销售数据叙事",
    layout="wide",
    page_icon="🎮"
)

# 加载数据
df_raw = load_data()
tables = make_tables(df_raw)
# 存储数据质量信息到会话状态
st.session_state["data_quality"] = tables["data_quality"]

# 侧边栏导航
st.sidebar.title("🎮 导航菜单")
menu_option = st.sidebar.radio(
    "选择模块",
    ["引言与数据说明", "核心指标概览", "深度分析", "洞察与启示"]
)

# 主内容区
st.sidebar.markdown("---")
st.sidebar.info("""
项目信息：
- 数据集：Video Game Sales
- 分析工具：Streamlit + Plotly + Altair
- 作者：学生姓名
- 课程：#EFREIDataStoriesWUT2025
""")

# 根据导航显示对应模块
if menu_option == "引言与数据说明":
    show_intro()
elif menu_option == "核心指标概览":
    show_overview(tables)
elif menu_option == "深度分析":
    show_deep_dives(tables)
elif menu_option == "洞察与启示":
    show_conclusions()