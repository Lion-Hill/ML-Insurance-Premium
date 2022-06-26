import streamlit as st
import pandas as pd
import numpy as np
from html_module import section, callout, line_break, title


st.set_page_config(
    page_title="Data | 사자동산",  # 전체 타이틀
    page_icon="🦁",  # 아이콘
)


# 데이터 프레임 가져오기
DATA_URL = 'data/insurance.csv'


# 데이터 로드 함수
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data


# data 로드
data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("")


# insurance raw data load section
section("Insurance Data", 250)
with st.expander("Insurance Premium Raw Data 보기 🔍"):
    st.table(data)
line_break()


# column 소개 section
section("Column")
callout(['Kaggle - Insurance Premium DataSet의 컬럼 입니다.'])
# line_break()
columns_text = [
    ['age', 'The Age of the policyholder'],
    ['sex', ' The Gender of the policyholder'],
    ['bmi', 'The Body Mass Index of the Policyholder'],
    ['children', 'Number of Children of the Policyholder'],
    ['smoker', 'A Column whether the Policyholder is Smoker or No Smoker'],
    ['region', 'The Region where the Policyholder belongs to'],
    ['charges', 'The Premium Charged to the Policyholder', ]
]
st.table(pd.DataFrame(columns_text, columns=['title', 'description']))
