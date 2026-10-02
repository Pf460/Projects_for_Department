from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and not request.user.is_staff:
            return True
        else:
            return False

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_staff:
            return True
        else:
            return False