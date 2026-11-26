# 🎓 Student Grade Analyzer Using Python

A beginner-friendly web application that helps students calculate their academic performance by entering subject marks. The application automatically calculates total marks, average, grade and pass/fail status, with downloadable PDF and PNG result reports.

## 🚀 Features

- **Student Welcome Page** – Simple and user-friendly interface.
- **Subject Marks Entry** – Enter student name, subject names and marks.
- **Dynamic Subject Addition** – Add multiple subjects using the Add Subject button.
- **Automatic Calculations** – Calculate total marks and average.
- **Grade Evaluation** – Automatically assign grades based on average marks.
- **Pass/Fail Evaluation** – Check whether the student passes or fails.
- **Result Display** – View a complete academic performance report.
- **PDF Download** – Download the academic result as a PDF.
- **PNG Download** – Save the result as an image.
- **Input Validation** – Prevent blank names, duplicate subjects and invalid marks.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Grade calculations and backend logic |
| Flask | Backend API |
| Flask-CORS | Frontend and backend communication |
| HTML | Frontend structure |
| CSS | User interface design |
| JavaScript | Frontend functionality and API integration |
| html2canvas | PNG export |
| jsPDF | PDF export |

## 📁 Project Structure

```text
student-grade-analyzer-using-python/
│
├── backend/
│   ├── app.py
│   └── grade_calculator.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── main.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shyamkailash/Student-Grade-Analyzer-Using-Python.git
```

### 2. Navigate to the project folder

```bash
cd student-grade-analyzer-using-python
```

### 3. Install backend dependencies

```bash
py -m pip install flask flask-cors
```

### 4. Start the Flask backend

```bash
py backend/app.py
```

The backend will run at:

```text
http://127.0.0.1:5000/
```

### 5. Start the frontend

- Open the `frontend` folder in VS Code.
- Open `index.html`.
- Right-click and select **Open with Live Server**.
- The application will open in your browser.

Keep the Flask backend running while using the frontend.

## 📊 Grade Calculation Rules

The application uses the following grading criteria:

| Average Marks | Grade |
|---|---|
| 90–100 | A |
| 80–89.99 | B |
| 70–79.99 | C |
| 60–69.99 | D |
| Below 60 | F |

**Pass/Fail Criteria:**

- PASS – Every subject mark must be at least 40.
- FAIL – If any subject mark is below 40.

## 🔄 Application Workflow

1. Student opens the application.
2. Clicks the Get Started button.
3. Enters their name and subject marks.
4. Adds additional subjects if required.
5. Submits the marks.
6. Flask processes the submitted data.
7. Python calculates the academic results.
8. The frontend displays the result.
9. Student downloads the report as PDF or PNG.

## 🔌 Backend API

**Endpoint:** `POST /api/calculate`

Example request:

```json
{
  "student_name": "Shyam",
  "marks": {
    "NLP": 98,
    "FCV": 87,
    "SE": 89,
    "CN": 75
  }
}
```

Example response:

```json
{
  "student_name": "Shyam",
  "subjects": {
    "NLP": 98,
    "FCV": 87,
    "SE": 89,
    "CN": 75
  },
  "total": 349,
  "average": 87.25,
  "grade": "B",
  "result": "PASS"
}
```

## 🧪 Input Validation

The application validates:

- Empty student names.
- Empty subject names.
- Duplicate subject names.
- Marks below 0.
- Marks above 100.
- Missing subject marks.
- At least one subject must be entered.

## 🎯 Learning Outcomes

Through this project, I practised:

- Python functions and dictionaries.
- Conditional statements and loops.
- Input validation and exception handling.
- Flask REST API development.
- Frontend and backend integration.
- JavaScript Fetch API.
- Generating downloadable PDF and PNG reports.

## 🔮 Future Enhancements

- Bulk student marks upload using CSV files.
- Class-wise student performance reports.
- Roll number management.
- Class performance statistics.
- Student result comparison.

## 👨‍💻 Author

**Shyam Kailash S**

B.Tech – Artificial Intelligence and Machine Learning

GitHub: [@shyamkailash](https://github.com/shyamkailash)

---

*Built as part of the Student Grade Analyzer Python internship module.*