import streamlit as st

st.set_page_config(page_title="데이터 소개", page_icon="👋")
st.title("데이터 소개 및 개요")

st.write("이 웹 애플리케이션은 사용자가 업로드한 CSV 데이터의 기술통계를 확인하고 시각화하는 도구입니다.")

# 데이터 설명 영역
st.info("""
**[AI 데이터 분석 요약: 학생 성적 데이터(Students Performance)]**
이 데이터셋은 총 1,000명의 학생을 대상으로 환경적 요인이 학업 성취도에 미치는 영향을 분석하기 위한 자료입니다.

* **인구통계 및 배경 변수:** 성별(gender), 인종/민족 그룹(race/ethnicity), 부모의 교육 수준(parental level of education), 점심 식사 지원 여부(lunch), 시험 대비 과정 수강 여부(test preparation course)
* **평가 지표 (수치형 데이터):** 수학 점수(math score), 읽기 점수(reading score), 쓰기 점수(writing score)

좌측 사이드바의 **'1 시각화'** 메뉴로 이동하여 `StudentsPerformance.csv` 파일을 업로드하시면, 각 과목 점수의 기술통계량과 데이터 분포(히스토그램)를 확인하실 수 있습니다.
""")