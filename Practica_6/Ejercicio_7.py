nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = []
def media(lista):
    try:
        AVG = sum(lista) / len(lista)
        print(AVG)
    except ZeroDivisionError:
        print("No")
media(nums)
media(lista)