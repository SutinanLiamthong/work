import csv
import array as arr
def calculater(grade):
    n=0
    for i in range(n,len(grades)):
        if(grade[i] == 'A'):
            print(grade[i])
            sum = 4.0 
            n=n+1
            
        if(grade[i] == 'B'):
            
            sum = 3.5 
            n=n+1
            return (sum)
        if(grade[i] == 'C'):
        
            sum = 3.0
            n=n+1 
            return (sum)
        if(grade[i] == 'D'):
            
            sum = 2.5
            n=n+1 
            return (sum) 
        if(grade[i] == 'F'):
            
            sum = 2.0 
            n=n+1
             return (sum)
        else:
            
            sum = 0
            n=n+1
             return (sum)
      

with open('D:\example\semester1.csv') as semester1file:
    readCSV = csv.reader(semester1file,delimiter=',') 
    grades = []
    credits = []
    for row in readCSV:

        grade = row[2]
        grades.append(grade)
        
        
            
        print(calculater(grades))
             
     