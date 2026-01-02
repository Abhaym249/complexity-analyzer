Time & Space Complexity Analyzer
📌 Project Overview

The Time & Space Complexity Analyzer is an interactive tool that analyzes source code and provides an estimated time and space complexity along with a human-readable explanation.

The project is designed to help students and developers understand how their code behaves in terms of performance, making it especially useful for DSA learning, interview preparation, and academic evaluation.

🎯 Problem Statement

Understanding time and space complexity is challenging for beginners, especially when dealing with nested loops, recursion, and conditional logic.

This project automates complexity analysis and explains it in simple language, reducing manual effort and improving conceptual clarity.

✨ Key Features

Analyzes time complexity (Big-O notation)

Analyzes space complexity

Supports:

Loops

Nested loops

Conditional statements

Basic recursion patterns

Provides AI-based explanations of the result

Clean, interactive UI with modern design

Beginner-friendly output

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python

Framework: Flask

AI Integration: Gemini API

IDE: VS Code

⚙️ How It Works

User enters source code

Code is parsed and analyzed

Logical structures are detected

Time & space complexity are estimated

AI generates a clear explanation

Result is displayed on the UI

📂 Project Structure
complexity-analyzer/
│
├── app.py                     # Main Flask application
├── analyzer.py                # Core complexity analysis logic
├── ai_explainer.py            # AI-based explanation module
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
│
├── templates/
│   └── index.html             # Frontend interface
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── assets/
│       └── background.png
│
└── utils/
    └── helpers.py             # Utility functions

🚀 How to Run the Project

Clone the repository

git clone https://github.com/your-username/complexity-analyzer.git


Navigate to the project directory

cd complexity-analyzer


Install dependencies

pip install -r requirements.txt


Run the application

python app.py


Open your browser and visit:

http://127.0.0.1:5000/

🧪 Example Use Cases

Analyze DSA practice code

Understand nested loop behavior

Learn Big-O notation visually

Prepare for coding interviews

Academic project demonstration

🔮 Future Enhancements

Support for multiple programming languages

More accurate recursion analysis

AST-based parsing

Code visualization

Export results as PDF

👨‍💻 Author

Abhay Sharma
B.Tech Computer Science Engineering
Interests: DSA, AI, Full-Stack Development

📄 License

This project is developed for educational and academic purposes.
