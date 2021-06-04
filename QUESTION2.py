# Aapne jo pichle question mein (Question 1) file download kari hai, usko read karke usme 
# number of lines count kar ke print karein. Aapne sirf uss file ki number of lines Count karne ka code likhna hai.

# Hint: Har \n ke baad nayi line shuru hoti hai. Aap yeh use kar ke nayi line ka ko pehchan sakte ho.


 
# my_file = open("people1 exersice.py","r")
# counter=0
# # content=my_file.read
# file_data = my_file.read()
# number_of_lines=file_data.split("\n")
# for i in number_of_lines:
#     if i:
#         counter+=1
# print("these is number of lines")
# print(counter)



my_file = open("people1 exersice.py","r")
counter=0
# content=my_file.read
file_data = my_file.read()
number_of_lines=file_data.split("\n")
i=1
while i<=len(number_of_lines):
    if i:
        counter+=1
    i+=1    
print("these is number of lines")
print(counter)
