# Iss file mein dhyaan se dekhoge toh ek insaan ka naam aur ek sheher ka naam milegaYeh sheher woh 
# sheher hai jisme woh insaaan rehta hai. Ab aapne ek aisa code likhna hai jo:

#     Delhi mein rehne waale logon ko ek alag file mein daale. Delhi waali file ka naam "delhi.txt" hona chaiye.
#     Shimla mein rehne waale logon ko ek alag file mein daale. Shimla waali file na naam "shimla.txt" hona chaiye
#     Aur saare log jo delhi aur shimla mein nahi rehte, unko ek alag file mein daale. Iss file ka naam "others.txt" hona chaiye



 
file = open("delhi.txt.py","r")
file_data = file.read()
print (file_data)
file.close() 



 
my_file = open("shimla.py")
file_data = my_file.read()
print (file_data)
my_file.close() 




 
other = open("other.py")
file_data = other.read()
print (file_data)
other.close() 