# Student Performance Analytics System

## Objective
A beginner-friendly Python data-analysis project that summarizes student marks, assigns grades, checks pass/fail status, analyzes subjects, and identifies top performers.

## Technologies
- Python
- NumPy
- Pandas

## Dataset
`students.csv` contains 20 sample records. Columns include student ID, name, department, marks in Python/Mathematics/Statistics, and attendance percentage. These are illustrative records, not real student results.

## Features
- Reads CSV data with Pandas
- Calculates total and average marks using NumPy
- Assigns grades using a clearly defined rule
- Checks pass/fail status
- Summarizes class and subject performance
- Lists top-performing students
- Saves calculated results to `student_analysis_results.csv`

## Project rules
- Grade: A+ (90+), A (80–89.99), B (70–79.99), C (60–69.99), D (50–59.99), F (below 50)
- Pass: at least 40 marks in every subject
- Attendance requirement: at least 75%
These are starter assumptions; change them if your trainer specifies different rules.

## Setup and run
1. Install Python 3.10 or later.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   python -m pip install pandas numpy
   ```
4. Run:
   ```bash
   python main.py
   ```

Keep `main.py` and `students.csv` in the same folder. The program writes `student_analysis_results.csv` after it runs.

## Before submission
- Run and test the code yourself.
- Understand and personalize the functions and grading rules.
- Add screenshots of your actual output to `screenshots/`.
- Complete `Project_Documentation.md` with your own details and what you learned.
- Verify the final repository and submission instructions with your trainer.
