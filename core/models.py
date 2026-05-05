from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150, help_text="e.g. Web Application Developer")
    tagline = models.CharField(max_length=255, help_text="Short motivating phrase")
    bio = models.TextField(help_text="Professional summary for About Me section")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover/', blank=True, null=True)
    email = models.EmailField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    available_for_work = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps & Tools'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(
        default=80,
        help_text="Proficiency percentage 0–100 (used for progress bar display)"
    )
    order = models.PositiveIntegerField(default=0)
    icon_class = models.CharField(
        max_length=80, blank=True,
        help_text="Optional: a CSS class or emoji for the skill icon"
    )

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    company_url = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current")
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text="Use newlines; each line becomes a bullet point")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"

    @property
    def duration_label(self):
        start = self.start_date.strftime('%b %Y')
        if self.is_current or not self.end_date:
            return f"{start} — Present"
        return f"{start} — {self.end_date.strftime('%b %Y')}"

    @property
    def description_bullets(self):
        return [line.strip() for line in self.description.splitlines() if line.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    institution_url = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True, help_text="Leave blank if ongoing")
    is_ongoing = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_year', 'order']

    def __str__(self):
        return f"{self.degree} — {self.institution}"

    @property
    def year_label(self):
        if self.is_ongoing or not self.end_year:
            return f"{self.start_year} — Present"
        return f"{self.start_year} — {self.end_year}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly identifier, e.g. my-cool-project")
    tagline = models.CharField(max_length=255, blank=True, help_text="One-liner shown on card")
    description = RichTextUploadingField(help_text="Full description shown on project detail page")
    thumbnail = models.ImageField(
        upload_to='projects/',
        help_text="Full-height screenshot for hover scroll preview (tall image recommended)"
    )
    tech_stack = models.CharField(
        max_length=500,
        help_text="Comma-separated list, e.g. Django, PostgreSQL, React"
    )
    live_url = models.URLField(blank=True, help_text="Leave blank to hide button")
    github_url = models.URLField(blank=True, help_text="Leave blank to hide button")
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Resume(models.Model):
    label = models.CharField(max_length=100, default="Download CV")
    file = models.FileField(upload_to='resume/', help_text="Upload PDF file")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Resume / CV"

    def __str__(self):
        return f"Resume — {self.updated_at.strftime('%Y-%m-%d')}"


class ContactMessage(models.Model):
    """Stores messages submitted via the contact form."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"From {self.name} <{self.email}> — {self.sent_at.strftime('%Y-%m-%d')}"
