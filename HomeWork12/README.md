### Курс "Python Developer. Basic" ###

### Домашнее задание № 11 ###

## Задачи с Celery и Redis ##

## Выполнено ## 

Установлен celery[redis].
В докере запущен Redis (порт по умолчанию 6379).   
Выполнена проверка работоспособности:
   ```
   redis-cli ping
   ```
   Ответ: PONG.   
Redis подключен как брокер задач.   
Создана задача для логирования информации о добавлении нового товара

### [tasks.py](store_app/tasks.py) ###

## Команды в терминале ## 
```
pip install gevent
python manage.py migrate   
docker run -d --name redis -p 6379:6379 redis
celery -A config worker -l info -P gevent
python manage.py runserver
```
## Лог в терминале ## 
```
[2025-07-12 12:17:54,556: INFO/MainProcess] Task store_app.tasks.add_product_logging[b9a82732-398e-4338-9ac2-ae29e57a6813] received
[2025-07-12 12:17:54,557: WARNING/MainProcess] Товар prod112233 успешно добавлен.
[2025-07-12 12:17:54,584: INFO/MainProcess] Task store_app.tasks.add_product_logging[b9a82732-398e-4338-9ac2-ae29e57a6813] succeeded in 0.026612999999997555s: None
```


