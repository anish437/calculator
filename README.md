# 🧮 Python Terminal Calculator

A lightweight, continuous command-line calculator built with pure Python. This application allows users to chain multiple mathematical operations sequentially using previous results, mimicking a real pocket calculator directly inside the terminal.

## ✨ Features

- **Continuous Calculation:** Chain operations (`+`, `-`, `*`, `/`) seamlessly by passing the result of your last calculation into the next one.
- **Dynamic Control Flow:** Choose whether to keep calculating with your current total or reset to start a fresh sequence.
- **Dictionary-Mapped Functions:** Utilizes first-class Python functions mapped inside a dictionary for clean, modular, and scalable operation handling.
- **Clean Loop Execution:** Uses a traditional procedural `while` loop to manage user sessions dynamically without exiting prematurely.

## 🛠️ Tech Stack

- **Language:** Python 3.x (No external libraries required)

## 🏃‍♂️ Getting Started

Since this project runs entirely in the standard terminal, it requires zero external dependencies to install.

### 1. Clone the Repository

```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Run the Application

Execute the script using your local Python interpreter:

```bash
python calculator.py
```

*(Note: Replace `calculator.py` with whatever you named your file!)*

## 🕹️ How to Use

1. Enter your **first number** when prompted.
2. Select an operator from the displayed list (`+`, `-`, `*`, `/`).
3. Enter the **next number**.
4. View your result instantly.
5. Type `'y'` to continue using that result for your next math operation, or type `'n'` to reset/exit.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! If you want to expand this project, consider adding:
- Safety guards for division by zero (`n2 == 0`).
- Advanced operations like exponents (`**`) or modulo (`%`).
- Error handling for when a user types a letter instead of a number.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
