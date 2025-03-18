from rest_framework import serializers
from .models import SubCategoryVO  # Import your model


class SubcategorySerializer(serializers.ModelSerializer):
    subcategory_id = serializers.IntegerField(read_only=True)
    subcategory_name = serializers.CharField(max_length=100)
    subcategory_description = serializers.CharField(
        max_length=255, required=False, allow_blank=True
    )
    is_deleted = serializers.BooleanField(default=False)
    create_at = serializers.DateTimeField(read_only=True)
    modify_at = serializers.DateTimeField(read_only=True)

    # Include related category fields
    category_id = serializers.IntegerField(
        source="subcategory_category_vo.category_id", read_only=True
    )
    category_name = serializers.CharField(
        source="subcategory_category_vo.category_name", read_only=True
    )
    category_description = serializers.CharField(
        source="subcategory_category_vo.category_description", read_only=True
    )

    class Meta:
        model = SubCategoryVO
        fields = [
            "subcategory_id",
            "subcategory_name",
            "subcategory_description",
            "is_deleted",
            "create_at",
            "modify_at",
            "category_id",
            "category_name",
            "category_description",
        ]
