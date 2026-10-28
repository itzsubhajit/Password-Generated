# Password-Generator
# 🔐 Random Password Generator & Strengthener

A password security web application built with **Python and Streamlit** that helps users generate random passwords and create modified variations of memorable words.

🌐 **Live Demo:** https://randompassword-generator.streamlit.app/

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://randompassword-generator.streamlit.app/)

## 📌 Project Overview

Creating strong and unique passwords is an important part of protecting online accounts. Secure passwords should be difficult to guess and should not be reused across multiple services.

This project provides a simple, interactive web application for generating random passwords with customizable settings and experimenting with password-strengthening techniques.

## ✨ Features

- **Random Password Generation:** Generate passwords using Python's cryptographically secure `secrets` module.
- **Custom Password Length:** Select the desired length of a generated password.
- **Character Customization:** Choose uppercase letters, lowercase letters, numbers, and special characters.
- **Password Strengthener:** Generate a modified variation of a word using character substitutions and random additions.
- **Strength Assessment:** Receive a basic password-strength estimate and improvement suggestions.
- **Interactive Interface:** Use a web-based interface built with Streamlit.
- **Security Awareness:** Learn about password length, uniqueness, and safer password practices.

## 🛠️ Technologies Used

- **Python** — Application logic and password generation.
- **Streamlit** — Interactive web interface.
- **Secrets** — Cryptographically secure random selection.
- **String** — Character sets for password generation.
- **Regular Expressions (`re`)** — Basic password-strength assessment.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Start the application

```bash
python -m streamlit run app.py
```

The application will normally open at:

`http://localhost:8501`

## 📂 Project Structure

```text
RandomPasswordGenerator/
├── app.py
├── requirements.txt
└── README.md
```

## 🔒 Security Considerations

- The random password generator uses Python's `secrets` module for secure random choices.
- Longer, unique, randomly generated passwords are recommended for important accounts.
- The password strength assessment is a heuristic, not a guarantee of security.
- The word-strengthening feature uses substitutions and random additions, but the original word may remain guessable.
- Never share passwords or commit real credentials to a public repository.

## 🔮 Future Enhancements

- Add a password entropy estimator.
- Add an option to exclude ambiguous characters.
- Support generating multiple passwords at once.
- Add passphrase generation.
- Improve password-strength analysis.
- Add downloadable password lists with appropriate security precautions.

## 🎯 Project Objective

The objective of this project is to demonstrate Python programming, secure random generation, interactive web application development, and basic password-security principles through a practical tool.

## 👨‍💻 Author

**Subhajit Pramanick**

Explore the live application: https://randompassword-generator.streamlit.app/

---

⭐ If you find this project useful, consider giving the repository a star.

