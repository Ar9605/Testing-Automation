# 🧪 Selenium Testing Automation Project

This project automates website testing using **Python**, **Selenium**, and **Pytest**.  
It is designed to test common web form elements such as **text boxes, checkboxes, and buttons**, ensuring that they function correctly and reliably.  
The project demonstrates a structured automation testing workflow that can easily scale to larger web applications.

---

## 🚀 Features

- Automated browser interactions using **Selenium WebDriver**
- Modular design with reusable test fixtures (`conftest.py`)
- Automated testing of:
  - Textbox inputs and validation
  - Form submissions
  - Button clicks and element presence
- Integration with **Pytest** for easy test execution and reporting
- Compatible with **Chrome**, **Edge**, and **Firefox** browsers

---

## 🧩 Project Structure

selenium_automation_project/
│
├── conftest.py # Common setup and teardown for all test cases
├── test_form_submission.py # Tests form elements and submission functionality
├── textbox_submission.py # Tests textbox and input field validation
├── requirements.txt # List of dependencies
└── README.md # Project documentation

---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/Ar9605/Testing-Automation.git
cd Testing-Automation

2. Create and activate a virtual environment
python -m venv selenium_env
Windows:
selenium_env\Scripts\activate
Mac/Linux:
source selenium_env/bin/activate

3. Install dependencies
pip install -r requirements.txt

🧠 How to Run Tests
Run all tests:
pytest -v

Run a specific test file:
pytest test_form_submission.py -v

Generate an HTML test report:
pytest --html=report.html --self-contained-html

🧰 Tech Stack
Language: Python
Testing Framework: Pytest
Automation Tool: Selenium WebDriver
Driver Management: WebDriver Manager
Report Generation: Pytest-HTML

📸 Example Test Scenarios
Open a target webpage automatically
Fill out a form with valid/invalid data
Validate textbox input fields
Click buttons and verify expected output
Capture and log results

🧑‍💻 Author
Abhinav Raj
Python Developer | Automation & Data Enthusiast
📧 abhinav.raj6@tcs.com
