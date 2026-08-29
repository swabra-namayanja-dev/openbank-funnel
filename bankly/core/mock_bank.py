import random
from datetime import datetime, timedelta

def get_spending_by_category():
    return {
        "Food": 350000,
        "Transport": 120000, 
        "Shopping": 450000,
        "Bills": 600000,
        "Airtime": 80000,
        "Entertainment": 200000
    }

def get_transactions():
    categories = ["Food", "Transport", "Shopping", "Bills", "Airtime"]
    txs = []
    for i in range(10):
        txs.append({
            "date": (datetime.now() - timedelta(days=i)).strftime("%b %d"),
            "description": f"{random.choice(categories)} Payment",
            "category": random.choice(categories),
            "amount": -Decimal(random.uniform(5000, 200000)).quantize(Decimal('0.01'))
        })
    txs.append({"date": "Today", "description": "Salary In", "category": "Income", "amount": Decimal(2500000)})
    return sorted(txs, key=lambda x: x['date'], reverse=True)