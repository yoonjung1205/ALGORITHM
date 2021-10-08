def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 입력된 str이 같은 경우
    if str1 == str2:
        answer = 1
        return answer * 65536
        
    # 다중집합 선언, 저장
    str1_a = []
    str2_b = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha() and str1[i] not in ' ' and str1[i+1] not in ' ':
            str1_a.append([str1[i],str1[i+1]])
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha() and str2[i] not in ' ' and str2[i+1] not in ' ':
            str2_b.append([str2[i],str2[i+1]])
    
    
    # 변환되기 전에 공집합 처리를 했었는데, 변환 후 공집합인건 고려를 안해줌 -> 변환 후 고려해줌
    # 변환된 str이 공집합인 경우
    if not str1_a and not str2_b:
        answer = 1
        return answer * 65536
    
    inter = 0
    for ele in str1_a:
        if ele in str2_b:
            str2_b.remove(ele)  # 중복을 방지하기 위해 한쪽에 교집합 부분을 지워준다 aaabbb aaaabb일 경우
            inter += 1
            
    union = len(str1_a) + len(str2_b)   # 중복된 부분(교집합부분)을 빼줬기때문에 두 집합의 합만 구해줘도 된다.
    answer = int((inter / union) * 65536)
    # print('a: ',str1_a)
    # print('b: ',str2_b)
    # print('inter: ',inter)
    # print('union: ',union)
    
    return answer