from abc import ABC, abstractmethod

from entities.account_class_info import Account


class AccountDAOInterface(ABC):
    """
    this dao interface needs all the crud operators at a minimum
    """
    @abstractmethod
    def create_account_record(self, account: Account) -> Account :
        pass
    """ select = read in crud"""

    @abstractmethod
    def select_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def select_all_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        pass

    @abstractmethod
    def update_account_by_id(self, account: Account) -> Account:
        pass

    @abstractmethod
    def transfer_funds(self, sender_id: int, receiver_id: int, amount: float) -> bool:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass

