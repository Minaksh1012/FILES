# Aapke paas ek list hai. Iss list mein har string ko ek 
# file-question3.txt naam ki file mein nayi line mein daalo. Aapki list yeh rahi:
# batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
# students_file = open("navgurukul_students.html", "w")
# students_file.write("<html>\n")
# students_file.write("<head>\n")
# students_file.write("<title>NavGurukul Students</title>\n")
# students_file.write("</head>\n")
# students_file.write("<body>\n")
# students_file.write("<ul>")
# for student in batch1_students:
#     students_file.write("<li>" + student + "</li>\n")
# students_file.write("</ul>\n")
# students_file.write("</body>\n")
# students_file.write("</html>\n")
# students_file.close() 

 
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
file=open("file_question3.txt","w")
# for bank in banks_list:
#     file.write(bank)
file.write("\nkotak")
file.write("\nHDFC")
file.write("\nRBL")
file.write("\nSBI")
file.write("\nBank of Baroda")
file.close()







