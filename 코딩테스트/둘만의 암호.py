from string import ascii_lowercase
"""
https://school.programmers.co.kr/learn/courses/30/lessons/155652
둘만의 암호
"""


def solution(s, skip, index):    
    alpha= list(ascii_lowercase)
    
    for i in range(0,len(skip)):
        skipAlpha = skip[i]
        alpha.remove(skipAlpha)
    answer = ""

    for i in range(0,len(s)):
        sAlpha = []
        alphaIndex = []
        sAlpha = s[i]
        alphaIndex = alpha.index(sAlpha) + index     
        if( alphaIndex >= len(alpha)):
            alphaIndex = alphaIndex - len(alpha)
        
        answer = answer + str(alpha[alphaIndex])

    return answer

solution("aukks", 'wbqd', 5)







