from prettytable import PrettyTable

# 객체 생성
table = PrettyTable()

table.field_names = ["pokemon name" , "type"]
# add_rows 라는 메소드 사용
table.add_rows(
    [
    ['pikachu', 'electric'],
    ['squirtle', 'water'],
    ['charmander', 'fire']
    ]
)
print(table)

# 객체 속성 변경 -> 객체에 접근 후 속성 이용
table.padding_width = 20
print(table)


