# 🧮📂 File Sorter & Smart Calculator App

This project is a two-in-one Python application:

1. **File Sorter**: Organizes files in a selected folder by **extension**, **creation date**, or **filename keyword**.
2. **Smart Calculator**: Performs arithmetic operations with **error handling**, **operation history tracking**, and optional **GUI support**.

> Designed for learning, productivity, and daily utility!

---

## ✨ Features

### 📁 File Sorter
- Organize files by:
  - 🔠 **Extension** (e.g., `.txt`, `.jpg`, `.py`)
  - 📅 **Creation Date**
  - 🔍 **Keyword in Filename**
- Automatically creates folders and moves files into them.

### 🧮 Calculator (Console + Optional GUI)
- Supports:
  - ➕ Addition
  - ➖ Subtraction
  - ✖️ Multiplication
  - ➗ Division
- Handles invalid inputs and division by zero.
- Stores history in:
  - 📂 `logs/operation_log.txt`
  - 🗃️ `history.db` (SQLite database)
- Optional GUI using **Tkinter** with input field and result display.

---

## 🛠 Technologies Used

- **Python 3**
- **Tkinter** *(optional, for GUI)*
- **SQLite3**
- **Logging module**

---

## 📁 Project Structure

```
FileSorterCalculator/
├── file_sorter.py             # File sorting utility
├── calculator.py              # CLI calculator
├── calculator_gui.py          # GUI calculator (optional)
├── db_helper.py               # SQLite helper for history tracking
├── logs/
│   └── operation_log.txt      # Plain text log of calculations
├── history.db                 # SQLite database (auto-generated)
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## 🚀 Getting Started

### 🔸 1. Clone the Repository
```bash
git clone https://github.com/your-username/FileSorterCalculator.git
cd FileSorterCalculator
```

### 🔸 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install tk
```

### 🔸 3. Run File Sorter
```bash
python file_sorter.py
```

You’ll be prompted to enter the folder path and sorting method.

### 🔸 4. Run Calculator (Console)
```bash
python calculator.py
```

Enter expressions like `5 + 3` or `10 / 2`. Type `exit` to quit.

### 🔸 5. Run Calculator (GUI)
```bash
python calculator_gui.py
```

---

## 🧪 Example Usage

### CLI Calculator

**Input:**
```text
>> 7 * 6
```

**Output:**
```text
Result: 42
```

**Saved to:**
- `logs/operation_log.txt`
- `history.db`

---

## 💾 SQLite History

Operations are saved in a database:

```sql
Table: operations
---------------------
id INTEGER PRIMARY KEY
expression TEXT
result TEXT
timestamp DATETIME
```

To view:
- Use **DB Browser for SQLite**
- Or query directly:
```sql
SELECT * FROM operations;
```

---

## 📸 Screenshots

> Add your screenshots here

```
📷 FileSorter sorting directory...
📷 Calculator GUI performing 15 / 3...
```

---

## 🔍 requirements.txt

```
tk
```

---

## 📝 To-Do

- [ ] Add support for more operations (modulo, power, etc.)
- [ ] Display history in GUI
- [ ] Add progress/status bar in File Sorter
- [ ] Export history as CSV using Pandas

---

## 👩‍💻 Author

**Bandaru Nikitha**

- 💼 Passionate Python Developer
- 🛠️ Building productivity tools & smart apps

---

## 📄 License

This project is licensed under the **MIT License**.  
You’re free to use, modify, and distribute it with credit.

---

## ⭐️ Support

If you find this project helpful, consider ⭐️ starring the repo on GitHub!
