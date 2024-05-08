# BLOG REST API

This is a simple REST API for a blog. It allows you to create, read, update and delete blog posts.

## Installation

1. Clone the repository
```bash
git clone https://github.com/bugemarvin/Nifty-Works-Plus-interview.git
```
2. Change into the directory
```bash
cd Nifty-Works-Plus-interview/question-two
```
3. Install virtualenv
```bash
python3 -m pip install virtualenv
```
4. Create a virtual environment
```bash
python3 -m venv .q2
```
5. Activate the virtual environment
```bash
source .q2/bin/activate
```
6. Install the dependencies with 
```bash
pip install -r requirements.txt
```
7. Run the application
```bash
./manage.py runserver 8001 (or any port of your choice e.g 8000 optional)
```

## Usage

The API has the following endpoints:

### Welcome
* **Route**: `/api/v1`
* **Method**: `GET`
* **Description**: *Welcome message for the the blog API*

#### Expample
```json
{
    "message": "Welcome to the Blog API"
}
```

### Register
* **Route**: `/api/v1/auth/register`
* **Method**: `POST`
* **Description**: *Register a new user*

#### Example
```json
{
    "first_name": "jhon",
    "last_name": "doe",
    "email": "jhondoe@xyz.com",
    "password": "password"
}
```

### Login
* **Route**: `/api/v1/auth/login`
* **Method**: `POST`
* **Description**: *Login a user*

#### Example
```json
{
    "email": "jhondoe@xyz.com",
    "password": "password"
}
```

### Create Post
* **Route**: `/api/v1/blog/create`,
* **Method**: `POST`
* **Description**: *Create a new blog post*

#### Example
```json
{
    "title": "My first blog post",
    "content": "This is my first blog post"
}
```

### Get All Posts
* **Route**: `/api/v1/blog/list`,
* **Method**: `GET`
* **Description**: *Get all blog posts*

#### Example
```json
{
    "posts": [
        {
            "id": 1,
            "title": "My first blog post",
            "content": "This is my first blog post"
        }
    ]
}
```

### Get Post
* **Route**: `/api/v1/blog/list/?title=My first blog post`,
* **Method**: `GET`
* **Description**: *Get a single blog post*

#### Example
```json
{
    "post": {
        "id": 1,
        "title": "My first blog post",
        "content": "This is my first blog post"
    }
}
```

### Update Post
* **Route**: `/api/v1/blog/update/?title=My first blog post`,
* **Method**: `PUT`
* **Description**: *Update a blog post*

#### Example
```json
{
    "title": "My first blog post",
    "content": "This is my first blog post updated"
}
```

### Delete Post
* **Route**: `/api/v1/blog/delete/?title=My first blog post`,
* **Method**: `DELETE`
* **Description**: *Delete a blog post*

#### Example
```json
{
    "message": "Post deleted successfully"
}
```