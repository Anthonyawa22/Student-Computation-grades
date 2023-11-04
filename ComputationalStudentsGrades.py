import tkinter as tk

# this is the function that calculate the percentage of students total scores over obtained each student score

def cal_percentage(total_scores, obtained_scores):
    return(obtained_scores/total_scores) * 100

# this function assign grades to students based on the percentage obtained
def grades(percentage):
    if percentage > 70:
        return 'A'
    elif percentage > 60:
        return 'B'
    elif percentage > 50:
        return 'C'
    elif percentage > 45:
        return 'D'
    else:
        return 'Fail'

# this function  perform the action of the Analyze button on the GUI frame

def analyze_grades():
    students = []
    total_scores = int(total_scores_entry.get())

# this get a loop  values inputted from each students and analyse the percentage and grades
    for i in range(15):
        first_name = first_name_entries[i].get()
        last_name = last_name_entries[i].get()
        scores = int(scores_entries[i].get())
        percentage = cal_percentage(total_scores, scores)
        grade = grades(percentage)
        students.append({'first_name': first_name, 'last_name': last_name, 'scores': scores, 'percentage': percentage, 'grade': grade})

# a code that sort grades based on percentage in a descending manner
    students.sort(key=lambda x: x['percentage'], reverse=True)
    
# the code below display the results of the inputted value on a text box created on GUI
    display_result.delete('1.0', tk.END)
    for i, student in enumerate(students):
        display_result.insert(tk.END, "{}. {} {}: Percentage = {:.2f}%, Grade = {}\n".format(i+1, student['first_name'][0], student['last_name'][0], student['percentage'], student['grade']))

#this code compute and display total numbers of As,Bs,Cs,Ds, and fail gotten by the students
    grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'Fail': 0}
    for student in students:
        grade_count[student['grade']] += 1

    display_result.insert(tk.END, "\nTotal Grades breakdown:\n")
    for grade, count in grade_count.items():
        display_result.insert(tk.END, "{}s: {}\n".format(grade, count))

# Create GUI main window frame
root = tk.Tk()
root.title("A Simple Computational Student Grades Program")

# Create labels and entries for total scores, 3 loops of student names, and scores
total_scores_label = tk.Label(root, text="Total Marks:")
total_scores_label.grid(row=0, column=0, padx=10, pady=10)
total_scores_entry = tk.Entry(root)
total_scores_entry.grid(row=0, column=1, padx=10, pady=10)

first_name_entries = []
last_name_entries = []
scores_entries = []

student_details_label = tk.Label(root, text="ENTER STUDENTS FIRSTNAME, LASTNAME AND THEIR SCORES")
student_details_label.grid(row=1, columnspan=6, padx=10, pady=10)


# this create label of firstname,lastname and scores inputted for each student
for i in range(15):
    first_name_label = tk.Label(root, text="First Name: ")
    first_name_label.grid(row=i+2, column=0, padx=10, pady=5)
    first_name_entry = tk.Entry(root)
    first_name_entry.grid(row=i+2, column=1, padx=10, pady=5)
    first_name_entries.append(first_name_entry)

    last_name_label = tk.Label(root, text="Last Name: ")
    last_name_label.grid(row=i+2, column=2, padx=10, pady=5)
    last_name_entry = tk.Entry(root)
    last_name_entry.grid(row=i+2, column=3, padx=10, pady=5)
    last_name_entries.append(last_name_entry)

    scores_label = tk.Label(root, text="Scores:")
    scores_label.grid(row=i+2, column=4, padx=10, pady=5)
    scores_entry = tk.Entry(root)
    scores_entry.grid(row=i+2, column=5, padx=10, pady=5)
    scores_entries.append(scores_entry)

# this create a text box that display the result after analyses of the inputted value.
display_result = tk.Text(root, height=12, width=60)
display_result.grid(row=17, columnspan=6, padx=10, pady=10)

# create a button to print out result
button = tk.Button(root, text="Print Result", command=analyze_grades)
button.grid(row=18, columnspan=6, padx=10, pady=10)

# Run the tkinter loop
root.mainloop()


