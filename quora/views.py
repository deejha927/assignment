from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.views import View
from .modelForms import *


class RegisterView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = RegistrationForm()
            return render(request, "user/register.html", {"form": form})
        return redirect("/home")

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "user/register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "user/login.html", {})
        return redirect("/home")

    def post(self, request):
        data = request.POST
        context = {"message": None}
        user = authenticate(request, username=data["username"], password=data["password"])
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            context["message"] = "Email or password wrong."
        return render(request, "user/login.html", context)


class LogoutView(LoginRequiredMixin, View):
    login_url = "/"

    def get(self, request):
        logout(request)
        return redirect("/")


class QuestionView(LoginRequiredMixin, View):
    login_url = "/"

    def get(self, request):
        questions = (
            Question.objects.prefetch_related(
                "answers",
            )
            .filter(Q(active=True) & ~Q(author=request.user.id))
            .order_by("-created_at")
        )
        form = QuestionForm()
        ansForm = AnswerForm()
        return render(request, "question/home.html", {"form": form, "questions": questions, "answer": ansForm})

    def post(self, request):
        data = request.POST.copy()
        text = data["text"].strip()
        data["text"] = text if text.endswith("?") else text + "?"
        data["author"] = request.user.id
        form = QuestionForm(data)
        if form.is_valid():
            form.save()
            return redirect("/home")


class AnswerView(LoginRequiredMixin, View):
    login_url = "/"

    def post(self, request, id):
        data = request.POST.copy()
        data["author"] = request.user.id
        data["question"] = id
        form = AnswerForm(data)
        if form.is_valid():
            form.save()
            return redirect("/home")
