from django.contrib import admin
from product.models import ProductVO

class ProductVOAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_quantity', 'product_category_id', 'product_subcategory_id', 'is_deleted', 'created_at', 'updated_at')
    list_filter = ('is_deleted', 'product_category_id', 'product_subcategory_id')
    search_fields = ('product_name', 'product_description')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(ProductVO, ProductVOAdmin)
