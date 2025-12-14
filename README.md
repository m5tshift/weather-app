# Weather App

Простое веб-приложение для отображения текущей температуры (погода) с настроенным мониторингом.

## Ключевые задачи

- Создать веб-приложение, отображающее текущую температуру
- Упаковать приложение в Docker-контейнер
- Настроить мониторинг доступности приложения по HTTP
- Настроить дополнительный мониторинг параметров приложения (опционально)

## Реализация

| Задача | Реализация |
|--------|------------|
| Отображение текущей погоды | Приложение на Python с использованием FastAPI (файл: app/main.py), получает данные через OpenWeatherMap API |
| Контейнеризация | Dockerfile в директории app/, образ собирается с необходимыми зависимостями |
| Мониторинг доступности | HTTP-check через curl в docker-compose.yml, проверка состояния эндпоинта /health |
| Дополнительный мониторинг | Использование Prometheus для сбора метрик и Grafana для визуализации |

## Технологии

- Python 3.12
- FastAPI
- httpx
- Docker, Docker Compose
- WeatherAPI
- Prometheus
- Grafana

## Запуск локально

1. Установите Docker и Docker Compose (если он не установлен вместе с Docker Desktop как Compose v2)
2. Склонируйте репозиторий
    ```bash
    git clone https://github.com/m5tshift/weather-app.git
    cd weather-app
    ```
3. Создайте файл .env скопировав из .env.example в директории app/
    ```bash
    cd app
    cp .env.example .env
    ```
3. Задайте переменную окружения - API ключ [WeatherAPI](https://www.weatherapi.com) в файле `.env`:
    ```
    WEATHER_API_KEY="ваш_api_ключ"
    ```
    P.S. В данный момент в файле .env.example уже указан ключ, действительный до 23.12.2025
4. Соберите проект с помощью docker compose:

    ```bash
    docker compose up --build
    ```
- Приложение будет доступно по адресу http://localhost:8080
- Prometheus по http://localhost:9090
- Grafana по http://localhost:3000 (username: admin, password: admin)

## Мониторинг

Мониторинг сконфигурирован через yaml файлы, в качестве дашборда используется [FastAPI Observability](https://grafana.com/grafana/dashboards/18739-fastapi-observability/). Устанавливается через provisioning.