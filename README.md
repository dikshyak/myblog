# MyBlog — Django Blog Project

A full-featured blog web application built with Django 6.0.5 and Python 3.13. Built from scratch with models, views, templates, admin panel, automated tests and CI/CD via GitHub Actions.

---

## What it does

- Public blog where anyone can read posts
- Admin panel where the author can create, edit and delete posts
- Each post has a title, slug, excerpt, content, cover image, author, published status and timestamps
- Clean URLs like `/posts/my-first-post/` instead of `/posts/1/`
- Automated tests that run on every push to GitHub

---

## Tech stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Programming language |
| Django 6.0.5 | Web framework |
| SQLite | Database |
| Pillow | Image handling |
| GitHub Actions | CI/CD pipeline |

---

## Project structure

```
myblog/
├── .github/
│   └── workflows/
│       └── django.yml       # CI/CD pipeline
├── myblog/
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Root URL router
│   └── wsgi.py              # Production server entry point
├── posts/
│   ├── migrations/          # Database migration history
│   ├── templates/
│   │   └── posts/
│   │       ├── base.html    # Master layout
│   │       ├── list.html    # All posts page
│   │       └── detail.html  # Single post page
│   ├── admin.py             # Admin panel configuration
│   ├── models.py            # Post model
│   ├── tests.py             # Automated tests
│   ├── urls.py              # Posts URL patterns
│   └── views.py             # Page logic
├── .gitignore
├── manage.py                # Django command line tool
└── requirements.txt         # Python dependencies
```

---

## Post model fields

| Field | Type | Description |
|---|---|---|
| title | CharField | Title of the post |
| slug | SlugField | URL-friendly version of title |
| excerpt | TextField | Short summary shown in post list |
| content | TextField | Full body of the post |
| image | ImageField | Optional cover image |
| author | ForeignKey | Links to Django User model |
| published | BooleanField | Controls visibility on the blog |
| created | DateTimeField | Auto-set when post is created |
| updated | DateTimeField | Auto-updated when post is edited |

---

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/dikshyak/myblog.git
cd myblog
```

### 2. Create and activate virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

---

## Usage

| URL | Description |
|---|---|
| `http://127.0.0.1:8000/posts/` | Public blog — all published posts |
| `http://127.0.0.1:8000/posts/<slug>/` | Single post detail page |
| `http://127.0.0.1:8000/admin/` | Admin panel — manage posts |

---

## Running tests

```bash
python manage.py test
```

Expected output:

```
Ran 3 tests in 0.XXXs
OK
```

### What the tests check

- Post list page loads successfully
- Published post appears in the list
- Post detail page loads via slug URL

---

## CI/CD

Every push to the `main` branch automatically triggers GitHub Actions which:

1. Sets up Python 3.13
2. Installs all dependencies from `requirements.txt`
3. Runs database migrations
4. Runs all 3 tests

Green checkmark means everything is working. Red X means something broke and needs fixing before it reaches users.

---

## Daily workflow

```bash
cd C:\Users\LOQ\Desktop\myblog
venv\Scripts\activate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/posts/` in your browser.

---

## What I learned building this

- Setting up a Python virtual environment
- Installing and configuring Django
- Creating database models and running migrations
- Writing views and URL patterns
- Building HTML templates with Django template language
- Using the Django admin panel
- Writing automated tests
- Pushing code to GitHub
- Setting up CI/CD with GitHub Actions

---

## Author

**Dikshya Khadka**
GitHub: [@dikshyak](https://github.com/dikshyak)

---

## Next steps

- [ ] Deploy to the internet (Railway or Render)
- [ ] Add user registration and login
- [ ] Add comments system
- [ ] Add search functionality
- [ ] Switch to PostgreSQL database
- [ ] Add REST API with Django REST Framework