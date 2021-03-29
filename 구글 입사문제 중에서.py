
def count(n):
    n=str(n)
    y=0
    for i in range(0, len(n)):
        if n[i]== "8":
            y+=1
    return y

result=0
for i in range(1,10001):
    result+=count(i)

result

"""https://codingdojang.com/scode/393?answer_mode=hide
1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?

8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
(※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)"""
