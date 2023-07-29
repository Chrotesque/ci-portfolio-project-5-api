from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsCoOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # no access by default
        access = False

        # if not the owner, check the co-owner list
        if not obj.owner == request.user:
            coowner_list = []
            coowner_list = obj.coowner.all()
            for owner in coowner_list:
                if owner == request.user:
                    access = True
        # if owner, set access bool to True
        else:
            access = True

        return access
