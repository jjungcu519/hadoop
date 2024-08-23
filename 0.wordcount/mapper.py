import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split() #리스트 형태로 바뀜
    
    for word in words:
        print(f'{word}\t1')