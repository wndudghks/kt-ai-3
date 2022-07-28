def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        count=0
        for i in range(2,num):#1과 자기 자신, 2개의 약수를 count하지 않음
            if num%i==0:
                count+=1
        if count%2==0:
            answer+=num
        else:
            answer-=num
    return answer

left = int(input('left: '))
right = int(input('right: '))
c = solution(left, right)
print(c)