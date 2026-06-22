#Substract current total from calories burnt
def burn_calories(current_total, activity_mins):

    calories_burned = activity_mins * 8.5

    #New total after workout
    new_total = current_total - calories_burned
    return new_total

#Adds functions add calories from a meal to the current total.
def log_meal(base_calories, meal_weight):

    #Meal weight is equal to caloroes of meat
    total_calories = base_calories + meal_weight
    return total_calories

def main():
    #Starting calories for the day.
    daily_calories = 2000.0

    #Add breakfast calories
    daily_calories=log_meal(daily_calories, 450.0)
    print(f"Calories after breakfast: {daily_calories}")

    #Substract calories burned from workout.
    remaining_calories = burn_calories(daily_calories, 30)
    print(f"Remaining calories after workout: {remaining_calories}")

main()