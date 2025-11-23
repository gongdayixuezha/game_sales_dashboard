import streamlit as st
from utils.lang import get_text

def show_conclusions():
    st.markdown(f"<div class='section-title'>{get_text('core_insights_title')}</div>", unsafe_allow_html=True)
    
    # 洞察1（带图标）
    st.markdown(f"""
    <div class='card'>
        <h4 style='color: #3498db; display: flex; align-items: center;'>
            <svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
                <polyline points='22 12 18 12 15 21 9 3 6 12 2 12'></polyline>
            </svg>
            {get_text('trend_insight_title')}
        </h4>
        <p>• {get_text('trend_insight_1')}</p>
        <p>• {get_text('trend_insight_2')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 洞察2
    st.markdown(f"""
    <div class='card'>
        <h4 style='color: #e74c3c; display: flex; align-items: center;'>
            <svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
                <circle cx='12' cy='12' r='10'></circle>
                <path d='M2 12h20'></path>
                <path d='M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z'></path>
            </svg>
            {get_text('region_insight_title')}
        </h4>
        <p>• {get_text('region_insight_1')}</p>
        <p>• {get_text('region_insight_2')}</p>
        <p>• {get_text('region_insight_3')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 洞察3
    st.markdown(f"""
    <div class='card'>
        <h4 style='color: #2ecc71; display: flex; align-items: center;'>
            <svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
                <path d='M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2'></path>
                <circle cx='9' cy='7' r='4'></circle>
                <path d='M22 21v-2a4 4 0 0 0-3-3.87'></path>
                <path d='M16 3.13a4 4 0 0 1 0 7.75'></path>
            </svg>
            {get_text('competition_insight_title')}
        </h4>
        <p>• {get_text('competition_insight_1')}</p>
        <p>• {get_text('competition_insight_2')}</p>
        <p>• {get_text('competition_insight_3')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 行动启示（分角色）
    st.markdown(f"<div class='section-title'>{get_text('action_recommendations_title')}</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='card' style='border-top: 4px solid #3498db;'>
            <h4 style='color: #3498db;'>{get_text('for_publishers')}</h4>
            <ul>
                <li>{get_text('publisher_recom_1')}</li>
                <li>{get_text('publisher_recom_2')}</li>
                <li>{get_text('publisher_recom_3')}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='card' style='border-top: 4px solid #e74c3c;'>
            <h4 style='color: #e74c3c;'>{get_text('for_developers')}</h4>
            <ul>
                <li>{get_text('developer_recom_1')}</li>
                <li>{get_text('developer_recom_2')}</li>
                <li>{get_text('developer_recom_3')}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='card' style='border-top: 4px solid #2ecc71;'>
            <h4 style='color: #2ecc71;'>{get_text('for_investors')}</h4>
            <ul>
                <li>{get_text('investor_recom_1')}</li>
                <li>{get_text('investor_recom_2')}</li>
                <li>{get_text('investor_recom_3')}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 局限性说明（折叠面板）
    with st.expander(get_text('limitations_improvements'), expanded=False):
        st.markdown(f"""
        <div class='card' style='background-color: #f8f9fa;'>
            <p>• {get_text('limitation_1')}</p>
            <p>• {get_text('limitation_2')}</p>
            <p>• {get_text('limitation_3')}</p>
        </div>
        """, unsafe_allow_html=True)