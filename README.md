# Flask-Project

Flask-Project is a web application built with Flask for managing employees. The application allows users to list, register, edit, and remove employees. It also includes logging and error handling to ensure smooth operation.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#Technologies-Used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project is designed to help manage employee data efficiently. It provides a user-friendly interface for performing CRUD (Create, Read, Update, Delete) operations on employee records. The application uses Flask for the backend, SQLAlchemy for database(Postgress) interactions, and Bootstrap for styling.

### Project Structure
The project is organized into several modules:

- **Models:** Defines the database models for the application.
- **Views:** Contains the route handlers and view functions for the application.
- **Forms:** Defines the forms used in the application.
- **Services:** Contains the business logic for manipulating data from the models.
- **Templates:** Contains the HTML templates for rendering the views.
- **Static:** Contains static files such as CSS, JavaScript, and images.
- **log** Contains logs file with actions, info, warning and erros

## Technologies Used

- **Flask:** A lightweight WSGI web application framework.
- **SQLAlchemy:** An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Flask-Migrate:** Handles SQLAlchemy database migrations for Flask applications using Alembic.
- **Flask-WTF:** Simple integration of Flask and WTForms, including CSRF protection.
- **Logging:** Track actions and errors for better debugging and monitoring.
- **CSRF:** protection for secure form submissions using Flask-WTF.
- **Multi-language support:** Enable multi-language support with Flask-Babel
- **Bootstrap:** A popular front-end framework for developing responsive and mobile-first websites.

  ## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/Python_Automacao.git
    cd Python_Automacao
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database:**

    ```bash
    flask db upgrade
    ```

6. **Run the application:**

    ```bash
    flask run
    ```
## Usage

Once the application is running, you can access it in your web browser at `http://127.0.0.1:5000/funcionarios`. From there, you can navigate through the different functionalities to manage employee data.

### Logging In

To implement...

### Managing Employees

- **List Employees:** View a list of all registered employees.
- **View Employee Details:** Click on an employee's name to view their details.
- **Register Employee:** Use the "Cadastrar novo Funcionario" button to add a new employee.
- **Edit Employee:** Click on the "Editar" link next to an employee to edit their details.
- **Remove Employee:** Click on the "Remover" link next to an employee to delete their record.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Feel free to customize this README to better fit your project's specifics and requirements. If you have any questions or need further assistance, please don't hesitate to ask.
