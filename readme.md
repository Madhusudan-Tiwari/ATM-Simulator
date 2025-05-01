# 🏧 ATM Simulator

A basic command-line ATM Simulator built in Python. It supports account registration, secure login, and basic banking functions like checking balance, deposits, and withdrawals. User data is now stored persistently using a JSON file.

---

## ✅ Features Implemented

- [x] **User Registration**
  - Unique account number required
  - 4-digit PIN setup with validation
  - Initial deposit input with amount check
  - Now saved to a json file

- [x] **User Login**
  - PIN-authenticated access to accounts
  - Graceful error handling for wrong or invalid inputs

- [x] **Account Menu**
  - Balance check
  - Deposit & withdrawal
  - Logout & return to main menu

---

## 🛠️ Technologies Used

- Python 3.x
- Built-in data structures (dictionary)

---

## 🚀 How to Run

```bash
python main.py

```

## 🚀 Future Goals
 - Enhance Security: Implement encryption for storing sensitive data like PINs.

 - User Transactions History: Track and display user transaction history (deposits and withdrawals).

 - ATM Simulation with More Features: Add more functionalities like loan requests, fund transfer, and account statement generation.

 - Graphical User Interface (GUI): Create a GUI version of the ATM simulator using a library like Tkinter for a better user experience.

 - Unit Testing: Implement unit tests to ensure the system works correctly under different scenarios.

 - Error Handling: Improve error handling to make the program more robust against unexpected user inputs.