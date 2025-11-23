import pandas as pd
import numpy as np

def make_tables(df_raw):
    """数据预处理：清洗、特征工程，返回各模块所需数据表"""
    # 1. 数据清洗
    df_clean = df_raw.copy()
    # 处理缺失值（Year 列填充为 0 标记未知年份，后续筛选可排除）
    df_clean["Year"] = pd.to_numeric(df_clean["Year"], errors="coerce").fillna(0).astype(int)
    # 去除重复值
    df_clean = df_clean.drop_duplicates(subset=["Name", "Platform", "Year"], keep="first")
    # 过滤异常销售额（排除 0 或负值）
    df_clean = df_clean[df_clean["Global_Sales"] > 0]

    # 2. 特征工程：添加年代分组
    df_clean["Decade"] = (df_clean["Year"] // 10) * 10
    df_clean["Decade"] = df_clean["Decade"].replace(0, "Unknown")

    # 3. 各模块数据表
    tables = {}

    # 时间序列数据（年度销售）
    timeseries = df_clean[df_clean["Year"] != 0].groupby("Year").agg({
        "Global_Sales": "sum",
        "NA_Sales": "sum",
        "EU_Sales": "sum",
        "JP_Sales": "sum",
        "Other_Sales": "sum",
        "Name": "count"
    }).rename(columns={"Name": "Game_Count"}).reset_index()
    tables["timeseries"] = timeseries

    # 区域-类型数据（修正：删除错误的分组代码，直接通过销售额列拆分拼接）
    na_genre = df_clean.groupby("Genre")["NA_Sales"].sum().reset_index().rename(columns={"NA_Sales": "Sales"})
    na_genre["Region"] = "North America"
    eu_genre = df_clean.groupby("Genre")["EU_Sales"].sum().reset_index().rename(columns={"EU_Sales": "Sales"})
    eu_genre["Region"] = "Europe"
    jp_genre = df_clean.groupby("Genre")["JP_Sales"].sum().reset_index().rename(columns={"JP_Sales": "Sales"})
    jp_genre["Region"] = "Japan"
    tables["region_genre"] = pd.concat([na_genre, eu_genre, jp_genre])

    # 发行商排名数据（Top 20）
    publisher_rank = df_clean.groupby("Publisher").agg({
        "Global_Sales": "sum",
        "Name": "count"
    }).rename(columns={"Name": "Game_Count"}).sort_values("Global_Sales", ascending=False).head(20).reset_index()
    tables["publisher_rank"] = publisher_rank

    # 平台销售数据（核心修复：按 Decade + Platform 双重分组，保留年代信息）
    # 步骤1：按年代和平台分组，统计销售额和游戏数量
    platform_decade_sales = df_clean.groupby(["Decade", "Platform"]).agg({
        "Global_Sales": "sum",  # 各年代-平台的总销售额
        "Name": "count"         # 各年代-平台的游戏数量
    }).rename(columns={"Name": "Game_Count"}).reset_index()

    # 步骤2：筛选全局销售额前15的平台（避免图表过于拥挤）
    top_platforms = df_clean.groupby("Platform")["Global_Sales"].sum().nlargest(15).index.tolist()
    platform_sales = platform_decade_sales[platform_decade_sales["Platform"].isin(top_platforms)]

    tables["platform_sales"] = platform_sales

    # 数据质量统计
    data_quality = {
        "Total_Records": len(df_raw),
        "Cleaned_Records": len(df_clean),
        "Missing_Year_Pct": f"{df_raw['Year'].isna().mean()*100:.1f}%",
        "Duplicate_Records": len(df_raw) - len(df_raw.drop_duplicates(subset=["Name", "Platform", "Year"])),
        "Max_Global_Sales": f"{df_clean['Global_Sales'].max():.2f}M"
    }
    tables["data_quality"] = data_quality

    return tables