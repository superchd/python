from itertools import permutations as pmt
def solution(n):

    #가능한 조합 만들기
    mptlist = list(pmt(n,len(n)))
    tmp =[]

    #리스트로 변환
    for i in mptlist:
        word= ''.join(i)
        tmp.append(word)

    #중복 단어 제거
    diclist = sorted(list(set(tmp)))
    print(diclist[-1:])
    #다음 단어 반환 및 마지막 단어면 자신 반환
    return diclist[diclist.index(n)+1] if n !=diclist[-1:] else n

print(solution("ABD"))
print(solution("ACBA"))