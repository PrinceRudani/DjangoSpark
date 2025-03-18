from django.db import models
from django.db.models.signals import post_save
from category.models import CategoryVO
from subcategory.models import SubCategoryVO


# Create your models here.
class ProductVO(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField()
    product_image_name = models.ImageField()
    product_image_path = models.TextField()
    product_category_id = models.ForeignKey(CategoryVO,
                                            on_delete=models.PROTECT,
                                            db_column='product_category_vo')
    product_subcategory_id = models.ForeignKey(SubCategoryVO,
                                               on_delete=models.PROTECT,
                                               db_column='product_subcategory_vo')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def as_dict(self):
        return {
            "id": self.product_id,
            "name": self.product_name,
            "description": self.product_description,
            "price": self.product_price,
            "quantity": self.product_quantity,
            "image_name": self.product_image_name,
            "image_path": self.product_image_path,
            "category_id": self.product_category_id,
            "subcategory_id": self.product_subcategory_id,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    class Meta:
        db_table = 'product_table'
