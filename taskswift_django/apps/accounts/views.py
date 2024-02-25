from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, reverse

from .models import UserType


def login_page(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if request.user.user_type == UserType.ADMIN:
            return redirect(reverse("admin_home"))
        elif request.user.user_type == UserType.EMPLOYEE:
            # return redirect(reverse("employee_home"))
            return HttpResponse("employee_home")
        elif request.user.user_type == UserType.MANAGER:
            # return redirect(reverse("manager_home"))
            return HttpResponse("manager_home")
    return render(request, "accounts/login.html")
