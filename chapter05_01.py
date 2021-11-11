# Chapter05_01
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lambda)

# 함수 정의 방법

# def funtion_name(parameter):
#   code

# 예제 1
def first_func(w):
    print("Hello, ", w)

word = "Good Boy"

first_func(word)
print(first_func(word))

# 예제 2 / 함수형 프로그래밍

def return_func(w1):
    value = "Hello, " + str(w1)
    return value

x = return_func('Good boy2')
print(x)

# 예제 3 (다중반환) : 리턴형태에 대해 딕셔너리, 튜플, 일반변수, 리스트 등 

def func_mul(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x, y, z)

# 튜플 리턴

def func_mul2(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

q = func_mul2(20)

print(type(q), q, list(q))


# 리스트 리턴

def func_mul3(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]  # 리스트 형태로 괄호 변경

p = func_mul3(30)

print(type(p), p, set(p))

# 딕셔너리 리턴

def func_mul4(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2' : y2, 'v3' : y3}  # 중괄호에 키, 밸류값이 없으면 set 형태이므로 딕셔너리 형태를 유지하도록 하자

d = func_mul4(30)

print(type(d), d, d.get('v2'), d. items(), d.keys())

# 중요
# *args, **kwargs

# *args(언팩킹)
def args_func(*args): # 매개변수 명 자유 # 가변 인자로 사용가능 # 튜플형태로 변환
    for i , v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **kwargs(언팩킹) # 딕셔너리형은 별표 2개 붙여서 사용 , 키와 밸류인것을 매개변수로 넘길때 사용한다

def kwargs_func(**kwargs) : # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park', name3 = 'Kim', sendSMS = True)

# 전체 혼합 # 인수의 갯수에 구애받지 않고 내가 원하는 형태로 다양한 기능 수행 가능
def example(arg_1, arg_2, *args, **kargs):
    print(arg_1, arg_2, args, kargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1= 20, age2 = 30, age3 = 40)


# 중첩함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")    
    func_in_func(num + 100)

nested_func(100)

# 실행 불가
# func_in_func(1000) # 부모함수를 호출하지 않으면 자식 함수를 호출할 수 없음. 


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

#def mul_func(x, y):
#    return x * y

# Lambda x, y: x * y  # 같은 결과값을 반환해주는 함수

# 일반적 함수 -> 할당
def mul_func(x, y):
    return x * y

q = mul_func(10, 50)
print(q)  # print(mul_func(10, 50))과 동일한 결과값 도출

mul_func_var = mul_func
print(mul_func_var(20, 50))

# 람다 함수 -> 할당
lambda_mul_func = lambda x,y : x * y # 익명 함수기 때문에 정의 필요함
print(lambda_mul_func(50, 50))

def func_final(x, y, func):
    print('>>>>>', x * y * func(100, 100))

func_final(10, 20, lambda x,y:x*y)
