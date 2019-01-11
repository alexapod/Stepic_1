"""
2.4 Строки и символы
GC-состав является важной характеристикой геномных последовательностей и определяется как процентное
соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.
Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
(программа не должна зависеть от регистра вводимых символов).
Например, в строке "acggtgttat" процентное содержание символов G и C равно 4/10⋅100=40.0,
где 4 -- это количество символов G и C,  а 10 -- это длина строки.

Sample Input:
acggtgttat
Sample Output:
40.0
"""
s = input().lower()
print((s.count('g') + s.count('c')) / len(s) * 100)
