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
