n = int(input())

# 1 자리
# 1

# 2 자리
# 22

# 3 자리
# 122, 221, 333

# 4 자리
# 1221, 1333, 3331, 4444

# 5 자리
# 13331, 44441, 22122, 33322, 22333, 14444

# 동적프로그래밍을 사용하되, 검증을 통해 테스트가 필요할듯 

# 5자리는 f(5) = f(4) + 2 ,, f(3) + 2 ,, f(2) + 2 ,, f(1) + 2 
# 머리 아픈게 선택한 숫자가 그 전의 배열과 연속되면 어쩌징?/// 

# 배열을 무한으로 만들어서, 검증이 실패되면 자르는것은? 너무 시간이 많이 걸리는 일 같다 .... 

