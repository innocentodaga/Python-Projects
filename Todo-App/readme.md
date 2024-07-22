# Simple ToDo App

A simple ToDo application built using Kivy and KivyMD. This app allows users to add, view, and manage their to-do items with a clean and intuitive user interface.

## Features

- Add new to-do items
- View a list of to-do items
- Mark items as completed

## Requirements

- Python 3.6 or higher
- Kivy 2.0.0 or higher
- KivyMD 2.0.0 or higher

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/innocentodaga/Python-Projects/tree/main/Todo-App.git
    cd todo-app
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip install kivy kivymd
    ```

## Usage

1. **Run the application:**

    ```sh
    python main.py
    ```

2. **Add ToDo items:**

    - Enter the details of the to-do item in the provided input fields and add it to the list.

3. **Mark items as completed:**

    - Click on the checkbox next to a to-do item to mark it as completed.

## File Structure
│
├── TodoApp.py # Main application file
├── Main.kv # Kivy layout file
├── README.md # This README file
└── assets/ # Directory for assets like images, fonts, etc.
