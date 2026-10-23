# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
- **Project title:** Student Performance Analytics System
- **Student name:** D Jaya Vardhan Reddy
- **Course:** Python with AI

## 2. Objective
The objective is to use Python, NumPy and Pandas to process student records and generate understandable summaries of marks, grades, pass/fail results, attendance and subject performance.

## 3. Technologies Used
- Python: program logic, functions, conditions and loops
- Pandas: reading CSV data and organizing/analyzing records
- NumPy: total and average calculations

## 4. Dataset Description
The starter dataset contains 20 illustrative student records. It includes student ID, name, department, marks in Python, Mathematics and Statistics, and attendance percentage. The data is sample data and does not represent actual students.

## 5. Implementation
1. Read `students.csv` into a Pandas DataFrame.
2. Check that required columns exist and that records are available.
3. Use NumPy to calculate each student's total and average marks.
4. Use a function and conditional statements to assign grades.
5. Use a loop and conditions to calculate pass/fail and attendance status.
6. Calculate class-level and subject-level statistics.
7. Display top performers and save the detailed results to a new CSV file.

## 6. Key Features
- Student dataset preview
- Total and average marks
- Grade assignment
- Pass/fail classification
- Class average, highest and lowest average
- Subject-wise average, highest and lowest marks
- Top five performers
- Attendance requirement check
- Export of calculated results

## 7. Output / Screenshots
DATASET PREVIEW
Student_ID         Name Department  Python  Mathematics  Statistics  Attendance_Percent
    STU001 Aarav Sharma        CSE      88           91          84                  92
    STU002   Diya Reddy       AIDS      76           82          79                  95
    STU003 Ishaan Kumar        ECE      67           72          70                  88
    STU004  Ananya Nair        CSE      95           94          97                  98
    STU005  Rohan Patel       AIDS      54           61          58                  78

Dataset shape: 20 rows, 7 columns

============================================================
STUDENT PERFORMANCE ANALYTICS SYSTEM
============================================================
Number of students: 20
Overall class average: 73.08
Highest student average: 96.00
Lowest student average: 37.67
Students passed: 18
Students failed: 2
Students meeting attendance requirement: 19

SUBJECT-WISE ANALYSIS
------------------------------------------------------------
Python: average=71.80, highest=98, lowest=33
Mathematics: average=73.50, highest=96, lowest=38
Statistics: average=73.95, highest=97, lowest=42
Best-performing subject: Statistics (73.95 average)

TOP 5 PERFORMERS
------------------------------------------------------------
Student_ID          Name Department  Average_Marks Grade
    STU020   Sara Thomas        CSE          96.00    A+
    STU004   Ananya Nair        CSE          95.33    A+
    STU008    Saanvi Rao       AIDS          90.00    A+
    STU013   Advik Verma        CSE          90.00    A+
    STU016 Myra Kulkarni        CSE          88.67     A

STUDENT RESULTS
------------------------------------------------------------
Student_ID           Name  Total_Marks  Average_Marks Grade Result Attendance_Status
    STU001   Aarav Sharma        263.0          87.67     A   Pass Meets requirement
    STU002     Diya Reddy        237.0          79.00     B   Pass Meets requirement
    STU003   Ishaan Kumar        209.0          69.67     C   Pass Meets requirement
    STU004    Ananya Nair        286.0          95.33    A+   Pass Meets requirement
    STU005    Rohan Patel        173.0          57.67     D   Pass Meets requirement
    STU006     Meera Iyer        249.0          83.00     A   Pass Meets requirement
    STU007    Kabir Singh        139.0          46.33     F   Fail Meets requirement
    STU008     Saanvi Rao        270.0          90.00    A+   Pass Meets requirement
    STU009      Arjun Das        215.0          71.67     B   Pass Meets requirement
    STU010      Ira Menon        185.0          61.67     C   Pass Meets requirement
    STU011   Vihaan Gupta        251.0          83.67     A   Pass Meets requirement
    STU012     Tara Joshi        141.0          47.00     F   Pass Meets requirement
    STU013    Advik Verma        270.0          90.00    A+   Pass Meets requirement
    STU014   Nisha Pillai        175.0          58.33     D   Pass Meets requirement
    STU015   Reyansh Shah        221.0          73.67     B   Pass Meets requirement
    STU016  Myra Kulkarni        266.0          88.67     A   Pass Meets requirement
    STU017   Dev Malhotra        113.0          37.67     F   Fail Below requirement
    STU018    Aadhya Bose        233.0          77.67     B   Pass Meets requirement
    STU019 Kian Fernandes        201.0          67.00     C   Pass Meets requirement
    STU020    Sara Thomas        288.0          96.00    A+   Pass Meets requirement

Saved detailed results to student_analysis_results.csv
PS C:\Users\Jaya Vardhan\Downloads\student-performance-analytics-starter\student-performance-analytics> ^C
PS C:\Users\Jaya Vardhan\Downloads\student-performance-analytics-starter\student-performance-analytics> python main.py
DATASET PREVIEW
------------------------------------------------------------
Student_ID         Name Department  Python  Mathematics  Statistics  Attendance_Percent
    STU001 Aarav Sharma        CSE      88           91          84                  92
    STU002   Diya Reddy       AIDS      76           82          79                  95
    STU003 Ishaan Kumar        ECE      67           72          70                  88
    STU004  Ananya Nair        CSE      95           94          97                  98
    STU005  Rohan Patel       AIDS      54           61          58                  78

