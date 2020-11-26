"""Задание 2"""


dialogs=   {'Как дела?': 'хорошо',
           'Что делаешь?': 'программирую',
           'Где учишься?': 'в институте',
           }

def ask_user():
   letter=input("Введите Ваш вопрос:")  
   if letter in dialogs.keys():
     print(dialogs.get(letter))
            


ask_user()