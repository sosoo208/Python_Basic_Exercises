import math

location = {
    '점1': (0,0),
    '점2': (3,4)
}

distance = math.dist(location['점1'], location['점2'])
print("두 점 사이의 거리 : ", distance)