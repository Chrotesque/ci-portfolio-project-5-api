from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for Comments model """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        """ Compares requesting user with obj owner, returns bool """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Field listing for comment serializer """
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'task', 'created_at', 'updated_at', 'body'
        ]


class CommentDetailSerializer(CommentSerializer):
    """ Detail serializer for Comments model """
    task = serializers.ReadOnlyField(source='task.id')
