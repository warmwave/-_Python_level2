import socket
import json
from config import get_server_socket
s = get_server_socket()
print("Server started")
client, addr = s.accept()
print("Client connected: ",client, addr)

while True:
    print("Waiting data")

    data = json.loads(client.recv(1024).decode("utf-8"))
    print("Data received")

    if "exit" not in data:
        print(data)
    else:
        client.close()
        s.close()
        print("Exit")
        break






# Присутствие
# Каждый пользователь при подключении к серверу отсылает сервисное сообщение о присутствии — presence с необязательным полем type:
# {
# 	"action": "presence",
# 	"time": <unix timestamp>,
# 	"type": "status",
# 	"user": {
# 			"account_name":  "C0deMaver1ck",
# 			"status":      "Yep, I am here!"
# 	}
# }
#

# Коды ответов сервера
# JIM-протокол использует коды ошибок HTTP. Перечислим поддерживаемые:
# 1xx — информационные сообщения:
# 100 — базовое уведомление;
# 101 — важное уведомление.
# 2xx — успешное завершение:
# 200 — OK;
# 201 (created) — объект создан;
# 202 (accepted) — подтверждение.
# 4xx — ошибка на стороне клиента:
# 400 — неправильный запрос/JSON-объект;
# 401 — не авторизован;
# 402 — неправильный логин/пароль;
# 403 (forbidden) — пользователь заблокирован;
# 404 (not found) — пользователь/чат отсутствует на сервере;
# 409 (conflict) — уже имеется подключение с указанным логином;
# 410 (gone) — адресат существует, но недоступен (offline).
# 5xx — ошибка на стороне сервера:
# 500 — ошибка сервера.
# Коды ошибок могут быть дополнены новыми.
#
# Сообщения-ответы имеют следующий формат (в зависимости от кода ответа):
# {
#     "response": 1xx / 2xx,
#     "time": <unix timestamp>,
#     "alert": "message (optional for 2xx codes)"
# }
#
# Или такой:
# {
#     "response": 4xx / 5xx,
#     "time": <unix timestamp>,
#     "error": "error message (optional)"
# }
