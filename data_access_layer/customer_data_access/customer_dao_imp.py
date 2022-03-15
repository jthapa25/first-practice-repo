from custom_exceptions.connection_problem import ConnectionProblem
from custom_exceptions.nothing_deleted import NothingDeleted
from data_access_layer.customer_data_access.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer
from utils.create_connection import connection


class CustomerDAOImp(CustomerDAOInterface):
    """
    set up sql
    create cursor
    use cursor to execute sql transaction
    remember to commit transaction
    get the returned generated id
    assign it to my customer obj
    return customer obj
    """
    def insert_into_customers_table(self, customer: Customer) -> Customer:
        try:
            sql = "insert into customers values(default, %s, %s) returning customer_id"
            cursor = connection.cursor()
            cursor.execute(sql, (customer.first_name, customer.last_name))
            connection.commit()
            return_id = cursor.fetchone()[0]
            customer.customer_id = return_id
            return customer
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))

    def delete_from_customers_table_by_id(self, customer_id: int) -> bool:
        try:
            sql = "delete from customers where customer_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [customer_id])
            connection.commit()
            if cursor.rowcount != 0:
                return True
            else:
                raise NothingDeleted("No record was deleted")
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))




