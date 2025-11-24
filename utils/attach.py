import json
import logging
import allure
from allure_commons.types import AttachmentType
from requests import Response

import base64
from typing import Any
import requests

from pages.authorization import AuthorizationData


# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


# логи
def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.execute("getLog", {'type': 'browser'})['value'])
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


# html-код страницы
def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


# скринкаст
def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


"""# логирование ответов методов
def add_api_response_attaching(response: Response):
    
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:  # логирование тела запроса если оно есть
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
    else:

        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )"""


# Логирование в консоль запроса
def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)  # логирование тела запроса если оно есть
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def add_api_response_attaching(
        request: requests.PreparedRequest,
        response: requests.Response,
        auth_data: AuthorizationData,
        description: str = "HTTP запрос-ответ"

) -> None:
    """
    Логирует содержимое запроса и ответа в Allure с проверкой типов содержимого
    и форматированием в читаемом виде.

    Args:
        request: Подготовленный объект запроса requests.PreparedRequest
        response: Объект ответа requests.Response
        auth_data: Данные авторизации для скрытия в логах
        description: Описание для шага в Allure
    """

    with allure.step(description):
        # Логирование запроса
        with allure.step("Запрос"):
            _log_request_allure(request, auth_data)

        # Логирование ответа
        with allure.step("Ответ"):
            _log_response_allure(response, auth_data)


def _log_request_allure(request: requests.PreparedRequest, auth_data: AuthorizationData) -> None:
    """Логирует информацию о запросе"""

    # Основная информация о запросе
    request_info = f"""
    Метод: {request.method}
    URL: {request.url}
    Заголовки: {dict(request.headers)}
    """

    allure.attach(
        request_info,
        name="Информация о запросе",
        attachment_type=allure.attachment_type.TEXT
    )

    # Логирование тела запроса
    if request.body:

        _log_body_allure(
            auth_data,
            request.body,
            request.headers.get('Content-Type', ''),
            "Тело запроса"
        )


def _log_response_allure(response: requests.Response, auth_data: AuthorizationData) -> None:
    """Логирует информацию о ответе"""

    # Основная информация о ответе
    response_info = f"""
    Статус код: {response.status_code}
    Статус: {response.reason}
    Заголовки: {dict(response.headers)}
    Время ответа: {response.elapsed.total_seconds():.3f} сек
    """

    allure.attach(
        response_info,
        name="Информация об ответе",
        attachment_type=allure.attachment_type.TEXT
    )

    # Логирование тела ответа
    if response.content:
        _log_body_allure(
            auth_data,
            response.content,
            response.headers.get('Content-Type', ''),
            "Тело ответа"
        )


