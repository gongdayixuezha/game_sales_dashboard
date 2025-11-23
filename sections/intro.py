import streamlit as st
from utils.lang import get_text

def show_intro():
    st.markdown(f"<div class='section-title'>{get_text('background_goal_title')}</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='card'>
        <p>{get_text('background_content')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<div class='section-title'>{get_text('dataset_description_title')}</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='card'>
        <ul>
            <li><strong>{get_text('dataset_source')}</strong></li>
            <li><strong>{get_text('dataset_scale')}</strong></li>
            <li><strong>{get_text('dataset_fields')}</strong></li>
            <li><strong>{get_text('dataset_unit')}</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<div class='section-title'>{get_text('analysis_framework_title')}</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <h3 style='color: #3498db;'>📈</h3>
            <h4>{get_text('global_overview')}</h4>
            <p>{get_text('global_overview_desc')}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <h3 style='color: #e74c3c;'>🔍</h3>
            <h4>{get_text('deep_analysis')}</h4>
            <p>{get_text('deep_analysis_desc')}</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <h3 style='color: #2ecc71;'>💡</h3>
            <h4>{get_text('insights_recommendations')}</h4>
            <p>{get_text('insights_recommendations_desc')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 数据质量提示（美化）
    st.markdown(f"<div class='section-title'>{get_text('data_quality_note')}</div>", unsafe_allow_html=True)
    data_quality = st.session_state.get("data_quality", {})
    st.markdown(f"""
    <div class='card' style='background-color: #fef9e7; border-left: 4px solid #f39c12;'>
        <p>• {get_text('original_records')}：{data_quality.get('Total_Records', 'N/A')}</p>
        <p>• {get_text('cleaned_records')}：{data_quality.get('Cleaned_Records', 'N/A')}</p>
        <p>• {get_text('missing_year_pct')}：{data_quality.get('Missing_Year_Pct', 'N/A')}（可能影响部分趋势分析）</p>
        <p>• {get_text('duplicate_records')}：{data_quality.get('Duplicate_Records', 'N/A')}（已移除）</p>
        <p>• {get_text('max_sales_single')}：{data_quality.get('Max_Global_Sales', 'N/A')}（《Wii Sports》）</p>
    </div>
    """, unsafe_allow_html=True)