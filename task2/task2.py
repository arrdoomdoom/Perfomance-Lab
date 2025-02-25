def read_input():
    line = input().split(' ')
    file1 = line[0]
    if len(line) == 2:
        file2 = line[1]
    else:
        file2 = input()
    
    return file1, file2

def find_positions(circle_center, circle_r, file):
    positions = []
    for line in file:
        point = line.split(' ')
        x = float(point[0])
        y = float(point[1])
        
        distance = ((x - float(circle_center[0]))**2) + ((y - float(circle_center[1]))**2)
        if distance < float(circle_r)**2:
            positions.append(1)
        elif distance == float(circle_r)**2:
            positions.append(0)
        else:
            positions.append(2)

    return '\n'.join(map(str, positions))

if __name__ == '__main__':
    file1, file2 = read_input() 
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        circle_center = f1.readline().split(' ')
        circle_r = float(f1.readline())
        
        print(find_positions(circle_center, circle_r, f2))