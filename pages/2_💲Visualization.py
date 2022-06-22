import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from html_module import section, callout, line_break

"""
대충 시각화
"""


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


# seaborn - box plot 그리기
def sns_box_plot(data, x):
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(data=data, x=x)
    st.pyplot(fig)


# seaborn - line plot 그리기
def sns_line_plot(data, x, y):
    fig = plt.figure(figsize=(10, 4))
    sns.lineplot(data=data, x=x, y=y)
    st.pyplot(fig)


# seaborn - bar plot 그리기
def sns_bar_plot(data, x, y):
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(data=data, x=x, y=y)
    st.pyplot(fig)


# 수치형 그래프 그리기
def number_graph(col):
    page = st.sidebar.selectbox(
        "Select a Graph",
        [
            "Box Plot",
            "Line Plot",
        ]
    )
    if page == 'Line Plot':
        sns_line_plot(data, col, 'charges')
    elif page == 'Box Plot':
        sns_box_plot(data, col)


# 범주형 그래프 그리기
def category_graph(col):
    page = st.sidebar.selectbox(
        "Select a Graph",
        [
            "Bar Plot",
        ]
    )

    if page == 'Bar Plot':
        sns_bar_plot(data, col, 'charges')
    



# main 함수
def main():
    col = st.sidebar.selectbox(
        "📊 시각화를 할 컬럼을 선택해주세요",
        [
            'Age',
            'Sex',
            'Smoker'
        ]
    )

    if col == 'Age':
        number_graph('age')
    elif col == 'Sex':
        category_graph('sex')
    elif col == 'Smoker':
        category_graph('smoker')


main()
