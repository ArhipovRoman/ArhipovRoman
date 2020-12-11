groupmates = [
	{"name": "Александр",
	 "surname": "Иванов",
	 "exams": ["Инф","Web","ЭЭиС"],
	 "marks": [4,3,5]
	 },
	{"name": "Иван",
	 "surname": "Петров",
	 "exams": ["История","АиГ","КТП"],
	 "marks": [4,4,4]
	 },
	{"name": "Кирилл",
	 "surname": "Смирнов",
	 "exams": ["Философия","ИС","КТП"],
	 "marks": [5,5,5]
	 },
	{"name": "Архипов",
	 "surname": "Роман",
	 "exams": ["Web","VR","BD"],
	 "marks": [5,4,4]
	 },
	{"name": "Максим",
	 "surname": "Елиневский",
	"exams": ["Web","VR","BD"],
	 "marks": [4,4,4]
	 }
	]
a = float(input())
def sort_by_mark(students):
    for student in students:
        b = sum(student["marks"])
        c = b/3
        if c >= a:
            print(student["name"],student["surname"],student["marks"])
sort_by_mark(groupmates)

