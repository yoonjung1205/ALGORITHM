T = int(input())


def check_2(string, start, end):
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False

    return True


def check(string):
    start = 0
    end = len(string) - 1


    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            if check_2(string,start+1,end):
                return 1

            if check_2(string,start,end-1):
                return 1

            else:
                return 2
    return 0


for _ in range(T):
    string = input()
    result = 0
    case = 0
    result = check(string)
    print(result)