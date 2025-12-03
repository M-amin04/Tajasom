from django.contrib import admin
from .models import CompanyInfo, CompanyContact, TeamMember, Client, CompanyHistory

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'years_experience', 'completed_projects', 'happy_clients']
    list_editable = ['years_experience', 'completed_projects', 'happy_clients']

@admin.register(CompanyContact)
class CompanyContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email', 'working_hours']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'email', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']

@admin.register(CompanyHistory)
class CompanyHistoryAdmin(admin.ModelAdmin):
    list_display = ['year', 'title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'year']