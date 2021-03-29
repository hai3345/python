"""https://codingdojang.com/scode/408?langby=python#answer-filter-area
1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다."""

a=input()
def Q1(a):
    b=[]
    for i in range(0, len(a)):
        b.append(a[i] - a[i - 1])
    del b[0]

    c = min(b)
    d = b.index(c)

    y = a[d], a[d + 1]
    return y
Q1(a)
