from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer for Profile model """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """ Compares requesting user with obj owner, returns bool """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Field listing for profile serializer """
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'image', 'is_owner'
        ]
