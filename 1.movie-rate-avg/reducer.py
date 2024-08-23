import sys

current_movie_id = None
current_sum = 0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    movie_id,rating = line.split('\t')
    rating = int(rating)

    if current_movie_id == movie_id:
        current_sum += rating
        current_count +=1
    else:
        if current_movie_id is not None:
            current_avg = current_sum / current_count
            print(f'{movie_id}\t{current_avg}')

        current_movie_id = movie_id
        current_sum = rating
        current_count = 1

        current_movie_id = movie_id
        current_sum = rating
        current_count +=1

if current_movie_id == movie_id:
    current_avg = current_sum / current_count
    print(f'{movie_id}\t{current_avg}')