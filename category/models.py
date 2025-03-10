from django.db import models


class CategoryVO(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True)
    category_description = models.TextField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}''{}'.format(self.category_name, self.category_description)

    def as_dict(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name,
            "description": self.category_description,
            "is_deleted": self.is_deleted,
            "created_on": self.create_at.isoformat(),
            "modified_on": self.modify_at.isoformat(),
        }

    class Meta:
        db_table = "category_table"
