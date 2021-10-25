# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 :

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''python start''')
print("""python start""")

print()

# separator 옵션
print('p','y','t','h','o','n', sep='')
print('010', '7777', '1234', sep='-')
print('python','google.com', sep='@')

print()

# end 옵션

print('wlecome to', end=' ')
print('IT news', end=' ')
print('Web Site')
print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

# format 사용 (d:3, s:'python', f:3.1445454)
d=digit 정수
s=string 문자열
f=실수
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}' .format('one', 'two'))
--> 순서가 지정됨

# %s
print('%10s' % (nice))
--> 10개의 자리를 확보하고 왼쪽부터 공백으로 처리함.

print('{:>10}'.format('nice'))
print('%-10s' % ('nice'))
print('{:10}' .format('nice'))
--> 부등호 생략하는경우 오른쪽으로 공백처리함.

print('{:_>10}' .format('nice'))
--> 공백으로 언더바로 채움

print('{:^10}' .format('nice'))
--> ^사용시 중앙정렬기능

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
--> .을 붙이면 5글자만 절삭, .이 없으면 전부 출력 가능

print('{:10.5}' .format('pythonstudy'))
--> 공간은 10개가 있고 5글자만 출력

# %d
print('%d %d' % (1,2))
print('{} {}' .format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print('%1.8f' % (3.144343434343))
--> 정수부 1번째 소수부 8번째 자리까지 출력

print('{:f}' .format(3.144141454545))
print('%06.2f' % (3.141592653589793))
-->정수부는 6자리지만 1자리기 때문에 0으로 채우고 소수부 2번째자리까지.

print('{:06.2f}' .format(3.141592653589793))

