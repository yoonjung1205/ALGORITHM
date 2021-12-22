# string

### ord(): 아스키코드를 십진수로 변환 chr(): 아스키코드로 변환

```python
cnt = [0]*26
s = 'aba'
for x in s:
    cnt[ord(x)-ord('a')] += 1
print(cnt) # 문자의 개수 알 수있음

s = 'aBa'
for x in s:
    if 'a'<=x<='z':
        cnt[ord(x)-ord('a')] += 1
    elif 'A'<=x<='Z':
        print('대문자있음',x)
    elif '0'<=x<='9':
        print('숫자')
print(cnt)
```



