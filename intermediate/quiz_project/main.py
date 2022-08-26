from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# 객체 리스트 생성
question_bank = []
for i in question_data:
    q = Question(i['text'], i['answer'])
    question_bank.append(q)    

# 형태 = QuizBrain(객체 리스트)
quiz = QuizBrain(question_bank)

still_has = quiz.still_has_questions()
while still_has:  
    """True / 퀴즈가 있을 때까지 while문 실행"""          
    quiz.next_question()
    
print(f"You've completed the quiz\nYour final score was:{quiz.score}/{quiz.question_number}")
