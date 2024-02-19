''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.)

*   Create a VE and name it quiz_ve. Install the 3rd party libraries- wordcloud and imageio.
    Make sure your VE is NOT part of your repository. Make sure your .gitignore
    IS part of your repo. The code will produce a heart-shaped wordcloud of the most
    frequently appearing words in the text of Romeo and Juliet.

*   Create a dictionary of each student where the student FULL NAME (proper casing) is the key
    and the GPA is the value. 

*   print out the dictionary

*   print out the corresponding GPA for student - Luke Brazzi

*   push your repo to GitHub. Only your VE should not be in your repo. Everything else should be
    pushed. Submit your Github repo URL in the response field of the quiz.

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv


# create a file object to open the file in read mode
students = open('students.csv', 'r')


# create a csv object from the file object
csv_reader=csv.reader(students)

#skip the header row
next(csv_reader)

#create an outfile object for the pocessed record
outfile=open('processedStudents.csv', 'w', newline='')



#create a new dictionary named 'student_dict'
student_dict={}



#use a loop to iterate through each row of the file
for row in csv_reader: 

   


    #check if the GPA is below 3.0. If so, write the record to the outfile
    gpa=float(row[8])
    if gpa > 3.0:
        outfile.write(str(gpa))
        



    # append the record to the dictionary with the student Full name in proper case 
    # as the Key and the value as the GPA
    full_name = (f"{row['firstname']} {row['lastname']}")
    full_name_title=student_dict[full_name.strip().title()]
    student_dict.append([full_name_title][gpa])





#print the entire dictionary
print(student_dict)

#Print the corresponding GPA for student 'Luke Brazzi'
print("GPA for Luke Brazzi:", student_dict.get('Luke Brazzi',)['gpa'])

#close the outfile
outfile.close()


#display the wordcloud
from pathlib import Path
from wordcloud import WordCloud
import imageio.v2 as imageio
import matplotlib.pyplot as plt


text = Path("RomeoAndJuliet.txt").read_text()
mask_image = imageio.imread("mask_heart.png")
wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")
plt.imshow(wordcloud)
plt.show()







