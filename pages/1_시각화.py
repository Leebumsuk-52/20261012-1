import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 데이터 시각화 및 통계")
st.write("분석할 CSV 파일을 업로드해 주세요.")

# 1. 파일 업로드 기능
uploaded_file = st.file_uploader("CSV 파일 업로드", type=['csv'])

if uploaded_file is not None:
    # 데이터 읽기
    df = pd.read_csv(uploaded_file)
    
    st.divider()
    st.subheader("1. 데이터 미리보기")
    st.dataframe(df.head())
    
    # 2. 기술통계량 출력
    st.subheader("2. 기술통계 요약")
    st.write(df.describe())
    
    st.divider()
    
    # 3. Plotly 라이브러리를 활용한 변수 시각화
    st.subheader("3. 변수 시각화 (Plotly)")
    
    # 숫자형 데이터 컬럼만 추출
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if len(numeric_cols) > 0:
        selected_col = st.selectbox("시각화할 변수를 선택하세요", numeric_cols)
        
        # Plotly 히스토그램 생성
        fig = px.histogram(df, x=selected_col, title=f"{selected_col} 데이터 분포", template="plotly_white")
        st.plotly_chart(fig)
    else:
        st.warning("시각화할 수 있는 숫자형 변수가 데이터에 없습니다.")