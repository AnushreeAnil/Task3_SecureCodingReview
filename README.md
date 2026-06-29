# 🔒 Secure Coding Review - Python Login System

## 📌 Project Overview

This project demonstrates a **Secure Coding Review** of a simple Python-based login application. The objective is to identify common security vulnerabilities through manual code inspection, provide remediation recommendations, and demonstrate secure coding practices.

The project includes both an intentionally vulnerable implementation and an improved secure version for comparison.

---

## 🎯 Objectives

- Perform a secure code review of a Python application.
- Identify common security vulnerabilities.
- Explain the impact of each vulnerability.
- Implement secure coding techniques.
- Recommend best practices for developing secure applications.

---

## 🛠 Technologies Used

- Python 3
- SQLite
- hashlib (Password Hashing)
- Manual Code Review

---

## 📂 Project Structure

```
Task3_SecureCodingReview/
│
├── vulnerable_login.py
├── secure_login.py
├── Secure_Coding_Review_Report.pdf
├── README.md
└── screenshots/
```

---

## 🚨 Security Vulnerabilities Identified

- SQL Injection
- Hardcoded Credentials
- Plain Text Password Handling
- Information Disclosure through Error Messages
- Missing Input Validation

---

## ✅ Security Improvements

The secure version includes the following improvements:

- Parameterized SQL Queries
- Password Hashing using SHA-256
- Input Validation
- Generic Error Messages
- Proper Exception Handling
- Secure Database Connection Management

---

## 📊 Manual Security Review Summary

| Vulnerability            | Severity | Status |
| ------------------------ | -------- | ------ |
| SQL Injection            | High     | Fixed  |
| Hardcoded Credentials    | High     | Fixed  |
| Plain Text Password      | High     | Fixed  |
| Information Disclosure   | Medium   | Fixed  |
| Missing Input Validation | Medium   | Fixed  |

---

## 📷 Screenshots

Screenshots of the vulnerable code, secure code, and review report are available in the **screenshots** folder.

---

## 📄 Report

The complete findings, recommendations, and remediation steps are documented in:

**Secure_Coding_Review_Report.pdf**

---

## 👩‍💻 Author

**Anushree Anil**

CodeAlpha Cyber Security Internship – Task 3

---

## 📜 License

This project is created for educational and internship purposes only.
