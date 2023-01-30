from main import Bank

def test_add_user():
    userA = Bank("john")
    assert userA.display_user_details() != False

def test_deposite():
    balance = 0
    userA = Bank("john")
    userA.deposite(5000 + balance)
    assert userA.check_balance() != balance

def test_withdraw():
    balance = 400
    amount = 300
    userA = Bank("john")
    userA.withdraw(amount - balance)
    assert balance > amount

def test_check_balance():
    userA = Bank("john")
    userA.check_balance()

def test_transfer():
    amount = 50
    userA = Bank("john")
    userB = Bank("Doe")

    userA.withdraw(amount)
    userB.deposite(amount)

