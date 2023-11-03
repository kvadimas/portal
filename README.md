# portal
Единый хаб для множества сервисов. Таких как блог, личная страничка и тд. Есть API и документация.

## Roadmap

- [x] MVP:
    - [x] отображение постов и тегов
    - [x] админка
    - [x] тесты
    - [x] шаблон bootstrap
    - [x] Markdown
    - [x] все упаковано в docker
- [ ] Полноценная функциональность блога:
    - [ ] публикация постов не из админки
    - [ ] docs
    - [ ] about
- [ ] API
- [ ] Frontend

## Инструкция по сборке и запуску

Для сборки и запуска проекта выполните следующие шаги:

1. Клонируйте репозиторий с помощью команды:

```bash
git clone git@github.com:kvadimas/portal.git
```

2. Перейдите в директорию проекта.

3. Запустите проект с использованием Docker, выполнив команду:
```bash
docker-compose up -d
```

4. Зайдите в кондейнер backend:

```bash
docker compose exec backend sh
```

5. Выполните миграции и выгрузите статику:

```bash
python3 manage.py migrate
python3 manage.py collectstatic --noinput
```

6. Для выхода из кондейнера:

```bash
exit
```

7. После успешной сборки и запуска проекта, откройте веб-браузер и перейдите по следующему адресу:
```bash
http://localhost:80
```

## Стек технологий

Проект разработан с использованием следующего стека технологий:

1. Django
2. Django DRF
3. Docker

## Использовались библиотеки


[python-dotenv](https://pypi.org/project/python-dotenv/)

[remark42](https://github.com/umputun/remark42)

