# 완전탐색 문제인가??
> ## 고려해야할점
>> * 정수가 엄청 클 수 도있겠다 그래서 문자열로 저장해야할듯
>> * dfs하면 시간이 너무 많이 걸리는데, 이걸 어떻게 해결해야할지?? 


```python

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers)
    #return str(int(''.join(numbers)))
```

>> * sort를 람다함수를 이용해서 하는데, 첫번째 인덱스 부터 비교해서 정렬을 하는것 같다. 인덱스 뒤에서 부터하는거랑 앞에서 하는거랑 무슨차이지?   
>> 시간복잡도가 얼마일까? dfs하면 큰일나는 문제였따~~ 
    
### 좌측은 radix sort , 우측은 그냥 nlogn 이 걸리는 sort를 쓴 결과야

>> 왜 radix sort가 시간이 더 걸리는지 분석을 해봐야겠다. 

<img width="757" alt="스크린샷 2022-07-12 오후 5 30 28" src="https://user-images.githubusercontent.com/63406434/178453274-927a7402-ff6e-4bc1-be96-8993fb50d27f.png">
