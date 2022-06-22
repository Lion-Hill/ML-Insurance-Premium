"""
0. 간략 개요
1. 데이터 소개 + 컬럼 소개
2. EDA 인사이트 + 방향성
3. 시각화
4. 모델링
"""
import streamlit as st
import pandas as pd
import numpy as np
from html_module import section, callout, line_break


# 데이터 프레임 가져오기
DATA_URL = 'data/insurance.csv'


# 데이터 로드 함수
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data


data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("")

section("Insurance Data", 250)
with st.expander("Insurance Premium Raw Data 보기 🔍"):
    st.table(data)
callout(['보험료 데이터'])
line_break()

section("Column")
