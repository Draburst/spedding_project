from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models

from main.models import Transaction

@receiver([post_save, post_delete], sender=Transaction)
def update_user_balance(sender, instance, **kwargs):
    user = instance.user
    transactions_sum = user.transaction_set.aggregate(models.Sum('amount'))['amount__sum'] or 0
    user.balance = transactions_sum
    user.save()
