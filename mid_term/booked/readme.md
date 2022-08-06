# 내가 푼 방식
>  1. 데이터 전처리 ( 시간과 이름 그리고 예약 그리고 예약x 까지 정보를 담아서 자료를 만든다. 단 이때 시간은 datetime 모듈을 이용한다.)
>  2. 모든 데이터를 하나의 리스트에 넣고, 시간을 기준으로 정렬한다. 
>  3. 데이터를 인덱스 순서로, 하나씩 돌아가는데, 어떤 한 데이터를 선택하면 후보가 되는 다음 데이터들의 집합을 만들고, 이 집합중에서 가장 빠른 놈을 고른다. (아마, 
> 이 집합을 선택하는 과정에서 시간이 많이 걸리는것 같다.)
>  4. 너무 컴퓨터의 사고에 익숙해졌나 ? 파이썬 답지 않은 코드인것 같다. 

# 다른 풀이 

```python

def solution(booked, unbooked):
    current_time = "00:00"
    result = []

    while booked and unbooked:
        if booked[0][0] > unbooked[0][0] and current_time < booked[0][0]:
        # 와 대박 직관적으로 짯다. ??:?? 형식을 그대로 유지하다니.. 대박인데 ... 거의 자연어 수준이네.....
            time, name = unbooked.pop(0)
        else:
            time, name = booked.pop(0)

        time = current_time if current_time > time else time 
        current_time = calculate_time(time)
        result.append(name)

    result.extend([b[1] for b in booked])
    result.extend([u[1] for u in unbooked])

    return result

def calculate_time(time):
    hour, minute = [int(x) for x in time.split(":")]
    # 나처럼 datetime 모듈을 굳이 사용하지는 않았구만 
    minute += 10
    if minute >= 60:
        hour += 1
        minute -= 60
    return str(hour).zfill(2) + ":" + str(minute).zfill(2)
  # 시간 포맷을 : 으로 유지 했네 오 
```
