
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

