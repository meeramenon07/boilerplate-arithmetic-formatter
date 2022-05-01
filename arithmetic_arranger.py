
def arithmetic_arranger(problems, answer = False):
 if len(problems) > 5 :
  return "Error: Too many problems."
 top_num = []
 bottom_num = []
 operator = []
 for problem in problems:
     components = problem.split()
     top_num.append(components[0])
     operator.append(components[1])
     bottom_num.append(components[2])
    #check for * or /
 if "*" in operator or  "/" in operator:
     return "Error: Operator must be '+' or '-'."
  #check if digits
for i in range(len(top_num)):
     if not(top_num[i].isdigit() and bottom_num[i].isdigit()): 
      return "Error: Numbers must only contain digits."
    #check for length error
for i in range(len(top_num)):
     if len(top_num[i]) > 4 or len(bottom_num[i]) > 4 :
      return "Error: Numbers cannot be more than four digits."
first_row = []
second_row = []
third_row = []
fourth_row = []
for i in range(len(top_num)): 
    if len(top_num[i] > len(bottom_num[i])):
      first_row.append(""*2 + top_num[i])
    else:
      first_row.append("" *(len(bottom_num[i]) - len(top_num[i])+2)+ top_num[i])
for i in range(len(bottom_num)):
    if len(bottom_num[i] > len(top_num[i])):
       second_row.append(operator[i] + "" + bottom_num[i])
    else:
       second_row.append(operator[i] + "" *(len(top_num[i]) - len(bottom_num[i] + 1) + bottom_num[i]) 
for i in range(len(top_num)): 

      
  third_row.append("-" * (max(len(top_num[i]), len(bottom_num[i])) + 2))
if answer:
  for i in range(len(top_num)):
      if operator[i] == "+":
           ans = str(int(top_num[i] + bottom_num[i]))
      else:
           ans = str(int(top_num[i] - bottom_num[i]))
      if len(ans) > max(len(top_num[i]), len(bottom_num[i])):
         fourth_row.append("" + ans)
      else:
                 fourth_row.append("" * (max(len(top_num[i]), len(bottom_num[i])) - len(ans) + 2) + ans)

     arranged_problems = "".join(first_row) + "\n" + "".join(second_row) + "\n" + "".join(third_row) + "\n" + "".join(fourth_row)
else:
     arranged_problems = "".join(first_row) + "\n" + "".join(second_row) + "\n" + "".join(third_row)
return arranged_problems 












 














      

  
    
      

  
















