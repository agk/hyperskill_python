# students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]
student = [name for (name, grade) in students if grade == "A"]
print(student)