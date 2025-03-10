from django.contrib import admin
from .models import SubCategoryVO  # Import your model
from category.models import CategoryVO  # Import Category model (used in ForeignKey)

# Define an admin class for SubCategoryVO
class SubCategoryVOAdmin(admin.ModelAdmin):
    # List the fields you want to display in the admin list view
    list_display = ('subcategory_id', 'subcategory_name', 'subcategory_category_id', 'is_deleted', 'create_at', 'modify_at')
    list_filter = ('is_deleted', 'subcategory_category_id')  # Filter options in admin
    search_fields = ('subcategory_name', 'subcategory_description')  # Enable search by these fields
    ordering = ('-create_at',)  # Order the records by create_at in descending order
    readonly_fields = ('create_at', 'modify_at')  # Make create_at and modify_at fields read-only

    # Optional: You can add custom form fields or fieldsets
    fieldsets = (
        (None, {
            'fields': ('subcategory_name', 'subcategory_category_id', 'subcategory_description', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('create_at', 'modify_at'),
            'classes': ('collapse',),
        }),
    )

# Register the model with the admin site
admin.site.register(SubCategoryVO, SubCategoryVOAdmin)
