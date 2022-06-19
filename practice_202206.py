# # 작심삼일 일일코딩 2022.6.1 (수) 시작

# # 키워드값

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age = 20)
# profile(main_lang="자바", age = 25, name = "김태호")


# # 작심삼일 일일코딩 2022.6.1 (수) 끝.

# # 작심삼일 일일코딩 2022.6.2 (목) 시작

# # 가변인자

# # def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# #     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
# #     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
# profile("김태호", 25, "Kotlin", "Swift")

# # 작심삼일 일일코딩 2022.6.2 (목) 끝.

# # 작심삼일 일일코딩 2022.6.3 (금) 시작.
# # 지역변수와 전역변수

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# print("전체 총 : {0}".format(gun))
# #checkpoint(2) # 2명이 경계근무 나감
# gun = checkpoint_ret(gun, 2)

# print("남은 총 : {0}".format(gun))

# # 전역변수를 많이 쓰면 코드 관리가 어려워 져서 권장되지는 않음
# # 반환(return)을 통한 전달값 형태의 코드를 많이 씀

# # 작심삼일 일일코딩 2022.6.3 (금) 끝.

# # 작심삼일 일일코딩 2022.6.4 (토) 시작

# # Quiz) 표준 체중을 구하는 프로그램

# # * 표준체중 : 각 개인의 키에 적당한 체중

# # (성별에 따른 공식)
# # 남자 : 키 (m) x 키(m) x 22
# # 여자 : 키 (m) x 키(m) x 21

# # 조건 1 : 표준 체중은 별도의 함수 내에서 계산
# #         *함수명 : std_weight
# #         *전달값 : 키(height), 성별(gender)

# # 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# # (출력예제)
# # 키 175 cm 남자의 표준 체중은 67.38kg 입니다.


# def std_weight(height, gender): # 키는 m 단위 (실수), gender ="남자"/"여자"

#     if gender =="남자": 
#         return height * height * 22
#     else:
#         return height * height * 21
        
# height = 175 # cm
# gender = "남자"

# weight = round(std_weight(height / 100, gender), 2)

# print("키 {0} cm {1} 표준 체중은 {2} kg 입니다.".format(height,gender, weight))

# # 작심삼일 일일코딩 2022.6.4 (토) 끝.

# # 작심삼일 일일코딩 2022.6.5 (일) 시작.
# # 표준입출력

# print("python", "Java", "Java script", sep=" vs ")

# print("python", "Java", sep=",", end="?") # end : 줄바꿈이 아닌 뒷 문장이 한줄에 출력
# print("무엇이 더 재미있을까요?")

# # import sys
# # print("Python", "Java", file=sys.stdout) # 표준출력
# # print("Python", "Java", file=sys.stderr) # 표준에러

# #시험성적
# # scores = {"수학":0, "영어":50, "코딩":100}
# # # print(scores.items())
# # for subject, score in scores.items():
# # #     print(subject, score)
# #      print(subject.ljust(8), str(score).rjust(4), sep=":")

# #은행대기순번표
# # 001, 002, 003,...
# # for num in range(1,21):
# #     print("대기번호 : " + str (num).zfill(3))

# # answer = input("아무 값이나 입력하세요: ") #입력된 값이 answer 에 들어감
# # print("입력하신 값은 " + answer + "입니다.")
# # 주의 : 사용자 입력 형태는 항상 문자열 (str) 로 저장이 됨

# # 작심삼일 일일코딩 2022.6.5 (일) 끝.

# # 작심삼일 일일코딩 2022.6.6 (월) 시작
# # 다양한 출력 포멧

# # 빈자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공감을 확보
# print("{0: >10}".format(500))

# # 양수일 땐 +로 표시, 은수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬 하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(-500))

# # 3자리마다 콤마를 찍어주기
# print("{0:,}".format(100000000000000))


# # 3자리마다 콤마를 찍어주기, +_- 부호도 붙이기
# print("{0:+,}".format(100000000000000))
# print("{0:+,}".format(-100000000000000))

# # 3자리마다 콤마를 찍어주기, +_- 부호도 붙이기, 자릿수 확보하기
# # 돈이 많으면 빈 자리는 ^ 채워주기

# print("{0:^<+30,}".format(10000000000000))

# #소수점 출력
# print("{0:f}".format(5/3))

# #소수점 특정자리수 (소수점 3쨰에서 반올림)
# print("{0:.2f}".format(5/3))

# # 작심삼일 일일코딩 2022.6.6 (월) 끝.

# # 작심삼일 일일코딩 2022.6.7 (화) 시작
# # 파일 입출력

# # score_file = open("score.txt", "w", encoding="utf8")
# # print("수학 : 0", file=score_file)
# # print("영어 : 50", file=score_file)
# # score_file.close()

# # 작심삼일 일일코딩 2022.6.7 (화) 끝.

# # 작심삼일 일일코딩 2022.6.8 (수) 시작
# # 파일 입출력 (계속)

# # score_file = open("score.txt", "a", encoding="utf8")
# # score_file.write("과학 : 80")
# # score_file.write("\n코딩 : 100")
# # score_file.close()

# # score_file = open("score.txt", "r", encoding="utf8")
# # print(score_file.read())
# # score_file.close()

# # score_file = open("score.txt", "r", encoding="utf8")
# # print(score_file.readline(), end="") # 줄별로 읽기 동작을 수행하고 한 줄 읽고 커서는 다음 줄로 이동
# # print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# # score_file.close()

