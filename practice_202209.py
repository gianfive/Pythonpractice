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

# 작심삼일 일일코딩 2022.9.2 (토) 시작

# weather = input("오늘 날씨 어떄요?")
# if weather == "비" or "눈":
#     print("우산을 챙기세요") # 조건이 맞지 않으면 아무 문장이 출력되지 않음
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")

# 작심삼일 일일코딩 2022.9.2 (토) 끝.

# 작심삼일 일일코딩 2022.9.3 (일) 시작

temp = int(input("기온은 어때요?"))
if temp >= 30:
    print("너무 더워요 나가지 마세요")
elif 10 <= temp <= 30:
    print("괜찮은 날씨에요")
elif 0<= temp <= 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

# 작심삼일 일일코딩 2022.9.3 (일) 끝.

