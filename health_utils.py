def calculate_bmi(height, weight):
    return round(weight / (height ** 2), 2)

def calculate_bmr(height, weight, age, gender):
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return round(bmr, 2)