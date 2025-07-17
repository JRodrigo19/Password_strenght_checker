# 🔐 Password Strength Checker

A Python CLI tool that evaluates password strength by checking:
- Character complexity (uppercase, lowercase, digits, symbols)
- Length (minimum and recommended)
- Whether the password exists in a known weak password list (`mrp4p3r`)

---

## 🚀 Features

✅ Real-time password strength feedback  
✅ Scoring from 0 to 100 based on complexity  
✅ Detects weak or predictable passwords using a curated Portuguese wordlist  
✅ Uses Python 3.10+ `match-case` for clean and modern syntax  
✅ Ready for cybersecurity portfolios and educational use

---

## 📚 Wordlist: `passwords_list.txt`

This file contains the **`mrp4p3r` wordlist**, a curated list of commonly used weak passwords in **Portuguese**. Examples include:

- 123456
- senha123
- meuamor
- brasil2023
- admin

If the entered password matches any line in this list, it will automatically be marked as weak:

<img width="810" height="185" alt="image" src="https://github.com/user-attachments/assets/8544e362-4e0a-4cac-9e65-b13d83215876" />

---

Wordlist Integration

  - The script will automatically load passwords_list.txt on startup.

  - If the file is missing, the script will notify the user and skip the weak password check.

---

⚙️ Requirements

  - Python 3.10 or higher

  - passwords_list.txt containing the mrp4p3r entries (one per line)

---

▶️ Running the Script

  - python password_strength_checker.py

  <img width="1034" height="189" alt="Captura de tela 2025-07-17 112230" src="https://github.com/user-attachments/assets/a58466ba-0597-4b09-8537-64539cc1a21d" />

---

🧪 Scoring Criteria:

  - Criterion	Points
  - Contains letters	+10
  - Contains uppercase	+30
  - Contains lowercase	+10
  - Contains digits	+10
  - Contains special characters	+30
  - Length 8–11 characters	+5
  - Length ≥ 12 characters	+10
  - Found in wordlist	0 (password is flagged as insecure)

---

📁 Project Structure

password_strength_checker/

├── password_strength_checker.py   # Main script

├── passwords_list.txt             # mrp4p3r wordlist (Portuguese weak passwords)

└── README.md                      # This documentation

---

💡 Use Cases

  - Red team password policy simulation
  - Internal security training (Portuguese-speaking users)
  - Cybersecurity student projects
  - Password auditing tools for localized targets

---

📜 License

  - MIT License — Free for personal and academic use. Use ethically.

---

👤 Author

  - Rodrigo Prazeres
  - Cybersecurity Analyst 
