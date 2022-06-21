# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
age_in_months = int(age*12)
age_in_weeks = int(age*52)
age_in_days = int(age*365)
final_age = int(90)
left_months = (final_age * 12) - (age * 12)
left_weeks = (final_age * 52) - (age * 52)
left_days = (final_age * 365) - (age * 365)
print(f'You have {left_days} days, {left_weeks} weeks and {left_months} months left.')

