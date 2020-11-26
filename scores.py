"""Оценки
Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу."""



students_scores= [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
                  {'school_class':'5b', 'scores':[3,3,2,4,4]},
                  {'school_class':'6v', 'scores':[2,5,5,3,4]},
                  {'school_class':'7a', 'scores':[4,4,3,3,5]}
]
#средний балл по каждому классу

for score in students_scores:
    print(f"Средний балл: {sum(score['scores'])/len(score['scores'])}")


#средний балл по школе
scores_sum = 0
for score in students_scores:
  scores_sum += (sum(score['scores']))/(len(score['scores']))

print (f"Средний балл по школе:{scores_sum/4}")
