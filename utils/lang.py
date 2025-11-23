# 语言配置文件：集中管理所有中英文文本，支持实时切换
lang_dict = {
    # 全局通用文本
    "app_title": {"zh": "全球电子游戏销售数据叙事", "en": "Global Video Game Sales Data Narrative"},
    "sidebar_title": {"zh": "🎮 游戏销售分析", "en": "🎮 Game Sales Analysis"},
    "menu_option": {"zh": "📌 选择模块", "en": "📌 Select Module"},
    "global_filter": {"zh": "🔍 全局筛选", "en": "🔍 Global Filter"},
    "select_decade": {"zh": "选择年代", "en": "Select Decades"},
    "decade_help": {"zh": "筛选特定年代的游戏数据", "en": "Filter game data by specific decades"},
    "project_info": {"zh": "📊 项目信息", "en": "📊 Project Info"},
    "data_source": {"zh": "数据集：Video Game Sales", "en": "Dataset: Video Game Sales"},
    "total_records": {"zh": "记录数：16,598 条", "en": "Total Records: 16,598"},
    "time_range": {"zh": "时间范围：1980s-2010s", "en": "Time Range: 1980s-2010s"},
    "analysis_dimensions": {"zh": "分析维度：趋势、区域、发行商、平台", "en": "Analysis Dimensions: Trend, Region, Publisher, Platform"},
    "unit_note": {"zh": "📈 数据来源：Video Game Sales Dataset | 单位：销售额（百万美元）", "en": "📈 Data Source: Video Game Sales Dataset | Unit: Sales (Million USD)"},
    "Unknown": {"zh": "未知", "en": "Unknown"},
    
    # 模块名称
    "module_intro": {"zh": "引言与数据说明", "en": "Introduction & Data Description"},
    "module_overview": {"zh": "核心指标概览", "en": "Core Metrics Overview"},
    "module_deep_dive": {"zh": "深度分析", "en": "Deep Dive Analysis"},
    "module_conclusion": {"zh": "洞察与启示", "en": "Insights & Recommendations"},
    
    # 核心指标概览文本
    "core_kpi_title": {"zh": "🎯 核心销售指标", "en": "🎯 Core Sales Metrics"},
    "total_global_sales": {"zh": "全球总销售额", "en": "Total Global Sales"},
    "total_games": {"zh": "游戏总数", "en": "Total Games"},
    "active_platforms": {"zh": "活跃平台", "en": "Active Platforms"},
    "top_publisher": {"zh": "头部发行商", "en": "Top Publisher"},
    "top_genre": {"zh": "热门游戏类型", "en": "Top Genre"},
    "region_trend_title": {"zh": "🌍 区域分布与近期趋势", "en": "🌍 Region Distribution & Recent Trend"},
    "top_ranking_title": {"zh": "🏆 热门类型与平台", "en": "🏆 Top Genres & Platforms"},
    "regional_sales_share": {"zh": "各地区销售额占比", "en": "Regional Sales Share"},
    "recent_10y_trend": {"zh": "近10年全球销售额趋势", "en": "Global Sales Trend (Last 10 Years)"},
    "top5_genre_sales": {"zh": "Top5 游戏类型销售额", "en": "Top5 Genre Sales"},
    "top5_platform_sales": {"zh": "Top5 游戏平台销售额", "en": "Top5 Platform Sales"},
    "data_quality_detail": {"zh": "📊 数据质量详情", "en": "📊 Data Quality Details"},
    "original_records": {"zh": "原始记录数", "en": "Original Records"},
    "cleaned_records": {"zh": "清洗后记录数", "en": "Cleaned Records"},
    "missing_year_pct": {"zh": "年份缺失比例", "en": "Missing Year Percentage"},
    "duplicate_records": {"zh": "重复记录数", "en": "Duplicate Records"},
    "max_sales_single": {"zh": "单款游戏最高销售额", "en": "Max Sales (Single Game)"},
    "vs_5y_ago": {"zh": "vs 5年前", "en": "vs 5 Years Ago"},
    
    # 深度分析文本
    "time_trend_title": {"zh": "📅 时间趋势：行业发展脉络", "en": "📅 Time Trend: Industry Development"},
    "select_year_range": {"zh": "选择年份范围", "en": "Select Year Range"},
    "display_options": {"zh": "📊 显示选项", "en": "📊 Display Options"},
    "show_sales": {"zh": "显示销售额", "en": "Show Sales"},
    "show_count": {"zh": "显示游戏数量", "en": "Show Game Count"},
    "region_preference_title": {"zh": "🌍 区域偏好：各市场游戏类型差异", "en": "🌍 Regional Preference: Market Genre Differences"},
    "select_regions": {"zh": "选择区域", "en": "Select Regions"},
    "publisher_competition_title": {"zh": "🏢 市场竞争：头部发行商格局", "en": "🏢 Market Competition: Top Publishers"},
    "select_topn_publisher": {"zh": "选择Top N发行商", "en": "Select Top N Publishers"},
    "genre_platform_title": {"zh": "🔥 类型-平台关联：热门组合分析", "en": "🔥 Genre-Platform Link: Popular Combination Analysis"},
    "sales_distribution_title": {"zh": "📊 销售额分布：市场集中度分析", "en": "📊 Sales Distribution: Market Concentration"},
    "adjust_bin_count": {"zh": "调整分箱数", "en": "Adjust Bin Count"},
    "top_games_detail_title": {"zh": "🎮 Top游戏详情", "en": "🎮 Top Games Details"},
    "select_topn_games": {"zh": "选择Top N游戏", "en": "Select Top N Games"},
    "platform_evolution_title": {"zh": "🎮 平台演变：各年代主流载体", "en": "🎮 Platform Evolution: Mainstream Carriers by Decade"},
    
    # 无数据提示文本（新增）
    "no_data_warning": {"zh": "暂无符合条件的时间序列数据，请调整筛选条件", "en": "No time series data matching the criteria, please adjust filters"},
    "no_data_in_range": {"zh": "所选年份范围内无数据", "en": "No data in the selected year range"},
    "no_region_data": {"zh": "所选区域无相关销售数据", "en": "No sales data for the selected regions"},
    "no_publisher_data": {"zh": "暂无发行商排名数据", "en": "No publisher ranking data available"},
    "no_data_for_heatmap": {"zh": "暂无足够数据生成热力图，请调整年代筛选", "en": "Insufficient data to generate heatmap, please adjust decade filters"},
    "no_valid_sales_data": {"zh": "暂无有效销售额数据", "en": "No valid sales data available"},
    "no_game_data": {"zh": "暂无游戏详情数据", "en": "No game details data available"},
    "no_platform_data": {"zh": "暂无平台销售数据", "en": "No platform sales data available"},
    
    # 引言模块文本
    "background_goal_title": {"zh": "📚 背景与目标", "en": "📚 Background & Goals"},
    "background_content": {
        "zh": "电子游戏行业已成为全球娱乐产业的支柱，2023 年全球市场规模超 2000 亿美元。本仪表盘基于 1980s-2010s 全球游戏销售数据集，探索行业发展趋势、区域偏好差异和市场竞争格局，为游戏发行商、开发者和投资者提供数据驱动的决策参考。",
        "en": "The video game industry has become a pillar of the global entertainment industry, with a global market size exceeding 200 billion USD in 2023. Based on the global game sales dataset from the 1980s to 2010s, this dashboard explores industry development trends, regional preference differences, and market competition patterns to provide data-driven decision support for game publishers, developers, and investors."
    },
    "dataset_description_title": {"zh": "📊 数据集说明", "en": "📊 Dataset Description"},
    "dataset_source": {"zh": "来源：Video Game Sales Dataset（开放数据集）", "en": "Source: Video Game Sales Dataset (Open Dataset)"},
    "dataset_scale": {"zh": "规模：16,598 条游戏销售记录", "en": "Scale: 16,598 Game Sales Records"},
    "dataset_fields": {
        "zh": "核心字段：游戏名称、平台、发行年份、类型、发行商、各地区销售额（北美、欧洲、日本、其他地区）、全球销售额",
        "en": "Core Fields: Game Name, Platform, Release Year, Genre, Publisher, Regional Sales (NA, EU, JP, Other), Global Sales"
    },
    "dataset_unit": {"zh": "单位：销售额以百万美元计", "en": "Unit: Sales in Million USD"},
    "analysis_framework_title": {"zh": "🔍 分析框架", "en": "🔍 Analysis Framework"},
    "global_overview": {"zh": "全局概览", "en": "Global Overview"},
    "global_overview_desc": {"zh": "核心销售指标与整体趋势", "en": "Core Sales Metrics & Overall Trends"},
    "deep_analysis": {"zh": "深度分析", "en": "Deep Analysis"},
    "deep_analysis_desc": {"zh": "趋势、区域、发行商、平台", "en": "Trend, Region, Publisher, Platform"},
    "insights_recommendations": {"zh": "洞察启示", "en": "Insights & Recommendations"},
    "insights_recommendations_desc": {"zh": "市场机会与策略建议", "en": "Market Opportunities & Strategic Recommendations"},
    "data_quality_note": {"zh": "⚠️ 数据质量说明", "en": "⚠️ Data Quality Note"},
    
    # 洞察启示模块文本
    "core_insights_title": {"zh": "💡 核心洞察", "en": "💡 Core Insights"},
    "trend_insight_title": {"zh": "行业趋势：2000-2010 年为黄金期，后续趋稳", "en": "Industry Trend: 2000-2010 as Golden Age, Stabilization Thereafter"},
    "trend_insight_1": {"zh": "2000-2010 年销售额占总规模的 68%，为行业爆发期（受益于 Wii、PS2 等主流平台普及）。", "en": "Sales from 2000-2010 accounted for 68% of the total scale, making it an industry boom period (benefiting from the popularity of mainstream platforms such as Wii and PS2)."},
    "trend_insight_2": {"zh": "2010 年后销售额略有下滑，可能与移动游戏崛起、数据集未覆盖移动平台有关。", "en": "Sales declined slightly after 2010, possibly related to the rise of mobile games and the dataset not covering mobile platforms."},
    "region_insight_title": {"zh": "区域偏好：差异显著，精准定位是关键", "en": "Regional Preference: Significant Differences, Precise Positioning is Key"},
    "region_insight_1": {"zh": "北美市场：动作类、体育类游戏最受欢迎（占比超 40%）。", "en": "North American Market: Action and Sports games are the most popular (accounting for over 40%)."},
    "region_insight_2": {"zh": "欧洲市场：与北美偏好相似，但赛车类游戏占比更高。", "en": "European Market: Similar to North American preferences, but Racing games have a higher proportion."},
    "region_insight_3": {"zh": "日本市场：角色扮演类（RPG）占比领先（25%），对西方主流类型接受度较低。", "en": "Japanese Market: Role-Playing Games (RPG) lead in proportion (25%), with low acceptance of mainstream Western genres."},
    "competition_insight_title": {"zh": "市场竞争：任天堂领跑，头部效应明显", "en": "Market Competition: Nintendo Leads, Significant Head Effect"},
    "competition_insight_1": {"zh": "任天堂（Nintendo）以超 1700 百万美元销售额稳居第一，占总市场的 18%。", "en": "Nintendo ranks first with over 1700 million USD in sales, accounting for 18% of the total market."},
    "competition_insight_2": {"zh": "Top 5 发行商（任天堂、EA、Activision 等）占据近 50% 市场份额，行业集中度高。", "en": "The top 5 publishers (Nintendo, EA, Activision, etc.) account for nearly 50% of the market share, indicating high industry concentration."},
    "competition_insight_3": {"zh": "平台方面：Wii、PS2、DS 是最成功的三款平台，合计销售额占比超 30%。", "en": "In terms of platforms: Wii, PS2, and DS are the three most successful platforms, with combined sales accounting for over 30%."},
    "action_recommendations_title": {"zh": "🚀 行动启示", "en": "🚀 Action Recommendations"},
    "for_publishers": {"zh": "发行商", "en": "For Publishers"},
    "publisher_recom_1": {"zh": "聚焦北美核心市场", "en": "Focus on the core North American market"},
    "publisher_recom_2": {"zh": "优先适配头部平台", "en": "Prioritize adaptation to top platforms"},
    "publisher_recom_3": {"zh": "合作头部 IP 降低风险", "en": "Collaborate with top IPs to reduce risks"},
    "for_developers": {"zh": "开发者", "en": "For Developers"},
    "developer_recom_1": {"zh": "北美/欧洲：深耕动作/体育类", "en": "NA/Europe: Deepen Action/Sports genres"},
    "developer_recom_2": {"zh": "日本：聚焦 RPG/策略类", "en": "Japan: Focus on RPG/Strategy genres"},
    "developer_recom_3": {"zh": "重启经典 IP 把握怀旧趋势", "en": "Revive classic IPs to seize the nostalgia trend"},
    "for_investors": {"zh": "投资者", "en": "For Investors"},
    "investor_recom_1": {"zh": "关注头部发行商布局", "en": "Monitor top publishers' layouts"},
    "investor_recom_2": {"zh": "布局高潜力类型赛道", "en": "Layout high-potential genre tracks"},
    "investor_recom_3": {"zh": "警惕平台迭代风险", "en": "Beware of platform iteration risks"},
    "limitations_improvements": {"zh": "⚠️ 局限性与未来改进", "en": "⚠️ Limitations & Future Improvements"},
    "limitation_1": {"zh": "数据集未覆盖移动游戏、PC 独立游戏等新兴领域，可能低估近年市场规模。", "en": "The dataset does not cover emerging fields such as mobile games and PC indie games, which may underestimate the recent market size."},
    "limitation_2": {"zh": "部分游戏年份缺失，可能影响趋势分析的准确性。", "en": "Missing release years for some games may affect the accuracy of trend analysis."},
    "limitation_3": {"zh": "未来可补充：用户评分与销售额相关性、发行周期分析、区域文化因素深挖。", "en": "Future supplements: Correlation between user ratings and sales, release cycle analysis, in-depth exploration of regional cultural factors."},
    
    # 图表标签文本
    "year": {"zh": "年份", "en": "Year"},
    "sales_million": {"zh": "销售额（百万）", "en": "Sales (Million)"},
    "game_count": {"zh": "游戏数量", "en": "Game Count"},
    "genre": {"zh": "游戏类型", "en": "Genre"},
    "platform": {"zh": "游戏平台", "en": "Platform"},
    "publisher": {"zh": "发行商", "en": "Publisher"},
    "region": {"zh": "地区", "en": "Region"},
    "decade": {"zh": "年代", "en": "Decade"},
    "global_sales": {"zh": "全球销售额", "en": "Global Sales"},
    "na_sales": {"zh": "北美销售额", "en": "NA Sales"},
    "eu_sales": {"zh": "欧洲销售额", "en": "EU Sales"},
    "jp_sales": {"zh": "日本销售额", "en": "JP Sales"},
    "sales": {"zh": "销售额", "en": "Sales"},
    "rank": {"zh": "排名", "en": "Rank"},
    "game_name": {"zh": "游戏名称", "en": "Game Name"},
    "release_year": {"zh": "发行年份", "en": "Release Year"},
    "sales_distribution": {"zh": "游戏销售额分布（百万美元）", "en": "Game Sales Distribution (Million USD)"},
    "count": {"zh": "游戏数量", "en": "Count"},
    "genre_platform_heatmap": {"zh": "游戏类型-平台销售额热力图（Top10平台）", "en": "Genre-Platform Sales Heatmap (Top10 Platforms)"},
    
    # 表格列名文本
    "table_rank": {"zh": "排名", "en": "Rank"},
    "table_name": {"zh": "游戏名称", "en": "Game Name"},
    "table_platform": {"zh": "平台", "en": "Platform"},
    "table_year": {"zh": "发行年份", "en": "Release Year"},
    "table_genre": {"zh": "类型", "en": "Genre"},
    "table_publisher": {"zh": "发行商", "en": "Publisher"},
    "table_na_sales": {"zh": "北美销售额", "en": "NA Sales"},
    "table_eu_sales": {"zh": "欧洲销售额", "en": "EU Sales"},
    "table_jp_sales": {"zh": "日本销售额", "en": "JP Sales"},
    "table_global_sales": {"zh": "全球销售额", "en": "Global Sales"},
    
    # 新增高级图表相关文本
    "regional_sales_trend": {"zh": "各地区销售额趋势", "en": "Regional Sales Trend"},
    "genre_game_count_vs_avg_sales": {"zh": "游戏类型：数量 vs 平均销售额", "en": "Game Genre: Count vs Average Sales"},
    "avg_sales_million": {"zh": "平均销售额（百万）", "en": "Average Sales (Million)"},
    "top3_publisher_region_performance": {"zh": "Top3发行商区域表现对比", "en": "Top3 Publishers' Regional Performance Comparison"},
    "sales_pct": {"zh": "销售额占比（%）", "en": "Sales Percentage (%)"},
    "genre_year_sales_bubble_chart": {"zh": "游戏类型-年份销售额动态气泡图", "en": "Genre-Year Sales Dynamic Bubble Chart"},
    "North America": {"zh": "北美", "en": "North America"},
    "Europe": {"zh": "欧洲", "en": "Europe"},
    "Japan": {"zh": "日本", "en": "Japan"},
    "Other": {"zh": "其他地区", "en": "Other Regions"}  # 已在前面条目补全逗号
}

def get_text(key):
    """
    获取当前语言对应的文本
    :param key: 文本标识（对应 lang_dict 中的键）
    :return: 当前语言的文本（默认中文，未找到时返回 key 本身）
    """
    from streamlit import session_state
    # 获取当前语言（默认中文）
    current_lang = session_state.get("lang", "zh")
    # 从字典中获取文本，未找到时返回 key 避免报错
    return lang_dict.get(key, {}).get(current_lang, key)