import streamlit as st
import pandas as pd
import numpy as np


# section 함수
def section(text):
    html = f"""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <br/>
        <div style="
            width:200px;
            background: rgb(220,172,255);
            background: linear-gradient(20deg, rgba(220,172,255,1) 0%, rgba(105,146,230,1) 100%);
            padding:7px;
            border:none;
            border-radius:10px;
        ">
            <h4 style="padding:4px;color:white;cursor:default;">
                <i class="fa-solid fa-magnifying-glass"></i>
                &nbsp;{text}
            </h4>
        </div>
    """
    return st.markdown(html, unsafe_allow_html=True)


# callout text 함수
def callout(text_list):
    html = """
        <div style="
            background-color:#eee;
            color:#666;
            padding: 20px;
            border-radius:3px;
            margin-top: 7px;
            box-shadow: 1px 1px 2px 1px rgba(0, 0, 0, 0.125);
        ">
        """
    for text in text_list:
        html += f'<span>{text}</span><br/>'
    html += "</div>"
    return st.markdown(html, unsafe_allow_html=True)


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


st.balloons() # 풍선 효과
st.title('보험료 데이터 회귀 분석') # title


# 개요 section
section('개요')
callout(['안녕하세요!', '간략한 프로젝트 개요 설명입니다.'])


# other section ...
section('데이터 출처')
section('분석 방향')
section('결과')


# texi
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
