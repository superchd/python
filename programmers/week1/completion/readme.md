# 완주하지 못한선수 

> ### 효율성을 못잡았다.

> ### 다른 사람들의 코드를 보자!

> 단어의 개수 파악해주는 라이브러리 (딕셔너리로 리턴) -> 개꿀

```python

from collections import Counter

def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    answer = list(result.keys())[0]
    return answer
```
> **counter의 시간복잡도 -> O(N)**

> 딕셔너리를 만드는 또 다른 방법

```python

def solution(participant, completion):
    # 딕셔너리 선언
    count={}
    # 이때 i는 key값, 우측값은 value 값
    for i in participant: # 동명이인 구별
        try: count[i] += 1
        except: count[i]=1
    
    for j in completion: # 완주자 구별
        if j in count:
            count[j] -= 1
    # 이 구문이 이해가 안간다. 
    answer = [k for k, v in count.items() if v > 0]
    return answer[0]
```

> hash 함수 사용

```python
def solution(participant, completion):
    hashDict = {}
    hashSum = 0

    for p in participant:
        hashDict[hash(p)] = p
        hashSum += hash(p)
    
    for c in completion:
        hashSum -= hash(c)

    return hashDict[hashSum]
```

> * hash는 고유한 값을 주나보다. 아마 겹치지 않는 특정한 엄청 긴값을 주는것같은데 언제쓸까?? 








