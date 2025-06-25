# Week-2-Task-File-Sorter-
# 🧮📂 File Sorter & Calculator App

This project is a dual-function Python utility that includes:

1. **File Sorter** — Automatically organizes files in a directory based on extension, filename keyword, or creation date.
2. **Smart Calculator** — Performs arithmetic operations via a command-line or optional GUI, with error handling and operation history stored using SQLite and logs.

---

## 📦 Features

### 🔹 File Sorter
- Sort files by:
  - File **extension** (e.g., `.txt`, `.jpg`)
  - **Creation date**
  - Filename **keyword**
- Useful for cleaning up messy folders or organizing project files.

### 🔹 Calculator
- Supports: **Addition**, **Subtraction**, **Multiplication**, **Division**
- Handles errors like:
  - Division by zero
  - Invalid input
- Stores operation history:
  - Text logs in `logs/operation_log.txt`
  - SQLite database (`history.db`)
- Optional: Simple **GUI** using Tkinter

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** (for optional GUI)
- **SQLite3** (for history logging)
- **Logging module** (for plain-text logs)

---

## 📁 Project Structure

