
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)

SUBJECTS = ["Python", "Mathematics", "Statistics"]
PASS_MARK = 40
MIN_ATTENDANCE = 75
SUPPORT_AVERAGE = 50

st.title("📊 Student Performance Analytics System")
st.write(
    "Analyze student marks, grades, attendance, "
    "subject performance, and academic support needs."
)

st.sidebar.header("Settings")
pass_mark = st.sidebar.slider("Minimum subject pass mark", 0, 100, PASS_MARK)
attendance_limit = st.sidebar.slider(
    "Minimum attendance (%)", 0, 100, MIN_ATTENDANCE
)
support_limit = st.sidebar.slider(
    "Academic support average below", 0, 100, SUPPORT_AVERAGE
)

uploaded_file = st.file_uploader(
    "Upload a student CSV file (optional)",
    type=["csv"]
)

try:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("students.csv")

    required = [
        "Student_ID", "Name", "Department",
        *SUBJECTS, "Attendance_Percent"
    ]

    missing = [col for col in required if col not in df.columns]

    if missing:
        st.error("Missing required columns: " + ", ".join(missing))
        st.stop()

    if df.empty:
        st.warning("The dataset has no student records.")
        st.stop()

    numeric_columns = SUBJECTS + ["Attendance_Percent"]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    if df[required].isnull().any().any():
        st.error("The dataset contains missing or invalid required values.")
        st.stop()

    invalid_range = any(
        not df[col].between(0, 100).all()
        for col in numeric_columns
    )

    if invalid_range:
        st.error("Marks and attendance must be between 0 and 100.")
        st.stop()

    results = df.copy()
    marks = results[SUBJECTS].to_numpy(dtype=float)

    results["Total_Marks"] = np.sum(marks, axis=1)
    results["Average_Marks"] = np.mean(marks, axis=1).round(2)

    def assign_grade(average):
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        return "F"

    results["Grade"] = results["Average_Marks"].apply(assign_grade)

    results["Result"] = results[SUBJECTS].ge(pass_mark).all(axis=1).map(
        {True: "Pass", False: "Fail"}
    )

    results["Attendance_Status"] = np.where(
        results["Attendance_Percent"] >= attendance_limit,
        "Meets requirement",
        "Below requirement"
    )

    st.success(f"Successfully analyzed {len(results)} student records.")

    st.subheader("Class Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Students", len(results))
    col2.metric("Class Average", f"{results['Average_Marks'].mean():.2f}")
    col3.metric("Passed", int((results["Result"] == "Pass").sum()))
    col4.metric("Failed", int((results["Result"] == "Fail").sum()))

    st.divider()

    st.subheader("Subject-wise Performance")

    subject_averages = (
        results[SUBJECTS].mean()
        .sort_values(ascending=False)
        .rename("Average Marks")
    )

    st.bar_chart(subject_averages)
    st.write("Subjects ranked by average marks:")
    st.dataframe(subject_averages.reset_index().rename(
        columns={"index": "Subject"}
    ), use_container_width=True)

    st.subheader("Top Performers")

    top_students = results.nlargest(5, "Average_Marks")

    st.dataframe(
        top_students[
            ["Student_ID", "Name", "Department", "Average_Marks", "Grade"]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Students Needing Academic Support")

    support_students = results[
        results["Average_Marks"] < support_limit
    ]

    if support_students.empty:
        st.info("No students fall below the selected average threshold.")
    else:
        st.dataframe(
            support_students[
                ["Student_ID", "Name", "Average_Marks", "Grade"]
            ],
            use_container_width=True,
            hide_index=True
        )

    st.subheader("All Student Results")

    departments = ["All"] + sorted(results["Department"].unique().tolist())
    selected_department = st.selectbox("Filter by department", departments)

    filtered = results.copy()

    if selected_department != "All":
        filtered = filtered[
            filtered["Department"] == selected_department
        ]

    st.dataframe(filtered, use_container_width=True, hide_index=True)

    csv_data = results.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download analyzed results as CSV",
        data=csv_data,
        file_name="student_analysis_results.csv",
        mime="text/csv"
    )

    st.caption(
        "Grades and pass/attendance thresholds follow the rules defined "
        "in this project. Sample student records are fictional."
    )

except FileNotFoundError:
    st.error("students.csv was not found. Add it to the project folder.")
except pd.errors.EmptyDataError:
    st.error("The CSV file is empty.")
except pd.errors.ParserError:
    st.error("The CSV file could not be read. Check its format.")
