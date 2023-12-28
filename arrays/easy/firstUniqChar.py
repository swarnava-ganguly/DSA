s = "aabb"
d = {}
for i in range(0,len(s)):
    if s[i] not in d:
        d[s[i]] = d.get(s[i],0) + 1
    else:
        d[s[i]] = d[s[i]] + 1
print(d)
for i in d:
    if d[i] != -1:
        print(s.find(i))
        break
print(-1)