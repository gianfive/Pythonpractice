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
# pip install

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 작심 일일 코딩 2022.7.9 (토) 시작

