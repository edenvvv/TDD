def bmi_calc(height, weight):
    """calculate bmi by using height and weight"""
    if height == 0:
        return "cant divide by 0"
    if height < 0 or weight <= 0:
        return "unacceptable values"
    bmi = round(weight / (height * height), 2)
    return bmi


def bmi_status(bmi):
    """return status by the subjected bmi"""
    if bmi <= 0:
        return "unacceptable values"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obesity Rank 1"
    elif 35 <= bmi < 40:
        return "Obesity Rank 2"
    elif 40 <= bmi:
        return "Obesity Rank 3"
