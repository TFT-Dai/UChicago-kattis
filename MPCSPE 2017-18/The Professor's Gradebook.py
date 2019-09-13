#https://uchicago.kattis.com/problems/uchicagoplacement.gradebook

import math
def letter_grade(score):
    if 100 >= score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

class StudentGrade:
    def __init__(self, name, score):
        self.name = name
        self.score = score

N, M = map(int, input().split(' '))
max_score = 0
student = []
for i in range(N):
    ch, *scores = input().split(' ')
    scores = list(map(int, scores))
    score = sum(scores) - min(scores[:-1])
    max_score = max(max_score, score)
    student.append(StudentGrade(ch, score))

for i in range(N):
    grade = math.ceil(student[i].score / max_score * 100)
    letter = letter_grade(grade)
    s = f"{student[i].name} {student[i].score} {grade} {letter}"
    print(s)
