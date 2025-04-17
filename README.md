# 🧮 Secure Calculator in Python

A simple yet robust desktop calculator built in Python using `Tkinter` for the graphical interface and `numexpr` for safe expression evaluation — a better alternative to `eval()`.

---

## 🚀 Features

- ✅ Intuitive graphical interface
- ✅ Secure mathematical expression evaluation
- ✅ Error handling via pop-up messages
- ✅ Supports standard operators: `+`, `-`, `*`, `/`, `^`
- ✅ Parentheses and decimal support
- ✅ Reset button (`C`)
- ✅ Auto-display of results

---

## 🛡️ Why "secure"?

Instead of using Python’s native `eval()` (which is risky in certain contexts), this project relies on `numexpr` to safely evaluate math expressions **without executing arbitrary code**. Perfect if you want to avoid code injection or accidental vulnerabilities.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/secure-calculator.git
cd secure-calculator
