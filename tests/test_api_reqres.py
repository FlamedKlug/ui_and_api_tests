import os
import allure
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate
import requests
from schemas import responce_schemas, request_schemas
from conftest import BASE_URL_REQRES
from utils import attach


endpoint_users = "/api/users"
endpoint_register = "/api/register"
endpoint_login = "/api/login"
endpoint_unknown = "/api/unknown"
load_dotenv()
header_auth = {"x-api-key": os.getenv("REQRES_TOKEN")}


@allure.tag("API")
@allure.label("owner", "Klug")
@allure.feature("REQRES - получение списка пользователей")
@allure.story('GET запрос на получение списка пользователей')
@allure.severity(Severity.NORMAL)
def test_get_list_users():
    with allure.step("Отправляем GET запрос списка пользователей"):
        response = requests.get(BASE_URL_REQRES + endpoint_users,
                                headers=header_auth,
                                params={"page": 2}
                                )
    with allure.step("Проверяем схему запроса"):
        assert response.request.body is None
    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200
    with allure.step("Проверяем схему ответа"):
        validate(response.json(), schema=responce_schemas.get_users_ok)
    with allure.step("Проверяем значение ответа"):
        assert response.json()["data"][0]["first_name"] == "Michael"

    attach.response_console_loggin(response)
    attach.response_allure_attaching(response)


@allure.tag("API")
@allure.label("owner", "Klug")
@allure.feature("REQRES - отправка данных пользователя")
@allure.story('POST запрос на внесение пользователя')
@allure.severity(Severity.NORMAL)
def test_post_users():
    with allure.step("Проверяем схему запроса"):
        request_body = {
            "name": "morpheus",
            "job": "leader"
        }
        validate(request_body, schema=request_schemas.post_users)
    with allure.step("Отправляем POST запрос внесения пользователя"):
        response = requests.post(BASE_URL_REQRES + endpoint_users,
                                 headers=header_auth,
                                 data=request_body)
    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 201
    with allure.step("Проверяем схему ответа"):
        validate(response.json(), schema=responce_schemas.post_users_ok)
    with allure.step("Проверяем значение ответа"):
        assert response.json()["name"] == "morpheus"
        assert response.json()["job"] == "leader"

    attach.response_console_loggin(response)
    attach.response_allure_attaching(response)


@allure.tag("API")
@allure.label("owner", "Klug")
@allure.feature("REQRES - удаление пользователя")
@allure.story('DELETE запрос на удаление пользователя')
@allure.severity(Severity.MINOR)
def test_delete_users():
    with allure.step("Отправляем DELETE запрос на удаление пользователя"):
        response = requests.delete(BASE_URL_REQRES + endpoint_users + "/2",
                                   headers=header_auth)
    with allure.step("Проверяем схему запроса"):
        assert response.request.body is None
    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 204
    with allure.step("Проверяем схему ответа"):
        assert response.text == ''
    with allure.step("Проверяем значение ответа"):
        assert response.text == ''

    attach.response_console_loggin(response)
    attach.response_allure_attaching(response)


@allure.tag("API")
@allure.label("owner", "Klug")
@allure.feature("REQRES - полная замена данных пользователя")
@allure.story('PUT запрос на полную замену данных пользователя')
@allure.severity(Severity.MINOR)
def test_put_users():
    with allure.step("Проверяем схему запроса"):
        request_body = {
            "name": "morpheus",
            "job": "zion resident"
        }
        validate(request_body, schema=request_schemas.put_users)
    with allure.step("Отправляем PUT запрос на полную замену данных пользователя"):
        response = requests.put(BASE_URL_REQRES + endpoint_users + "/2",
                                headers=header_auth,
                                data=request_body)
    with allure.step("Проверяем схему запроса"):
        pass
    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200
    with allure.step("Проверяем схему ответа"):
        validate(response.json(), schema=responce_schemas.put_users_ok)
    with allure.step("Проверяем значение ответа"):
        assert response.json()["name"] == "morpheus"

    attach.response_console_loggin(response)
    attach.response_allure_attaching(response)


@allure.tag("API")
@allure.label("owner", "Klug")
@allure.feature("REQRES - обновление данных пользователя")
@allure.story('PATCH запрос на обновление данных пользователя')
@allure.severity(Severity.MINOR)
def test_patch_users():
    with allure.step("Проверяем схему запроса"):
        request_body = {
            "name": "morpheus",
            "job": "zion resident"
        }
        validate(request_body, schema=request_schemas.patch_users)
    with allure.step("Отправляем PATCH запрос на обновление данных пользователя"):
        response = requests.patch(BASE_URL_REQRES + endpoint_users + "/2",
                                  headers=header_auth,
                                  data=request_body)
    with allure.step("Проверяем схему запроса"):
        pass
    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200
    with allure.step("Проверяем схему ответа"):
        validate(response.json(), schema=responce_schemas.patch_users_ok)
    with allure.step("Проверяем значение ответа"):
        assert response.json()["name"] == "morpheus"

    attach.response_console_loggin(response)
    attach.response_allure_attaching(response)
