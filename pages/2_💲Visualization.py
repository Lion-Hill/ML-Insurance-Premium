import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from html_module import section, callout, line_break, title


st.set_page_config(
    page_title="Visualization | 사자동산",  # 전체 타이틀
    page_icon="🦁",  # 아이콘
)
title('Visualization')


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
    sns.lineplot(data=data, x=x, y=y, ci=None)
    st.pyplot(fig)


# seaborn - scatter plot 그리기
def sns_scatter_plot(data, x, y):
    fig = plt.figure(figsize=(10, 4))
    sns.scatterplot(data=data, x=x, y=y)
    st.pyplot(fig)


# seaborn - bar plot 그리기
def sns_bar_plot(data, x, y):
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(data=data, x=x, y=y, ci=None)
    st.pyplot(fig)


# seaborn - count plot 그리기
def sns_count_plot(data, x):
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(data=data, x=x)
    st.pyplot(fig)


# 수치형 그래프 그리기
def number_graph(col):
    page = st.sidebar.selectbox(
        "📊 그래프를 선택해주세요",
        [
            "Box Plot",
            "Line Plot",
            "Scatter Plot",
        ]
    )
    if page == 'Line Plot':
        sns_line_plot(data, col, 'charges')
    elif page == 'Box Plot':
        sns_box_plot(data, col)
    elif page == 'Scatter Plot':
        sns_scatter_plot(data, col, 'charges')


# 범주형 그래프 그리기
def category_graph(col):
    page = st.sidebar.selectbox(
        "📊 그래프를 선택해주세요",
        [
            "Bar Plot",
            "Count Plot",
        ]
    )

    if page == 'Bar Plot':
        sns_bar_plot(data, col, 'charges')
    elif page == 'Count Plot':
        sns_count_plot(data, col)


# main 함수
def main():
    col = st.sidebar.selectbox(
        "📊 시각화를 할 컬럼을 선택해주세요",
        [
            'Age',
            'Sex',
            'Bmi',
            'Children',
            'Smoker',
            'Region'
        ]
    )

    if col in ['Age', 'Bmi', ]:
        number_graph(col.lower())
    else:
        category_graph(col.lower())


callout(['charges와 비교합니다.'])
line_break()
main()
