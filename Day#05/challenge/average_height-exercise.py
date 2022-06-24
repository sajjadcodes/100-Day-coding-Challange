# Day 5.1 Average Height Exercise
## Find the link to the exercise in the resources

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_of_heights = 0
total_num = 0
avarage_height = 0

for height in student_heights:
    sum_of_heights += height
    total_num += 1

avarage_height = sum_of_heights / total_num

print(round(avarage_height))