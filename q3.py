# Q3 Teste Python

dictionary = {}

# building the dictionary
for i in range(3):
    print('Aluno ' + '{}'.format(i + 1) + ':')
    name = input('Digite o nome do aluno: ')
    grade = int(input('Digite a nota do aluno: '))
    dictionary[name] = grade

# getting max value and its associated key
max_grade = max(dictionary.values())
for key in dictionary.keys():
    if dictionary[key] == max_grade:
        best_student = key
        break

print('Aluno com maior nota: ' + best_student)
print('Nota: {}'.format(max_grade))
