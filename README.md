# Django Portfolio Website

A clean, responsive, **admin-driven portfolio** built with Django 4.2 and Tailwind CSS.  
Every section — profile, skills, experience, education, projects, resume, and contact — is managed entirely through the Django admin panel. No code changes needed to update your content.

---

## Table of Contents

- [Live Preview](#live-preview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Admin Guide](#admin-guide)
- [Project Structure](#project-structure)
- [Models Reference](#models-reference)
- [Customisation](#customisation)
- [Production Deployment](#production-deployment)
- [License](#license)

---

## Live Preview

http://www.punambhuyan.com/

---

## Features

| Section | What it does |
|---|---|
| **Hero / Cover** | Full-width LinkedIn-style cover banner + circular profile photo overlapping the edge |
| **About Me** | Bio text with automatic paragraph splitting |
| **Skills** | Animated progress bars grouped by category (Frontend / Backend / Database / DevOps) |
| **Experience** | Vertical timeline with bullet points and date range labels |
| **Education** | Vertical timeline with optional institution URLs |
| **Projects** | Responsive card grid with hover-scroll image preview + individual detail pages |
| **Rich Text Descriptions** | Project descriptions support bold, italic, lists, images, tables, and more via CKEditor |
| **Resume / CV** | Upload a PDF — a download button appears automatically |
| **Contact Form** | Working form that saves messages to the database (readable in admin) |
| **Navbar** | Sticky, mobile-responsive with active section highlighting on scroll |
| **Available for Work badge** | Toggle a green pulsing badge from the admin |
| **Social links** | GitHub, LinkedIn, Email, Website — appear only when filled in |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.13, Django 4.2 |
| Templates | Django Templates |
| Styling | Tailwind CSS (via CDN — no npm or build step required) |
| Rich Text | django-ckeditor 6.7 (CKEditor 4) |
| Images | Pillow 10+ |
| Static files | WhiteNoise 6.6 |
| Media cleanup | django-cleanup 8 |
| Database | SQLite (built-in — no external DB needed) |
| Fonts | Cormorant Garamond · DM Sans · JetBrains Mono (Google Fonts) |

---

## Prerequisites

Make sure the following are installed on your machine before you start:

| Tool | Minimum version | Check |
|---|---|---|
| Python | 3.10+ | `python --version` |
| pip | Latest | `pip --version` |
| Git | Any | `git --version` |

> **No Node.js, npm, or database server required.** Tailwind is loaded from CDN and SQLite is built into Python.

---

## Installation

Follow every step in order. Commands are shown for **Windows (PowerShell)** and **Mac / Linux (Terminal)**.

### 1. Clone the repository

```bash
git clone https://github.com/myselfpunam/myportfolio.git
cd your-repo-name
```

> Replace `your-username/your-repo-name` with your actual GitHub repository path.

---

### 2. Create a virtual environment

**Windows**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal prompt — this means the environment is active.

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Django 4.2
- Pillow (image processing)
- WhiteNoise (static file serving)
- django-cleanup (auto-delete orphaned media files)
- django-ckeditor (rich text editor)

---

### 4. Apply database migrations

```bash
python manage.py migrate
```

This creates the SQLite database file (`db.sqlite3`) and all required tables automatically.

---

### 5. Create a superuser (admin account)

```bash
python manage.py createsuperuser
```

Enter a username, email (optional), and password when prompted. You will use these credentials to log in to the admin panel.

---

### 6. (Optional) Load sample demo data

```bash
python seed_data.py
```

This fills the database with placeholder profile info, skills, experience, education, and projects so you can immediately see the site populated. You can edit or delete this data from the admin panel at any time.

---

## Running the Project

```bash
python manage.py runserver
```

Open your browser and visit:

| URL | Purpose |
|---|---|
| `http://127.0.0.1:8000/` | Your portfolio homepage |
| `http://127.0.0.1:8000/admin/` | Django admin panel (content management) |

Press `Ctrl + C` in the terminal to stop the server.

---

## Admin Guide

Everything on the site is controlled from **http://127.0.0.1:8000/admin/**. Log in with the superuser credentials you created in step 5.

### Profile

Go to **Core → Profile → Add Profile**.

| Field | What to enter |
|---|---|
| Name | Your full name |
| Title | Your job title, e.g. `Full Stack Developer` |
| Tagline | A short phrase, e.g. `Building things for the web` |
| Bio | Your About Me text. Use blank lines between paragraphs. |
| Profile image | Square photo — displayed as a circle |
| Cover image | Wide banner image (recommended: 1500×500px or wider) |
| Email | Your contact email |
| GitHub URL | Full URL, e.g. `https://github.com/username` |
| LinkedIn URL | Full URL |
| Website URL | Your personal website (optional) |
| Location | e.g. `London, UK` |
| Available for work | Tick to show the green pulsing badge |

> Only **one Profile record** is used. If you add more than one, the site uses the first.

---

### Skills

Go to **Core → Skills → Add Skill**.

- Set a **category** (Frontend / Backend / Database / DevOps & Tools / Other)
- Set **proficiency** as a number from 0 to 100 (drives the animated progress bar)
- Use **order** to control the display order within each category

---

### Experience

Go to **Core → Experiences → Add Experience**.

- Fill in **role**, **company**, **start date**, and **end date**
- Tick **is current** and leave end date blank if this is your current job
- In the **description** field, write one bullet point per line — each line becomes a list item on the site

---

### Education

Go to **Core → Educations → Add Education**.

- Fill in **degree**, **institution**, **start year**, and **end year**
- Tick **is ongoing** and leave end year blank if you are still studying
- Add an **institution URL** to make the institution name a clickable link

---

### Projects

Go to **Core → Projects → Add Project**.

| Field | Notes |
|---|---|
| Title | Project name |
| Slug | Auto-filled from the title — used in the URL (`/projects/my-project/`) |
| Tagline | One-line summary shown on the card |
| Description | Full rich text description with formatting, images, and links via CKEditor |
| Thumbnail | Upload a **tall, full-page screenshot** for the hover-scroll preview effect |
| Tech stack | Comma-separated, e.g. `Django, PostgreSQL, React` |
| Live URL | Optional — the "View Live Site" button only appears when filled |
| GitHub URL | Optional — the "View Source" button only appears when filled |
| Is featured | Tick to show a "Featured" badge on the card |
| Order | Lower numbers appear first |

---

### Resume / CV

Go to **Core → Resume/CVs → Add Resume/Cv**.

- Upload your PDF file
- Set a **label** (defaults to `Download CV`)
- The download button appears automatically in the navbar and Resume section once a file is uploaded

---

### Contact Messages

Go to **Core → Contact Messages** to read messages submitted via the contact form on your portfolio. Mark them as read using the **Mark selected messages as read** action.

---

## Project Structure

```
portfolio_project/
│
├── manage.py                      # Django management commands entry point
├── requirements.txt               # Python package dependencies
├── seed_data.py                   # Optional demo data loader
├── db.sqlite3                     # SQLite database (auto-created on migrate)
│
├── portfolio/                     # Django project configuration
│   ├── settings.py                # All settings (database, apps, media, CKEditor)
│   ├── urls.py                    # Root URL patterns
│   └── wsgi.py                    # WSGI entry point for deployment
│
├── core/                          # Main Django application
│   ├── models.py                  # All data models (see Models Reference below)
│   ├── views.py                   # index view + project_detail view
│   ├── urls.py                    # App URL patterns
│   ├── admin.py                   # Admin configuration with image previews
│   ├── migrations/                # Database migration files
│   └── templatetags/
│       └── portfolio_tags.py      # Custom template filters
│
├── templates/
│   ├── base.html                  # Navbar, footer, Tailwind config, all JS
│   ├── index.html                 # Single-page portfolio (all sections)
│   └── project_detail.html        # Individual project page
│
├── static/                        # Custom static assets (if any)
└── media/                         # Uploaded files — images and PDFs (auto-created)
    ├── profile/
    ├── cover/
    ├── projects/
    ├── resume/
    └── uploads/                   # CKEditor image uploads
```

---

## Models Reference

### Profile

```
name             CharField       Your full name
title            CharField       Job title
tagline          CharField       Short phrase shown under the name
bio              TextField       About Me body text
profile_image    ImageField      Circular avatar (uploads to media/profile/)
cover_image      ImageField      Full-width banner (uploads to media/cover/)
email            EmailField
github_url       URLField
linkedin_url     URLField
website_url      URLField
twitter_url      URLField
location         CharField       e.g. "London, UK"
available_for_work  BooleanField   Shows/hides the green Available badge
```

### Skill

```
name         CharField     Skill name, e.g. "Python"
category     CharField     frontend | backend | database | devops | other
proficiency  IntegerField  0–100, drives the animated progress bar
order        PositiveInt   Display order within the category
icon_class   CharField     Optional CSS class or emoji
```

### Experience

```
role          CharField   Job title
company       CharField   Company name
company_url   URLField    Optional — makes company name a link
location      CharField   Optional
start_date    DateField
end_date      DateField   Leave blank if is_current is ticked
is_current    BooleanField
description   TextField   One bullet point per line
order         PositiveInt
```

### Education

```
degree           CharField   e.g. "BSc Computer Science"
institution      CharField   University or school name
institution_url  URLField    Optional — makes institution name a link
location         CharField   Optional
start_year       IntegerField
end_year         IntegerField  Leave blank if is_ongoing is ticked
is_ongoing       BooleanField
description      TextField    Optional additional notes
order            PositiveInt
```

### Project

```
title        CharField              Project name
slug         SlugField              URL key — auto-filled from title
tagline      CharField              One-liner shown on the card
description  RichTextUploadingField Full description with rich text support
thumbnail    ImageField             Tall screenshot for hover-scroll preview
tech_stack   CharField              Comma-separated list of technologies
live_url     URLField               Optional
github_url   URLField               Optional
is_featured  BooleanField           Shows "Featured" badge
order        PositiveInt
```

### Resume

```
label       CharField   Button text (default: "Download CV")
file        FileField   PDF file
updated_at  DateTime    Auto-updated on save
```

### ContactMessage

```
name      CharField   Sender name
email     EmailField  Sender email
subject   CharField   Optional
message   TextField   Message body
sent_at   DateTime    Auto-set on creation
is_read   BooleanField
```

---

## Customisation

### Change accent colours

Edit the `tailwind.config` block inside `templates/base.html`:

```js
colors: {
  ink:        '#0D0D0D',   // Main text colour
  paper:      '#FAFAF8',   // Page background
  warm:       '#C49A6C',   // Accent — amber/gold
  'warm-light': '#F5EDE0', // Light accent background
  muted:      '#6B6B6B',   // Secondary text
  border:     '#E4E2DC',   // Borders and dividers
}
```

### Change fonts

Replace the Google Fonts `<link>` in `base.html` and update the `fontFamily` block:

```js
fontFamily: {
  display: ['"Cormorant Garamond"', 'Georgia', 'serif'],
  body:    ['"DM Sans"', 'system-ui', 'sans-serif'],
  mono:    ['"JetBrains Mono"', 'monospace'],
}
```

### Add a new section

1. Add a model in `core/models.py`
2. Run `python manage.py makemigrations && python manage.py migrate`
3. Register the model in `core/admin.py`
4. Pass the queryset from `core/views.py` → `index()`
5. Add a `<section id="your-section">` block in `templates/index.html`
6. Add a nav link in the navbar inside `templates/base.html`

---

## Production Deployment

### 1. Set environment variables

Create a `.env` file (never commit this to Git):

```env
SECRET_KEY=replace-with-a-long-random-string
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

Load these in `settings.py` using `os.environ.get(...)` or the `python-decouple` package.

### 2. Collect static files

```bash
python manage.py collectstatic
```

### 3. Recommended hosting options

| Platform | Notes |
|---|---|
| **Railway** | Free tier, automatic deploys from GitHub, easy env var setup |
| **Render** | Free tier with persistent disk for SQLite |
| **Fly.io** | Free tier, good for small apps |
| **VPS (DigitalOcean / Hetzner)** | Ubuntu + Gunicorn + Nginx for full control |

### 4. Switch to PostgreSQL (optional)

Install `psycopg2-binary`, then update `DATABASES` in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Media files in production

For persistent media storage (profile images, project thumbnails, uploaded CV) use:
- **AWS S3** with `django-storages`
- **Cloudinary** with `cloudinary-storage`

---

## License

MIT — free to use, fork, and deploy for personal or commercial portfolios.  
If you find this project useful, a star on GitHub is appreciated.
