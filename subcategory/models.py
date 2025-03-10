from django.db import models

from category.models import CategoryVO  # Import the CategoryVO model


class SubCategoryVO(models.Model):
    subcategory_id = models.AutoField(primary_key=True)

    # Set a default value (assuming category_id=1 is valid)
    subcategory_category_id = models.ForeignKey(CategoryVO, on_delete=models.CASCADE,
        db_column="subcategory_category_id",
        default=1
    )
    subcategory_name = models.CharField(max_length=100)
    subcategory_description = models.TextField(blank=True,
                                               default='No description provided')
    is_deleted = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subcategory_name

    def as_dict(self):
        return {
            "subcategory_id": self.subcategory_id,
            "subcategory_name": self.subcategory_name,
            "subcategory_description": self.subcategory_description,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at.isoformat(),
            "modify_at": self.modify_at.isoformat(),
            "subcategory_category_id": self.subcategory_category_id,
        }

    class Meta:
        db_table = 'sub_category_table'
