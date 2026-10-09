from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "quiz-application-secret-key"

# Question bank grouped by category.
QUESTION_BANK = {
    "Python": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "def", "function", "define"],
            "answer": "def"
        },
        {
            "question": "Which data type is used to store True or False?",
            "options": ["int", "str", "bool", "float"],
            "answer": "bool"
        },
        {
            "question": "What does len([10, 20, 30]) return?",
            "options": ["2", "3", "4", "30"],
            "answer": "3"
        },
        {
            "question": "Which symbol is used for a single-line comment in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": "#"
        },
        {
            "question": "Which method adds an item to the end of a list?",
            "options": ["add()", "insert()", "append()", "push()"],
            "answer": "append()"
        },
        {
            "question": "What is the output type of input() in Python?",
            "options": ["int", "float", "str", "bool"],
            "answer": "str"
        },
        {
            "question": "Which operator is used for exponentiation?",
            "options": ["^", "//", "**", "%%"],
            "answer": "**"
        },
        {
            "question": "Which collection stores key-value pairs?",
            "options": ["List", "Tuple", "Dictionary", "Set"],
            "answer": "Dictionary"
        },
        {
            "question": "What does == check in Python?",
            "options": ["Assignment", "Equality", "Identity only", "Addition"],
            "answer": "Equality"
        },
        {
            "question": "Which keyword is used to create a class?",
            "options": ["object", "class", "struct", "new"],
            "answer": "class"
        },
    ],
    "DBMS": [
        {
            "question": "What does DBMS stand for?",
            "options": ["Data Backup Management System", "Database Management System", "Database Memory System", "Data Base Machine System"],
            "answer": "Database Management System"
        },
        {
            "question": "Which key uniquely identifies a row?",
            "options": ["Foreign key", "Primary key", "Candidate value", "Normal key"],
            "answer": "Primary key"
        },
        {
            "question": "Which SQL command is used to retrieve data?",
            "options": ["GET", "SELECT", "FETCH", "SHOWROW"],
            "answer": "SELECT"
        },
        {
            "question": "Which JOIN returns matching rows from both tables?",
            "options": ["INNER JOIN", "FULL JOIN", "CROSS JOIN", "LEFT JOIN only"],
            "answer": "INNER JOIN"
        },
        {
            "question": "Which command adds a new row?",
            "options": ["INSERT", "ADD", "UPDATE", "CREATE"],
            "answer": "INSERT"
        },
        {
            "question": "What is a foreign key used for?",
            "options": ["To delete a database", "To create a relationship between tables", "To sort rows", "To encrypt data"],
            "answer": "To create a relationship between tables"
        },
        {
            "question": "Which SQL command changes existing data?",
            "options": ["CHANGE", "MODIFY", "UPDATE", "ALTERROW"],
            "answer": "UPDATE"
        },
        {
            "question": "Which normal form removes repeating groups?",
            "options": ["1NF", "2NF", "3NF", "BCNF"],
            "answer": "1NF"
        },
        {
            "question": "Which command removes a table completely?",
            "options": ["REMOVE", "DELETE TABLE", "DROP TABLE", "CLEAR"],
            "answer": "DROP TABLE"
        },
        {
            "question": "A row in a relational table is also called a:",
            "options": ["Attribute", "Tuple", "Domain", "Schema"],
            "answer": "Tuple"
        },
    ],
    "C Programming": [
        {
            "question": "Which function is the starting point of a C program?",
            "options": ["start()", "main()", "begin()", "run()"],
            "answer": "main()"
        },
        {
            "question": "Which symbol ends a C statement?",
            "options": [".", ":", ";", ","],
            "answer": ";"
        },
        {
            "question": "Which header file is commonly used for printf()?",
            "options": ["math.h", "stdio.h", "string.h", "stdlib.h"],
            "answer": "stdio.h"
        },
        {
            "question": "Which data type stores a single character?",
            "options": ["string", "char", "character", "text"],
            "answer": "char"
        },
        {
            "question": "Which operator is used to get the address of a variable?",
            "options": ["*", "&", "#", "@"],
            "answer": "&"
        },
        {
            "question": "Which loop is guaranteed to execute at least once?",
            "options": ["for", "while", "do-while", "nested for"],
            "answer": "do-while"
        },
        {
            "question": "Which keyword declares a constant variable?",
            "options": ["constant", "const", "fixed", "final"],
            "answer": "const"
        },
        {
            "question": "Which operator performs logical AND?",
            "options": ["&", "&&", "||", "!"],
            "answer": "&&"
        },
        {
            "question": "Which statement is used to make a decision?",
            "options": ["if", "scan", "print", "include"],
            "answer": "if"
        },
        {
            "question": "Which function is used to read formatted input?",
            "options": ["printf()", "scanf()", "input()", "read()"],
            "answer": "scanf()"
        },
    ],
    "General Knowledge": [
        {
            "question": "What is the capital of India?",
            "options": ["Mumbai", "New Delhi", "Bengaluru", "Chennai"],
            "answer": "New Delhi"
        },
        {
            "question": "How many days are there in a leap year?",
            "options": ["365", "366", "364", "360"],
            "answer": "366"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        },
        {
            "question": "How many continents are there?",
            "options": ["5", "6", "7", "8"],
            "answer": "7"
        },
        {
            "question": "Which is the largest ocean?",
            "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
            "answer": "Pacific"
        },
        {
            "question": "What is H2O commonly called?",
            "options": ["Oxygen", "Hydrogen", "Water", "Salt"],
            "answer": "Water"
        },
        {
            "question": "Which gas do plants mainly use during photosynthesis?",
            "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Carbon dioxide"
        },
        {
            "question": "How many hours are there in one day?",
            "options": ["12", "24", "36", "48"],
            "answer": "24"
        },
        {
            "question": "Which is the smallest prime number?",
            "options": ["0", "1", "2", "3"],
            "answer": "2"
        },
        {
            "question": "Which instrument is used to measure temperature?",
            "options": ["Barometer", "Thermometer", "Hygrometer", "Speedometer"],
            "answer": "Thermometer"
        },
    ],
}


@app.route("/")
def home():
    return render_template("index.html", categories=QUESTION_BANK.keys())


@app.route("/quiz", methods=["POST"])
def quiz():
    category = request.form.get("category")

    if category not in QUESTION_BANK:
        return redirect(url_for("home"))

    # Exactly 10 questions are displayed for every category.
    session["category"] = category
    session["questions"] = QUESTION_BANK[category]
    return render_template(
        "quiz.html",
        category=category,
        questions=QUESTION_BANK[category],
        time_limit=60
    )


@app.route("/result", methods=["POST"])
def result():
    category = session.get("category")
    questions = session.get("questions")

    if not category or not questions:
        return redirect(url_for("home"))

    score = 0
    user_answers = []

    for i, question in enumerate(questions):
        selected = request.form.get(f"question_{i}", "")
        user_answers.append(selected)

        if selected == question["answer"]:
            score += 1

    total = len(questions)
    percentage = round((score / total) * 100)

    if percentage >= 80:
        message = "Excellent work!"
    elif percentage >= 50:
        message = "Good attempt!"
    else:
        message = "Keep practicing!"

    return render_template(
        "result.html",
        category=category,
        score=score,
        total=total,
        percentage=percentage,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
