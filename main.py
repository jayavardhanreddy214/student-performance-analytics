
"""
Student Performance Analytics System
Technologies: Python, NumPy, Pandas
"""

import numpy as np
import pandas as pd

DATA_FILE = "students.csv"

SUBJECTS = ["Python", "Mathematics", "Statistics"]

PASS_MARK = 40
MIN_ATTENDANCE = 75
SUPPORT_AVERAGE = 50


# 1. Assign grades based on average marks
def assign_grade(average):
    """Assign a grade according to the student's average."""

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
    else:
        return "F"


# 2. Validate the dataset
def validate_data(df):
    """Check required columns, missing data and valid ranges."""

    required_columns = [
        "Student_ID",
        "Name",
        "Department",
        *SUBJECTS,
        "Attendance_Percent"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        print("Error: Missing columns:", ", ".join(missing_columns))
        return False

    if df.empty:
        print("Error: The dataset contains no student records.")
        return False

    # Convert marks and attendance to numeric values.
    numeric_columns = SUBJECTS + ["Attendance_Percent"]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Check for missing or non-numeric values.
    if df[required_columns].isnull().any().any():
        print("Error: Missing or invalid values found.")

        print("\nMissing/invalid values by column:")
        print(df[required_columns].isnull().sum())

        return False

    # Check that marks are between 0 and 100.
    for subject in SUBJECTS:
        if not df[subject].between(0, 100).all():
            print(
                f"Error: {subject} marks must be between 0 and 100."
            )
            return False

    # Check attendance range.
    if not df["Attendance_Percent"].between(0, 100).all():
        print("Error: Attendance must be between 0 and 100.")
        return False

    return True


# 3. Calculate student results
def calculate_student_results(df):
    """Calculate totals, averages, grades and student status."""

    result = df.copy()

    # NumPy numerical calculations.
    marks = result[SUBJECTS].to_numpy(dtype=float)

    result["Total_Marks"] = np.sum(marks, axis=1)
    result["Average_Marks"] = np.mean(marks, axis=1).round(2)

    grades = []
    pass_status = []
    attendance_status = []

    # Loop through every student.
    for _, student in result.iterrows():

        # Assign grade.
        grades.append(
            assign_grade(student["Average_Marks"])
        )

        # A student must pass every subject.
        if all(
            student[subject] >= PASS_MARK
            for subject in SUBJECTS
        ):
            pass_status.append("Pass")
        else:
            pass_status.append("Fail")

        # Check attendance requirement.
        if student["Attendance_Percent"] >= MIN_ATTENDANCE:
            attendance_status.append("Meets requirement")
        else:
            attendance_status.append("Below requirement")

    result["Grade"] = grades
    result["Result"] = pass_status
    result["Attendance_Status"] = attendance_status

    return result


# 4. Display overall class statistics
def show_overall_summary(results):
    """Display overall performance statistics."""

    print("\n" + "=" * 60)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 60)

    print(f"Number of students: {len(results)}")

    print(
        f"Overall class average: "
        f"{results['Average_Marks'].mean():.2f}"
    )

    print(
        f"Highest student average: "
        f"{results['Average_Marks'].max():.2f}"
    )

    print(
        f"Lowest student average: "
        f"{results['Average_Marks'].min():.2f}"
    )

    passed = (results["Result"] == "Pass").sum()
    failed = (results["Result"] == "Fail").sum()

    print(f"Students passed: {passed}")
    print(f"Students failed: {failed}")

    attendance_count = (
        results["Attendance_Status"] == "Meets requirement"
    ).sum()

    print(
        f"Students meeting attendance requirement: "
        f"{attendance_count}"
    )

    # Identify students needing academic support.
    support_students = results[
        results["Average_Marks"] < SUPPORT_AVERAGE
    ]

    print(
        f"Students needing academic support: "
        f"{len(support_students)}"
    )

    if not support_students.empty:
        print("\nSTUDENTS NEEDING ACADEMIC SUPPORT")

        print(
            support_students[
                ["Student_ID", "Name", "Average_Marks"]
            ].to_string(index=False)
        )


# 5. Subject-wise performance analysis
def show_subject_analysis(results):
    """Analyze and rank subjects by their average marks."""

    print("\nSUBJECT-WISE ANALYSIS")
    print("-" * 60)

    for subject in SUBJECTS:
        average = results[subject].mean()
        highest = results[subject].max()
        lowest = results[subject].min()

        print(
            f"{subject}: "
            f"Average = {average:.2f}, "
            f"Highest = {highest:.0f}, "
            f"Lowest = {lowest:.0f}"
        )

    # Rank subjects from highest to lowest average.
    subject_averages = results[SUBJECTS].mean()

    print("\nSubject averages in descending order:")

    print(
        subject_averages.sort_values(
            ascending=False
        ).round(2).to_string()
    )

    best_subject = subject_averages.idxmax()

    print(
        f"\nBest-performing subject: {best_subject} "
        f"({subject_averages.max():.2f})"
    )


# 6. Display top-performing students
def show_top_performers(results, number=5):
    """Display students with the highest average marks."""

    print(f"\nTOP {number} PERFORMERS")
    print("-" * 60)

    top_students = results.nlargest(
        number, "Average_Marks"
    )

    print(
        top_students[
            [
                "Student_ID",
                "Name",
                "Department",
                "Average_Marks",
                "Grade"
            ]
        ].to_string(index=False)
    )


# 7. Display complete student results
def show_student_results(results):
    """Display calculated results for every student."""

    print("\nCOMPLETE STUDENT RESULTS")
    print("-" * 60)

    columns = [
        "Student_ID",
        "Name",
        "Total_Marks",
        "Average_Marks",
        "Grade",
        "Result",
        "Attendance_Status"
    ]

    print(results[columns].to_string(index=False))


# 8. Main program
def main():
    """Load data, perform validation, analyze and save results."""

    try:
        df = pd.read_csv(DATA_FILE)

    except FileNotFoundError:
        print(
            f"Error: {DATA_FILE} not found. "
            "Keep it in the same folder as main.py."
        )
        return

    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return

    except pd.errors.ParserError:
        print("Error: Unable to read the CSV file format.")
        return

    # Validate the input data.
    if not validate_data(df):
        print("\nPlease correct the dataset and run again.")
        return

    # Display dataset preview.
    print("DATASET PREVIEW")
    print("-" * 60)

    print(df.head().to_string(index=False))

    print(
        f"\nDataset shape: {df.shape[0]} rows, "
        f"{df.shape[1]} columns"
    )

    # Process the data.
    results = calculate_student_results(df)

    # Display analysis.
    show_overall_summary(results)
    show_subject_analysis(results)
    show_top_performers(results)
    show_student_results(results)

    # Save the detailed results.
    try:
        results.to_csv(
            "student_analysis_results.csv",
            index=False
        )

        print(
            "\nSaved detailed results to "
            "student_analysis_results.csv"
        )

    except OSError as error:
        print(f"\nError saving results: {error}")


# Run the program.
if __name__ == "__main__":
    main()
