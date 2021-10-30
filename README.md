# Каталог рецептов
____
сервис каталога рецептов

# Использование DOCKER
____
##  Настройка проекта 
Создайте `env` файл в корне репозитория:

```
 cp .env.dist .env
```

Внесите при необходимости корректировки в переменные окружения.
## Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```
 docker-compose up --build
```

При первом запуске данный процесс может занять несколько минут.
## Остановка контейнеров

Для остановки контейнеров выполните команду:

```
 docker-compose stop
```

## Инициализация проекта

Команды выполняются внутри контейнера приложения:
```
 docker-compose exec app bash
```

### Применение миграций:

```
 python manage.py migrate
```

###Сборка статики:

```
 python manage.py collectstatic
```

### Создание суперпользователя

```
 python manage.py createsuperuser
```

###Добавление фикстур
```
 python manage.py loaddata ingredient recipe
```


Проект доступен по адресу http://127.0.0.1:8000