# #몇 줄인지 모를 때

# # score_file = open("score.txt", "r", encoding="utf8")
# # while True:
# #     line = score_file.readline()
# #     if not line:
# #         break
# #     print(line, end="")
# # score_file.close()

# # score_file = open("score.txt", "r", encoding="utf8")
# # lines = score_file.readlines() # 모든 라인을 리스트형태로 저장
# # for line in lines:
# #     print(line, end="")

# # score_file.close()

# # 작심삼일 일일코딩 2022.6.8 (수) 끝.

# # 작심삼일 일일코딩 2022.6.9 (목) 시작
# # pickle 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장을 해 주는 것

# # import pickle
# # profile_file = open("profile.pickle", "wb")
# # profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
# # profile_file.close()

# # profile_file = open("profile.pickle","rb")
# # profile = pickle.load(profile_file) # file 에 있는 정보를 profile에 불러오기

# # print(profile)
# # profile_file.close()

# # 작심삼일 일일코딩 2022.6.9 (목) 끝.

# # 작심삼일 일일코딩 2022.6.10 (금) 시작
# # with

# # import pickle

# # with open("profile.pickle", "rb") as profile_file:
# #     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")
    
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# # 작심삼일 일일코딩 2022.6.10 (금) 끝.

# # 작심삼일 일일코딩 2022.6.11 (토) 시작 
# # 퀴즈

# # for i in range (1, 51):
# #     with open(str(i) + "주차.txt" , "w", encoding="wtf8") as report_file:
# #               report_file.write(" - {0} 주차 주간보고 -".format(i))
# #               report_file.write("\n부서 : ")
# #               report_file.write("\n이름 : ")
# #               report_file.write("\n업무 요약 : ")

# 작심삼일 일일코딩 2022.6.11 (토) 끝. 

# 작심삼일 일일코딩 2022.6.12 (일) 시작
# 클래스

# 마린 : 공격 유닛, 군인 총을 쏠 수 있음
# name = "마린"
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # # 탱크 : 공격유닛, 탱크, 포를 쏠 수 있고 일반 시즈모드 있음

# # tank_name = "탱크"
# # tank_hp = 150
# # tank_damage = 35

# # print("{} 유닛이 생성되었습니다.".format(tank_name))
# # print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# # def attack(name, location, damage):
# #     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location,damage))

# # attack(name, "1시", damage)
# # attack(tank_name, "1시", tank_damage)

# # class Unit:
# #     def __init__(self, name, hp, damage):
# #         self.name = name
# #         self.hp = hp
# #         self.damage = damage
# #         print("{0} 유닛이 생성되었습니다.".format(self.name))
# #         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# # 작심삼일 일일코딩 2022.6.12 (일) 끝.

# # 작심삼일 일일코딩 2022.6.13 (월) 시작
# # __init

# class Unit: #객체생성, 인스턴스
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# # marine3 = Unit("마린", 40) # 오류 멧시지가 뜸. 항상 똑같이 해주어야 함


# # 작심삼일 일일코딩 2022.6.13 (월) 끝.

# # 작심삼일 일일코딩 2022.6.14 (화) 시작
# # 멤버변수

# # 레이스 : 공중유닛

# wraith1 = Unit("레이스", 80,5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# #프로토스
# # 다크아칸 마인드컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True
# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# # 유닛의 기본 정보는 이름(name), 체력(hp), 데미지(damage) 세 가지로만 정의되어 있기 때문에 클로킹을 쓰려면 아래에서 다시 정의해 주여야 한다.


# # 작심삼일 일일코딩 2022.6.14 (화) 끝.


# # 작심삼일 일일코딩 2022.6.16 (목) 시작
# # 메소드

# # 일반유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력] {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -=damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# # 작심삼일 일일코딩 2022.6.16 (목) 끝.

# 작심삼일 일일코딩 2022.6.17 (금) 시작
# 상속

# 메딕 : 의무병

# 일반유닛

# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# # 공격유닛

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         # self.name = name
#         # self.hp = hp
#         Unit.__init__(self, name, hp)
#         self.damage = damage


#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력] {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -=damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# # #파이어뱃 : 공격 유닛, 화염방사기
# # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")

# # #공격 2번 받는다고 가정
# # firebat1.damaged(25)
# # firebat1.damaged(25)

# # 작심삼일 일일코딩 2022.6.17 (금) 끝.

# # 작심삼일 일일코딩 2022.6.17 (토) 시작
# # 다중상속

# # 드랍쉽 : 공중 유닛, 수송기 마린/ 파이어팻 / 탱크 등을 수송. 공격기등 불가

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} :{1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
            
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# # 발키리 : 공중공격유닛, 한 번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 작심삼일 일일코딩 2022.6.17 (토) 끝.

# 작심삼일 일일코딩 2022.6.17 (일) 시작
# 연산자 오버로딩 : 자식 클래스에서 정의한 매소드를 쓰고 싶을 때


# from dataclasses import asdict
# from fcntl import DN_DELETE
# from stat import SF_APPEND


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, ldocation):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, ldocation, self.speed))
        Unit: Unit
        

# 공격유닛

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} :{1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
            
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0으로 처리
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name, location)


# 벌쳐 : 지상 유닛, 기동성이 좋음

vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛, 체력도 굉장히 좋음, 공격력도 좋음

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

# 작심삼일 일일코딩 2022.6.17 (일) 끝.