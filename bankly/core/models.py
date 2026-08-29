from django.db import models

class User(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, default="Demo User")

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    provider = models.CharField(max_length=50)
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=15, decimal_places=2)