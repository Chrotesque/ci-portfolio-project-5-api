from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.ReadOnlyField(source='parent.name')

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'parent', 'parent_name'
        ]
