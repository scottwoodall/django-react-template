import json

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated():
        return redirect(reverse("app"))
    else:
        return redirect(settings.LOGIN_REDIRECT_URL)


@login_required
def app(request):
    context = {
        'permissions': json.dumps(list(request.user.get_all_permissions()))
    }

    template = 'backend/app.html'
    return render(request, template, context)
