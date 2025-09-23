def my_add(a, b):
    return a+b

def my_sub(a, b):
    return a - b

if __name__ == "__main__": # 할당값을 줘서 안전장치 기능을 시킴
    print(my_add(1, 2))
    print(my_sub(3, 4))

print(f"mymodule안에서의 __name__: {__name__}")

#모듈을 개발할 때. 기능을 테스트하고 모듈을 쓴다고 했을 때
#(원치 않는 결과인 쓰레기 값이 포함될 것 같은 경우) 
#if __name__ == "__main__": 를 기입