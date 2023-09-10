# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) # type: ignore
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
i = 0
total_height=0
for height in student_heights:
  total_height += int(height)
  i += 1

print(f'{round(total_height/i)}')


