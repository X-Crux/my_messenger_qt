
def cheking_text(text, author):
    input_text = text.lower()
    words_hello = ("привет", "hello", "здравствуйте", "добрый день")
    words_bot = ("чат", "бот", "робот")
    users_name = ("Дмитрий", "Олег")

    for i in words_hello:
        if i in input_text:
            print("Приветствую тебя, " + author + "! " + "Как твои дела?")

    for i in words_bot:
        if i in input_text:
            print("Я чат-бот. Нужна ли моя помощь?")

    for i in users_name:
        if i in author.capitalize():
            print("Ух ты! Привет, " + author + "! " + "Мне очень нравится это имя!")

    return 0
