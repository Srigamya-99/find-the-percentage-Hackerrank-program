if __name__ == '__main__':
    n = int(input())  # Number of students' records
    student_marks = {}  # Dictionary to store students' marks
    for _ in range(n):
        name, *line = input().split()  # Read name and marks for each student
        scores = list(map(float, line))  # Convert marks to floats
        student_marks[name] = scores  # Store marks in the dictionary

    query_name = input()  # Name of the student to query

    # Calculate the average marks for the queried student
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])

    # Print the average marks rounded to 2 decimal places
    print("{:.2f}".format(average_marks))
