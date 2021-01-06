# Algorithm_study
###### sort 함수는 리스트.sort() 형식으로 사용되며 리스트의 원본값을 직접 수정 -> 메소드
###### sorted 함수는 sorted(리스트) 형식으로 사용되며 정렬 값을 반환 -> 파이썬 내장 함수

##### 아스테리크 (*) 사용법
######  a = [1,2,3,4]
###### 1.
###### -> print(*a) 할 시 1 2 3 4 와 같이 출력 됨(리스트에서 요소가 떨어저 나옴)
###### -> print(*a,sep='\n')와 같은 식으로 응용 가능 -> 1,2,3,4가 종으로 출력 / sep = '\n'는 출력하는 값 사이에 특정한 문자를 추가하여 출력함
###### 2.
###### -> *x, y = a 일 시 x = [1, 2, 3]가 y = 4가 저장됨
###### -> x,*y, z = a 일 시 x = 1, y = [2, 3], z = 4가 저장됨

###### set 함수를 사용하여 집합 형으로 바꾼 리스트들은 연산이 가능하다 -> 함수랑 똑같음

###### 리스트를 빈 리스트로 초기화 하려면 리스트.clear() 메소드를 사용

##### 한줄 for 문 사용법
###### -> [i for i in range(3)] 은 [0, 1, 2]를 반환함
###### -> [i for i in range(n) 조건문]과 같이 사용 가능
