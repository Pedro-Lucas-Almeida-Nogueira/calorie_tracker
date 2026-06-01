def calculate_tmb(gender, birth_date, created_at, height, weight):
    weight_kg = float(weight)
    height_cm = float(height * 100)
    age = created_at.year - birth_date.year
    tmb = 0

    #fórmula para homens
    if gender.lower() == "m":
        tmb = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
        return tmb
    
    #fórmula para mulheres
    tmb = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) -161

    return tmb

def calculate_calories_burned(tmb, activity_level):
    multiplier = 1
    match activity_level:
        case 1:
            multiplier = 1.2
        case 2:
            multiplier = 1.375
        case 3:
            multiplier = 1.55
        case 4:
            multiplier = 1.725
        case 5:
            multiplier = 1.9

    return tmb * multiplier