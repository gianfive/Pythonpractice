
#작심삼십일 일일코딩 2022.5.1 시작
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*8)
#참 / 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))
# 애완동물을 소개해 주세요~
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >=3

'''ㅇㅣ렇게 하면 여
여러 문장이
주석처리 됩니다.
'''
print("우리집 " + animal + "의 이름은" + name + "에요")
hobby = "공놀이"
#print(name + "는 " +str(age) + "살이며, " + hobby + "을 아주 좋아해여")
print("우리집", animal, "의 이름은", name, "에요", name, "는", age, "살이고, 취미는", hobby, "이에요")
print(name + "는 어른일까요? " + str(is_adult))
#작심삼십일 일일코딩 2022.5.1 끝

#작심삼십일 일일코딩 2022.5.2 (월) 시작
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

print(1+1) #2
print(3-1) #1
print(5*2) #10
print(6/2) #2

print(2**3) #2^3 = 8
print(5%3) #나머지 2
print(10%3) #1
print(5//3) #몫1
print (10//3) #3

print(10>3) # True
print(4 >= 7) #False
print(10 <3) #False
print(5<=5) #True

print(3 == 3) #True
print(4 == 2) #False
print(3+4==7) #True
print(1 !=3) # 은 앞뒤가 같지 않다. True
print(not(1 !=3)) # False

print((3>0) and (3<5)) # True
print((3>0) & (3<5)) # True

print((3>0) or (3>5)) # True


print(5>4>3) # True
print(5>4>7) # false

print(2+3*4) #14
print((2+3)*4) #20
number = 2+3*4 #14
print(number)
number = number + 2 #16
print(number)
number += 2 #18 +=는 number +2 와 같은 의미임
print(number)

number *=2 #36
print(number)
number /=2 #18
print(number)
number -= 2 #16
print(number)

number %=5 #0 (나머지)
print(number)

#작심삼십일 일일코딩 2022.5.2 (월) 끝

#작심삼십일 일일코딩 2022.5.3 (화) 시작

print(abs(-5)) #5
print(pow(4,2)) #4^2 = 4*4=16
print(max(5,12)) #12
print(min(5,12)) #5
print(round(3.14)) #3
print(round(4.99)) #5

from ipaddress import NetmaskValueError
from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) # dhffla. 4
print(sqrt(16)) # 제곱근. 4

from random import *

print(random())  #0.0 ~ 1.1 미만의 임의의 값 생성
print(random()*10) #0.0 ~10.0 미만의 임의의 값 생성
print(int(random()*10)) #0~10 미만의 임의의 값 생성
print(int(random()*10)) #0~10 미만의 임의의 값 생성
print(int(random()*10)) #0~10 미만의 임의의 값 생성
print(int(random()*10)+1) #1~10이하의 임의의 값 생성
print(int(random()*10)+1) #1~10이하의 임의의 값 생성
print(int(random()*10)+1) #1~10이하의 임의의 값 생성
print(int(random()*10)+1) #1~10이하의 임의의 값 생성
print(int(random()*10)+1) #1~10이하의 임의의 값 생성
print(int(random()*45+1)) #1~45 이하의 임의의 값 생성
print(int(random()*45+1)) #1~45 이하의 임의의 값 생성
print(int(random()*45+1)) #1~45 이하의 임의의 값 생성
print(int(random()*45+1)) #1~45 이하의 임의의 값 생성
print(int(random()*45+1)) #1~45 이하의 임의의 값 생성
print(int(random()*45+1)) #1~45 이하의 임의의 값 생성

print(randrange(1,46)) #  1~ 46 이하의 임의의 값 생성
print(randrange(1,46)) #  1~ 46 이하의 임의의 값 생성
print(randrange(1,46)) #  1~ 46 이하의 임의의 값 생성
print(randrange(1,46)) #  1~ 46 이하의 임의의 값 생성
print(randrange(1,46)) #  1~ 46 이하의 임의의 값 생성
print(randrange(1,46)) #  1~ 46 이하의 임의의 값 생성
print(randrange(1,46)) #  1~ 46 이하의 임의의 값 생성

print(randint(1,45)) #1~45 이하의 임의으 값 생성
print(randint(1,45)) #1~45 이하의 임의으 값 생성
print(randint(1,45)) #1~45 이하의 임의으 값 생성
print(randint(1,45)) #1~45 이하의 임의으 값 생성
print(randint(1,45)) #1~45 이하의 임의으 값 생성
print(randint(1,45)) #1~45 이하의 임의으 값 생성

#작심삼십일 일일코딩 2022.5.3 (화) 끝

#작심삼십일 일일코딩 2022.5.4 (수) 시작
# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시고

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

print("오프라인 스터디 모임 날짜는 매월 ", randint(4,28), "일로 선정되었습니다.")

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 ", date, "일로 선정되었습니다.")

#작심삼십일 일일코딩 2022.5.4 (수) 끝.

#작심삼십일 일일코딩 2022.5.5 (목) 시작'
#문자열

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"

print("성별 :" + jumin[7]) #컴퓨터는 index 인식을 첫자리를 0부터 시작함
print("연 :" + jumin[0:2]) #0번째부터 2번째 직전까지(즉, 0, 1번째 값만 가져옴)
print("월 :" + jumin[2:4]) 
print("일 :" + jumin[4:6])

print("생년월일 :" + jumin[:6]) # 처음부터 6 직전까지 (0을 생략학 바로 콜론:을 찍어도 됨)

print("뒤 7자리 :" + jumin[7:]) # 7번쨰부터 끝까지
print("뒤 7자리 :" + jumin[-7:]) # 뒤부터 할 때는 마이너스 1 (-1) 부터 시작

#작심삼십일 일일코딩 2022.5.5 (목) 끝.

#작심삼십일 일일코딩 2022.5.6 (금) 시작

#문자열

python = "Python is Amazing"
print(python.lower()) #소문자로 출력
print(python.upper()) #대문자로 출력
print(python[0].isupper()) #첫번째 글자가 대문자가 맞느냐? 맞으면 true
print(len(python)) #총 글자 길이가 17이 맞느냐? 공백포함 하여.
print(python.replace("Python","JAVA"))

index = python.index("n")
print(index) #n 글자가 몇번째에 위치하냐
index = python.index("n", index + 1) #두번째 n의 위치
print(index)

print(python.find("Java")) # find는 원하는 값이 포함되어 있지 않으면 "-1"이 출력됨
#print(python.index("Java")) # index는 원하는 값이 없으면 오류를 내면서 종료됨

print(python.count("n")) #n이라는 글자가 몇 번 나오나

# 문자열 포맷

print("a" + "b")
print("a", "b") #콤마는 띄어쓰기됨

#방법 1
print("나는 %d살입니다." % 20) # d는 정수값만 가능
print("나는 %s을 좋아해요." % "파이썬") #s는 문자열 스트링값을 넣겠다는 것
print("Apple 은 %c 로 시작해요." % "A") #C는 캐릭터라서 한 글자만 받겠다는 것임

# %s 로만 쓰면 각 출력을 잘 할 수 있다.

print("나는 %s살입니다." % 20) # d는 정수값만 가능
print("나는 %s색과 %s색을 좋아해여." % ("파란", "빨간"))

#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해여.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해여.".format("파란","빨간"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

#방법 4 (Python v 3.6 이상버전부터 사용 가능)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#작심삼십일 일일코딩 2022.5.6 (금) 끝.

#작심삼십일 일일코딩 2022.5.7 (토) 시작

#탈출문자

print("백문이 불여일견\n백견이 불여일타") #줄바꿈

#print("저는 "나도코딩" 입니다.") #오류

print('저는 "나도코딩" 입니다.')

print("저는 \"나도코딩\" 입니다.") #역슬러시는 문장내에서 그냥 출력해주는 역할


#\\ : 문장내에서 하나의 역슬러쉬로 간주

print("C:\\Users\\USER\\Desktop\\PythonWorkspace>")

#\r : 커서를 맨 앞으로 이동

print("Red Apple\rPine")

#\b : 백스페이스 (한글자 삭제)

print("Redd\bApple")

# \t : 탭 역할 (여덟칸)

print("Red\tApple")



#작심삼십일 일일코딩 2022.5.7 (토) 끝.


#작심삼십일 일일코딩 2022.5.8 (일) 시작

# Quiz 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com

# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                          (nav)      (5)          (1)       (!)
# 예) 생성된 비밀번호 nav51!

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
#print(my_str)
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0~5 직전까지 (0, 1, 2, 3, 4, 5)
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

#작심삼십일 일일코딩 2022.5.8 (일) 끝.

#작심삼십일 일일코딩 2022.5.9 (월) 시작

# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 원하는 값이 없을 시 -1로 반환
# 참고. print(python.index("Java")) # 원하는 값이 없을 시 오류가 남
print("hi")

print(python.count("n"))

#작심삼십일 일일코딩 2022.5.9 (월) 끝.

#작심삼십일 일일코딩 2022.5.10 (화) 시작

#문자열 포맷

# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살 입니다." %20) #d는 정수값만 가능

print("나는  %s을 좋아해요." % "파이썬") #%s는 문자열 을 넣겠다

print("Apple 은 %c로 시작해요" % "A") #% c는 한글자만

# %s
print("나는 %s살 입니다." %20) #d는 정수값만 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {} 색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1} 색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0} 색을 좋아해요.".format("파란", "빨간"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

#방법 4

age =20
color = "빨간"
print(f"나는 {age}살이며, {color} 색을 좋아해요.")

#리스트 []
#순서를 가지는 객체의 집합
#지하철 칸별로 10명, 20명, 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]

# 조세호 씨가 몇 번쨰 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))


#정렬

num_list=[5,2,4,3,1,]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
#print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)

#작심삼십일 일일코딩 2022.5.10 (화) 끝.


#작심삼십일 일일코딩 2022.5.11 (수) 시작

# 사전

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) 오류가 남
print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet) # true
print(5 in cabinet) # false
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님
print(cabinet)
cabinet["A-3"]="김종국"
cabinet["C-20"]="조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 춢력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

#작심삼십일 일일코딩 2022.5.11 (수) 끝.

#작심삼십일 일일코딩 2022.5.12 (목) 시작

#튜플

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")

print (name, age, hobby)

#작심삼십일 일일코딩 2022.5.12 (목) 끝.
