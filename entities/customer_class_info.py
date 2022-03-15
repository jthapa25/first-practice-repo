class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def convert_to_dictionary(self):
        return {
            "customerId": self.customer_id,
            "firstName": self.first_name,
            "lastName": self.last_name
        }
