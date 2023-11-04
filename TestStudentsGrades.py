import unittest
import tkinter as tk
from ComputationalStudentsGrades import cal_percentage, grades, analyze_grades

class TestStudentsGrades(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.title("A Simple Computational Student Grades Program")

        self.total_scores_label = tk.Label(self.root, text="Total Marks:")
        self.total_scores_label.grid(row=0, column=0, padx=10, pady=10)
        self.total_scores_entry = tk.Entry(self.root)
        self.total_scores_entry.grid(row=0, column=1, padx=10, pady=10)

        self.first_name_entries = []
        self.last_name_entries = []
        self.scores_entries = []

        self.student_details_label = tk.Label(self.root, text="ENTER STUDENTS FIRSTNAME, LASTNAME AND THEIR SCORES")
        self.student_details_label.grid(row=1, columnspan=6, padx=10, pady=10)

        for i in range(15):
            first_name_label = tk.Label(self.root, text="First Name:")
            first_name_label.grid(row=i+1, column=0, padx=10, pady=5)
            first_name_entry = tk.Entry(self.root)
            first_name_entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.first_name_entries.append(first_name_entry)

            last_name_label = tk.Label(self.root, text="Last Name:")
            last_name_label.grid(row=i+1, column=2, padx=10, pady=5)
            last_name_entry = tk.Entry(self.root)
            last_name_entry.grid(row=i+1, column=3, padx=10, pady=5)
            self.last_name_entries.append(last_name_entry)

            scores_label = tk.Label(self.root, text="Scores:")
            scores_label.grid(row=i + 2, column=4, padx=10, pady=5)
            scores_entry = tk.Entry(self.root)
            scores_entry.grid(row=i + 2, column=5, padx=10, pady=5)
            self.scores_entries.append(scores_entry)

        self.display_result = tk.Text(self.root, height=12, width=60)
        self.display_result.grid(row=17, columnspan=6, padx=10, pady=10)

        self.button = tk.Button(self.root, text="Print Result", command=analyze_grades)
        self.button.grid(row=18, columnspan=6, padx=10, pady=10)

        self.root.mainloop()


    def test_cal_percentage(self):
        self.assertEqual(cal_percentage(100, 80), 80)
        self.assertEqual(cal_percentage(50, 25), 50)

    def test_grades(self):
        self.assertEqual(grades(91), 'A')
        self.assertEqual(grades(63), 'B')
        self.assertEqual(grades(57), 'C')
        self.assertEqual(grades(49), 'D')
        self.assertEqual(grades(25), 'Fail')

if __name__=='__main__':
    unittest.main()

