import pandas as pd
import streamlit as st

@st.cache_data(show_spinner="加载游戏销售数据中...")
def load_data():
    """加载并返回原始数据集（优先在线加载，备用本地文件）"""
    try:
        # 在线数据集链接（确保可访问）
        url = "https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/vgsales.csv"
        df = pd.read_csv(url)
    except:
        # 本地备用文件
        df = pd.read_csv("data/vgsales.csv")
    return df