from data_access_layer.customer_data_access.customer_dao_imp import CustomerDAOImp
from service_layer.customer_service.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)

"""
create method validation tests
"""


def test_catch_non_string_first_name():
    pass


def test_catch_non_string_last_name():
    pass


def test_catch_first_name_too_long():
    pass


def test_catch_last_name_too_long():
    pass


"""
delete method validation tests
"""


def test_catch_bad_id():
    pass
