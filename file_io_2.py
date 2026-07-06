#Creation of the text file 
#open() keyword used to create the file and also deals with inut and output of the function
file_handle=open("demo_ec.txt","w")
file_handle.write("Writing my first file -txt")
file_handle.write("\nRanju is busy")
file_handle.close()

#Read the contents from the file
file_handle=open("demo_ec.txt","r")
print(file_handle.read())
file_handle.close()

#Check If the file is Opened or not
#file.io means pre defined clean ups
print(file_handle.closed)

#Predefined Clean Up using with block
with open("demo_ec.txt","a")as file_handle:
    file_handle.write("\n I am writing 2nd line work like line live like a king ")

#seek()
with open("demo_ec.txt","w+")as file_handle:
    file_handle.write(" good job ")
    file_handle.seek(0) #0 to place the cursor in the beginning 
    print(file_handle.read())

#create csv files
import csv
with open("data.csv","r") as csv_handle:
    rows=csv.reader(csv_handle)
    for r in rows:
      print(r)
    rows_dictionary=csv.DictReader(csv_handle)
   # Dictionary O/P
    for data in rows_dictionary:
        print(data)
 
 #Write rows
    with open("data.csv","a")as csv_write_handle:
        writer_handle=csv.writer(csv_write_handle)
        writer_handle.writerow([1,"Rahul",67890,"2004-09-15"])
        writer_handle.writerow([1,"ram",67890,"20055"])



#file_handle.write("sl,student_name,usn,dob")
#file_handle.write("\n1,Ranju,2435,1996")
#file_handle.write("\n2,Shivaleela,3456,1896")
#file_handle.write("\n3.Vivekananda,3234,1863")
#file_handle.write("\n4,Chaitra,2355656,406bc")
