# 작심삼일 일일코딩 2022.9.1 (목)
# 퀴즈 #4

# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

### print(int(random() *10)+1) # 1 ~ 10 이하의 임의의 값 생성

# from random import *
# list = int(random() *10)+1
# print(list)

# from random import *
# users = range(1,21) # 1부터 21 직전까지 숫자를 생성
# # print(type(list))
# users = list(users)
# # print(type(user))

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users,4)

# print("치킨 : {0}".format(winners[0]))
# print("커피 : {0}".format(winners[1:]))

# 작심삼일 일일코딩 2022.9.1 (목) 끝.

# 작심삼일 일일코딩 2022.9.2 (금) 시작
# if
# 날씨에 따라서 서로 다른 준비물을 챙기는 코드

# weather = "머시라고라고라"
# if weather == "비":
#     print("우산을 챙기세요") # 조건이 맞지 않으면 아무 문장이 출력되지 않음
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")
    
# 작심삼일 일일코딩 2022.9.2 (금) 끝.

# 작심삼일 일일코딩 2022.9.3 (토) 시작

# weather = input("오늘 날씨 어떄요?")
# if weather == "비" or "눈":
#     print("우산을 챙기세요") # 조건이 맞지 않으면 아무 문장이 출력되지 않음
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")

# 작심삼일 일일코딩 2022.9.3 (토) 끝.

# 작심삼일 일일코딩 2022.9.4 (일) 시작

# temp = int(input("기온은 어때요?"))
# if temp >= 30:
#     print("너무 더워요 나가지 마세요")
# elif 10 <= temp <= 30:
#     print("괜찮은 날씨에요")
# elif 0<= temp <= 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# 작심삼일 일일코딩 2022.9.4 (일) 끝.

# 작심삼일 일일코딩 2022.9.5 (월) 시작
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0,1,2,3,4,]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(5):
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]

# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# 유천냉면 = ["서수정", "김용호", "김영우"]

# for 감사팀 in 유천냉면:
#     print("냉면 나왔습니다.", "네 {0}입니다.".format(감사팀))

# 작심삼일 일일코딩 2022.9.5 (월) 끝.

# 작심삼일 일일코딩 2022.9.6 화 시작
# while 반복문
# 다섯번 손님 부르고 없으면 커피 버림

# customer = "토르"
# index = 5

# while index >=1:
#     print("{0}! 커피가 준비되었습니다. 불러주는거 {1} 번 남았습니다.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피 버립니다.")

# 작심삼일 일일코딩 2022.9.6 화 끝.

# 작심삼일 일일코딩 2022.9.7 수 시작
# customer ="토르"
# person = "unknown"

# while person != customer:
#     person = input("이름이 어떻게 되세요?")
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# 작심삼일 일일코딩 2022.9.7 수 끝.

# 작심삼일 일일코딩 2022.9.10 토 시작
# continue 와 break

# absent = [2, 5] #결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent: # 1. 결석한 학생의 번호를 만나게 되면
#         continue  # 2. 아래 있는 명령문을 실행하지 않고 다음 반복을 실행한다는 의미
#     elif student in no_book:
#         print("오늘 수업 여기까지, {0} 은 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐". format(student))
    
# 작심삼일 일일코딩 2022.9.10 토 끝.

# 작심삼일 일일코딩 2022.9.11 일 시작
# 한 줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 100, 101, 102, 103, 104

# students = [1,2,3,4,5]
# print(students)

# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변화
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# 작심삼일 일일코딩 2022.9.11 일 끝.

# 작심삼일 일일코딩 2022.9.12 월 시작
# 퀴즈
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승객 수를 구하는 프로그램을 작성하시오.
# 조건 1 : 승객별 운행 소요시간은 5-50분 사이 난수
# 조건 2 : 당신은 소요시간 5-15분 사이 승객만 매칭해야 함

# (출력문 예제)
# [0] 1번째 손님 (소요시간 :15분)
# [0] 2번째 손님 (소요시간 :50분)
# [0] 3번째 손님 (소요시간 :5분)
# ..
# [0] 50번째 손님 (소요시간 :16분)

# 총 탑승 승객 2분

# 작심삼일 일일코딩 2022.9.12 월 끝.

# 작심삼일 일일코딩 2022.9.14 수 시작

# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1,51): #1~50 이라는 수(승객)
#     time = randrange(5, 51) # 5분에서 50분 소요시간 범위
#     if 5 <= time <=15: # 5분에서 15분 이내의 손님인 경우, 탑승 승객 수 증가 처리
#         print("[0] {0} 번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt  +=1 # 매칭 성공 하면 카운트가 올라감
#     else: # 매칭 실패한 경우 카운트는 증가 안함
#         print("[ ] {0} 번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승승객 : {0} 분".format(cnt))

# # # 작심삼일 일일코딩 2022.9.14 수 끝.

# # 작심삼일 일일코딩 2022.9.15 목 시작
# # 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# open_account()

# 작심삼일 일일코딩 2022.9.15 목 끝.

# 작심삼일 일일코딩 2022.9.16 금 시작

#입금
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
#     return balance + money

# #출금
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
#         return balance

# #출금 수수료
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance-money-commission

# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다.".format(commission, balance))

# 작심삼일 일일코딩 2022.9.16 금 끝.

# 작심삼일 일일코딩 2022.9.17 토 시작
# 기본값
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용언어: {2}" \
#         .format(name, age, main_lang))

# profile("유재석", 20, "Python")
# profile("김태호", 25, "JAVA")

# 같은학교 같은학년 같은반 같은 수업
    
# def profile(name, age=17, main_lang="python"):
#     print("이름: {0}\t나이: {1}\t주 사용언어: {2}" \
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 작심삼일 일일코딩 2022.9.17 토 끝.

# 작심삼일 일일코딩 2022.9.18 일 시작
 # 키워드값

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age = 25, name="김태호")

# 작심삼일 일일코딩 2022.9.18 일 끝.

# 작심삼일 일일코딩 2022.9.19 월 시작

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# 가변인자
def profile(name, age, *language):
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "c", "c++", "c#", "java script")
profile("김태호", 25, "kotlin", "swift")


# 작심삼일 일일코딩 2022.9.19 월 끝.

