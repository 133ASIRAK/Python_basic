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

