import streamlit as st
from datetime import date

st.set_page_config(page_title="AI Study Planner", page_icon="📚")

st.title("📚 AI-Based Smart Study Planner")

num_subjects = st.number_input(
    "Number of Subjects",
    min_value=1,
    max_value=10,
    value=1
)

subjects = []

for i in range(int(num_subjects)):
    st.subheader(f"Subject {i+1}")

    name = st.text_input(
        f"Subject Name {i+1}",
        key=f"name_{i}"
    )

    exam_date = st.date_input(
        f"Exam Date {i+1}",
        key=f"date_{i}"
    )

    difficulty = st.selectbox(
        f"Difficulty {i+1}",
        ["Easy", "Medium", "Hard"],
        key=f"diff_{i}"
    )

    subjects.append({
        "name": name,
        "exam_date": exam_date,
        "difficulty": difficulty
    })

study_hours = st.number_input(
    "Available Study Hours Per Day",
    min_value=1,
    max_value=24,
    value=4
)

if st.button("Generate Study Plan"):

    today = date.today()

    st.header("📅 Study Plan")

    for subject in subjects:

        days_left = (subject["exam_date"] - today).days

        if subject["difficulty"] == "Hard":
            recommended_hours = study_hours * 0.5
        elif subject["difficulty"] == "Medium":
            recommended_hours = study_hours * 0.3
        else:
            recommended_hours = study_hours * 0.2

        st.write("---")
        st.write(f"### 📖 {subject['name']}")
        st.write(f"📅 Exam Date: {subject['exam_date']}")
        st.write(f"⏳ Days Left: {days_left}")
        st.write(f"🎯 Difficulty: {subject['difficulty']}")
        st.write(f"🕒 Recommended Study Hours: {recommended_hours:.1f} hrs/day")

    st.success("Study Plan Generated Successfully!")
    st.balloons()
