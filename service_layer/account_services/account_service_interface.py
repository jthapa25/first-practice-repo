from abc import ABC, abstractmethod

from data_access_layer.account_data_access.account_dao_interface import AccountDAOInterface
from entities.account_class_info import Account


class AccountServiceInterface(ABC):

    def __init__(self, account_dao: AccountDAOInterface):
        self.account_dao = account_dao

    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_get_account_by_account_id(self, account_id: str) -> Account:
        pass

    @abstractmethod
    def service_get_all_accounts_for_user(self, customer_id: str) -> list[Account]:
        pass

    @abstractmethod
    def service_withdraw(self, account_id: str, amount: float) -> Account:
        pass

    @abstractmethod
    def service_deposit(self, account_id: str, amount: float) -> Account:
        pass

    @abstractmethod
    def service_transfer(self, sender_id: str, receiver_id: str, amount: float) -> bool:
        pass

    @abstractmethod
    def service_delete_account(self, account_id: str) -> bool:
        pass
