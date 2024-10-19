# Screenplay Design Pattern with Python & Selenium
This project implements the Screenplay design pattern using Python and Selenium for end-to-end testing of web applications.

---

## 📁 Project Structure
screenplay-python-selenium/
├── src/
│   ├── 🎭 actors/
│   │   └── UserActor.py
│   │
│   ├── 🚀 actions/
│   │   └── Actions.py
│   │
│   ├── ❓ questions/
│   │   └── Questions.py
│   │
│   ├── 📜 scenarios/
│   │   └── LoginScenario.py
│   │
│   ├── 📊 data/
│   │   ├── users.json
│   │   └── urls.json
│   │
│   └── ⚙️ configs/
│       ├── WebdriverConfig.py
│       ├── UserCredentialsConfig.py
│       └── UrlManagerConfig.py
│
├── .gitignore
├── readme.md
└── requirements.txt


## Overview
- **🎭 actors/**: Contains actor classes that represent users interacting with the application.
- **🚀 actions/**: Contains actions that actors can perform, such as logging in.
- **❓ questions/**: Contains questions to retrieve information from the application.
- **📜 scenarios/**: Contains the scenarios that define the tests to be executed.
- **📊 data/**: Stores application-related data.
- **⚙️ configs/**: Contains configuration files for WebDriver setup and other settings.

---

## Install Dependencies

1. **Create a virtual environment:**
   ```bash
    python -m venv venv
   ```
   
2. **After creating the virtual environment, activate it using:**
- *Windows:*
  ```bash
  .\venv\Scripts\activate
  ```
- *MacOS:*
  ```bash
  source venv/bin/activate
  ```
  
3. **Install the required dependencies:**
  ```bash
  pip install -r requirements.txt
  ```