def line_equation(pointA, pointB):
    result = ()
    sub = (pointA[0] - pointB[0])
    if pointA[0] == pointB[0] and pointA[1] == pointB[1]:
        raise ValueError('The points cannot be the same')
    if sub != 0:
        coordinate1 = (pointA[1] - pointB[1]) / sub
        coordinate2 = pointA[1] - ((pointA[1] - pointB[1]) / sub) * pointA[0]
        result = (coordinate1, coordinate2)
    return result



