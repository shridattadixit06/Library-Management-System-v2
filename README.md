# 📚 Library Management System (Python + Tkinter)

A simple **GUI-based Library Management System** built using **Python and Tkinter**.  
This project allows users to **register books**, **lend books to students**, and **safely manage book returns** using a clean and modern graphical interface.

The system uses **file-based storage (`.txt` files)** and is designed as a **college-level mini project** or a beginner-friendly Python GUI application.

---

## ✨ Features

- 🔐 **Password-protected access**
- 📘 **Register books** under multiple categories:
  - Programming
  - Economics
  - Science
- 📤 **Lend books** to students using:
  - Student Name
  - USN
  - Book ID
- 📥 **Safe return system**
  - Book is returned **only if the Book ID exists in lending records**
  - Prevents accidental deletion of data
- 🎨 **Modern dark-themed GUI**
- 🖥️ **Fullscreen responsive window**
- 📂 **Simple file-based storage (no database required)**

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** – GUI framework
- **pymsgbox** – popup dialogs and alerts

---

## 📁 Project Structure

```
Library-Management-System/
│
├── main.py
├── science.txt
├── programming.txt
├── economics.txt
├── lend.txt
└── README.md
```

---

## ▶️ How to Run the Project

1. Install Python 3  
2. Install dependency:
   ```bash
   pip install pymsgbox
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## 🔑 Default Login Credentials

- **Password:** `123`

> You can change the password directly in the source code.

---

## 🎯 Project Highlights

- Beginner-friendly logic
- Clean and modern GUI
- Safe return logic to avoid data loss
- Suitable for college mini-projects

---

## 🚀 Future Enhancements

- SQLite database integration
- Search and view all books
- Due date and fine calculation
- User roles (Admin / Student)

---

## 👨‍💻 Author

**Shridatta Dixit**  
Computer Science Engineering Student

---

⭐ If you like this project, feel free to star the repository!
