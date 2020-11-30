"""Практика: Сравнение строк"""

def string_qualifier(a,b):

  if type(a)==str and type(b)==str:
     if a==b:
        print(1)
     elif (a != b and (b=='learn')):
        print(3)
     elif (a != b and len(a) > len(b)):
        print(2)
     
  else:
    print(0)
  
        
a='helloooooooooooooooo'
b=0

string_qualifier(1, '1')