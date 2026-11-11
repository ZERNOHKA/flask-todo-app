# Практическая работа № 2 — Flask в Docker

Проект основан на [aixiamomo/flask-todo-app](https://github.com/aixiamomo/flask-todo-app).
Исходные страницы и база todo.sqlite сохранены, код запуска адаптирован под Python 3.

Открой терминал в этой папке и выполни:

    docker build -t flask-todo-app:v1 .
    docker images
    docker run -d -p 7345:7345 --name my-todo-container flask-todo-app:v1
    docker ps --filter name=my-todo-container

Открой http://localhost:7345. Добавь задачу, обнови страницу и проверь, что она осталась.
Журнал запуска: docker logs my-todo-container.
Остановка: docker stop my-todo-container.

Клонирование репозитория:

    git clone https://github.com/ZERNOHKA/flask-todo-app.git
    cd flask-todo-app
