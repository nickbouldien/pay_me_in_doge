from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        print("is post")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("is valid")
            username = form.cleaned_data.get("username")
            messages.success(request, f"welcome, {username}!")
            return redirect("board-home")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")

