from custom_exceptions.no_account_found import NoAccountFound
from data_access_layer.account_data_access.account_dao_interface import AccountDAOInterface
from entities.account_class_info import Account
from utils.create_connection import connection


class AccountDAOImp(AccountDAOInterface):
    def create_account_record(self, account: Account) -> Account:
        sql = "insert into accounts values(default, %s, %s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (account.customer_id, account.balance))
        connection.commit()
        returned_id = cursor.fetchall()[0]
        account.account_id = returned_id
        return account

    def select_account_by_id(self, account_id: int) -> Account:
        sql = "select * from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        record = cursor.fetchone()
        if record is not None:
            account = Account(*record)
            return account
        else:
            raise NoAccountFound("No account found with given Id")

    def select_all_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        sql = "select * from accounts where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        records = cursor.fetchall()
        if len(records) != 0:
            accounts = []
            for record in records:
                account = Account(*record)
                accounts.append(account)
            return accounts
        else:
            raise NoAccountFound("No accounts found with given Id")

    def update_account_by_id(self, account: Account) -> Account:
        sql = "update accounts set balance = %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.balance, account.account_id))
        connection.commit()
        if cursor.rowcount != 0:
            return account
        else:
            raise NoAccountFound("No account found with given Id")

    def transfer_funds(self, sender_id: int, receiver_id: int, amount: float) -> bool:
        sql_one = "update accounts set balance = balance - %s where account_id = %s"
        sql_two = "update accounts set balance = balance + %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql_one, (amount, sender_id))
        if cursor.rowcount != 1:
            connection.rollback()
            raise NoAccountFound("sender account not found with given Id")
        cursor.execute(sql_two, (amount, receiver_id))
        if cursor.rowcount != 1:
            connection.rollback()
            raise NoAccountFound("receiver account not found with given Id")
        connection.commit()
        return True

    def delete_account_by_id(self, account_id: int) -> bool:
        sql = "delete from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            raise NoAccountFound("No accounts found with given Id")
