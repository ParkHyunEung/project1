Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


##함수(=메서드) 선언부


def add_func(n1,n2):\
    result= n1 + n2
    return result




## 전역 변수부(=인스턴스 변수)

num1, num2, res = 100, 200, 0


## 메인 코드부:

res = add_func(num1, num2)
print(num1,'+',num2,'=',res)
