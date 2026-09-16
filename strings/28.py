haystack = "sadbutsad"
needle = "sad"
for i in range(len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle)]==needle:
        print(i)
    else:
        print(-1)