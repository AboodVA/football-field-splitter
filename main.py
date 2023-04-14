
#Data types
# String, int, float, bool


# print("HELLO"[-1])

# print("123" + "321")

# num = int("12")
#
# num = num + 10
# print(num)



# is_true = True
#
# print(is_true)

#NOT ALLOWED
#print("ads"+ 123)

# print(type("asd"))

# input = input("Enter a two digit number")
#
# first_num = int(input[0])
# second_num = int(input[1])
# sum = str(first_num + second_num)
#
# print("Sum of the two digits is " + sum)
#Mathemitical OPeration, (), **, *, / , + , -
#
# 3+5
# 7-5
# 4/2
# 3*2
# 3**2
# (3 + 2)*5


# BMI CALCULATOR

# height_m = float(input("Enter your height in meters"))
# weight_kg = float(input("Enter your weight in kg"))
#
#
# bmi = weight_kg / height_m ** 2
#
# print(f"Your bmi is {round(bmi,1)}.")


# score = 1;
# score += 1
# score -=1
# score *=2
# score /= 2

#Life in weeks

# age = int(input("What is your age?\n"))
# remaining_age = 90-age
#
#
# months = remaining_age * 12
# weeks = months * 4
# days = weeks * 7
#
# print(f"You have {months} months left, {weeks} weeks Left, "
#       f",{days} days left")




print("Hajz Al-Mal3b Cacluinator")

total_fee = float(input("How much is the fees for the football field?"))
num_of_people = float(input("How many peolpe are there?"))

fee_per_person = round(total_fee / num_of_people,1)

print(f"Each person should pay {fee_per_person} JOD")
