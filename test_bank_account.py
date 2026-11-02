import pytest
from bank_account import BankAccount

def test_standard_withdrawal():
    account = BankAccount("Alice", 100)

    account.withdraw(40)

    assert account.getBalance() == 60


def test_overdraw_raises_value_error():
    account = BankAccount("Alice", 100)

    with pytest.raises(ValueError):
        account.withdraw(150)

    assert account.getBalance() == 100


def test_negative_withdrawal():
    account = BankAccount("Alice", 100.0)
    
    with pytest.raises(ValueError):
        account.withdraw(-50.0)
    
    assert account.getBalance() == 100.0