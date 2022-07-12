# 작심 일일 코딩 2022.7.1 (금) 시작.
# 모듈

# import theater_module
# theater_module.price(3) #3명이서 영화보러 갔을 때 가격
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7)

# from theater_module import price_soldier as price
# price(5)

# 작심 일일 코딩 2022.7.1 (금) 끝.

# 작심 일일 코딩 2022.7.3 (일) 시작.

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# 작심 일일 코딩 2022.7.3 (일) 끝.

# 작심 일일 코딩 2022.7.4 (월) 시작

# # from travel import *
# trip_to=thailand.VietnamPackage()
# trip_to.detail()

# 작심 일일 코딩 2022.7.4 (월) 끝.

# 작심 일일 코딩 2022.7.6 (수) 시작

# 모듈 직접 실행

# class ThailandPackage:
#     def detail(self):
#         print("[태국 패키지 3박 5일] 방콕, 파타야 여향 (야시장 투어) 50만원")

# if __name__ == "main":
#     print("thailand 모듈을 직접 실행")
#     print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
#     trip_to=ThailandPackage()
#     trip_to.detail()

# else:
#     print("Thailand 외부에서 모듈 호출")

# 작심 일일 코딩 2022.7.6 (수) 끝.

# 작심 일일 코딩 2022.7.7 (목) 시작
# 패키지, 모듈위치

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand)

# 작심 일일 코딩 2022.7.7 (목) 끝.

# 작심 일일 코딩 2022.7.9 (토) 시작
# # pip install

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 작심 일일 코딩 2022.7.9 (토) 끝.


# 작심 일일 코딩 2022.7.11 (월) 시작
# 내장함수

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 좋은 언어입니다.".format(language))

#dir : 아딴 객체를 넘겨줳ㅆ을 떄 그 객체가 어떤 변수 함수 가지고있느지 표시

# print(dir())
# import random # 외장함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 작심 일일 코딩 2022.7.11 (월) 끝.

# 작심 일일 코딩 2022.7.12 (화) 시작
# 외장함수
# # 구글 : list of python modules
# # glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)

# import glob

# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# # os : 운영체제에서 재공하는 기본 기능

# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다")

# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time : 시간 관련 함수

# import time

# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S))

import datetime
# print("오늘 날짜는 ",datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장

td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)

# 작심 일일 코딩 2022.7.12 (화) 끝.


