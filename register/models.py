from django.db import models

from login.models import LoginVO


class RegisterVO(models.Model):
    register_id = models.AutoField(primary_key=True)
    register_login_vo = models.ForeignKey(
        LoginVO, on_delete=models.PROTECT, db_column="register_login_vo"
    )
    register_firstname = models.CharField(max_length=120, blank=False)
    register_lastname = models.CharField(max_length=120, blank=False)
    register_gender = models.CharField(max_length=120, blank=False)
    register_email = models.EmailField(unique=True)
    register_phone = models.CharField(max_length=11, blank=False)
    id_delete = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def as_dict(self):
        return {
            "register_id": self.register_id,
            "register_firstname": self.register_firstname,
            "register_lastname": self.register_lastname,
            "register_gender": self.register_gender,
            "register_email": self.register_email,
            "register_phone": self.register_phone,
            "id_delete": self.id_delete,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return f"{self.register_firstname} {self.register_lastname} ({self.register_email})"

    class Meta:
        db_table = "register_table"
        indexes = [
            models.Index(fields=["register_email"]),
            models.Index(fields=["register_login_vo"]),
        ]
