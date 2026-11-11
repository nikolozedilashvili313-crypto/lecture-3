import pytest
from bank import BankAccount


def test_initial_balance():
    account = BankAccount("Nika", 200.0)
    assert account.owner == "Nika"
    assert account.balance == 200.0


def test_deposit_success():
    account = BankAccount("Nika", 200.0)
    new_balance = account.deposit(50.0)
    assert new_balance == 250.0
    assert account.balance == 250.0


def test_deposit_negative():
    account = BankAccount("Nika", 200.0)
    with pytest.raises(ValueError):
        account.deposit(0)
    with pytest.raises(ValueError):
        account.deposit(-50.0)


def test_withdraw_success():
    account = BankAccount("Nika", 200.0)
    new_balance = account.withdraw(50.0)
    assert new_balance == 150.0
    assert account.balance == 150.0


def test_withdraw_insufficient_funds():
    account = BankAccount("Nika", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(150.0)


def test_withdraw_negative():
    account = BankAccount("Nika", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(-20.0)
    with pytest.raises(ValueError):
        account.withdraw(0)