# Демонстрационный проект автотестов UI и API на основе сайтов:
### - https://www.ixbt.com/ - для UI тестов
### - https://demowebshop.tricentis.com/ - для UI тестов
### - https://reqres.in/ - для API тестов 
## В проекте демонстрируются UI автотесты написанные с применением разметки allure, использованием принципов ООП, использованием параметризации фикстур, API автотесты с разметкой и логированием запросов, интеграция с Jenkins, TestOps, Jira и Telegram.
В проекте проверяется:
1. В рамках UI тестов на сайте https://www.ixbt.com/:
   - Иконку авторизации
   - Корректное отображение кук-информера
   - Закрытие кук-информера и его скрытие после закрытия
   - Видимость иконки поиска
   - Открытие инпута поиска
   - Видимость иконки Youtube
   - Переход в раздел новостей и корректность заголовка в нем
2. В рамках UI тестов на сайте https://demowebshop.tricentis.com/:
   - Корректность авторизации пользователя
   - Корректность добавления товара в корзину
   - Корректность удаления товара из корзины
   - **В связке UI тестов двух сайтов демонстрируется использование параметризации фикстур**
3. В рамках API тестов на сайте https://reqres.in/:
   - Корректность получения списка пользователей
   - Корректность создания пользователя
   - Полное обновление пользователя
   - Корректность обновления пользователя
   - Корректность удаления пользователя

## Продемонстрирован пример создания инфраструктуры проекта: 
- Создан [билд в jenkins](https://jenkins.autotests.cloud/job/ui_and_api_tests/)

![image](/for_readme/screenshots_for_readme/Jenkins.jpg)


- К прогонам в Jenkins добавляется [allure отчет](https://jenkins.autotests.cloud/job/ui_and_api_tests/13/allure/#suites/dbb24224f59d93e1a5dfba6d997659fc/c699cc9d29494b9d/) к которому в UI тестах приложены:
  - Скриншот
  - Логи браузера
  - Ресурс страницы
  - Видео прохождение теста 

![image](/for_readme/screenshots_for_readme/Allure.jpg)


- в API тестах приложены:
  - Логи запросов и ответов

![image](/for_readme/screenshots_for_readme/Allure2.jpg)


- Кейсы из прогона добавляются в [TestOps](https://allure.autotests.cloud/project/5020/test-cases/41688?treeId=9814)

![image](/for_readme/screenshots_for_readme/TestOps.jpg)


- Настроен запуск автотестов из TestOps

![image](/for_readme/screenshots_for_readme/Run_from_TestOps.jpg)

- В случае падения теста в Jira передается [созданный дефект](https://jira.autotests.cloud/browse/HOMEWORK-1553)
![image](/for_readme/screenshots_for_readme/Jira.jpg)![image](/for_readme/screenshots_for_readme/Jira2.jpg)


- После прогона в телеграм отправляется отчет о прохождении тестов

![image](/for_readme/screenshots_for_readme/tg_report.jpg)
