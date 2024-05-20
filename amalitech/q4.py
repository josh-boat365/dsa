# Codewriting
# Given a list of student grades (a value between 1 to
# 5) records in the following format: "[name]: [grade]", find the student with the highest average grade. 
# It is guaranteed that all students have different average grades.
# Note: Names do not contain spaces, and each grade is an integer in the string.
# Note: You are not expected to provide the most optimal solution, but a solution with time complexity not 
# worse than 0(records. length*) will fit within the execution time limit.


def solution(records):
    from collections import defaultdict
    
    #dictionary to store total grades and count of grads for each student
    students_grades = defaultdict(lambda: [0,0])
    
    #parse each record and update the student's total grades and count
    for record in records:
        name, grade = record.split(': ')
        grade = int(grade)
        students_grades[name][0] += grade #sum of grades
        students_grades[name][1] += 1     # count of grades
        
    highest_avg_grade = -1
    top_student = ''
    
    #calculate average for each student and find the highest average
    for name, (total_grade, count) in students_grades.items():
        avg_grade = total_grade / count
        if avg_grade > highest_avg_grade:
            highest_avg_grade = avg_grade
            top_student = name
            
    return top_student

#example
records = [
    'Alice: 4', 'Josh: 8', 'Gyan: 7'
]

print(solution(records))