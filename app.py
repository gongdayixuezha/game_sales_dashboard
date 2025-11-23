import streamlit as st
import pandas as pd
from utils.io import load_data
from utils.prep import make_tables
from sections.intro import show_intro
from sections.overview import show_overview
from sections.deep_dives import show_deep_dives
from sections.conclusions import show_conclusions
from utils.lang import get_text  # 导入语言工具函数

# 页面配置
st.set_page_config(
    page_title=get_text("app_title"),  # 动态标题（支持双语）
    layout="wide",
    page_icon="🎮",
    initial_sidebar_state="expanded"
)

# 初始化会话状态（语言默认中文，避免首次加载报错）
if "lang" not in st.session_state:
    st.session_state["lang"] = "zh"
if "selected_decade" not in st.session_state:
    st.session_state["selected_decade"] = ["1990", "2000", "2010"]
if "data_quality" not in st.session_state:
    st.session_state["data_quality"] = {}
if "df_clean" not in st.session_state:
    st.session_state["df_clean"] = pd.DataFrame()

# 全局样式美化（包含卡片、标题、KPI、筛选器样式）
st.markdown("""
    <style>
        /* 卡片样式 */
        .card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        /* 标题样式 */
        .section-title {
            color: #2c3e50;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
        }
        .section-title svg {
            margin-right: 10px;
        }
        /* KPI指标卡片 */
        .kpi-card {
            background-color: white;
            border-radius: 8px;
            padding: 18px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border-left: 4px solid;
        }
        /* 筛选器样式 */
        .filter-container {
            background-color: #f1f5f9;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
        }
        /* 语言切换按钮样式 */
        .lang-btn-group {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 15px;
        }
        .stButton>button {
            border-radius: 20px !important;
            padding: 8px 20px !important;
        }
        /* 表格样式优化 */
        .stDataFrame {
            border-radius: 8px;
            overflow: hidden;
        }
        /* 联系信息样式 */
        .contact-info {
            margin: 15px 0;
            text-align: center;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# 加载数据
df_raw = load_data()
tables = make_tables(df_raw)  # make_tables 返回字典，而非列表/元组
# 缓存关键数据到会话状态
st.session_state["data_quality"] = tables["data_quality"]
st.session_state["df_clean"] = tables["df_clean"]  # 通过键名获取清洗后的数据集

# 侧边栏配置（包含logo、联系信息、语言切换、导航、全局筛选）
with st.sidebar:
    # 新增logo和联系信息（放在最上方）
    col_logo1, col_logo2 = st.columns(2)
    with col_logo1:
        st.image("assets/logo1.png", width=100)
    with col_logo2:
        st.image("assets/logo2.png", width=100)
    
    # 个人和教授信息
    st.markdown("""
    <div class="contact-info">
        <p><strong>王瑞庆</strong><br>ruiqing.wang@efrei.net</p>
        <p><strong>Mano Joseph Mathew</strong><br>mano.mathew@efrei.fr</p>
    </div>
    <hr style="margin: 10px 0;">
    """, unsafe_allow_html=True)
    
    # 语言切换按钮组（中文/English）
    st.markdown("<div class='lang-btn-group'>", unsafe_allow_html=True)
    col_zh, col_en = st.columns(2)
    with col_zh:
        if st.button("中文", key="btn_zh", type="primary" if st.session_state["lang"] == "zh" else "secondary"):
            st.session_state["lang"] = "zh"
            st.rerun()  # 重新运行确保所有文本同步切换
    with col_en:
        if st.button("English", key="btn_en", type="primary" if st.session_state["lang"] == "en" else "secondary"):
            st.session_state["lang"] = "en"
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 侧边栏标题（双语动态切换）
    st.markdown(f"<h1 style='text-align: center; color: #2c3e50; margin-bottom: 20px;'>{get_text('sidebar_title')}</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 导航菜单（双语选项）
    menu_option = st.selectbox(
        get_text("menu_option"),
        [get_text("module_intro"), get_text("module_overview"), get_text("module_deep_dive"), get_text("module_conclusion")],
        index=1  # 默认选中"核心指标概览"
    )
    
    st.markdown("---")
    # 全局筛选器容器
    st.markdown(f"<div class='filter-container'><h4>{get_text('global_filter')}</h4></div>", unsafe_allow_html=True)
    
    # 年代筛选（双语支持）
    decades = ["1980", "1990", "2000", "2010", get_text("Unknown")]
    selected_decade = st.multiselect(
        get_text("select_decade"),
        options=decades,
        default=["1990", "2000", "2010"],
        help=get_text("decade_help")
    )
    st.session_state["selected_decade"] = selected_decade  # 同步到会话状态
    
    st.markdown("---")
    # 项目信息（双语动态切换）
    st.info(f"""
    {get_text('project_info')}：
    - {get_text('data_source')}
    - {get_text('total_records')}
    - {get_text('time_range')}
    - {get_text('analysis_dimensions')}
    """)

# 主内容区标题和说明（双语支持）
st.markdown(f"<h1 style='color: #2c3e50; margin-bottom: 10px;'>{get_text('app_title')}</h1>", unsafe_allow_html=True)
st.caption(get_text("unit_note"))
st.markdown("---")

# 导航逻辑（根据选中的菜单选项显示对应模块）
if menu_option == get_text("module_intro"):
    show_intro()
elif menu_option == get_text("module_overview"):
    show_overview(tables)
elif menu_option == get_text("module_deep_dive"):
    show_deep_dives(tables)
elif menu_option == get_text("module_conclusion"):
    show_conclusions()