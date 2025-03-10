from django.contrib import admin
from .models import CategoryVO  # Import your CategoryVO model

# Define an admin class for CategoryVO
class CategoryVOAdmin(admin.ModelAdmin):
    # List the fields you want to display in the admin list view
    list_display = ('category_id', 'category_name', 'category_description', 'is_deleted', 'create_at', 'modify_at')
    list_filter = ('is_deleted',)  # Filter options in admin
    search_fields = ('category_name', 'category_description')  # Enable search by these fields
    ordering = ('-create_at',)  # Order the records by create_at in descending order
    readonly_fields = ('create_at', 'modify_at')  # Make create_at and modify_at fields read-only

    # Optional: You can add custom form fields or fieldsets
    fieldsets = (
        (None, {
            'fields': ('category_name', 'category_description', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('create_at', 'modify_at'),
            'classes': ('collapse',),
        }),
    )

# Register the model with the admin site
admin.site.register(CategoryVO, CategoryVOAdmin)
