class QuizBrain:
    def __init__(self, list):
        self.question_number = 0 
        self.question_list = list
        self.score = 0
        
    def still_has_questions(self):
        """이거 생각못했음"""
        ## self.question_list의 길이와 question_number를 비교하여 리턴한 boolean을 while문에서 사용
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        # = 
        return self.question_number < len(self.question_list)           #
    
    def next_question(self):
        """현재 퀴즈를 보여주고, 입력한 뒤 답을 체크합니다"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}:{current_question.text}. (True/False):')
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            self.score +=1
            print("right")
        else: 
            print("wrong")
        print(f'Your current score is :{self.score}/{self.question_number}')
