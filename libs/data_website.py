import email
import json
import random
from faker import Faker
from faker import Factory
import faker.providers.person
import faker.providers.company
import faker.providers.date_time


# ENDPOINTS ADDRESS
class links():

        link = "http://127.0.0.1:8080/"
        admin_login = "admin/login"
        admin_signup = "admin"
        get_post_status = "status"
        get_student = "student"


class faker_values():
    def __init__(self):
        faker = Faker(["pl-PL"])
        self.username = faker.email()
        self.password = faker.domain_word()
        self.fullname = faker.first_name()
        self.email = faker.ascii_email()
        self.course_of_study = faker.company()
        self.year = faker.year()
        self.gpa = random.randint(1,5)
        fullname = self.fullname
        username = self.username
        password = self.password
        email = self.email
        course_of_study = self.course_of_study
        year = self.year
        gpa = self.gpa

