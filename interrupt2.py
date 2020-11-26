"""Задание 2"""

def discounted(price, discount, max_discount=20):
    try:
       price = float(price)
       discount = float(discount)
       max_discount = int(max_discount)
       if max_discount > 99:
          raise ValueError('Слишком большая максимальная скидка')
       else:
         return price - (price * discount / 100)
    except (TypeError,ValueError):
      print("Приведение типов не сработало")
     
a=discounted('string',10,200)
print(a)