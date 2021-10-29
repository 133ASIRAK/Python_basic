# chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700
print(n*700)

# 출력
print(n)
print(type(n))

# 동시선언
x = y = z = 700
print(x, y, z)

#선언
var = 75

#재선언
var="Change value"

#출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))
--> 출력값은 300으로 동일하나 내부적 처리가 다르다

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n
print(m, n)
print(type(m), type(n))
print()

m = 400
print(type(m), type(n))
print()

# id(identity) 확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print()

print(id(m) == id(n))

# 같은 오브젝트 참조 --> ???같은 값이 나와야함.
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m) == id(n))

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method 선언
# Pascal Case : NumberOfCollegeGraduates -> Class 선언
# Snake Case : number_of_college_graduates -> PYTHON 변수선언

NumberOfCollegeGraduates = 3
print(NumberOfCollegeGraduates)

stuendt_grade = 3

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 7
1AGE = 7
--> 숫자, 특수문자(_,$만 허용)으로 시작하면 에러남

# 예약어는 변수형으로 불가능
for = 3
as = 3
--> python reserved word 검색하면 예약어로 나오는경우 사용 불가
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""