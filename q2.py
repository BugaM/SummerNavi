# Q2 Teste Python
from math import factorial, log

vector = []

# building the vector
for i in range(10):
    if i % 2 == 0:
        vector.append(3**i + 7*factorial(i))
    else:
        vector.append(2**i + 4*log(i))

# getting vector's max value and it's index
max_value = max(vector)
index = vector.index(max_value)
print(index)

mean = sum(vector)/len(vector)
print("{:.2f}".format(mean))
