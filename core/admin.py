from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Experience, Education, Project, Resume, ContactMessage

admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio"
admin.site.index_title = "Content Management"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'available_for_work', 'profile_preview']
    fieldsets = (
        ('Identity', {
            'fields': ('name', 'title', 'tagline', 'bio', 'location', 'available_for_work')
        }),
        ('Images', {
            'fields': ('profile_image', 'cover_image'),
        }),
        ('Social Links', {
            'fields': ('email', 'github_url', 'linkedin_url', 'website_url', 'twitter_url'),
        }),
    )

    def profile_preview(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" style="width:40px;height:40px;border-radius:50%;object-fit:cover;" />',
                obj.profile_image.url
            )
        return "—"
    profile_preview.short_description = "Photo"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_editable = ['proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_editable = ['order']
    list_filter = ['is_current']
    search_fields = ['role', 'company']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_year', 'end_year', 'is_ongoing', 'order']
    list_editable = ['order']
    search_fields = ['degree', 'institution']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_featured', 'order', 'thumbnail_preview', 'created_at']
    list_editable = ['is_featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'tech_stack']
    list_filter = ['is_featured']

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="{}" style="width:80px;height:50px;object-fit:cover;border-radius:4px;" />',
                obj.thumbnail.url
            )
        return "—"
    thumbnail_preview.short_description = "Preview"


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['label', 'file', 'updated_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'sent_at', 'is_read']
    list_filter = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'sent_at']
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
