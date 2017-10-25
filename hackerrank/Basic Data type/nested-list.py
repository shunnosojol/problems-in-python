
# https://www.hackerrank.com/challenges/nested-list/problem

students = [[input(),float(input())] for _ in range(int(input()))] 
second_highest = sorted(list(set([mark for name,mark in students])))[1]
print("\n".join([name for name,mark in sorted(students) if mark==second_highest]))