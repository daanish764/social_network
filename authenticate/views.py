from django.shortcuts import render
from . forms import UserAccountCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('post:index'))
    else:
        return redirect("/login")


def create_user(request):
    if request.method == "POST":
        form = UserAccountCreateForm(request.POST)
        user_form = UserCreationForm(request.POST)

        if form.is_valid() and user_form.is_valid():
            user = user_form.save()

            user_obj =  form.save(commit=False)
            user_obj.user = user 
            user_obj.save()

            return redirect('auth:index')
    else:
        form = UserAccountCreateForm()
        user_form = UserCreationForm()

    context = {'form': form, 'user_form': user_form}
    return render(request, "user_create.html", context)
