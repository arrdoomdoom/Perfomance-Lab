def roadmap(n,m):
    path = [1]
    start = m
    while start != 1:
        path.append(start)
        start = (start + m - 1) % n
        if start == 0:
            start = n
    return ''.join(map(str, path))

def read_input():
    line = input().split(' ')
    n = int(line[0])
    if len(line) == 2:
        m = int(line[1])
    else:
        m = int(input())
    return n, m
    

if __name__ == '__main__':   
    n,m = read_input()
    print(roadmap(n, m))