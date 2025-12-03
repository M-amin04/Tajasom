from django.contrib import admin
from .models import CustomerRequest

@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'service_type', 'priority', 'status', 'is_read', 'created_at']
    list_filter = ['service_type', 'priority', 'status', 'is_read']
    search_fields = ['full_name', 'email', 'company']