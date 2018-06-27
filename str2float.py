from functools import reduce
def str2float(s):
    s1, s2 = s.split('.')
    def char2num(a):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[a]
    def num2numSeries(x, y):
        return x * 10 + y
    
    result = reduce(map(num2numSeries, s1)) + reduce(map(num2numSeries, s2)) / len(s2)
    return result



print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
