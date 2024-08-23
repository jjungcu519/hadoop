import sys

for line in sys.stdin:
    line = line.strip() #좌우 공백, 비어있는 공간 쳐내는 작업

    fields = line.split('\t')

    movie_id = fields[1]
    rating = fields[2]

    print(f'{movie_id}\t{rating}')