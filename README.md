# Django ToDo App

This repository contains code for a Django ToDo App, which allows users to create and manage ToDo items. It includes various components, such as models, serializers, views, and URLs, along with an admin interface for managing the ToDo items.

## Project Structure

The project structure is as follows:

- `models.py`: Contains the Django models for the ToDo items and tags.
- `serializers.py`: Includes serializers for converting model instances to JSON representations and vice versa.
- `views.py`: Contains the views for handling user requests and performing CRUD operations on the ToDo items.
- `urls.py`: Includes URL patterns to map endpoints to the corresponding views.
- `admin.py`: Configures the admin interface to display and manage the ToDo items and tags.

## Code Formatting and Comments

The provided code follows the PEP 8 style guidelines for Python code formatting. It uses four spaces for indentation, separates imports with newlines, and includes blank lines between class definitions. Additionally, comments have been added to explain the purpose and functionality of each class, method, and field.

## API Endpoints

The ToDo App provides the following API endpoints:

1. User Creation:
   - URL: `/users/`
   - Method: `POST`
   - Description: Creates a new user account.
   - Request Body:
     - `username`: The username of the user.
     - `password`: The password for the user account.

2. ToDo Item List and Creation:
   - URL: `/todos/`
   - Method: `GET`, `POST`
   - Description: Lists all the ToDo items or creates a new ToDo item.
   - Authentication: Requires authentication token in the request headers.
   - Request Body (for POST):
     - `title`: The title of the ToDo item.
     - `description`: The description of the ToDo item.
     - `due_date`: The due date of the ToDo item (optional).
     - `tags`: The tags associated with the ToDo item (optional).

3. ToDo Item Retrieval, Update, and Deletion:
   - URL: `/todos/<int:pk>/`
   - Method: `GET`, `PUT`, `PATCH`, `DELETE`
   - Description: Retrieves, updates, or deletes a specific ToDo item.
   - Authentication: Requires authentication token in the request headers.
   - Request Body (for PUT/PATCH):
     - `title`: The updated title of the ToDo item.
     - `description`: The updated description of the ToDo item.
     - `due_date`: The updated due date of the ToDo item (optional).
     - `tags`: The updated tags associated with the ToDo item (optional).

4. Authentication Token:
   - URL: `/login/`
   - Method: `POST`
   - Description: Obtains an authentication token for the user.
   - Request Body:
     - `username`: The username of the user.
     - `password`: The password for the user account.

## Models

The ToDo App includes the following models:

1. ToDoItem:
   - Fields:
     - `timestamp`: The timestamp of when the ToDo item was created.
     - `title`: The title of the ToDo item.
     - `description`: The description of the ToDo item.
     - `due_date`: The due date of the ToDo item (optional).
     - `tags`: The tags associated with the ToDo item (optional).
     - `status`: The status of the ToDo item. Can be 'OPEN', 'WORKING', 'DONE', or 'OVERDUE'.
     - `user`: The user who created the ToDo item.
   - Relationships:
     - Each ToDoItem is associated with a single User.
     - Each ToDoItem can have multiple Tags.

2. Tag:
   - Fields:
     - `name`: The name of the tag.
     - `user`: The user who created the tag.
   - Relationships:
     - Each Tag is associated with a single User.

## Getting Started

To run the Django ToDo App locally, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`
5. Access the app in your web browser at `http://localhost:8000`

Feel free to explore the app and use the provided APIs to create, retrieve, update, and delete ToDo items. Make sure to authenticate and include the authentication token in the request headers for protected endpoints.

## Contribution

Contributions to this project are welcome. If you find any issues or want to add new features, feel free to open a pull request.
