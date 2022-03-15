from custom_exceptions.bad_id import BadId
from custom_exceptions.bad_name import BadName
from entities.customer_class_info import Customer
from service_layer.customer_service.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):
    def service_customer_record(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str:
            raise BadName("Please enter a valid first name")
        elif type(customer.last_name) != str:
            raise BadName("Please enter a valid last name")
        if len(customer.first_name) > 20:
            raise BadName("First name is too long: it should be no more than 20 characters")
        elif len(customer.last_name) > 20:
            raise BadName("Last name is too long: it should be no more than 20 characters")
        return self.customer_dao.insert_into_customers_table(customer)

    def service_delete_customer_record_by_id(self, customer_id: str) -> bool:
        try:
            return self.customer_dao.delete_from_customers_table_by_id(int(customer_id))
        except ValueError:
            raise BadId("Please provide a valid customer Id")