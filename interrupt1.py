"""Задание 1"""

def hello_user():
    try:
      while True: 
        user_say=input('Как дела:?')
        break
      
    except KeyboardInterrupt:
      print("\nПока")
      
hello_user()
