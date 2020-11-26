
"""Практика возраст"""

user=input('Введите свой возраст:')
user_age =int(user)
print(f"Ваш возраст: {user_age}")



def age_status():
  user=input('Введите возраст пользователя:')
  user_age=int(user)
  if user_age <= 6:
    print("Пользователь ходит в десткий сад")
  elif user_age >=7 and user_age <= 18:
    print("Пользователь ходит в школу")
  elif user_age >18 and user_age <=24:
    print("Пользователь студент")
  elif user_age <=25:
    print("Пользователь работает")

age_status()