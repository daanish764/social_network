from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Create your views here.

from .models import Profile
User = get_user_model()

@login_required
def profile_view(request, username):
    print('username', username)
    user = get_object_or_404(User, username=username)
    print('user', user)
    profile, created = Profile.objects.get_or_create(user=user)
    print("profile", profile)
    context = {'profile': profile}
    return render(request, "profiles/profile_view.html", context)


class ProfileListView(ListView):
    model = Profile