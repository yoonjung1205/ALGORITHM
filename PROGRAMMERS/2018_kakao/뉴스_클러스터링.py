def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        answer = 1
        return answer * 65536
    
    elif not str1 and not str2:
        answer = 1
        return answer * 65536
    
    elif not str1 or not str2:
        answer = 0
        return answer
    
    str1_a = []
    str2_b = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha() and str1[i] not in ' ' and str1[i+1] not in ' ':
            str1_a.append([str1[i],str1[i+1]])
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha() and str2[i] not in ' ' and str2[i+1] not in ' ':
            str2_b.append([str2[i],str2[i+1]])
    
    inter = 0
    for ele in str1_a:
        if ele in str2_b:
            inter += 1
            
    union = len(str1_a) + len(str2_b) - inter
    answer = int((inter / union) * 65536)
    # print('a: ',str1_a)
    # print('b: ',str2_b)
    # print('inter: ',inter)
    # print('union: ',union)
    
    return answer