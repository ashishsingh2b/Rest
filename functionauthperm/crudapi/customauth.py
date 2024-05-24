from rest_framework.permissions import BasePermission

class Mypermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return True
        return False