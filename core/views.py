from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from itertools import groupby
from .models import Profile, Skill, Experience, Education, Project, Resume, ContactMessage


def index(request):
    profile = Profile.objects.first()
    skills_qs = Skill.objects.all()

    # Group skills by category
    skills_by_category = {}
    for skill in skills_qs:
        cat = skill.get_category_display()
        skills_by_category.setdefault(cat, []).append(skill)

    experiences = Experience.objects.all()
    education = Education.objects.all()
    projects = Project.objects.all()
    featured_projects = projects.filter(is_featured=True)
    resume = Resume.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_body = request.POST.get('message', '').strip()
        if name and email and message_body:
            ContactMessage.objects.create(
                name=name, email=email, subject=subject, message=message_body
            )
            messages.success(request, "Your message has been sent! I'll get back to you soon.")
            return redirect('index')
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'index.html', {
        'profile': profile,
        'skills_by_category': skills_by_category,
        'experiences': experiences,
        'education': education,
        'projects': projects,
        'featured_projects': featured_projects,
        'resume': resume,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    other_projects = Project.objects.exclude(pk=project.pk)[:3]
    return render(request, 'project_detail.html', {
        'project': project,
        'other_projects': other_projects,
    })
