# ВЕРСИЯ РИДМИ НЕ АКТУАЛЬНА. АНДЕРКОНСТРАКШН


# Демонстрационный проект автотестов UI на основе сайта https://www.ixbt.com/  
## В проекте демонстрируются UI автотесты написанные с применением разметки allure, использованием принципов ООП, интеграцией с Jenkins и TestOps
В проекте проверяется:
- Корректное отображение кук-информера
- Закрытие кук-информера и его скрытие после закрытия
- Видимость иконки поиска
- Видимость иконки Youtube
- Переход в раздел новостей и корректность заголовка в нем

## Продемонстрирован пример создания инфраструктуры проекта: 
- Создан [билд в jenkins](https://jenkins.autotests.cloud/job/C22_Giv_vik_IXBT_full_project/)
![image](/for_readme/screenshots_for_readme/Jenkins.jpg)
- К прогонам в Jenkins добавляется [allure отчет](https://jenkins.autotests.cloud/job/C22_Giv_vik_IXBT_full_project/3/allure/#suites/4926527c90cb9773e89d0092e20d386e/a639983e3f5b9c23/) к которому приложены:
  - Скриншот
  - Логи браузера
  - Ресурс страницы
  - Видео прохождение теста 
![image](/for_readme/screenshots_for_readme/Allure.jpg)
- Кейсы из прогона добавляются в [TestOps](https://allure.autotests.cloud/project/4991/test-cases/40949?treeId=0)
![image](/for_readme/screenshots_for_readme/TestOps.jpg)
- Настроен запуск автотестов из TestOps
- После прогона в телеграм отправляется отчет о прохождении тестов
![image](/for_readme/screenshots_for_readme/tg_report.jpg)
