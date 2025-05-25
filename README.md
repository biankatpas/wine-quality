# 🍷 Wine Quality Classifier

This project is a web application built with **Streamlit** that uses a pre-trained Machine Learning model to predict wine quality ("Good" or "Bad") based on its physicochemical characteristics.

## 📁 Project Structure

```
/
|-- app.py                   # Streamlit application source code
|-- wine_model.pkl           # Trained Machine Learning model
|-- wine_quality.ipynb       # Notebook with exploratory analysis and model training
|-- requirements.txt         # List of Python dependencies
|-- README.md                # This file
```

## 📋 Prerequisites

Before you begin, ensure you have **Python 3.8 or higher** installed on your machine.

## ⚙️ Installation and Setup

Follow the steps below to set up and run the project in your local environment.

### 1. Clone the Repository

First, clone this repository to your local machine:
```bash
git clone <YOUR_GIT_REPOSITORY_URL>
cd <PROJECT_FOLDER_NAME>
```

### 2. Create and Activate a Virtual Environment (venv)

```bash
python -m venv venv
```

After creating it, you need to activate it:

```bash
source venv/bin/activate
```

After activation, you will see (venv) at the beginning of your terminal prompt.

### 3. Install Dependencies

With the virtual environment activated, install all the required libraries listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## ▶️ How to Run the Application

With the environment set up and dependencies installed, start the Streamlit application with the following command:

```bash
streamlit run app.py
```

After running the command, your web browser should automatically open a new tab with the application running. If it doesn't, the terminal will display the Local and Network URLs where the app is being served.
