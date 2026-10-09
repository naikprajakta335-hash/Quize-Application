Quiz Application
Problem Statement
Develop a quiz application in Python with category selection, 10 questions, a timer, score calculation, and a final result.
Assigned Feature Set
Feature Set A:
Category selection
10 questions
Timer
Score calculation
Final result
Features Implemented
Category selection
Exactly 10 questions for each category
60-second countdown timer
Automatic submission when time expires
Score calculation
Percentage calculation
Final result page
Option to take another quiz
Responsive basic frontend
Technologies Used
Python
Flask
HTML
CSS
JavaScript
AI Tools Used
ChatGPT
Important AI Prompt / AI Usage
Example prompt: "Create a beginner-friendly Flask quiz application using Python with category selection, 10 questions, a timer, score calculation and final result."
The generated code was reviewed and tested before use.
Instructions to Run the Project
1. Open the project folder
Open a terminal inside the quiz_application folder.
2. Create a virtual environment
Windows:
python -m venv test
3. Activate the virtual environment
Windows Command Prompt:
test\Scripts\activate
Windows PowerShell:
.\test\Scripts\Activate.ps1
4. Install Flask
pip install -r requirements.txt
5. Run the application
python app.py
6. Open in browser
http://127.0.0.1:5000
Project Structure
quiz_application/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── quiz.html
│   └── result.html
│
└── static/
    └── style.css
