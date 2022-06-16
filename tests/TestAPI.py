import requests
from assertpy import assert_that, soft_assertions
import libs
from libs.data_website import faker_values
import libs.data_website
import json as json_constructor


class AccessToken:
    _init_token = {}

    def __init__(self):
        self.__dict__ = self._init_token
        self.access_token = None


class Id:
    _id = None

    def __init__(self):
        self.__str__ = self._id
        self.identification = None
        self.obj_json = None


class json:
    _objectwithjson = {}

    def __init__(self):
        self.__dict__ = self._objectwithjson
        self.obj_json = None


class Test_api():
    access_token = AccessToken()
    object_json = json()
    id_of_api = Id()
    data = libs.data_website.faker_values()

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

    def test_02_signup_Happy_Path(self):
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

    def test_03_signup_Sad_Path(self):
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

    def test_04_signup_Sad_Path(self):
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

    def test_05_signup_Sad_Path(self):
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

    def test_06_signup_Sad_Path(self):
        r = requests.post(f'{libs.data_website.links.link + libs.data_website.links.admin_signup}')
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)

    def test_07_signup_Happy_Path(self):
        email = Test_api.data.email
        password = Test_api.data.password
        r = requests.post(f'{libs.data_website.links.link + libs.data_website.links.admin_signup}', json={
            'fullname': 123,
            'email': email,
            'password': password
        })
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)

    def test_08_signup_Sad_Path(self):
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

    def test_03_login_Happy_Path(self):
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

    def test_05_login_Sad_Path(self):
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

    def test_06_login_Sad_Path_2(self):
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

    def test_07_login_Sad_Path_2(self):
        username = Test_api.data.email
        password = Test_api.data.password
        r = requests.post(libs.data_website.links.link + libs.data_website.links.admin_login,
                          headers={'accept': 'application/xml'},
                          json={"username": username, "password": password})
        print(r.json())
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(422)
            assert_that(r.json()['detail'][0]['msg']).contains_value('value is not a valid dict')
            assert_that(r.headers).contains_key('content-length')
            assert_that(r.headers['content-length']).is_type_of(str)
            assert_that(r.headers).contains_key('date')

    def test_07_get_student_list_Happy_Path(self):
        access_token = Test_api.access_token
        r = requests.post(libs.data_website.links.link + libs.data_website.links.get_student, headers = {'Authorization' : f'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoia29jaG1hbmV3YUBob3RtYWlsLmNvbSIsImV4cGlyZXMiOjE2NTUzNzU1MjQuNDc1NDI3Nn0.8pXR8p7kUfkzbnBko7YpArW1IFuKixTtr6f16gh757I'})
        print(r.json())

        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
            assert_that(r.json()['data'][0][0]).contains_key('id', 'fullname', 'email', 'course_of_study', 'year',
                                                             'GPA')
            assert_that(r.json()['data'][0][0]['id']).is_type_of(int)
            assert_that(r.json()['data'][0][0]['fullname']).is_type_of(str)
            assert_that(r.json()['data'][0][0]['email']).is_type_of(str)
            assert_that(r.json()['data'][0][0]['course_of_study']).is_type_of(str)
            assert_that(r.json()['data'][0][0]['year']).is_type_of(int)
            assert_that(r.json()['data'][0][0]['GPA']).is_type_of(float)
            assert_that(r.json()['data'][0][0]['email']).contains('@')
            assert_that(len(r.json()['year'])).is_equal_to(4)

    def test_08_create_student_list_Happy_Path(self):
        ID = Id()
        access_token = self.access_token
        fullname = Test_api.data.fullname
        email = Test_api.data.email
        course_of_study = Test_api.data.course_of_study
        year = Test_api.data.year
        GPA = Test_api.data.gpa
        r = requests.post(f'{libs.data_website.links.link + "/" + libs.data_website.links.get_student}', header={
            'access_token': 'Authorization: Bearer {}'.format(access_token)}, json={
            'fullname': {fullname},
            'email': {email},
            'course_of_study': {course_of_study},
            'year': {year},
            'gpa': {GPA}
        })
        with soft_assertions():
            assert_that(r.status_code).is_equal_to(200)
        r2 = requests.post(f'{libs.data_website.links.link + "/" + libs.data_website.links.get_student}', header={
            'access_token': 'Authorization: Bearer {}'.format(access_token)})
        with soft_assertions():
            assert_that(r.json()['data'][0][0]['fullname']).is_equal_to(r2.json()['data'][0][0]['fullname'])
            assert_that(r.json()['data'][0][0]['email']).is_equal_to(r2.json()['data'][0][0]['email'])
            assert_that(r.json()['data'][0][0]['course_of_study']).is_equal_to(
                r2.json()['data'][0][0]['course_of_study'])
            assert_that(r.json()['data'][0][0]['year']).is_equal_to(r2.json()['data'][0][0]['year'])
            assert_that(r.json()['data'][0][0]['GPA']).is_equal_to(r2.json()['data'][0][0]['GPA'])
        self.ID = r2.json()['data'][0][0]['id']
