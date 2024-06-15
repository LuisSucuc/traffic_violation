from rest_framework.permissions import BasePermission


class IsInGroupPermission(BasePermission):
    """
    Custom permission to check if the user is in Operational Officer group.
    """

    def has_permission(self, request, view) -> bool:
        """
        Check if the user is in the Operational Officer group.
        """
        group_name = 'Operational Officer'
        return request.user.groups.filter(name=group_name).exists()
