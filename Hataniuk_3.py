size=int(input("Введите размер массива: "))
array=[]
for s in range(size):
    value=int(input("Введите значение массива:"))
    array.append(value)
print("Массив имеет вид:",array)
for i in range(size):
    if int(array[i])%3==0:
        print(array[i])
