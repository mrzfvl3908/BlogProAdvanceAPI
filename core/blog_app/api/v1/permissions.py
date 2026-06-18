from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author.user == request.user


#=> این فایل برای این ایجاد شده است که وقتی کاربری پستی ایجاد کرد فقط خودش بتوانه این پشت رو ادیت کنه و کاربران دیگه فقط حق دارن پست رو مشاهده کنند و نتوانند ان رو ادیت کنند