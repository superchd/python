import copy

def exist(player, completion):
    for c in completion:
        if player == c:
            return True
    return False

def solution(participant, completion):
    answer = ''
    temp = copy.deepcopy(participant)
    print(participant)
    
    for p in participant:
        if exist(p, completion):
            temp.remove(p)
            completion.remove(p)
        
    return temp[0]