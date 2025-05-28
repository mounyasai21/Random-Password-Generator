
# Random Password Generator

This **Random Password Generator** is a Python-based application designed to generate secure, random passwords based on user-defined criteria. It offers both a **command-line** version (basic) and an enhanced **Graphical User Interface (GUI)** version built with Tkinter.

## 🚀 Features

### ✅ Basic Functionality (Command-Line Logic Behind the GUI)

* Generate random passwords of customizable length.
* Choose to include:

  * Uppercase letters
  * Lowercase letters
  * Digits
  * Symbols
* Exclude similar/confusing characters like `I`, `l`, `1`, `O`, `0`.
* Exclude custom characters entered by the user.

###  Advanced Functionality (GUI-Based)

* User-friendly GUI built using **Tkinter**.
* Select password length and complexity through checkboxes and input fields.
* **Password Strength Meter** that evaluates password quality.
* **Copy to Clipboard** with a single click.
* **Save Password to File** with timestamped entries.
* Customization of character exclusions for enhanced password control.

---

##  Key Concepts & Challenges Addressed

 Concept                    Description                                                         
 -------------------------  ------------------------------------------------------------------- 
 🔄 Randomization         -  Randomly generates secure passwords using Python's `random` module. 
 ✅ Input Validation      -  Ensures password length and character selections are valid.        
 🔡 Character Set Handling - Dynamically builds the character pool based on user preferences.    
 🖼 GUI Design             - Clean, intuitive interface using **Tkinter** widgets.               
 🔐 Security Rules         - Password strength scoring based on composition and length.          
 📋 Clipboard Integration  - Seamlessly copies password using the `pyperclip` module.            
 ⚙️ Customization           -Advanced settings for excluding confusing or unwanted characters.   


## 🛠 Requirements

* Python 3.x
* Tkinter (comes pre-installed with Python)
* `pyperclip`
  Install using:

  ```bash
  pip install pyperclip
  ```



## 📌 Future Improvements

* Add support for password categories (e.g., banking, social).
* Add option to show/hide password while typing.
* Implement encryption for saved passwords.
* Add theme customization and export/import settings.


## Output Screens
![Screenshot 2025-05-28 234241](https://github.com/user-attachments/assets/ef324ce8-aaa9-414f-b444-251c6aaa57fa)
![Screenshot 2025-05-28 234323](https://github.com/user-attachments/assets/bdf063a3-4fc6-4318-b955-33a99525a282)
![Screenshot 2025-05-28 234414](https://github.com/user-attachments/assets/11c1b824-f088-47b4-998e-e797238def9a)
![Screenshot 2025-05-28 234605](https://github.com/user-attachments/assets/9a64e4b7-1d83-4b94-9070-ca0e90ee018e)

## Video Reference


https://github.com/user-attachments/assets/71ed0d26-af09-437c-a27f-c81d033ed749

