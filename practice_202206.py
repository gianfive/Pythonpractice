# 작심삼일 일일코딩 2022.6.1 (수) 시작

# 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age = 20)
profile(main_lang="자바", age = 25, name = "김태호")


# 작심삼일 일일코딩 2022.6.1 (수) 끝.

# 작심삼일 일일코딩 2022.6.2 (목) 시작

# 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
profile("김태호", 25, "Kotlin", "Swift")

# 작심삼일 일일코딩 2022.6.2 (목) 끝.

# 작심삼일 일일코딩 2022.6.3 (금) 시작.
# 지역변수와 전역변수

gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_ret(gun, 2)

print("남은 총 : {0}".format(gun))

# 전역변수를 많이 쓰면 코드 관리가 어려워 져서 권장되지는 않음
# 반환(return)을 통한 전달값 형태의 코드를 많이 씀

# 작심삼일 일일코딩 2022.6.3 (금) 끝.

# 작심삼일 일일코딩 2022.6.4 (토) 시작

# Quiz) 표준 체중을 구하는 프로그램

# * 표준체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키 (m) x 키(m) x 22
# 여자 : 키 (m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         *함수명 : std_weight
#         *전달값 : 키(height), 성별(gender)

# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력예제)
# 키 175 cm 남자의 표준 체중은 67.38kg 입니다.


def std_weight(height, gender): # 키는 m 단위 (실수), gender ="남자"/"여자"

    if gender =="남자": 
        return height * height * 22
    else:
        return height * height * 21
        
height = 175 # cm
gender = "남자"

weight = round(std_weight(height / 100, gender), 2)

print("키 {0} cm {1} 표준 체중은 {2} kg 입니다.".format(height,gender, weight))

# 작심삼일 일일코딩 2022.6.4 (토) 끝.
