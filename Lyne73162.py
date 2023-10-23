#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:04:40 2023

@author: Lynenaccache
"""
import numpy as np
#S09_4 
##Write a program that converts a vector of values in Angstroms (Å) to nanometers.
#The program must construct an array of 21 equally spaced values ranging from 1.0 Å to 5.0 Å that can correspond 
#for example to values of an interatomic distance, and must convert the values to nanometers using the same array 
#for save the result. Finally, the program must write the array. (Data: 1 Å = 0.1 nm).

angstrom_to_nm = 0.1  
start_angstrom = 1.0  
end_angstrom = 5.0   
num_values = 21       

step_size = (end_angstrom - start_angstrom) / (num_values - 1)

values_in_nm = []

current_value = start_angstrom
for _ in range(num_values):
    values_in_nm.append(current_value * angstrom_to_nm)
    current_value += step_size

print("Values in nm : ", values_in_nm)


#S09_5 Table of values
#In Exercise S04_4 we explained how a table of values of a function could be generated so that the values 
#of the axis of the abscissa were equally spaced. Now we will do the same but using numpy arrays.
#Make a program in the following code cell that calculates and writes, according to what was explained there, 
#a table of values of the Gaussian function


x0 = float(input("Enter the value of x0: "))
s = float(input("Enter the value of s: "))


x_start = float(input("Enter the initial value of x: "))
x_end = float(input("Enter the final value of x: "))
num_points = int(input("Enter the number of points: "))

x_values = np.linspace(x_start, x_end, num_points)

y_values = (1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_values - x0) / s)**2)

print("x                y")
for x, y in zip(x_values, y_values):
    print(f"{x:.3f}          {y:.5f}")


#S09_6 Sea temperature statistics
#data are in the list called temp_mar sorted chronologically:
#temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
#We also have a second list with the name of the months:
#months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
#'November', 'December']
#Write a program that
#•	Define the above lists.
#•	Convert the temp mar list to a NumPy array.
#•	Determine, using the statistical functions of numpy, and write:
#o	The average sea surface temperature in 2014. (Approximate response: 17.9 ºC.)
#o	The month in which the sea surface has been coldest and its temperature. (Answer: 13.3 ºC, February.)
#o	The month in which the sea surface has been warmest and its temperature. (Answer: 22.3 ºC, August.)


import numpy as np

# Define the list
temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Convert the temp mar list to a NumPy array.
temp_mar_array = np.array(temp_mar)

# Calculate the average sea surface temperature in 2014

average_temp_2014 = np.mean(temp_mar_array[-12:])  # Last 12 months represent 2014
print(f"The average sea surface temperature in 2014 was approximately {average_temp_2014:.1f} ºC.")

# Find the coldest month and its temperature
coldest_month_index = np.argmin(temp_mar_array)
coldest_month = months[coldest_month_index]
coldest_temp = temp_mar_array[coldest_month_index]
print(f"The coldest month was {coldest_month} with a temperature of {coldest_temp:.1f} ºC.")

# Find the warmest month and its temperature
warmest_month_index = np.argmax(temp_mar_array)
warmest_month = months[warmest_month_index]
warmest_temp = temp_mar_array[warmest_month_index]
print(f"The warmest month was {warmest_month} with a temperature of {warmest_temp:.1f} ºC.")



#S09_10 Exam grades
#Make a program that asks for the number of students who have taken an exam and the marks (from 0 to 10)
# that they have obtained in the theory part and the problem part (in different lines), 
#which account 40% and a 60% respectively in the final grade. These notes must be saved in 2 vectors.
#The program:
#1.	Write a table with 4 columns containing the student's order index (0, 1, 2, ...), 
#theory note, problem mark and total mark.
#2.	You must also write the maximum total grade, the minimum total grade and the average total grade.
#3.	And finally you have to write the position (index) of the maximum total grade.



num_students = int(input("Enter the number of students who took the exam: "))


students = []

for i in range(num_students):
    theory = float(input(f"Enter the theory mark for student {i + 1} (0-10): "))
    problem = float(input(f"Enter the problem mark for student {i + 1} (0-10): "))
    total = 0.4 * theory + 0.6 * problem
    students.append((i, theory, problem, total))


max_total = max(students, key=lambda x: x[3])
min_total = min(students, key=lambda x: x[3])
average_total = sum(student[3] for student in students) / num_students

print("\nStudent       |      Theory Mark |     Problem Mark     |      Total Mark")
for student in students:
    print(f"{student[0]:>7}      | {student[1]:>11.2f}     |    {student[2]:>12.2f}      |     {student[3]:>10.2f}")


print(f"\nMaximum Total Grade: {max_total[3]:.2f} (Student {max_total[0] + 1})")
print(f"Minimum Total Grade: {min_total[3]:.2f} (Student {min_total[0] + 1})")
print(f"Average Total Grade: {average_total:.2f}")


