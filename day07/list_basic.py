

# 우리반 학생 10명의 수학점수를 저장

math_points = [78, 95, 70, 100, 90, 50, 15, ]

total = 0
for p in math_points:
    total += p

evg = total / len(math_points)

print(f' 총점: {total}점, 평균: {evg}점')