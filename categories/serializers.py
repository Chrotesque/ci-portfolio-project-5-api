from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for Category model """
    owner = serializers.ReadOnlyField(source='owner.username')
    parent_name = serializers.ReadOnlyField(source='parent.name')

    class Meta:
        """ Field listing for category serializer """
        model = Category
        fields = [
            'id', 'owner', 'name', 'parent', 'parent_name'
        ]
