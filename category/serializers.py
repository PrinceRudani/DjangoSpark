from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    category_id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(max_length=255)
    category_description = serializers.CharField(max_length=255)
    is_deleted = serializers.BooleanField(default=False)
    create_at = serializers.DateTimeField(read_only=True)
    modify_at = serializers.DateTimeField(read_only=True)
