
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