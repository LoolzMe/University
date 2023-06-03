import numpy as np

student = [0, 0, 12.7, 4.3, 3.2, 2.8, 2.6, 2.4, 2.4, 2.3, 2.3, 2.1, 2.1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

def student_f(length):
    if length > 16:
        return 2
    else: 
        return student[length]


def appr(std, length):
    return student_f(length) * std / np.sqrt(length)
    
    
def stud(obj):
    length = len(obj)
    return student[length] * np.std(obj, ddof=1) / np.sqrt(length)


def combineErrors(obj, error_obj, weights_obj):
    S = obj[0]
    weight = weights_obj[0]
    error = error_obj[0]

    for i in range(1, len(obj)):
        Wa = weight ** 2 - weight
        Wb = weights_obj[i] ** 2 - weights_obj[i]
        w = weight + weights_obj[i]
        W = w**2 - w

        
        error = np.sqrt((Wa / W) * (error ** 2) + (Wb / W) * (error_obj[i] ** 2) + ((weight * weights_obj[i]) * (S - obj[i]) ** 2) / (w * W))
        
        S = S * (weight / w) + obj[i] * (weights_obj[i] / w)
        weight += weights_obj[i]


    return [S, appr(error, weight)]