# FastAPI Multi-Page Greet App

A modular FastAPI web app that greets users based on their name and age. Built with clean template inheritance, form validation, and dynamic routing — perfect for showcasing backend skills.

---

## Features

- Multi-page routing (`/`, `/greet`)
- Jinja2 templates with inheritance (`base.html`, `index.html`, `greet.html`)
- Form validation and error handling
- Deployed on Render: [https://fastapi-multipe-greet.onrender.com](https://fastapi-multipe-greet.onrender.com)

---

## Tech Stack

| Tool       | Purpose           |
|------------|-------------------|
| FastAPI    | Backend framework |
| Jinja2     | HTML templating   |
| Uvicorn    | ASGI server       |
| Render     | Cloud deployment  |

---

## Project Structure

```
fastapi_multiple_greet/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── greet.html
├── requirements.txt
└── render.yaml
```

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/akhila-a3/fastapi_multiple_greet.git
cd fastapi_multiple_greet
pip install -r requirements.txt
uvicorn app:app --reload
```

Then visit: `http://127.0.0.1:8000`

---

## Usage

1. Enter your name and age on the homepage.
2. Submit the form to receive a personalized greeting.
3. View dynamic messages based on your age group.

---

## Learnings and Highlights

- Practiced modular design and template reuse
- Implemented clean error handling and form validation
- Deployed a FastAPI app with Render for public access

---

## Future Improvements

- Add age-based avatars or emojis
- Store greetings in a database
- Add unit tests and CI/CD pipeline

---

## Author

Akhila Raveendran P M  
GitHub: [https://https://github.com/Akhila-04-03/fastapi_multipe_greet/new/main](https://https://github.com/Akhila-04-03/fastapi_multipe_greet/new/main)

---

## License

This project is licensed under the MIT License.
