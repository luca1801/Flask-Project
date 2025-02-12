# Flask-Project

Flask-Project is a web application built with Flask for managing employees. The application allows users to list, register, edit, and remove employees. It also includes logging and error handling to ensure smooth operation.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project is designed to help manage employee data efficiently. It provides a user-friendly interface for performing CRUD (Create, Read, Update, Delete) operations on employee records. The application uses Flask for the backend, SQLAlchemy for database(Postgress) interactions, and Bootstrap for styling.

## Features

- List all employees
- View details of a specific employee
- Register a new employee
- Edit employee details
- Remove an employee
- Logging for tracking actions and errors
- CSRF protection for secure form submissions
- Multi-language support with Flask-Babel

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