Dataset shape: 20 rows, 7 columns

============================================================
STUDENT PERFORMANCE ANALYTICS SYSTEM
============================================================
Number of students: 20
Overall class average: 73.08
Highest student average: 96.00
Lowest student average: 37.67
Students passed: 18
Students failed: 2
Students meeting attendance requirement: 19
Students needing academic support: 3

STUDENTS NEEDING ACADEMIC SUPPORT
Student_ID         Name  Average_Marks
    STU007  Kabir Singh          46.33
    STU012   Tara Joshi          47.00
    STU017 Dev Malhotra          37.67

SUBJECT-WISE ANALYSIS
------------------------------------------------------------
Python: Average = 71.80, Highest = 98, Lowest = 33
Mathematics: Average = 73.50, Highest = 96, Lowest = 38
Statistics: Average = 73.95, Highest = 97, Lowest = 42

Subject averages in descending order:
Statistics     73.95
Mathematics    73.50
Python         71.80

Best-performing subject: Statistics (73.95)

TOP 5 PERFORMERS
------------------------------------------------------------
Student_ID          Name Department  Average_Marks Grade
    STU020   Sara Thomas        CSE          96.00    A+
    STU004   Ananya Nair        CSE          95.33    A+
    STU008    Saanvi Rao       AIDS          90.00    A+
    STU013   Advik Verma        CSE          90.00    A+
    STU016 Myra Kulkarni        CSE          88.67     A

COMPLETE STUDENT RESULTS
------------------------------------------------------------
Student_ID           Name  Total_Marks  Average_Marks Grade Result Attendance_Status
    STU001   Aarav Sharma        263.0          87.67     A   Pass Meets requirement
    STU002     Diya Reddy        237.0          79.00     B   Pass Meets requirement
    STU003   Ishaan Kumar        209.0          69.67     C   Pass Meets requirement
    STU004    Ananya Nair        286.0          95.33    A+   Pass Meets requirement
    STU005    Rohan Patel        173.0          57.67     D   Pass Meets requirement
    STU006     Meera Iyer        249.0          83.00     A   Pass Meets requirement
    STU007    Kabir Singh        139.0          46.33     F   Fail Meets requirement
    STU008     Saanvi Rao        270.0          90.00    A+   Pass Meets requirement
    STU009      Arjun Das        215.0          71.67     B   Pass Meets requirement
    STU010      Ira Menon        185.0          61.67     C   Pass Meets requirement
    STU011   Vihaan Gupta        251.0          83.67     A   Pass Meets requirement
    STU012     Tara Joshi        141.0          47.00     F   Pass Meets requirement
    STU013    Advik Verma        270.0          90.00    A+   Pass Meets requirement
    STU014   Nisha Pillai        175.0          58.33     D   Pass Meets requirement
    STU015   Reyansh Shah        221.0          73.67     B   Pass Meets requirement
    STU016  Myra Kulkarni        266.0          88.67     A   Pass Meets requirement
    STU017   Dev Malhotra        113.0          37.67     F   Fail Below requirement
    STU018    Aadhya Bose        233.0          77.67     B   Pass Meets requirement
    STU019 Kian Fernandes        201.0          67.00     C   Pass Meets requirement
    STU020    Sara Thomas        288.0          96.00    A+   Pass Meets requirement

Saved detailed results to student_analysis_results.csv


## 8. Final Outcome
SUBJECT-WISE ANALYSIS
------------------------------------------------------------
Python: Average = 71.80, Highest = 98, Lowest = 33
Mathematics: Average = 73.50, Highest = 96, Lowest = 38
Statistics: Average = 73.95, Highest = 97, Lowest = 42

## 9. Challenges and Learning
One challenge I faced while developing the Student Performance Analytics System was handling student marks and attendance data correctly. Missing values, invalid marks, or attendance percentages outside the valid range could lead to incorrect analysis.

I addressed this by implementing a data validation function using Pandas. The program checks for required columns, missing or invalid values, and ensures that marks and attendance percentages are between 0 and 100.

Another challenge was calculating student totals and averages efficiently. I used NumPy functions such as `np.sum()` and `np.mean()` to perform numerical calculations on the subject marks. I also used Python functions, loops, and conditional statements to assign grades, determine pass/fail status, and check attendance requirements.


Through this project, I learned how to:
- Use Python functions and loops to organize program logic.
- Apply conditional statements to assign grades and determine student results.
- Load and process CSV files using Pandas DataFrames.
- Use NumPy to calculate total and average marks.
- Validate data before performing analysis.
- Analyze subject-wise performance and identify top-performing students.
- Export processed results to a CSV file using Pandas.

This project helped me understand how Python, NumPy, and Pandas can be combined to build a practical data analytics application.

## 10. GitHub Repository

**Repository Name:** Student Performance Analytics System

**GitHub Repository URL:** https://github.com/jayavardhanreddy214/student-performance-analytics/tree/main

The repository contains the Python source code, student dataset, dependency file, README, and project documentation. It allows others to review the implementation and run the project locally.
