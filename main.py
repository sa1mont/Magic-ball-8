import random
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно", 
           "Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать", "Перспективы не очень хорошие"]
print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Как Вас зовут?")
print(f"Привет {name}")

flag = True

while flag == True:
    question = input("Какой у Вас вопрос?")
    answer = random.choice(answers)
    print(answer)
    a = input("Есть ли у Вас какие-либо ещё вопросы? Если есть, то напишите 'да', если нет вопросов, то напишите что угодно")
    if a.lower() == "да":
        continue
    else:
        print("Возвращайтесь если возникнут вопросы!")
        break