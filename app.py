import streamlit as st
import joblib
import pandas as pd
from timetable_generator import generate_timetable

# Load model and encoders
model = joblib.load("model/study_planner.pkl")
goal_encoder = joblib.load("model/goal_encoder.pkl")
skill_encoder = joblib.load("model/skill_encoder.pkl")
focus_encoder = joblib.load("model/focus_encoder.pkl")

# Title
st.title("AI-Powered Personalized Study Planner")

st.write(
    "Get a personalized study focus recommendation and timetable using Machine Learning."
)

# Inputs
year = st.selectbox(
    "Year of Study",
    [1, 2, 3, 4]
)

goal = st.selectbox(
    "Goal",
    list(goal_encoder.classes_)
)

hours = st.slider(
    "Available Study Hours Per Day",
    1,
    10,
    4
)

skill_level = st.selectbox(
    "Skill Level",
    list(skill_encoder.classes_)
)

study_time = st.selectbox(
    "Preferred Study Time",
    ["Morning", "Evening", "Night"]
)

sleep_hours = st.slider(
    "Sleep Hours",
    5,
    10,
    8
)

# Prediction Button
if st.button("Generate Recommendation"):

    goal_encoded = goal_encoder.transform([goal])[0]
    skill_encoded = skill_encoder.transform([skill_level])[0]

    input_data = pd.DataFrame(
        [[year, goal_encoded, hours, skill_encoded]],
        columns=[
            "year",
            "goal",
            "hours",
            "skill_level"
        ]
    )

    prediction = model.predict(input_data)

    focus = focus_encoder.inverse_transform(
        prediction
    )[0]

    st.success(
        f"Recommended Focus Area: {focus}"
    )

    # Timetable
    timetable = generate_timetable(
        focus,
        study_time
    )

    timetable_df = pd.DataFrame(
        timetable,
        columns=[
            "Time Slot",
            "Activity"
        ]
    )

    st.subheader("Suggested Study Plan")

    st.table(timetable_df)

    # Download CSV
    csv = timetable_df.to_csv(index=False)

    st.download_button(
        label="Download Timetable",
        data=csv,
        file_name="study_timetable.csv",
        mime="text/csv"
    )

    # Career Recommendation
    career_map = {
        "DSA": "Software Engineer",
        "ML Foundations": "Machine Learning Engineer",
        "ML Projects": "AI Engineer",
        "Deep Learning": "Deep Learning Engineer",
        "Research": "Research Scientist",
        "CP": "Competitive Programmer",
        "Core Subjects": "System Software Engineer",
        "Academics": "Academic Excellence Track"
    }

    career = career_map.get(
        focus,
        "Technology Professional"
    )

    st.subheader("Recommended Career Path")

    st.info(career)

    # Summary
    st.subheader("Study Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Study Hours",
            f"{hours} hrs/day"
        )

    with col2:
        st.metric(
            "Sleep Hours",
            f"{sleep_hours} hrs/day"
        )

    with col3:
        st.metric(
            "Focus Area",
            focus
        )

    completion = (hours / (24 - sleep_hours)) * 100

    st.write(
        f"Daily Study Utilization: {completion:.1f}%"
    )

    st.progress(
        min(completion / 100, 1.0)
    )

    st.subheader("ℹ About This Project")

    st.write(
        """
        This project uses Machine Learning to recommend
        personalized study focus areas and generate
        customized study schedules based on a student's
        goals, academic year, skill level, and available
        study time.
        """
    )