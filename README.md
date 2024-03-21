# Blog

This repository contains the source code for a simple blog application.

## Description

This blog application is designed to provide a platform for users to create, edit, and publish blog posts. It includes features such as user authentication, post management, and more.

## Specificities Implemented

### 1. User Authentication
   - Users can register for an account.
   - Registered users can log in to access additional features.
   - Password hashing for security.

### 2. Post Management
   - Users can create new blog posts.
   - Users can edit and delete their own posts.
   - Posts are displayed with titles, authors, publication dates, and content.


### 3. Responsive Design
   - The application is designed to be mobile-friendly, adapting to different screen sizes and devices.

## Installation

To run this application locally, follow these steps:

1. Clone the repository to your local machine:
```
git clone https://github.com/Malickkk/Blog.git
```

3. Navigate to the cloned directory:
cd Blog

4. Build and start the Docker containers using Docker Compose:
```
docker-compose up --build -d
```

6. Once the containers are up and running, you can access the application by opening your web browser and navigating to `http://localhost:8000`.

### Without Docker

To run this application without Docker, navigate to the cloned directory and run:
```
./manage.py runserver
```

You can access the application by opening your web browser and navigating to `http://localhost:8000`.

## Technologies Used

- Django
- Docker
- sqlite
- HTML
- CSS
- JavaScript

## Contributors

- [Malickkk](https://github.com/Malickkk)

## License

This project is licensed under the [MIT License](LICENSE).
