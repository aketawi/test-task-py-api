# Описание
Исполненое тестовое задание по [данной технической задаче](https://docs.google.com/document/d/1W6u7UdD3adnMs-TSDbr6_s52GEMFloeKDtmcJSi6GRs/).

# Установка
Скопировать репозиторий:
```bash
git clone --depth 1 https://github.com/aketawi/test-task-py-api
```

Подписаться на API и скопировать токены в файл `.env`:
```env
# https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
export HF_TOKEN="..."

# https://apilayer.com/marketplace/sentiment-api
# https://apilayer.com/marketplace/spamchecker-api
export APILAYER_TOKEN="..."
```

Запустить проект:
```
chmod +x ./run.sh
./run.sh
```

Скрипт установит зависимости в рабочую директорию. Проект использует пакет-менеджер UV, но может быть использован и без него.

# Использование
```bash
# Получить все запросы
curl localhost:8000/api/v1/requests/

# Получить один запрос по его ID
curl localhost:8000/api/v1/requests/<id>
curl localhost:8000/api/v1/requests/42

# Отправить новый запрос
curl localhost:8000/api/v1/requests/new -d <data> -H "Content-Type: application/json"
curl localhost:8000/api/v1/requests/new -d '{"text": "Не приходит СМС"}' -H "Content-Type: application/json"
```

Анализ тональности и категории через API предоставленый в задании не всегда срабатывает на русском, примеры на английском:
```bash
curl localhost:8000/api/v1/requests/new -d '{"text": "This is the worst ever, I cant get my payment from you"}' -H "Content-Type: application/json"
# Ожидаемый ответ:
# {
#   "id": 88,
#   "status": "open",
#   "sentiment": "negative",
#   "category": "оплата"
# }

curl localhost:8000/api/v1/requests/new -d '{"text": "yay wahoo thanks everything is so good actually :D"}' -H "Content-Type: application/json"
# Ожидаемый ответ:
# {
#   "id": 89,
#   "status": "open",
#   "sentiment": "positvie",
#   "category": "другое"
# }
```
