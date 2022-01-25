def solution(brown, yellow):
    answer = []
    num = brown + yellow
    arr = []    # num 의 약수를 담을 arr
    for i in range(num,0,-1):
        if num % i == 0:
            arr.append(i)
    # print(arr)
    
    # arr 길이가 짝수일 때,
    if len(arr) % 2 == 0:
        for i in range(len(arr)//2):
            if arr[i] > brown:
                continue
            garo = arr[i]
            sero = arr[len(arr)-1-i]
            if (garo - 2) * (sero - 2) == yellow:
                answer.append(garo)
                answer.append(sero)
                break
    # 홀수일때,
    else:
        for i in range((len(arr)//2)+1):
            if arr[i] > brown:
                continue
            if i == (len(arr)//2):  # 3*3처럼 제곱수일때
                garo = arr[i]
                sero = arr[i]
            else:
                garo = arr[i]
                sero = arr[len(arr)-1-i]
            if (garo - 2) * (sero - 2) == yellow:
                answer.append(garo)
                answer.append(sero)
                break
                
    return answer