
# 📝 To-Do App

![To-Do App Banner](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuPnZx5C2OuE-1iCN2pJrD9YqHoJ2c5ngAXt-BeRfX4kg9lOwlntVaqeut2wtM4BHCO0I&usqp=CAU)

A feature-rich, user-friendly To-Do List web application built with Django. Manage your tasks effectively with an intuitive interface, session management, and user authentication.

----------

## 🚀 Features

-   ✅ Add, update, and delete tasks.
-   👤 User authentication (signup, login, and logout).
-   🔒 Secure session management.
-   🌟 Mark tasks as completed or pending.
-   📱 Responsive design for desktop and mobile devices.
-   🎨 Attractive and customizable UI.


----------

## 🛠️ Technologies Used

-   **Backend**: Django (Python)
-   **Frontend**: HTML, CSS, Bootstrap
-   **Database**: SQLite (default) / Customizable for PostgreSQL or MySQL
-   **Others**:
    -   JavaScript for interactions
    -   Font Awesome for icons

----------

## 🚧 Project Structure

```plaintext
To-Do/
├── myproject/               # Main Django project directory
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project URLs
├── todo/                    # Main app directory
│   ├── templates/           # HTML templates
│   │   └── todo/
│   │       ├── task_list.html
│   │       └── login.html
│   ├── static/              # Static files (CSS, JS, images)
│   ├── models.py            # Task model
│   ├── views.py             # Application views
├── static/                  # Shared static files
├── templates/               # Shared templates
├── db.sqlite3               # SQLite database file
└── README.md                # Project documentation

```

----------

## 🖥️ Getting Started

### Prerequisites

-   Python 3.9+
-   Django 4.0+
-   A virtual environment setup (recommended)

### Installation Steps

1.  Clone the repository:
    
    ```bash
    git clone https://github.com/Rugwiroparfait/To-Do.git
    cd To-Do
    
    ```
    
2.  Create and activate a virtual environment:
    
    ```bash
    python -m venv env
    source env/bin/activate  # For Linux/MacOS
    env\Scripts\activate     # For Windows
    
    ```
    
3.  Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
4.  Apply migrations:
    
    ```bash
    python manage.py migrate
    
    ```
    
5.  Run the server:
    
    ```bash
    python manage.py runserver
    
    ```
    
6.  Open in your browser:
    
    ```
    http://127.0.0.1:8000/
    
    ```
    

----------

## 🏗️ How to Contribute

Contributions are welcome! Follow these steps:

1.  Fork the repository.
2.  Create a new branch:
    
    ```bash
    git checkout -b feature-name
    
    ```
    
3.  Commit your changes:
    
    ```bash
    git commit -m "Add your feature description"
    
    ```
    
4.  Push to your branch:
    
    ```bash
    git push origin feature-name
    
    ```
    
5.  Create a Pull Request.

----------

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/license/mit).

----------

## ✨ Acknowledgments

-   Thanks to the Django community for their incredible framework.
-   Inspired by popular task management tools.