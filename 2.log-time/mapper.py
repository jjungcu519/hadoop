import sys
import re #정규표현식 사용

time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')

for line in sys.stdin:
    line = line.strip()
    #line.split(':')[1]

    jackpot = time_pattern.search(line)

    if jackpot:
        hour = jackpot.group(1)
        print(f'{hour}\t1')