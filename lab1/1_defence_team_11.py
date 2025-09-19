from functools import reduce

# Приклад 1
numbers = [7, 2, 9, 4, 6]

result = reduce(lambda x, y: x if x > y else y, numbers)

print(result)  # 9

# Приклад 2
words = ["I", "like", "data", "mining!"]
sentence = reduce(lambda x, y: x + " " + y, words)

print(sentence)  # I like data mining!

# Приклад 3
cart = [
    {"name": "яблука", "price": 15, "qty": 2},   # 15 * 2 = 30
    {"name": "хліб", "price": 25, "qty": 1},    # 25 * 1 = 25
    {"name": "молоко", "price": 30, "qty": 3}   # 30 * 3 = 90
]

total = reduce(lambda acc, item: acc + item["price"] * item["qty"], cart, 0)

print("Total cost:", total)  # 145

# Приклад 4
people = [
    {"name": "Oleh", "age": 15},
    {"name": "Maria", "age": 22},
    {"name": "Ivan", "age": 67},
    {"name": "Anna", "age": 34},
    {"name": "Natalia", "age": 70},
]

def group_people(acc, person):
    age = person["age"]
    if age < 18:
        acc["child"].append(person["name"])
    elif age < 65:
        acc["adult"].append(person["name"])
    else:
        acc["senior"].append(person["name"])
    return acc

groups = reduce(group_people, people, {"child": [], "adult": [], "senior": []})

print(groups) 
'''Результат: {
  'child': ['Oleh'],
  'adult': ['Maria', 'Anna'],
  'senior': ['Ivan', 'Natalia']
}'''
