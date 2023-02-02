# -*- coding: utf-8 -*-
"""
@author: bstarly
"""

'''
Qn 1 (10 points)
Read the file ‘grades.csv’. Write code that finds and displays the 5 student IDs 
and their corresponding grades who received the lowest grades in the class. 
Some students have not appeared for the exam, but they are not to be treated as 0. 
They need to be simply skipped from the computation. (20points)
'''


'''
Qn 2 (20 points)
Open and read the contents of the file – ‘2_NoofParts_assem.txt’. Perform the following (20 points):
a)	Calculate how many entries are available in that file excluding the header.
b)	Calculate the sum of all parts from each file. Essentially, finding the sum of all values contained in the 2nd column of the file.
c)	Extract the part ID that has the largest associated no. of parts from the entire list.
'''


'''
Qn 3 (25 points)
Using a python script, open the files contained in the .zip file – “3_Jobs_Completed_log.zip”. 
Scan the files for the line that starts with the word string – “Jobs Completed.. ”. Extract the number associated with this line and for all instances that this word string appears across all log files, count the total sum across all files contained within the .zip file. (20points) 

For example:

 	Jobs Completed.. 10 2018-09-04 08:21:28.503153

Extract the number 10 from this sentence which signifies the total number of jobs completed at the point in time.  
Find for all instances in which the string - ‘Jobs Completed’ appears, 
find the total number of jobs completed by adding the numbers from across the provided log files.
'''



'''
Qn 4 (20 points)
For the same files above, calculate the following:
a)	How many jobs were completed in the period between 15th Aug 2018 to 15th Sept 2018?
b)	The day of the year in which the maximum number of jobs was completed.
c)	Calculate the total number of days elapsed between the time at which the first job batch was completed to the last batch completed.
'''




'''
Qn 5 (25 points)
Read the following (6_Part1.stl) triangular mesh file available in ASCII format. 
For those of you aware of 3D printing, you will recognize this is as a .STL file. 
For those who aren’t aware of what a .STL file is, please read up online on the format of a .STL ascii file. 
An ASCII formatted .STL file can be opened in any text editor. 
Every vertex of the triangle is preceeded by the word ‘vertex’ followed by the x, y and z coordinates. 
Therefore, ONE Triangle should have 3 vertex entries. Typically, the units is not specified, 
but you can assume it to be in millimeters. 

Write functions that calculate the following: (20 points)
a.	Find the total number of triangles listed in the file.
b.	Store the coordinates of each triangle in a 3-tuple list containing N indices, where N is the total number of triangles.
c.	List the area of each triangle in the file. Compute the total surface area of all triangles listed in the file. Read up online on the formula to calculate the area of a triangle, given three vertices.
'''
