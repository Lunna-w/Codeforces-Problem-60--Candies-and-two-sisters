t = int(input())
 
for _ in range(t):
    n = int(input())
    ways = 0
    if n > 1:
        ways = (n - 1) // 2
    print(ways)