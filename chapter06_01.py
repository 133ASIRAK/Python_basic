# Chpater06_01
# 파이썬 클래스
# OOP (객체지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임 스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제 1

class Dog1: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog1)

# 인스턴스화
a = Dog1("mikky", 2)
b = Dog1("baby", 3)

# 네임스페이스
print('dog1', a.__dict__) 
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

print(Dog1.species)
print(a. species)
print(b. species)

if a.species == 'firstdog' :
    print('{0} is a {1}'.format(a.name, a.species))

# 예제2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(self)
        print('Func2 called')

f= SelfTest()

# print(dir(f))

print(id(f))
# f. func1() # 예외
f. func2() # self method가 있으면 클래스를 생성한 인스턴스화 시킨 변수가 self로 넘어감

SelfTest.func1() # 클래스로 직접 호출
# SelfTest.func2() # 예외 # 하나의 매개변수를 요구하지만 들어가지 않았기 때문에 에러가 발생
SelfTest.func2(f) # 인스턴스로 호출


# 예제3
# 클래스 변수, 인스턴스 변수

class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0 # 재고
    
    def __init__(self, name): # 생성자
        # 인스턴스 변수
        self. name = name
        Warehouse.stock_num += 1

    def __del__(self): # 소멸자
        Warehouse.stock_num -= 1

        
user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)

print(user1.__dict__)
print(user2.__dict__)

print('before', Warehouse.__dict__) # stock_num : 2 결과값 확인 가능

print('>>>', user1.stock_num) # 2

del user1
print('after', Warehouse.__dict__) # user1의 값을 지웠으므로 stock_num 결과값이 1로 변함


# 예제4 

class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self): 
        return '{} is {} years old.'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4) # 각각 자기만의 정보를 가지고 있음
d = Dog('kk', 5)

# 메소드 호출
print(c. info())
print(d. info())

# 메소드 호출
print(c. speak('Wal Wal'))
print(d. speak('kang kang'))

