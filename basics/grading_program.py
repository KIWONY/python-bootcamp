student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for i in student_scores:
    score = student_scores[i]       # 키 값
    if score > 90: 
        # 딕셔너리에 데이터 추가 /  i는 student_scores의 키 값
        student_grades[i] = "Outstanding"
    elif score > 80:
        student_grades[i] = "Exceeds Expectations"
    elif score > 70:
        student_grades[i] = "Acceptable"
    else: 
        student_grades[i] = "Fail"

print(student_grades)

# {'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}




