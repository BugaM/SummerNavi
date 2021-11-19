# Q1 Teste de Python

count = 0
for i in range(1,5000001):
    if i % 2 == 0 and i % 49 == 0 and i % 37 == 0:
        count += 1
print(count)

