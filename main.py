## 함수
def add_func(n1, n2):
    result = n1 + n2
    return result

def sub_func(n1, n2):
    return n1 - n2

def mul_func(n1, n2):
    return n1 * n2

def div_func(n1, n2):
    return n1 / n2

def square_func(n1, n2):
    return n1 ** n2

## 전역변수
num1, num2, res = 100, 200, 0


## 메인코드
res = add_func(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)

res = mul_func(num1, num2)
print(num1, '*', num2, '=', res)

res = div_func(num1, num2)
print(num1, '/', num2, '=', res)

res = square_func(num1, num2)
print(num1, '**', num2, '=', res)
