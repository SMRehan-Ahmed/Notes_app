# **Notes App**

A Flask-based web application for creating, storing, and managing notes with secure user authentication.

## **Table of Contents**
* Features
* Tech Stack
* Installation
* Usage
* Project Structure
* Code Overview

## **Features**
* **User Authentication**: Secure user registration and login using hashed passwords.
* **Note Management**: Create, view, and delete notes associated with your account.
* **Session Management**: Manage user sessions with login and logout features.
* **Flash Messages**: Display notifications for user actions like successful logins, errors, and note actions.

## **Tech Stack**
* **Flask**: A micro web framework used for building web applications in Python.
* **SQLAlchemy**: An ORM (Object-Relational Mapping) library for database interactions.
* **Flask-Login**: A library that handles user session management and authentication.
* **Werkzeug Security**: Provides utilities for hashing and checking passwords.
* **Jinja2**: A templating engine for rendering HTML templates with dynamic content.

## **Installation**
### **Clone the repository**:

git clone https://github.com/SMRehan-Ahmed/Notes_app
cd notes-app

### **Create a virtual environment**:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### **Install dependencies**:

pip install -r requirements.txt

### **Set up the database:**

flask db init
flask db migrate -m "Initial migration."
flask db upgrade

### **Run the application:**

python main.py

### **Access the app**: Open http://127.0.0.1:5000/ in your web browser.

## **Usage**
Sign Up: Create a new account to start using the app.
Login: Access your notes by logging in with your credentials.
Add Notes: Use the interface to create new notes.
Delete Notes: Easily remove notes you no longer need.




## **Project Structure**

![image](https://github.com/user-attachments/assets/5e75c0a2-01e8-400b-82f3-944c6d2e737c)


## **Code Overview**
main.py
The entry point of the application. It initializes the Flask app and runs the server.
website/__init__.py
Contains the application factory that initializes the Flask app and configures extensions.
website/models.py
Defines the database models: User and Note. User stores user data, and Note stores individual notes.
website/auth.py
Handles authentication-related routes: sign up, login, and logout. It uses Flask-Login to manage user sessions and Werkzeug Security for password hashing.
website/views.py
Contains the main routes for the application, including the homepage where users can add and manage their notes. The routes are protected by Flask-Login to ensure that only authenticated users can access them.
website/templates/
This folder contains the HTML templates rendered by the Flask app. The templates are powered by the Jinja2 templating engine, which allows dynamic content to be inserted into the HTML.

