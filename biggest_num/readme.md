# Greedy 

> ## 문자열을 모두 체크한다. 어찌보면 완전탐색이라고 볼 수도 있겠는데 왜 greedy라고 명칭할까??
>> ## 4177252841로 예를 들어 보겠다. 
>>> 자료구조는 2개, tank라는 리스트와 k 정수 하나이다.
>>> number의 인덱스를 순회하면서, 숫자하나 하나씩을 tank라는 리스트에 넣어보고, 조건에 따라 넣은 숫자를 다시 뺄지, 아니면 tank에 있는 원소를 뺄지 정한다.  
>>> 4  
>>> 41  
>>> 417 -> 4x7 -> xx7 : k = 2 // 7을 넣어보고 7을 뺄지 아니면 tank의 원소들을 제거할지 고려한다.   
>>> 77  
>>> 772  
>>> 7725  -> 77x5 : k = 3 
>>> 7752
>>> 77528 -> 775x8 : k = 4 // 종료  
>>> 
> ## 처음 내가 접근한 방식::
>> 10개의 queue를 만들고, number의 인덱스를 순회하면서, 조건에 따라 number의 인덱스를 10개의 queue에 넣어주고, 이 10개의 queue를 연결리스트로 묶어준다.  
>> 이 연결리스트에서 작은 숫자가 담긴 박스에서 원소를 꺼내면서 그 인덱스들을 연결리스트에서 제거한다.   
>> 생긴 문제::
>> 나의 알고리즘 처럼 하면 4177252841 에서 4x77x5x854x 처럼된다. 
>> 제일 처음 나오는 4보다 작은 숫자가 4개나 있기에, 4가 제거되지 못한다. 숫자의 나열이 아니라, 이 숫자들이 자릿수마다 가지는 비중이 다르기 때문에 생긴 문제이다.  
>> 요런 숫자의 크기를 구하는 문제는 숫자 하나씩을 순회하면서, 그 전에 만든 숫자보다 큰지 안큰지 비교해나가는게 좋은것 같다. 
>> 