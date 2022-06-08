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

# 작심삼일 일일코딩 2022.6.5 (일) 시작.
# 표준입출력

print("python", "Java", "Java script", sep=" vs ")

print("python", "Java", sep=",", end="?") # end : 줄바꿈이 아닌 뒷 문장이 한줄에 출력
print("무엇이 더 재미있을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준출력
# print("Python", "Java", file=sys.stderr) # 표준에러

#시험성적
# scores = {"수학":0, "영어":50, "코딩":100}
# # print(scores.items())
# for subject, score in scores.items():
# #     print(subject, score)
#      print(subject.ljust(8), str(score).rjust(4), sep=":")

#은행대기순번표
# 001, 002, 003,...
# for num in range(1,21):
#     print("대기번호 : " + str (num).zfill(3))

# answer = input("아무 값이나 입력하세요: ") #입력된 값이 answer 에 들어감
# print("입력하신 값은 " + answer + "입니다.")
# 주의 : 사용자 입력 형태는 항상 문자열 (str) 로 저장이 됨

# 작심삼일 일일코딩 2022.6.5 (일) 끝.

# 작심삼일 일일코딩 2022.6.6 (월) 시작
# 다양한 출력 포멧

# 빈자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공감을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 은수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬 하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(-500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000000))


# 3자리마다 콤마를 찍어주기, +_- 부호도 붙이기
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))

# 3자리마다 콤마를 찍어주기, +_- 부호도 붙이기, 자릿수 확보하기
# 돈이 많으면 빈 자리는 ^ 채워주기

print("{0:^<+30,}".format(10000000000000))

#소수점 출력
print("{0:f}".format(5/3))

#소수점 특정자리수 (소수점 3쨰에서 반올림)
print("{0:.2f}".format(5/3))

# 작심삼일 일일코딩 2022.6.6 (월) 끝.

# 작심삼일 일일코딩 2022.6.7 (화) 시작
# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# 작심삼일 일일코딩 2022.6.7 (화) 끝.

# 작심삼일 일일코딩 2022.6.8 (수) 시작
# 파일 입출력 (계속)

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기 동작을 수행하고 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

#몇 줄인지 모를 때

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 라인을 리스트형태로 저장
for line in lines:
    print(line, end="")

score_file.close()

# 작심삼일 일일코딩 2022.6.8 (수) 끝.