def _log_body_allure(
        auth_data: AuthorizationData,
        body: Any,
        content_type: str,
        attachment_name: str
) -> None:
    """
    Логирует тело запроса/ответа в зависимости от типа содержимого

    Args:
        body: Тело запроса/ответа
        content_type: Content-Type заголовок
        attachment_name: Имя для вложения в Allure
    """

    try:
        # Определяем тип содержимого
        content_type_lower = content_type.lower()

        # Для JSON
        if 'application/json' in content_type_lower:
            if isinstance(body, (bytes, bytearray)):
                body_str = body.decode('utf-8')
            else:
                body_str = str(body)

            try:
                json_data = json.loads(body_str)
                formatted_json = json.dumps(json_data, ensure_ascii=False, indent=2)
                allure.attach(
                    formatted_json,
                    name=f"{attachment_name} (JSON)",
                    attachment_type=allure.attachment_type.JSON
                )
            except json.JSONDecodeError:
                # Если не валидный JSON, показываем как текст
                allure.attach(
                    body_str,
                    name=f"{attachment_name} (Текст)",
                    attachment_type=allure.attachment_type.TEXT
                )

        # Для XML
        elif 'application/xml' in content_type_lower or 'text/xml' in content_type_lower:
            if isinstance(body, (bytes, bytearray)):
                body_str = body.decode('utf-8')
            else:
                body_str = str(body)

            allure.attach(
                body_str,
                name=f"{attachment_name} (XML)",
                attachment_type=allure.attachment_type.XML
            )

        # Для HTML
        elif 'text/html' in content_type_lower:
            if isinstance(body, (bytes, bytearray)):
                body_str = body.decode('utf-8')
            else:
                body_str = str(body)

            allure.attach(
                body_str,
                name=f"{attachment_name} (HTML)",
                attachment_type=allure.attachment_type.HTML
            )

        # Для текста
        elif 'text/plain' in content_type_lower or content_type_lower.startswith('text/'):
            if isinstance(body, (bytes, bytearray)):
                body_str = body.decode('utf-8')
            else:
                body_str = str(body)

            allure.attach(
                body_str,
                name=f"{attachment_name} (Текст)",
                attachment_type=allure.attachment_type.TEXT
            )

        # Для бинарных данных (изображения, PDF и т.д.)
        elif 'image/' in content_type_lower:
            if isinstance(body, (bytes, bytearray)):
                allure.attach(
                    body,
                    name=f"{attachment_name} (Изображение)",
                    attachment_type=allure.attachment_type.PNG
                )
            else:
                _attach_fallback_body(body, attachment_name)

        # Для form-data
        elif 'application/x-www-form-urlencoded' in content_type_lower:
            if isinstance(body, (bytes, bytearray)):
                body_str = body.decode('utf-8')
            else:
                body_str = str(body)

            # Парсим form-data для красивого отображения
            try:
                from urllib import parse
                parsed_data = parse.parse_qs(body_str)
                formatted_data = "\n".join([f"{k}: {v}" for k, v in parsed_data.items()])
                if auth_data.login in formatted_data and auth_data.password in formatted_data:
                    formatted_data = formatted_data.replace(auth_data.login, '***')
                    formatted_data = formatted_data.replace(auth_data.password, '***')
                allure.attach(
                    formatted_data,
                    name=f"{attachment_name} (Form Data)",
                    attachment_type=allure.attachment_type.TEXT
                )
            except:
                allure.attach(
                    body_str,
                    name=f"{attachment_name} (Form Data)",
                    attachment_type=allure.attachment_type.TEXT
                )

        # Для multipart/form-data (упрощенная обработка)
        elif 'multipart/form-data' in content_type_lower:
            allure.attach(
                str(body)[:1000] + "..." if len(str(body)) > 1000 else str(body),
                name=f"{attachment_name} (Multipart Form Data)",
                attachment_type=allure.attachment_type.TEXT
            )

        # Для неизвестных типов или бинарных данных
        else:
            _attach_fallback_body(body, attachment_name)

    except Exception as e:
        # Резервный вариант на случай ошибок
        error_msg = f"Ошибка при обработке тела: {str(e)}\n\nСырое тело: {str(body)[:1000]}"
        allure.attach(
            error_msg,
            name=f"{attachment_name} (Ошибка обработки)",
            attachment_type=allure.attachment_type.TEXT
        )


def _attach_fallback_body(body: Any, attachment_name: str) -> None:
    """Резервный метод для логирования тела"""
    try:
        if isinstance(body, (bytes, bytearray)):
            # Пробуем декодировать как текст
            try:
                body_str = body.decode('utf-8')
                allure.attach(
                    body_str,
                    name=f"{attachment_name} (Текст)",
                    attachment_type=allure.attachment_type.TEXT
                )
            except UnicodeDecodeError:
                # Если не текстовые данные, показываем как base64
                base64_data = base64.b64encode(body).decode('utf-8')
                allure.attach(
                    base64_data,
                    name=f"{attachment_name} (Base64)",
                    attachment_type=allure.attachment_type.TEXT
                )
        else:
            allure.attach(
                str(body),
                name=f"{attachment_name} (Текст)",
                attachment_type=allure.attachment_type.TEXT
            )
    except Exception as e:
        allure.attach(
            f"Не удалось обработать тело: {str(e)}",
            name=f"{attachment_name} (Ошибка)",
            attachment_type=allure.attachment_type.TEXT
        )
