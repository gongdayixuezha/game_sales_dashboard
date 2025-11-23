import pandas as pd
import numpy as np

def make_tables(df_raw):
    """
    数据预处理核心函数：
    1. 清洗原始数据，生成 df_clean
    2. 生成各分析模块所需的表格（时间序列、发行商排名、区域-类型、平台销售等）
    3. 返回包含所有表格的字典（确保包含 df_clean 键，修复 KeyError 问题）
    """
    # ---------------------- 1. 数据清洗：生成 df_clean（关键：后续所有分析基于此数据集）----------------------
    df_clean = df_raw.copy()
    
    # 1.1 处理缺失值：关键字段非空（名称、平台、全球销售额）
    df_clean = df_clean.dropna(subset=["Name", "Platform", "Global_Sales"])
    
    # 1.2 年份字段处理：转为数值类型，无法转换的设为NaN；生成年代字段（Decade）
    df_clean["Year"] = pd.to_numeric(df_clean["Year"], errors="coerce")  # 字符串年份转数值（无效值设为NaN）
    df_clean["Decade"] = df_clean["Year"].apply(
        lambda x: str(int((x // 10) * 10)) if pd.notna(x) and x >= 1980 else get_text("Unknown")
    )  # 1980年后的年份生成年代（如1995→1990），其他设为"Unknown"
    
    # 1.3 处理重复值：按游戏名称、平台、年份去重（避免同一游戏多次统计）
    df_clean = df_clean.drop_duplicates(subset=["Name", "Platform", "Year"], keep="first")
    
    # 1.4 过滤异常值：全球销售额>0（排除无效销售数据）
    df_clean = df_clean[df_clean["Global_Sales"] > 0]
    
    # ---------------------- 2. 生成各分析模块所需表格 ----------------------
    # 2.1 时间序列表：年度销售额+游戏数量（用于趋势分析）
    timeseries = df_clean.groupby("Year").agg(
        Global_Sales=("Global_Sales", "sum"),
        NA_Sales=("NA_Sales", "sum"),
        EU_Sales=("EU_Sales", "sum"),
        JP_Sales=("JP_Sales", "sum"),
        Game_Count=("Name", "count")  # 年度发布游戏数量
    ).reset_index()
    # 过滤无效年份（只保留1980年及以后的数据）
    timeseries = timeseries[(timeseries["Year"] >= 1980) & (pd.notna(timeseries["Year"]))].sort_values("Year")
    
    # 2.2 发行商排名表：按全球销售额排序（Top N 分析）
    publisher_rank = df_clean.groupby("Publisher").agg(
        Global_Sales=("Global_Sales", "sum"),
        Game_Count=("Name", "count")  # 发行商发布的游戏总数
    ).reset_index().sort_values("Global_Sales", ascending=False)
    # 过滤无效发行商名称
    publisher_rank = publisher_rank[publisher_rank["Publisher"].notna() & (publisher_rank["Publisher"] != "")]
    
    # 2.3 区域-类型销售表：各地区不同类型游戏的销售额（区域偏好分析）
    # 北美地区
    region_genre_na = df_clean.groupby(["Genre", "Decade"]).agg(Sales=("NA_Sales", "sum")).reset_index()
    region_genre_na["Region"] = "North America"
    # 欧洲地区
    region_genre_eu = df_clean.groupby(["Genre", "Decade"]).agg(Sales=("EU_Sales", "sum")).reset_index()
    region_genre_eu["Region"] = "Europe"
    # 日本地区
    region_genre_jp = df_clean.groupby(["Genre", "Decade"]).agg(Sales=("JP_Sales", "sum")).reset_index()
    region_genre_jp["Region"] = "Japan"
    # 合并三大区域数据
    region_genre = pd.concat([region_genre_na, region_genre_eu, region_genre_jp], ignore_index=True)
    
    # 2.4 平台销售表：各平台按年代的销售额（平台演变分析）
    platform_sales = df_clean.groupby(["Platform", "Decade"]).agg(
        Global_Sales=("Global_Sales", "sum")
    ).reset_index().sort_values(["Decade", "Global_Sales"], ascending=[True, False])
    # 过滤无效平台名称
    platform_sales = platform_sales[platform_sales["Platform"].notna() & (platform_sales["Platform"] != "")]
    
    # 2.5 数据质量统计：用于数据说明模块
    data_quality = {
        "Total_Records": len(df_raw),  # 原始数据总记录数
        "Cleaned_Records": len(df_clean),  # 清洗后有效记录数
        "Missing_Year_Pct": f"{df_clean['Year'].isna().sum() / len(df_clean) * 100:.1f}%",  # 年份缺失比例
        "Duplicate_Records": len(df_raw) - len(df_raw.drop_duplicates(subset=["Name", "Platform", "Year"])),  # 重复记录数
        "Max_Global_Sales": f"{df_clean['Global_Sales'].max():.2f}M"  # 单款游戏最高销售额
    }
    
    # ---------------------- 3. 返回包含所有表格的字典（关键：确保键名正确）----------------------
    return {
        "df_clean": df_clean,          # 清洗后的原始数据集（供深度分析模块使用）
        "timeseries": timeseries,      # 时间序列表（趋势分析）
        "publisher_rank": publisher_rank,  # 发行商排名表（竞争分析）
        "region_genre": region_genre,  # 区域-类型销售表（区域偏好分析）
        "platform_sales": platform_sales,  # 平台销售表（平台演变分析）
        "data_quality": data_quality   # 数据质量统计（数据说明）
    }

# 辅助函数：获取多语言文本（避免依赖循环，直接复用 lang.py 逻辑）
def get_text(key):
    from streamlit import session_state
    # 简化版语言字典（仅包含当前文件所需文本）
    lang_dict = {
        "Unknown": {"zh": "未知", "en": "Unknown"}
    }
    lang = session_state.get("lang", "zh")
    return lang_dict.get(key, {}).get(lang, key)