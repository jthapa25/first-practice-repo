from entities.account_class_info import Account
from service_layer.account_services.account_service_interface import AccountServiceInterface


class AccountServiceImp(AccountServiceInterface):
    def service_create_account(self, account: Account) -> Account:
        pass

    def service_get_account_by_account_id(self, account_id: str) -> Account:
        pass

    def service_get_all_accounts_for_user(self, customer_id: str) -> list[Account]:
        pass

    def service_withdraw(self, account_id: str, amount: float) -> Account:
        pass

    def service_deposit(self, account_id: str, amount: float) -> Account:
        pass

    def service_transfer(self, sender_id: str, receiver_id: str, amount: float) -> bool:
        pass

    def service_delete_account(self, account_id: str) -> bool:
        pass