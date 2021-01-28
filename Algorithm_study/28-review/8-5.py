for _ in range(int(input())):
    a, b, c = map(int,input().split())
    # 층
    if c%a == 0:
        floor = str(a)
    else:
        floor = str(c%a)
    # 호수
    if c%a == 0:
        ho = str(c//a)
    else:
        ho = str(c // a + 1)
    if len(ho) == 1:
        ho = '0'+ho
    print(floor+ho)