"""
seed_data.py — Run this once to populate your portfolio with demo content.

Usage:
    python manage.py shell < seed_data.py
OR:
    python seed_data.py  (if you're in the project root)
"""
import os, sys, django

# ── Bootstrap Django if run as a standalone script
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    django.setup()

from datetime import date
from core.models import Profile, Skill, Experience, Education, Project

# ── Profile
Profile.objects.all().delete()
Profile.objects.create(
    name="Alex Morgan",
    title="Web Application Developer",
    tagline="Building clean, scalable web solutions — one commit at a time.",
    bio="""I'm a full-stack web developer with 4+ years of experience turning complex problems into elegant, performant applications. My craft lives at the intersection of thoughtful backend architecture and polished user interfaces.

I specialize in Python/Django on the backend and modern JavaScript on the frontend, with a strong emphasis on clean code, CI/CD workflows, and cloud-native deployments. I've shipped products used by thousands of users and love collaborating with driven teams.

When I'm not coding, I'm contributing to open-source projects, writing about software architecture, or exploring the mountains with a camera in hand.""",
    email="alex@example.com",
    github_url="https://github.com/alexmorgan",
    linkedin_url="https://linkedin.com/in/alexmorgan",
    website_url="https://alexmorgan.dev",
    location="Berlin, Germany",
    available_for_work=True,
)
print("✅ Profile created")

# ── Skills
Skill.objects.all().delete()
skills_data = [
    # Frontend
    ("HTML5 / CSS3", "frontend", 95),
    ("JavaScript (ES2022+)", "frontend", 88),
    ("Tailwind CSS", "frontend", 90),
    ("React.js", "frontend", 78),
    # Backend
    ("Python", "backend", 95),
    ("Django / DRF", "backend", 92),
    ("Node.js", "backend", 70),
    ("REST API Design", "backend", 90),
    # Database
    ("PostgreSQL", "database", 88),
    ("SQLite", "database", 85),
    ("Redis", "database", 65),
    # DevOps
    ("Docker", "devops", 78),
    ("Git / GitHub", "devops", 92),
    ("Linux / Bash", "devops", 80),
    ("AWS (EC2, S3)", "devops", 65),
]
for i, (name, cat, prof) in enumerate(skills_data):
    Skill.objects.create(name=name, category=cat, proficiency=prof, order=i)
print("✅ Skills created")

# ── Experience
Experience.objects.all().delete()
Experience.objects.create(
    role="Senior Full-Stack Developer",
    company="TechFlow GmbH",
    company_url="https://example.com",
    location="Berlin, Germany",
    start_date=date(2022, 3, 1),
    is_current=True,
    description="""Led development of a multi-tenant SaaS analytics platform serving 12,000+ users
Reduced API response times by 65% through query optimization and Redis caching
Architected a microservices migration from a monolithic Django application
Mentored 3 junior developers and established code review standards""",
    order=0,
)
Experience.objects.create(
    role="Django Developer",
    company="Pixel Republic",
    company_url="https://example.com",
    location="Remote",
    start_date=date(2020, 6, 1),
    end_date=date(2022, 2, 28),
    is_current=False,
    description="""Built REST APIs consumed by mobile apps with 50k+ downloads
Integrated third-party payment gateways (Stripe, PayPal) into e-commerce platform
Automated deployment pipelines using GitHub Actions and Docker
Collaborated with design team to implement pixel-perfect UI components""",
    order=1,
)
Experience.objects.create(
    role="Junior Web Developer",
    company="StartupHub",
    location="Munich, Germany",
    start_date=date(2019, 1, 1),
    end_date=date(2020, 5, 31),
    is_current=False,
    description="""Developed internal tools with Python/Django that saved 10h/week of manual work
Maintained and improved WordPress + WooCommerce sites for client portfolio
Assisted in database design and query optimization for PostgreSQL databases""",
    order=2,
)
print("✅ Experience created")

# ── Education
Education.objects.all().delete()
Education.objects.create(
    degree="M.Sc. Web and Data Science",
    institution="University of Koblenz",
    location="Koblenz, Germany",
    start_year=2023,
    is_ongoing=True,
    description="Focus areas: Machine Learning, Distributed Systems, Advanced Web Technologies.",
    order=0,
)
Education.objects.create(
    degree="B.Sc. Computer Science & Engineering",
    institution="BRAC University",
    location="Dhaka, Bangladesh",
    start_year=2015,
    end_year=2019,
    description="Graduated with distinction. Thesis: 'Optimising Database Query Plans with Learned Models'.",
    order=1,
)
print("✅ Education created")

# ── Projects
Project.objects.all().delete()
Project.objects.create(
    title="SaaS Analytics Dashboard",
    slug="saas-analytics-dashboard",
    tagline="Real-time business intelligence for growing startups.",
    description="""A multi-tenant analytics platform built with Django and React that aggregates data from multiple sources into a unified dashboard.

Key features include real-time WebSocket updates, custom chart builder, CSV/Excel export, role-based access control, and white-label support for agencies.

The backend exposes a comprehensive REST API with DRF, protected by JWT authentication. The frontend is a React SPA consuming that API with recharts for visualisation.""",
    tech_stack="Django, DRF, React, PostgreSQL, Redis, WebSockets, Docker",
    live_url="https://example.com",
    github_url="https://github.com/example/saas-dashboard",
    is_featured=True,
    order=0,
)
Project.objects.create(
    title="E-Commerce Platform",
    slug="ecommerce-platform",
    tagline="Full-featured online store with Stripe payments and inventory management.",
    description="""A fully-featured e-commerce platform built from scratch with Django. Supports product variants, inventory tracking, coupon codes, and Stripe Checkout integration.

Includes a custom admin dashboard with sales analytics, order management, and customer segmentation. Deployed on AWS with auto-scaling and CloudFront CDN for static assets.""",
    tech_stack="Django, PostgreSQL, Stripe API, Celery, AWS S3, Tailwind CSS",
    github_url="https://github.com/example/ecommerce",
    is_featured=True,
    order=1,
)
Project.objects.create(
    title="Odoo Mobile Shop ERP",
    slug="odoo-mobile-shop-erp",
    tagline="Custom Odoo 17 ERP modules for a multi-location mobile retailer.",
    description="""Custom Odoo 17 module development for a mobile phone retail chain with 5 locations. Built IMEI tracking, cashback management, brand filtering, and supplier credit systems.

Integrated barcode scanning for stock-in/out operations and developed a custom dashboard for the store manager with daily sales summaries and low-stock alerts.""",
    tech_stack="Odoo 17, Python, PostgreSQL, XML (Views), JavaScript (OWL)",
    is_featured=False,
    order=2,
)
Project.objects.create(
    title="Personal Finance Tracker",
    slug="personal-finance-tracker",
    tagline="Multi-currency expense tracking dashboard for Bangladesh & Germany.",
    description="""A React-based personal finance dashboard for tracking expenses across two countries (Bangladesh & Germany) in BDT, EUR, and USD with fixed conversion rates.

Features month-by-month balance breakdowns, income vs. expense charts, business vs. personal expense tagging, and collapsible monthly cards with Indian-style number formatting.""",
    tech_stack="React, JSX, Tailwind CSS, Django, SQLite",
    github_url="https://github.com/example/finance-tracker",
    is_featured=False,
    order=3,
)
print("✅ Projects created")
print("\n🎉 All demo data seeded successfully!")
print("   Run: python manage.py createsuperuser — to create your admin account.")
print("   Run: python manage.py runserver     — to start the development server.")
