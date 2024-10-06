'''def user_inputfordict(number):
	students_list=[]
	for i in range(1, number+1):
		data=dict()
		print("_"*25)
		print(f"Enter {i} Student data")
		data['name']=input("Enter Your Name: ")
		scores={
			'PP':float(input("Enter Your PP Marks: ")),
			'DS':float(input("Enter Your DS marks: ")),
			'DBMS':float(input("Enter Your DBMS marks: "))
			}
		data['subjects']=scores
		students_list.append(data)
		number-=1
		
	return students_list
	
print(user_inputfordict(2))
		
		
		'''
		
		
		def user_inputfordict(num_students):
    """Collects student information."""
    students_list = []
    for _ in range(num_students):
        name = input("Enter your name: ")
        scores = {
            'PP': float(input("Enter your PP Marks: ")),
            'DS': float(input("Enter your DS Marks: ")),
            'DBMS': float(input("Enter your DBMS Marks: "))
        }
        students_list.append({"name": name, "subjects": scores})
    return students_list

def calculate_subject_averages(students_list):
    """Calculates subject-wise averages."""
    total_students = len(students_list)
    pp_total, ds_total, dbms_total = 0, 0, 0  # Totals for each subject

    for student in students_list:
        pp_total += student["subjects"]["PP"]
        ds_total += student["subjects"]["DS"]
        dbms_total += student["subjects"]["DBMS"]

    # Calculate averages
    pp_avg = pp_total / total_students
    ds_avg = ds_total / total_students
    dbms_avg = dbms_total / total_students

    return {"PP": pp_avg, "DS": ds_avg, "DBMS": dbms_avg}

def get_topper(students_list):
    """Finds the student with the highest average score across all subjects."""
    toppers = []
    highest_average = 0

    for student in students_list:
        # Calculate average score for the student
        subjects = student["subjects"]
        average_score = sum(subjects.values()) / len(subjects)

        # Update the highest average and toppers list
        if average_score > highest_average:
            highest_average = average_score
            toppers = [student["name"]]  # Reset toppers list
        elif average_score == highest_average:
            toppers.append(student["name"])  # Add to toppers list

    return toppers, highest_average

def main():
    """Main function to handle the flow."""
    num_students = int(input("Enter the number of students (e.g., 20): "))
    students_list = user_inputfordict(num_students)

    # Calculate subject-wise averages
    subject_averages = calculate_subject_averages(students_list)
    print("\nSubject-wise Average Marks:")
    for subject, avg in subject_averages.items():
        print(f"{subject}: {avg:.2f}")

    # Find the topper(s)
    toppers, highest_avg = get_topper(students_list)
    print("\nTopper(s):")
    print(", ".join(toppers))
    print(f"Highest Average Score: {highest_avg:.2f}")

# Run the program
if __name__ == "__main__":
    main()

