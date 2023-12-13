# <오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20171723 이름 : 조한성

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

# %%
def solution(my_string, target):
    if target in my_string:     # my_string이 target 문자열 내에 있다면 
        return 1    # 1 반환
    else:   # 아니라면
        return 0    # 0 반환

if __name__=='__main__': 
    print(solution('sayhellotopython', 'hello'))    # 결과 확인



# %%
# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.

# 제한사항 
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.

# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}

    answer = ''
    input = letter.split()  # 모스부호 입력값이 공백으로 나눠져 있으므로 .split 메서드로 나누기

    # 입력값에 있는 부호를 모두 찾아 변환하기 위한 for문
    for i in input: # 입력값의 모스 부호를 찾아
        answer+=morse[i]  # 모스 딕셔너리에서 추출하여 answer에 이어붙이기
    return answer 

# 결과 확인
if __name__=='__main__':
    print(solution('- .... . .-. . .. ...  -. --- .-.. --- ...- . --- ..-. .-.. .. ..-. . .-- .. - .... --- ..- - -.. . ... .--. .- .. .-.  --- ..-. .-.. .. ..-. .'))



# %%
# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.

# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.


# a b c d e f g h i j
# 0 1 2 3 4 5 6 7 8 9

# 아스키 코드표 사용
# 파라미터가 int 이므로 +97 적용 시 소문자 알파벳 해당

def solution(age):
    answer = ''

        # 'int' object is not iterable
        # can only concatenate str (not "int") to str

    for i in str(age):  # age 순회, int는 not iterable이므로 str으로 casting
        # 아스키코드표를 참조하여 맞는 character 리턴하기 위해 + 97연산, chr 메서드로 아스키코드대로 casting
        # str에 대해 + 연산으로 이어붙이기
        answer += chr(int(i)+97) 

    return answer 

if __name__=='__main__':    # 출력 확인
    print(solution(999))


# %%
# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.

# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    answer = 0

    # 중심이 원점인 두 원의 방정식은 x^2 + y^2 = r1^2, x^2 + y^2 = r2^2
    # 제한사항을 참고한다면 r2 > r1이므로 r2 내에 r1이 존재 
    # 원 위의 점도 포함이므로 range 메서드의 범위는 -r2 ~ r2+1  
    # 따라서 x축, y축을 이중 for문으로 훝으면서 r1^2(원 r1) 보다 크고 r2^2(원 r2)보다 작은 점 카운트

    for x in range(-r2, r2+1):  
        for y in range(-r2, r2+1):  # 축, y축을 이중 for문으로 훝으면서
            if r1*r1 <= x*x + y*y <= r2*r2:     # r1^2(원 r1) 보다 크고 r2^2(원 r2)보다 작은 점 카운트
                answer=answer+1 # 카운트
    return answer # 카운트 값 반환

if __name__=='__main__':
    print(solution(10,100)) # 결과 출력




# %%
# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
numbers = [8, 30, 17, 2, 23]

# 초기 로직 기반 코드 - 폐기
# def solution(numbers):

#     num = []
#     i=0

#     for i in range(len(numbers)):
#         if len(str(numbers[i])) == 4:
#             num.append(int(numbers[i]/1000))

#         elif len(str(numbers[i])) == 3:
#             num.append(int(numbers[i]/100))
        
#         elif len(str(numbers[i])) == 2:
#             num.append(int(numbers[i]/10))
            
#         elif len(str(numbers[i])) == 1:
#             num.append(int(numbers[i]))
            
#     num = sorted(num)
#     print(num)

#     # ????

# if __name__=='__main__':
#     print(solution(numbers)) # 결과 출력



from functools import cmp_to_key    # 조건 정렬을 사용하기 위한 라이브러리 import

# 조건 정렬을 하기 위한 decision 메서드 dec
# 두 수를 파라미터로 받아 문자열로 casting -> 이어붙이기 -> 다시 int casting 후 - 연산
# 이를 통해 str casting을 통해 붙인 두 수의 비교가 가능
# 반환값은 - or + 
def dec(num1, num2):
    # print(int(str(num1) + str(num2)) - int(str(num2) + str(num1)))
    # print(int(str(num2) + str(num1)) - int(str(num1) + str(num2)))
    return int(str(num1) + str(num2)) - int(str(num2) + str(num1)) 

def solution(numbers):
    answer = '' # 정답 문자열 정의
        
    # 조건에 맞게 주어진 리스트 정렬

    # cmp_to_key(dec)를 통해 정의된 dec메서드로 기반으로 조건 정렬 
    # dec가 아규먼트이므로 리턴되는 - or + 에 따라 sorting 
    numbers.sort(key=cmp_to_key(dec), reverse = True)   
    numbers = list(map(str, numbers))   # map 메서드를 사용해서 리스트 내 int 를 str으로 변환 -> 붙이기 위함
    # print(numbers)

    # 문자열 붙이기
    for i in numbers:
        answer += i

    return answer

if __name__=='__main__':
    print(solution(numbers))        # 결과 출력