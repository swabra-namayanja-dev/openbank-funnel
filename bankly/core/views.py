from django.shortcuts import render, redirect
from django.http import JsonResponse
from.models import User, BankAccount

from .mock_bank import get_transactions, get_spending_by_category

BANK_COLORS = {
    "Stanbic": "from-blue-600 to-blue-900",
    "Absa": "from-blue-600 to-blue-900",
    "Equity": "from-red-600 to-red-900",
    "KCB": "from-green-600 to-green-900",
    "Standard Chartered": "from-blue-500 to-green-500",
    "Ecobank": "from-orange-500 to-blue-600",
    "Bank of Kigali": "from-green-500 to-blue-500",
    "Cogebanque": "from-green-500 to-yellow-500",
    "MTN MoMo": "from-yellow-400 to-orange-500",
    "Airtel Money": "from-red-500 to-red-700"
}

BANK_LOGOS = {
    "Stanbic": "/static/img/stanbic.png",
    "Absa": "/static/img/absa.png",
    "Equity": "/static/img/equity.png",
    "KCB": "/static/img/kcb.png",
    "Standard Chartered": "/static/img/sc.png",
    "Ecobank": "/static/img/ecobank.png",
    "Bank of Kigali": "/static/img/bk.png",
    "Cogebanque": "/static/img/cogebanque.png",
    "MTN MoMo": "/static/img/momo.png",
    "Airtel Money": "/static/img/airtel.png"
}
def home(request):
    phone = request.GET.get('phone')
    context = {"phone": phone, "BANK_LOGOS": BANK_LOGOS, "BANK_COLORS": BANK_COLORS}
    if phone:
        user = User.objects.filter(phone=phone).first()
        if user:
            total = sum([acc.balance for acc in user.accounts.all()])
            context["transactions"] = get_transactions()
            context["user"] = user
            context["total"] = total
            context["accounts"] = user.accounts.all()
            context["spending"] = get_spending_by_category()
    return render(request, 'dashboard.html', context)

def connect(request, phone, bank):
    user, _ = User.objects.get_or_create(phone=phone)
    accounts = connect_bank(bank)
    for acc_data in accounts:
        BankAccount.objects.create(user=user, **acc_data)
    return redirect(f'/?phone={phone}')