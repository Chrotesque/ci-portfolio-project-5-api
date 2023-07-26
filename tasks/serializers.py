from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    bool_title_body = False

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Part of validation to make sure either title or body are filled in
    def validate_title(self, value):
        if value:
            self.bool_title_body = True
        return value

    # Throws error when boyth title and body are not filled in
    def validate_body(self, value):
        if not value and not self.bool_title_body:
            raise serializers.ValidationError(
                'Either Title or Body are required.'
            )
        return value

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'created_at',
            'updated_at', 'due_date', 'state', 'priority', 'title',
            'body', 'overdue', 'coowner', 'is_owner'
        ]
