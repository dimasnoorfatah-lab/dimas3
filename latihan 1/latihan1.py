
import random

print("Program menampilkan n bilangan acak yang lebih kecil dari 0.5")

n = int(input("Masukkan nilai N: "))

i = 0
while i < n:
    data = random.random()  
    if data < 0.5:         
        print(f"data ke: {i+1} => {data}")
        i += 1

print("Selesai")

