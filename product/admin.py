from django.utils.html import format_html
from django.contrib import admin
from product.models import ProductVO


class ProductVOAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "product_price",
        "product_quantity",
        "product_category_id",
        "product_subcategory_id",
        "product_image_tag",
        "is_deleted",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_deleted", "product_category_id", "product_subcategory_id")
    search_fields = ("product_name", "product_description")
    readonly_fields = ("created_at", "updated_at", "product_image_tag")

    def product_image_tag(self, obj):
        if obj.product_image_name:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:5px;"/>'.format(
                    obj.product_image_name.url
                )
            )
        return "No Image"

    product_image_tag.short_description = "Image Preview"


admin.site.register(ProductVO, ProductVOAdmin)
