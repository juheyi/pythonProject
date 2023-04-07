def divider(a, b):
   try:
       return a / b
   except ZeroDivisionError:
       print("Вы не можете делить на число ноль!")
       return 0
   except TypeError:
       print("Вы не можете делить нечисловые значения!")
       return 0
   except ValueError:
       print("Вы не можете делить нечисловые значения!")
       return 0

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

result = []

for key in data:

   res = divider(key, data[key])

   result.append(res)

print(result)