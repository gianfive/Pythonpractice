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

# # 작심삼일 일일코딩 2022.6.18 (토) 시작
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

# 작심삼일 일일코딩 2022.6.18 (토) 끝.

# 작심삼일 일일코딩 2022.6.19 (일) 시작
# 연산자 오버로딩 : 자식 클래스에서 정의한 매소드를 쓰고 싶을 때


# from dataclasses import asdict
# from fcntl import DN_DELETE
# from stat import SF_APPEND

# 일반유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
        
#     def move(self, ldocation):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, ldocation, self.speed))
#         Unit: Unit
        

# # 공격유닛

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         # self.name = name
#         # self.hp = hp
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} :{1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
            
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0으로 처리
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중유닛이동]")
#         self.fly(self.name, location)


# 벌쳐 : 지상 유닛, 기동성이 좋음

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛, 체력도 굉장히 좋음, 공격력도 좋음

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# 작심삼일 일일코딩 2022.6.19 (일) 끝.

# 작심삼일 일일코딩 2022.6.20 (월) 시작
# pass

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# 서플라이 디폿 : 건물, 1개 건물 = 8유닛

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

# 작심삼일 일일코딩 2022.6.20 (월) 끝.

# 작심삼일 일일코딩 2022.6.21 (화) 시작
# super

# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         super.location = location


# from asyncio.tasks import _T1
# from calendar import c


# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         # super().__init__()
#         Unit.__init__(self)
#         Flyable.__init__(self)

# 드랍쉽
# dropship = FlyableUnit()

# 작심삼일 일일코딩 2022.6.21 (화) 끝.

# 작심삼일 일일코딩 2022.6.22 (수) 시작
# 스타크래프트 전반전

# from random import *

# # 일반유닛

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
        
#     def move(self, ldocation):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, ldocation, self.speed))
#         Unit: Unit
    
#     def damaged(self, demage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.". format(self.name))

        
# # 공격유닛

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# #탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜 더 높은 공격력, 이동불가
#     seize_developed = False # 시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
        
#         # 현재 시즈모드 일 때 -> 시즈모드 해제
#         else: 
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False
            
            
# # # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0으로 처리
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중유닛이동]")
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False # 클로킹 모드 (해제 상태)

#     def clocking(self):
#         if self.clocked == True: # 클로킹 모드이므로 해제
#             print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
#             self.clocked = False
#         else : # 클로킹 모드 해제이므로 모드설정
#             print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
#             self.clocked = True 

# # 작심삼일 일일코딩 2022.6.22 (수) 끝.

# # 작심삼일 일일코딩 2022.6.23 (목) 시작
# # 스타크래프트 후반전

# def game_start():
#     print("[알림] ㅅ ㅐ로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임을 퇴장하셨습니다.")

# # 실제 게임 시작

# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기
# w1 = Wraith()

# # 유닛 일괄 괄니 (생성된 모든 유닛 append)

# attak_units = []

# attak_units.append(m1)
# attak_units.append(m2)
# attak_units.append(m3)
# attak_units.append(t1)
# attak_units.append(t2)
# attak_units.append(w1)

# # 전군이동

# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# # 공격 모드 준비 
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5~20)

# # 게임종료
# game_over()

# 작심삼일 일일코딩 2022.6.23 (목) 끝.

# 작심삼일 일일코딩 2022.6.24 (금) 시작

# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.quit

# (출력예제)

# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
# class House:
#     #매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type=house_type
#         self.deal_type=deal_type
#         self.price=price
#         self.completion_year=completion_year

#     #매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type\
#             , self.price, self.completion_year)

# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0} 대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# 작심삼일 일일코딩 2022.6.24 (금) 끝.

# 작심삼일 일일코딩 2022.6.25 (토) 시작
# 예외처리

# try:
#     print("나누기 전용계산기")
#     nums = []
#     nums.append(int(input("첫번째수입력 : ")))
#     nums.append(int(input("두번째수입력 : ")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

# except ValueError:
#     print("에러! 잘못값입력")

# except ZeroDivisionError as err:
#     print(err)

# except Exception as err:
#     print("알수 없는 에러")
#     print(err)

# 작심삼일 일일코딩 2022.6.25 (토) 끝.

# 작심삼일 일일코딩 2022.6.26 (일) 시작

# try:
#     print("한자리 전용 계산기")
#     num1 = int(input("첫째자리숫자입력"))
#     num2 = int(input("둘째자리숫자입력"))
#     if num1 >=10 or num2 >=10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")
 
# 작심삼일 일일코딩 2022.6.26 (일) 끝.

# 작심삼일 일일코딩 2022.6.27 (월) 시작
# 사용자 정의 에러처리

# from socket import MsgFlag


# class BigNumberError(Exception):
#     def __init(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#             return self.msg

# try:
#     print("한자리 전용 계산기")
#     num1 = int(input("첫째자리숫자입력:"))
#     num2 = int(input("둘째자리숫자입력:"))
#     if num1 >=10 or num2 >=10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))

#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")

# except BigNumberError as err:
#     print("에러가 발생하였습니다.. 한자리 숫자만 입력하세요")
#     print(err)

# 작심삼일 일일코딩 2022.6.27 (월) 끝.

# 작심삼일 일일코딩 2022.6.28 (화) 시작

# finally 프로그램이 강제 종료되는 것을 막음으로서 우리 프로그램의 완성도를 높일 수가 있다.

# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")


# 작심삼일 일일코딩 2022.6.28 (화) 끝.

# 작심삼일 일일코딩 2022.6.29 (수) 시작

# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집
# 대기 손님의 치킨 요리 시간 줄이고자 자동 주문 시스템
# 시스템 코드 확인, 적절한 예외처리 구문 넣으시오

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 치킨 총 량은 10마리
#         치킨 소진시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
while(True):
    try: 
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <=0:
            raise ValueError
        else:
            print("[대기번호 {0}], {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break

# 작심삼일 일일코딩 2022.6.29 (수) 끝.

# 작심삼일 일일코딩 2022.6.30 (목) 시작
# 모듈 필요한 것들 끼리 부품처럼 잘 만들어진 것
def price(people):
      print("{0} 명 가격은 {1}원 입니다.".format(people, people*10000))

# 작심삼일 일일코딩 2022.6.30 (목) 끝.
    

