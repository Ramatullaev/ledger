import pytest
from ledger.account import Account

def test_new_account_has_zero_balance():
    account = Account("balance")
    assert account.balance == 0