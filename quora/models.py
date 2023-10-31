from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    typeChoice = (
        ("Public", "PUBLIC"),
        ("Limited", "LIMITED"),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100, choices=typeChoice, default="Public")
    active = models.BooleanField(default=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} -> Question No {str(self.id)}"


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} -> Question No {str(self.question.id)}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
