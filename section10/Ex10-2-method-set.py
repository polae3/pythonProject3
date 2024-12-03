'''
파일명: Ex10-2-method-set.py

'''
# 교집합 intersection()
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}

result = s1.intersection(s2)
print(result)

# 차집합 difference()
result = s1.difference(s2)
print(result)