# ✈️ Flights Management & Analytics App

A Python-based Flight Management and Analytics application built using **Streamlit, Python OOP, and MySQL**. The application allows users to search and check flight information and explore airline-related insights through interactive data visualizations.

## 📌 Project Overview

The Flights Management & Analytics App is designed to provide a simple and interactive interface for accessing flight information and analyzing airline data.

The application is developed using Streamlit for the frontend, Python for application logic, Object-Oriented Programming (OOP) for code organization, and MySQL for database management.

It provides two main functionalities:

1. **Check Flights:** Allows users to search for flights and view matching flight details.
2. **Analytics:** Displays airline-related insights using interactive bar charts and visualizations.

## 🚀 Features

### 1. Check Flights

- Search and check available flight information.
- Retrieve flight records from the MySQL database.
- Display matching flight results in an organized format.
- Interact with flight information through a Streamlit interface.

### 2. Analytics Dashboard

- Explore airline-related data.
- View data insights through interactive bar charts.
- Understand airline frequency and distribution.
- Present database information in a visual and easy-to-understand format.

### 3. Database Integration

- MySQL database connectivity.
- SQL queries for retrieving flight information.
- Separate database operations from the main application code.
- Python-based database interaction.

### 4. Object-Oriented Programming

- Uses classes and methods to organize database operations.
- Separates application logic from database connectivity.
- Improves code readability, reusability, and maintainability.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| MySQL | Relational database management |
| SQL | Database queries and data retrieval |
| Python OOP | Code organization and reusability |
| Pandas | Data handling and processing |
| Plotly / Streamlit Charts | Data visualization |
| Python-dotenv | Environment variable management |
| Virtual Environment | Dependency isolation |

## 📂 Project Structure

```text
Flights-App/
│
├── app.py                 # Main Streamlit application
│
├── dbhelper.py            # MySQL database connection and SQL queries
│
├── .env                   # Database credentials and configuration
│
├── .gitignore             # Files excluded from Git tracking
│
├── requirements.txt       # Python project dependencies
│
└── .venv/                 # Python virtual environment
```

### File Explanation

**1. app.py**

The main application file responsible for the Streamlit user interface.

Responsibilities