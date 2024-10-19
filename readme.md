# Screenplay Design Pattern with Python & Selenium
This project implements the Screenplay design pattern using Python and Selenium for end-to-end testing of web applications.

---

## 📁 Project Structure
screenplay-python-selenium/
├── src/
│   ├── 🎭 actors/
│   │    └── UserActor.py
│   │
│   ├── 🚀 actions/
│   │    ├── account/
│   │    │   ├── LoginActions.py
│   │    │   └── LogoutActions.py
│   │    └── invoice/
│   │        └── InvoiceActions.py
│   │    
│   ├── 🖱️ interactions/
│   │    └── Interactions.py
│   │
│   ├── ❓ questions/
│   │    ├── account/
│   │    │   ├── LoginQuestions.py
│   │    │   └── LogoutQuestions.py
│   │    └── invoice/
│   │        └── InvoiceQuestions.py
│   │
│   ├── 📜 scenarios/
│   │    └── LoginScenario.py
│   │
│   ├── 📊 data/
│   │    ├── users.json
│   │    └── urls.json
│   │
│   └── ⚙️ configs/
│        ├── WebdriverConfig.py
│        ├── UserCredentialsConfig.py
│        └── UrlManagerConfig.py
│
├── .gitignore
├── readme.md
└── requirements.txt


## Overview
🎭 actors/: Contains actor classes that represent users interacting with the application. Each actor encapsulates specific behaviors and data, allowing for a clear modeling of user interactions.

🚀 actions/: Houses the actions that actors can perform, organized by functionality. Each module includes specific functions for carrying out tasks.

🖱️ interactions/: Contains the Interactions, which defines generic methods for interacting with user interface elements, facilitating code reuse across different scenarios.

❓ questions/: Organizes the questions that actors can ask to retrieve information from the application, also categorized by functionality, enabling efficient data retrieval and validations.

📜 scenarios/: Contains scripts that define test scenarios,outlining the sequence of actions that actors should follow to perform specific application tests.

📊 data/: Stores relevant data for testing, allowing for easy modification and management of the data used during tests.

⚙️ configs/: Includes configuration files that manage WebDriver setup, user credentials, and URL management. These files centralize configuration definitions, making it easier to maintain and customize tests.

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