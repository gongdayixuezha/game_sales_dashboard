# 全球电子游戏销售数据叙事 Dashboard
## 项目介绍
本项目是基于 Streamlit 构建的交互式数据叙事应用，聚焦 1980s-2010s 全球电子游戏销售数据，探索行业趋势、区域偏好和市场竞争格局。

## 数据集
- 来源：[Video Game Sales Dataset](https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/vgsales.csv)
- 规模：16,598 条游戏销售记录
- 核心字段：游戏名称、平台、发行年份、类型、发行商、各地区销售额、全球销售额

## 功能模块
1. 引言与数据说明：项目背景、数据集详情、数据质量说明
2. 核心指标概览：全球总销售额、游戏总数、头部发行商等 KPI
3. 深度分析：时间趋势、区域偏好、发行商排名、平台演变
4. 洞察与启示：核心发现与行动建议

## 运行步骤
1. 克隆代码仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 运行应用：`streamlit run app.py`
4. 访问本地地址：http://localhost:8501

## 技术栈
- 前端框架：Streamlit ≥ 1.33
- 数据处理：Pandas、Numpy
- 可视化：Plotly、Altair
- 数据格式：CSV、PyArrow

## 交付物说明
- `app.py`：主应用入口
- `sections/`：各功能模块页面
- `utils/`：数据加载、预处理、可视化工具函数
- `data/`：备用数据集文件
- `requirements.txt`：依赖包清单
- `demo_video.md`：演示视频脚本

## 演示视频脚本（2-4 分钟）
1. 开场白（30 秒）：介绍项目主题、数据集和核心目标
2. 功能演示（2 分钟）：
   - 导航菜单使用
   - 筛选器交互（年份范围、区域选择）
   - 各可视化图表的解读（趋势图、对比图、排名图）
3. 核心洞察总结（1 分钟）：提炼 3 个关键发现及应用价值
4. 结尾（30 秒）：说明局限性和未来改进方向