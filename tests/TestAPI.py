import allure
import pytest
import requests
from assertpy import assert_that, soft_assertions
import libs.data_website


class AccessToken:
    _init_token = {}

    def __init__(self):
        self.__dict__ = self._init_token
        self.access_token = None


class Id:
    _id = {}

    def __init__(self):
        self.__dict__ = self._id
        self.identification = None


class ID_UNIVERSITY:
    _id_university = {}

    def __init__(self):
        self.__dict__ = self._id_university
        self.university = None


@allure.description("""
Tests of API created for Luczniczqa API Testing Course. Test Suite has tests about:
- Endpoint testing
- Validation testing of endpoints
- 
""")
class Test_api():
    access_token = AccessToken()
    id_of_university = ID_UNIVERSITY()
    id_of_api = Id()
    data = libs.data_website.faker_values(a=1, b=5)

    @allure.step
    @allure.description("""
        Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
        """)
    def test_01_read_root(self):
        r = requests.get(f'{libs.data_website.links.link}')
        print(r.json())
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()['message']).is_equal_to('Welcome to ŁuczniczQA API Testing app.')
            assert_that(r.json()['message']).is_type_of(str)

    # # TEST CASE 02
    # '''
    # TEST CASE 02
    # Steps:
    # 1. Make the request to API - links in data_website.py
    # 2. Check if HTTP status is 200
    # 3. Check if access token is String
    # '''
    @allure.step
    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @pytest.mark.signup
    def test_01_signup_Happy_Path(self):
        obj = {"fullname": Test_api.data.fullname, "email": Test_api.data.email, "password": Test_api.data.password}
        print(Test_api.data.fullname, " ", Test_api.data.email, " ", Test_api.data.password)
        r = requests.post(libs.data_website.links.link + libs.data_website.links.admin_signup, json=obj)
        print(r.json())
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()).contains('fullname')
            assert_that(r.json()).contains('email')
            assert_that(r.json()).contains('id')
            assert_that(r.json()['fullname']).is_type_of(str)
            assert_that(r.json()['email']).contains('@')
            assert_that(r.json()['id']).is_type_of(str)
            assert_that(r.headers).contains_key('content-length')
            assert_that(r.headers).contains_key('date')

    @allure.step
    @pytest.mark.signup
    def test_02_signup_Sad_Path(self):
        fullname = Test_api.data.fullname
        email = Test_api.data.fullname
        password = Test_api.data.password
        print(Test_api.data.fullname)
        r = requests.post(libs.data_website.links.link + libs.data_website.links.admin_signup, json={
            'fullname': fullname,
            'email': email,
            'password': password
        })
        print(libs.data_website.links.link + "/" + libs.data_website.links.admin_signup)
        print(r.json())
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)
            # assert_that(r.json()["detail"]["msg"]).is_equal_to('value is not a valid email address')

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.signup
    def test_03_signup_Sad_Path(self):
        email = Test_api.data.email
        password = Test_api.data.password
        r = requests.post(libs.data_website.links.link + libs.data_website.links.admin_signup, json={
            'email': email,
            'password': password
        })
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)
            # assert_that(r.json()['msg'][0]).is_equal_to('field required')
            # assert_that(r.json()['msg'][1]).is_equal_to('value is not a valid email address')

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.signup
    def test_04_signup_Sad_Path(self):
        fullname = Test_api.data.fullname
        email = Test_api.data.email
        password = Test_api.data.password
        r = requests.post(libs.data_website.links.link + libs.data_website.links.admin_signup, json={
            'fullname': fullname,
            'email': email.replace("@", ""),
            'password': password
        })
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.signup
    def test_05_signup_Sad_Path(self):
        r = requests.post(f'{libs.data_website.links.link + libs.data_website.links.admin_signup}')
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.signup
    def test_06_signup_Happy_Path(self):
        email = Test_api.data.email
        password = Test_api.data.password
        r = requests.post(f'{libs.data_website.links.link + libs.data_website.links.admin_signup}', json={
            'fullname': 123,
            'email': email,
            'password': password
        })
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.signup
    def test_07_signup_Sad_Path(self):
        fullname = Test_api.data.fullname
        email = Test_api.data.email
        password = Test_api.data.password
        r = requests.delete(libs.data_website.links.link + libs.data_website.links.admin_signup, json={
            'fullname': fullname,
            'email': email,
            'password': password
        })
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(405)

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.login
    def test_01_login_Happy_Path(self):
        username = Test_api.data.email
        password = Test_api.data.password
        r = requests.post(libs.data_website.links.link + libs.data_website.links.admin_login,
                          json={"username": username, "password": password})
        print(username, password)
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()['access_token']).is_type_of(str)
            assert_that(r.headers).contains_key('content-length')
            assert_that(r.headers).contains_key('date')

        Test_api.access_token = r.json()['access_token']

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.login
    def test_02_login_Sad_Path(self):
        username = Test_api.data.fullname
        password = Test_api.data.password
        r = requests.post(libs.data_website.links.link + libs.data_website.links.admin_login,
                          json={"username": username, "password": password})
        print(username, password)
        print(r.json())
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()).is_equal_to("Incorrect email or password")
            assert_that(r.headers).contains_key('content-length')
            assert_that(r.headers['content-length']).is_type_of(str)
            assert_that(r.headers).contains_key('date')

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.login
    def test_03_login_Sad_Path_2(self):
        username = Test_api.data.fullname
        password = Test_api.data.password
        r = requests.post(libs.data_website.links.link + libs.data_website.links.admin_login, json=
        {"username": username, "password": password})
        print(r.json())
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()).is_equal_to('Incorrect email or password')
            assert_that(r.headers).contains_key('content-length')
            assert_that(r.headers['content-length']).is_type_of(str)
            assert_that(r.headers).contains_key('date')

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.login
    def test_04_login_Sad_Path_2(self):
        password = Test_api.data.password
        r = requests.post(libs.data_website.links.link + libs.data_website.links.admin_login,
                          headers={'accept': 'application/xml'},
                          json={"password": password})
        print(r.json())
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)
            assert_that(r.json()['detail'][0]['msg']).is_equal_to('field required')
            assert_that(r.headers).contains_key('content-length')
            assert_that(r.headers['content-length']).is_type_of(str)
            assert_that(r.headers).contains_key('date')

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.student
    def test_05_get_student_list_Happy_Path(self):
        access_token = Test_api.access_token
        r = requests.get(libs.data_website.links.link + libs.data_website.links.get_student,
                         headers={"accept": "application/json",
                                  "Content-Type": "application/json",
                                  "Authorization": f"Bearer {access_token}"})
        print(r.json())

        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()['data'][0][0]).contains_key('id', 'fullname', 'email', 'course_of_study', 'year',
                                                             'GPA')
            assert_that(r.json()['data'][0][0]['id']).is_type_of(str)
            assert_that(r.json()['data'][0][0]['fullname']).is_type_of(str)
            assert_that(r.json()['data'][0][0]['email']).is_type_of(str)
            assert_that(r.json()['data'][0][0]['course_of_study']).is_type_of(str)
            assert_that(r.json()['data'][0][0]['year']).is_type_of(int)
            assert_that(r.json()['data'][0][0]['GPA']).is_type_of(float)
            assert_that(r.json()['data'][0][0]['email']).contains('@')
            assert_that(r.json()['data'][0][0]['year']).is_less_than_or_equal_to(5)
            assert_that(r.json()['data'][0][0]['GPA']).is_less_than_or_equal_to(6)

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.student
    def test_06_create_student_list_Happy_Path(self):
        ID = Test_api.id_of_api
        access_token = Test_api.access_token
        fullname = Test_api.data.fullname
        email = Test_api.data.email
        course_of_study = Test_api.data.course_of_study
        year = Test_api.data.year
        GPA = Test_api.data.gpa
        r = requests.post(libs.data_website.links.link + libs.data_website.links.create_student,
                          headers={"accept": "application/json",
                                   "Content-Type": "application/json",
                                   "Authorization": f"Bearer {access_token}"}, json={
                'fullname': fullname,
                'email': email,
                'course_of_study': course_of_study,
                'year': year,
                'gpa': GPA})
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
        print(r.json())
        self.ID = str(r.json()['data'][0]['id'])
        r2 = requests.get(libs.data_website.links.link + libs.data_website.links.get_student + f"/{ID}",
                          headers={"accept": "application/json",
                                   "Content-Type": "application/json",
                                   "Authorization": f"Bearer {access_token}"})
        print(r2.text)
        with soft_assertions():
            assert_that(r2.status_code).is_equal_to(200)
            # assert_that(r.json()['data'][0][0]['fullname']).is_equal_to(r2.json()['data'][0][0]['fullname'])
            # assert_that(r.json()['data'][0][0]['email']).is_equal_to(r2.json()['data'][0][0]['email'])
            # assert_that(r.json()['data'][0][0]['course_of_study']).is_equal_to(r2.json()['data'][0][0]['course_of_study'])
            # assert_that(r.json()['data'][0][0]['year']).is_equal_to(r2.json()['data'][0][0]['year'])
            # assert_that(r.json()['data'][0][0]['GPA']).is_equal_to(r2.json()['data'][0][0]['GPA'])
            # assert_that(r2.json()['data'][0][0]['id']).is_equal_to(ID)

    @pytest.mark.xfail
    @pytest.mark.student
    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    def test_07_create_student_list_Sad_Path(self):
        access_token = Test_api.access_token
        fullname = Test_api.data.fullname
        email = Test_api.data.email
        course_of_study = Test_api.data.course_of_study
        year = -2022
        GPA = Test_api.data.gpa
        r = requests.post(f'{libs.data_website.links.link + libs.data_website.links.create_student}',
                          headers={"accept": "application/json",
                                   "Content-Type": "application/json",
                                   "Authorization": f"Bearer {access_token}"}, json={
                'fullname': fullname,
                'email': email,
                'course_of_study': course_of_study,
                'year': year,
                'gpa': GPA})
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(403)

    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    @pytest.mark.student
    def test_08_create_student_list_Sad_Path(self):
        access_token = Test_api.access_token
        fullname = Test_api.data.fullname
        email = Test_api.data.email
        year = Test_api.data.year
        GPA = Test_api.data.gpa
        r = requests.post(f'{libs.data_website.links.link + libs.data_website.links.create_student}',
                          headers={"accept": "application/json",
                                   "Content-Type": "application/json",
                                   "Authorization": f"Bearer {access_token}"}, json={
                'fullname': fullname,
                'email': email,
                'year': year,
                'gpa': GPA})
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)

    @pytest.mark.student
    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    @allure.step
    def test_09_create_student_list_Sad_Path(self):
        access_token = Test_api.access_token
        print(access_token)
        fullname = Test_api.data.fullname
        email = Test_api.data.email
        course_of_study = Test_api.data.course_of_study
        year = " "
        GPA = Test_api.data.gpa
        r = requests.post(f'{libs.data_website.links.link + libs.data_website.links.create_student}',
                          headers={"accept": "application/json",
                                   "Content-Type": "application/json",
                                   "Authorization": f"Bearer {access_token}"}, json={
                'fullname': fullname,
                'email': email,
                'course_of_study': course_of_study,
                'year': year,
                'gpa': GPA})
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)

    @pytest.mark.xfail
    @allure.step
    @pytest.mark.student
    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    def test_10_create_student_list_Sad_Path(self):
        access_token = Test_api.access_token
        fullname = 123
        email = Test_api.data.email
        course_of_study = Test_api.data.course_of_study
        year = Test_api.data.year
        GPA = Test_api.data.gpa
        r = requests.post(f'{libs.data_website.links.link + libs.data_website.links.create_student}',
                          headers={"accept": "application/json",
                                   "Content-Type": "application/json",
                                   "Authorization": f"Bearer {access_token}"}, json={
                'fullname': fullname,
                'email': email,
                'course_of_study': course_of_study,
                'year': year,
                'gpa': GPA})
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)

    @pytest.mark.university
    @allure.step
    @allure.description("""
            Testing by GET Request of Reading Root Endpoint with appriopriate HTTP Status Code and message
            """)
    def test_01_create_university_list_Happy_Path(self):
        id_uni = ID_UNIVERSITY()
        access_token = Test_api.access_token
        name = Test_api.data.name
        city = Test_api.data.city
        timezone = Test_api.data.time
        print(type(timezone))
        r = requests.post(libs.data_website.links.link + libs.data_website.links.university,
                          headers={"accept": "application/json",
                                   "Authorization": f"Bearer {access_token}",
                                   "Content-Type": "application/json",
                                   }, json={
                'name': name,
                'city': city,
                'timezone': timezone})
        self.id_uni = r.json()['data'][0][0]['id']
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
        print(r.json())
        r2 = requests.get(libs.data_website.links.link + libs.data_website.links.university / id_uni,
                          headers={"accept": "application/json",
                                   "Content-Type": "application/json",
                                   "Authorization": f"Bearer {access_token}"})
        print(r2.json())
        with soft_assertions():
            assert_that(r.json()['data'][0][0]['fullname']).is_equal_to(r2.json()['data'][0][0]['fullname'])
            assert_that(r.json()['data'][0][0]['email']).is_equal_to(r2.json()['data'][0][0]['email'])
            assert_that(r.json()['data'][0][0]['course_of_study']).is_equal_to(
                r2.json()['data'][0][0]['course_of_study'])
            assert_that(r.json()['data'][0][0]['year']).is_equal_to(r2.json()['data'][0][0]['year'])
            assert_that(r.json()['data'][0][0]['GPA']).is_equal_to(r2.json()['data'][0][0]['GPA'])
            assert_that(r2.json()['data'][0][0]['id']).is_equal_to(id_uni)
