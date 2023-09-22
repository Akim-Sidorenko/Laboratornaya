
def count_numbers():
    lst =[]
    int_count = 0
    float_count = 0
    n=int(input("Введите количество элементов в списке: "))
    for i in range (n):
     num = input(f"Введите элемент {i+1}: ")
     try:
      num=int(num)
      int_count +=1
     except ValueError:
      try:
        num=float(num)
        float_count +=1
      except ValueError:
        print (f"Элемент {i+1} не является числом")
        continue
      lst.append(num)
    return int_count, float_count,lst
int_count, float_count,lst = count_numbers()
print("Количество целых чисел:", int_count)
print("Количество чисел с плавающей запятой:", float_count)