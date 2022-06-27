import streamlit as st
import pandas as pd
import numpy as np
from html_module import line_break, section, callout, title
from PIL import Image


# 전체 페이지 설정
st.set_page_config(
    page_title="사자동산의 데이터 분석 페이지",  # 전체 타이틀
    page_icon="🦁",  # 아이콘
    initial_sidebar_state="expanded",  # 왼쪽 사이드바
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


st.balloons()  # 풍선 효과
title('보험료 데이터 회귀 분석')
# st.title('보험료 데이터 회귀 분석')  # title


# 개요 section
section('개요')
image = Image.open('images/main.png')
st.image(image,)
callout([
    '안녕하세요! 사자동산의 미니 프로젝트 페이지 입니다.',
    '저희는 Kaggle의 보험료 데이터 회귀 예측을 했습니다.'
])
line_break()

# other section ...
section('데이터 출처')
link = 'https://www.kaggle.com/datasets/simranjain17/insurance'
st.markdown(link, unsafe_allow_html=True)
st.caption('Kaggle Insurance Premium Data 페이지로 이동하기')
line_break()

section('팀 노션')
notion_link = 'https://www.notion.so/Kaggle-ca13e0f8b55648f7a12d0d68e3344552'
st.markdown(notion_link, unsafe_allow_html=True)
st.caption('미니 프로젝트 노션 페이지로 이동하기')


