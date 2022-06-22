import streamlit as st
import pandas as pd
import numpy as np

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

st.balloons()

st.title('보험료 데이터 회귀 분석')

section1 = """
<div style="background-color: #2e6595;padding:5px;">
    <h4 style="padding:4px;color:white;">개요</h4>
</div>
"""
st.markdown(section1, unsafe_allow_html=True)

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     def lowercase(x): return str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data


# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)
