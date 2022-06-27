import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from html_module import section, callout, line_break, title
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_log_error


st.set_page_config(
    page_title="Modeling | 사자동산",  # 전체 타이틀
    page_icon="🦁",  # 아이콘
)
title('Modeling')


# 데이터셋 로드 함수
@st.cache
def data_load():
    X_train = pd.read_csv('data/X_train.csv')
    y_train = pd.read_csv('data/y_train.csv')
    X_test = pd.read_csv('data/X_test.csv')
    y_test = pd.read_csv('data/y_test.csv')
    return X_train, X_test, y_train, y_test


# 파라미터 세팅 함수
def set_params(learning_rate, seed, metric, max_depth, n_estimators, subsample):
    params = {
        'learning_rate': learning_rate,
        'objective': 'regression',
        'metric': metric,
        'seed': seed,
        'max_depth': max_depth,
        'n_estimators': n_estimators,
        'subsample': subsample
    }
    return params


# 데이터셋 로드 함수
# @st.cache
def dataset_load(X_train, X_test, y_train, y_test):
    train_dataset = lgb.Dataset(X_train, y_train)
    test_dataset = lgb.Dataset(X_test, y_test)
    return train_dataset, test_dataset


# lgb 학습 함수
def train_lgb(train_dataset, test_dataset, params):
    lgb_model = lgb.train(
        params, train_dataset, 10000, test_dataset,
        verbose_eval=500, early_stopping_rounds=100
    )
    return lgb_model


# 손실함수 리턴 함수
def set_loss(y_test, y_predict):
    mae = mean_absolute_error(y_test, y_predict)
    mse = mean_squared_error(y_test, y_predict)
    rmse = mse ** 0.5
    rmsle = mean_squared_log_error(y_test, y_predict) ** 0.5
    return mae, mse, rmse, rmsle


# 손실함수 출력 함수
def print_loss(loss):
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("MAE", round(loss[0], 3))
    col2.metric("MSE", int(loss[1]))
    col3.metric("RMSE", round(loss[2], 3))
    col4.metric("RMSLE", round(loss[3], 5))


# 모델 회귀 그래프 그리기 함수
def print_re_graph(y_test, y_predict):
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_predict)
    ax.plot([1121.87, 63770.43], [1121.87, 63770.43], '--r')
    plt.xlabel("True Charges")
    plt.ylabel("Predicted Charges")
    plt.tight_layout()
    st.pyplot(fig)


section('개요')
callout(['LightGBM 사용'])
line_break()

section('파라미터 설정하여 모델링하기', 300)
col1, col2 = st.columns(2)
with col1:
    # metric = st.radio('metric', ['mae', 'mse', 'rmse'])
    metric = st.selectbox('metric', ('mae', 'mse', 'rmse'))
    line_break()
    learning_rate = float(st.slider('learning rate', 0.0, 1.0, 0.3))
    line_break()
    max_depth = int(st.slider('max depth', 1, 10, 5))

with col2:
    seed = int(st.slider('seed', 0, 100, 42))
    line_break()
    n_estimators = int(st.select_slider(
        'n_estimator', options=list(range(100, 501, 100))))
    line_break()
    subsample = float(st.slider('subsample', 0.0, 1.0, 0.7))


line_break()
model_btn = st.button('모델링 Start')
line_break()
X_train, X_test, y_train, y_test = data_load()
train_dataset, test_dataset = dataset_load(X_train, X_test, y_train, y_test)

if model_btn:
    params = set_params(learning_rate, seed, metric,
                        max_depth, n_estimators, subsample)

    # my_bar = st.progress(0)
    lgb_model_state = st.text('2분은 족히 넘게 걸립니다. 조금만 기다려 주세요 Loading...')
    lgb_model = train_lgb(train_dataset, test_dataset, params)
    # for percent_complete in range(100):
    # time.sleep(0.1)
    # my_bar.progress(percent_complete + 1)
    lgb_model_state.success("모델링 완료")

    y_predict = lgb_model.predict(X_test)
    loss = set_loss(y_test, y_predict)
    print_loss(loss)
    with st.expander("손실함수 그래프 보기 🔍"):
        print_re_graph(y_test, y_predict)
