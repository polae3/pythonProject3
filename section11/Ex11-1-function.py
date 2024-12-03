'''
파일명: Ex11-1-function.py

함수 (Function)
    특정 작업을 수행하기 위해 독립적으로 설계된 코드 블록
    입력값을 받아서 처리한 후, 결과를 반환하거나, 반환없이 작업을 수행할 수 있다.

함수 정의 형식:
def 함수이름(매개변수):
    수행할 코드
    return 변환값

# 매개변수와 반환값은 없으면 생략 가능
'''

# welcome 함수 정의
def welcome():  # 매개변수 없음, 리턴값 없음 => 실행 후 끝나는 함수
    print('프로그램 시작!')
    print('Hello, Python')
    print('Nice to meet you')
    print('프로그램 종료!')

# 함수 호출 실행
welcome()
welcome()
welcome()
welcome()
welcome()
welcome()
welcome()
welcome()

