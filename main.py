print("Welcome the Multiplication Table")
number = int(input("For Which Number would you like to get multiplication table?\n"))
print("Here you Go: ")
def mult(numbers):
  num1 = 1 * number
  print(f"{number} * 1 = {num1}")
  num2 = 2 * numbers
  print(f"{number} * 2 = {num2}")
  num3 = 3 * number
  print(f"{number} * 3 = {num3}")
  num4 = 4 * number
  print(f"{number} * 4 = {num4}")
  num5 = 5 * number
  print(f"{number} * 5 = {num5}")
  num6 = 6 * number
  print(f"{number} * 6 = {num6}")
  num7 = 7 * number
  print(f"{number} * 7 = {num7}")
  num8 = 8 * number
  print(f"{number} * 8 = {num8}")
  num9 = 9 * number
  print(f"{number} * 9 = {num9}")
  num10 = 10 * number
  print(f"{number} * 10 = {num10}")
  
mult(number)
