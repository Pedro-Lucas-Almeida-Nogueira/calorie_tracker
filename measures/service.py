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