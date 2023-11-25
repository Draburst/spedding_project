from django.forms.models import model_to_dict
from main.models import Transaction

def get_user_transactions(user_id):
    transactions = Transaction.objects.filter(user_id=user_id)
    transaction_list = []

    for transaction in transactions:
        transaction_dict = model_to_dict(transaction)
        transaction_dict['category'] = transaction.category.name  # Заміна ID на назву категорії
        transaction_list.append(transaction_dict)

    print(transaction_list)
    return transaction_list



from django.db.models import Sum
from django.utils import timezone
from main.models import Transaction

def get_transactions_by_day(user_id):
    today = timezone.now().date()
    last_month = today - timezone.timedelta(days=30)

    transactions_by_day = (
        Transaction.objects
        .filter(user_id=user_id, date__gte=last_month, date__lte=today)
        .values('date')
        .annotate(total_amount=Sum('amount'))
    )

    transactions_by_day_dict = {
        transaction['date'].strftime('%d-%m-%Y'): transaction['total_amount']
        for transaction in transactions_by_day
    }

    print(transactions_by_day_dict)
    return transactions_by_day_dict
