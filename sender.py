import requests

while True:
    text = input("Сообщение: ", )
    author = input("Имя автора: ", )

    response = requests.post(
        'http://127.0.0.1:5000/send_message',
        json={'text': text, 'author': author}
    )
    print(response.status_code)
    print(response.text)
