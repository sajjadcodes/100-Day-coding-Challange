# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name1_t = name1_lower.count('t')
name1_r = name1_lower.count('r')
name1_u = name1_lower.count('u')
name1_e = name1_lower.count('e')
total_true_name1 = name1_t + name1_r + name1_u +name1_e
#love
name1_l= name1_lower.count('l')
name1_o = name1_lower.count('o')
name1_v = name1_lower.count('v')
name1_e = name1_lower.count('e')
total_love_name1 = name1_l + name1_o + name1_v + name1_e 
#name two
name2_lower =name2.lower()
name2_t = name2_lower.count('t')
name2_r = name2_lower.count('r')
name2_u = name2_lower.count('u')
name2_e = name2_lower.count('e')

total_true_name2 = name2_t + name2_r + name2_u +name2_e
#name two love
name2_l= name2_lower.count('l')
name2_o = name2_lower.count('o')
name2_v = name2_lower.count('v')
name2_e = name2_lower.count('e')
total_love_name2 = name2_l + name2_o + name2_v + name2_e

total_love = total_love_name1 + total_love_name2
toal_true_love= total_true_name1 +total_true_name2 
score =int(f"{toal_true_love}{total_love}") 
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score< 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")