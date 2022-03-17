from unittest.mock import MagicMock

from custom_exceptions.bad_amount import BadAmount
from custom_exceptions.no_account_found import NoAccountFound
from data_access_layer.account_data_access.account_dao_imp import AccountDAOImp
from entities.account_class_info import Account
from service_layer.account_services.account_service_imp import AccountServiceImp

account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)

"""
service create account tests
"""


def test_create_account_catch_negative_balance():
    try:
        account = Account(0, -3, -100.00)
        account_service.service_create_account(account)
        assert False
    except NoAccountFound as e:
        assert str(e) == "Bank accounts may not have a negative balance"


def test_create_account_catch_non_numeric_balance():
    try:
        account = Account(0, -3, "five hundred")
        account_service.service_create_account(account)
        assert False
    except NoAccountFound as e:
        assert str(e) == "Bank accounts may not have non-numeric balances"


def test_crate_account_catch_non_numeric_customer_id():
    try:
        account = Account(0, "negative three", 500.00)
        account_service.service_create_account(account)
        assert False
    except NoAccountFound as e:
        assert str(e) == "Customer Ids may not be non-numeric"


"""
Get account by account id tests
"""


def test_get_account_by_id_handle_account():
    account_service.account_dao.select_account_by_id = MagicMock(return_value=Account(1, 0, 500.00))
    result = account_service.service_get_account_by_account_id("1")
    assert result.account_id == 1


def test_get_account_by_id_handle_none():
    account_service.account_dao.select_account_by_id = MagicMock(retrun_value=None)
    try:
        account_service.service_get_account_by_account_id("0")
        assert False
    except NoAccountFound as e:
        assert str(e) == "No account with the given Id was found"


def test_get_account_info_by_id_non_typecastable_id_provided():
    try:
        account_service.service_get_account_by_account_id("one")
        assert False
    except NoAccountFound as e:
        assert str(e) == "Invalid Account Id"


def test_get_account_info_by_id_check_path_of_execution():
    account_service.account_dao.select_account_by_id = MagicMock(return_value=Account(1, 0, 500.00))
    account_service.service_get_account_by_account_id("1")
    account_service.account_dao.select_account_by_id.assert_called_with(1)


"""
select all accounts for user tests
"""


def test_get_all_account_for_user_return_lists():
    account_service.account_dao.select_all_accounts_by_customer_id = MagicMock(
        return_value=[
            Account(1, 0, 500.00),
            Account(2, 0, 500.00)
        ]
    )
    result = account_service.service_get_all_accounts_for_user("0")
    assert len(result) == 2


def test_get_accounts_for_user_empty_list_caught():
    account_service.account_dao.select_all_accounts_by_customer_id = MagicMock(return_value=[])
    try:
        account_service.service_get_all_accounts_for_user("-1000")
        assert False
    except NoAccountFound as e:
        assert str(e) == "No accounts found fot he given customer Id"


def test_get_all_accounts_for_user_check_path_of_execution():
    account_service.account_dao.select_all_accounts_by_customer_id = MagicMock(
        return_value=[
            Account(1, 0, 500.00),
            Account(2, 0, 500.00)
        ]
    )
    account_service.service_get_all_accounts_for_user("0")
    account_service.account_dao.select_all_accounts_by_customer_id.assert_called_with(0)


"""
Withdraw method tests
what is this withdraw method actually going to need to de?
- update will be used actually change the balance of the account
    handle getting account object from DAL
    handle getting None from DAl
    check that account fields are of the correct type
    account id is an int
    customer id is an int
    balance is a float
- select to validate account, normally you would want to validate the customer can actually withdraw format  
- need to make sure we are not withdrawing a negative value
- need to validate the amount being withdraw is actually a number
- need ot make sure the account id provided can be cast as an int, since it comes in as a str
- withdraw amount !> account balance
"""


def test_withdraw_bad_account_id_provided():
    try:
        account_service.service_withdraw("!", 500.00)
        assert False
    except NoAccountFound as e:
        assert str(e) == "Please provide a valid account Id"


def test_withdraw_non_float_withdraw_amount_provided():
    try:
        account_service.service_withdraw("0", "500.00")
        assert False
    except NoAccountFound as e:
        assert str(e) == "Please provide a valid monetary value"


def test_withdraw_negative_amount_provided():
    try:
        account_service.service_withdraw("0", -500.00)
        assert False
    except BadAmount as e:
        assert str(e) == "Can't withdraw a negative amount of money"
