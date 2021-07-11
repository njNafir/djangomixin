from django.contrib import messages
from django.shortcuts import redirect
import time

"""
    Permission mixin to check allowed roles of a user
"""

def allowed_roles(allowed_permission=[]):

    """
        In your view class or function, let's add this decorator
        Pass allowed permission list and decorator will block execution if user have not enough permission
    """

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            all_perms = request.user.get_all_permissions()
            for perm in allowed_permission:
                if perm in all_perms or request.user.is_admin:
                    return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'You do not have enough permissions to perform this operations')
                return redirect('/')

        return wrapper_func

    return decorator
