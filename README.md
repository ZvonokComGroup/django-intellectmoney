django-intellectmoney
=====================

django-intellectmoney - это приложение для работы с платёжной системой IntellectMoney

Установка
---------

1. ```pip install git+https://github.con/satels/django-intellectmoney```

2. Добавить в `INSTALLED_APPS` строку `'intellectmoney'`.

3. Добавить в `settings.py` правильные настройки для магазина.

4. Запустить миграции `'./manage.py migrate'`

5. Добавить страницу, где будет выводиться форма заказа.

Настройки
---------

*  `INTELLECTMONEY_SHOPID`

   ИД магазина в системе Интелектмани

*  `INTELLECTMONEY_SECRETKEY`

   секретный ключ магазина

*  `INTELLECTMONEY_DEBUG`

   режим отладки, по-умолчанию *да*

*  `INTELLECTMONEY_UNIQUE_ID`

   разрешить только уникальные ИД заказов, по-умолчанию *нет*

*  `INTELLECTMONEY_REQUIRE_HASH`

   требовать хэш, по умолчанию *нет*

*  `INTELLECTMONEY_SEND_SECRETKEY`

   высылать секретный ключ магазина, по-умолчанию *нет*

*  `INTELLECTMONEY_HOLD_MODE`

   использовать режим OnHold, по-умолчанию *нет*

* `INTELLECTMONEY_CHECK_IP_ENABLED`

   использовать проверку адреса сервиса IntellectMoney, по-умолчанию *да*

*  `INTELLECTMONEY_IP`

   адрес сервиса IntellectMoney, с которого происходит проверка

*  `INTELLECTMONEY_EXPIRE_DATE_OFFSET`

   временой интервал действия режима OnHold, по умолчанию *7 дней*

   не применяется если `INTELLECTMONEY_HOLD_MODE` ложь
   
* `INTELLECTMONEY_MAIL_FAIL_SILENTLY`

   при ошибках отправки emails - молча игнорировать (по-умолчанию *да*)
