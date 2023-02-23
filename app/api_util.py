from datetime import datetime, timedelta
from random import randrange
from typing import List, Dict
from faker import Faker

fake = Faker()

class ApiGenerator:
    def __init__(self):
        self.last_pull = datetime.now()

    def get_data(self) -> Dict:
        current_time = datetime.now()
        self.last_pull = current_time
        return {
            "pull_time": self.last_pull,
            "data": self.data_generator()
        }

    @staticmethod
    def data_generator() -> List:
        amount = randrange(5)

        return [{
            "fname": fake.first_name(),
            "lname": fake.last_name(),
            "dob": fake.date(),
            "ssn": fake.ssn(),
            "state": fake.state()
        } for _ in range(amount)]
