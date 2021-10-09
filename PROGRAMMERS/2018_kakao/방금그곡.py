def solution(m, musicinfos):
    answer = ''
    if '#' in m:
        m = m.replace('A#','a')
        m = m.replace('C#','c')
        m = m.replace('D#','d')
        m = m.replace('F#','f')
        m = m.replace('G#','g')
        m = m.replace('E#','e')
    result = []
    for musicinfo in musicinfos:
        music_s,music_e,title,info = musicinfo.split(',')
        
        # 재생시간(시:분 -> 분)
        H,M = map(int,music_s.split(':'))
        music_s = H*60 + M
        H,M = map(int,music_e.split(':'))
        music_e = H*60 + M
        playing_time = music_e - music_s
        print(playing_time)
        
        if '#' in info:
            info = info.replace('A#','a')
            info = info.replace('C#','c')
            info = info.replace('D#','d')
            info = info.replace('F#','f')
            info = info.replace('G#','g')
            info = info.replace('E#','e')
        print(music_s,music_e,title,info)
        
        # 음악길이
        m_l = len(info)
        
        # 재생시간 동안 재생된 음(= 악보정보*몫 + 나머지), 나머지가 아니어도 된다.. 
        music = info * (playing_time//m_l) + info[:playing_time]
        print(m,music)
        
        
        # 입력된 음악이 재생된 음악에 있는 경우
        if m in music:
            result.append([playing_time,music_s,title])
    
    # 일치하는 음악이 없는 경우
    if not result:
        return "(None)"
    # 일치하는 음악이 하나인 경우
    elif len(result) == 1:
        answer = result[0][2]
        
    # 일치하는 음악이 여러개인 경우
    else:
        result = sorted(result,key=lambda x:(-x[0],x[1]))   # 재생시간이 가장길고(내림차순), 먼저 들어온 순(오름차순)으로 정렬
        #result.sort(key=lambda x:(-x[0],x[1]))
        answer = result[0][2]
    
    return answer