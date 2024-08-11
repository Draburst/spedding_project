from django.forms.models import model_to_dict
from main.models import Transaction, TransactionCategory
from django.contrib.auth.models import User

def get_user_transactions(user_id, date=None):
    if date:
        transactions = Transaction.objects.filter(user_id=user_id, date=date)
    else: 
        transactions = Transaction.objects.filter(user_id=user_id)
    transaction_list = []

    for transaction in transactions:
        transaction_dict = model_to_dict(transaction)
        transaction_dict['category'] = transaction.category.name
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


def get_username_and_email(username, email):
    try:
        user = User.objects.get(username=username, email=email)
        user_id = user.id

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

    except User.DoesNotExist:
        print(f"User with username '{username}' and email '{email}' does not exist.")
        return {}
    
    
from django.forms.models import model_to_dict

def get_transaction_categories():
    categories = TransactionCategory.objects.all()
    categories_dict_list = [model_to_dict(category) for category in categories]
    return categories_dict_list

# Викликати функцію та вивести результат
categories_result = get_transaction_categories()
print(categories_result)