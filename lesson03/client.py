import socket
import json
from config import get_client_socket
from console_menu import print_menu, get_command

def send_data(s):
    data = {
        "text": input("Input text: "),
        "user": input("Input username: "),
        "age": int(input("Input age: "))
    }

    s.send(json.dumps(data).encode("utf-8"))

    print("Data sended")

def exit_program(s):
    s.send(json.dumps({"exit": ""}).encode("utf-8"))
    print("Exit")
    exit()

if __name__ == "__main__":
    s = get_client_socket()
    menu = ["Send data", "Exit"]

    actions = {"1":send_data, "2":exit_program}

    while True:
        print_menu(menu)
        command = get_command(menu)

        actions[command](s)