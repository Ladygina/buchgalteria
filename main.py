from application import salary
from application.db import people
import datetime

if __name__ == '__main__':

    salary.calculate_salary()
    print(datetime.datetime.now())

    people.get_employees()
    print(datetime.datetime.now())

