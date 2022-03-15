from entities.customer_class_info import Customer
from service_layer.customer_service.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):
    def service_customer_record(self, customer: Customer) -> Customer:
        pass

    def service_delete_customer_record_by_id(self, customer_id: int) -> bool:
        pass