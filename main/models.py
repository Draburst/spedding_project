from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.balance = 0

        super(User, self).save(*args, **kwargs)


class TransactionCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.category}"


