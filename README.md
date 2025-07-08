# Описание
Исполненое тестовое задание по [данной технической задаче](https://docs.google.com/document/d/1W6u7UdD3adnMs-TSDbr6_s52GEMFloeKDtmcJSi6GRs/).

# Установка и тестирование
Скопировать репозиторий:
```bash
git clone --depth 1 https://github.com/aketawi/test-task-py-api
```

Подписаться на API и скопировать токены в файл `.env`:
```env
# https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
export HF_TOKEN=""

# https://apilayer.com/marketplace/spamchecker-api
# https://apilayer.com/marketplace/sentiment-api
export APILAYER_TOKEN=""
```

Запустить проект:
```
./run.sh
```
