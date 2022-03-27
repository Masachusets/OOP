class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (self.finished_courses + self.courses_in_progress) \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        if self.grades:
            average_rating = sum(*self.grades.values()) / len(*self.grades.values())
            return f'Имя: {self.name} \n' \
                   f'Фамилия: {self.surname} \n' \
                   f'Средняя оценка за домашние задания: {average_rating: .{1}f} \n' \
                   f'Курсы в процессе изучения: {", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"} \n' \
                   f'Завершённые курсы: {", ".join(self.finished_courses) if self.finished_courses else "Нет"}'
        else:
            return f'Имя: {self.name} \n' \
                   f'Фамилия: {self.surname} \n' \
                   f'Средняя оценка за домашние задания: Нет оценок \n' \
                   f'Курсы в процессе изучения: {", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"} \n' \
                   f'Завершённые курсы: {", ".join(self.finished_courses) if self.finished_courses else "Нет"}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Кто-то не студент'
        elif self.grades and other.grades:
            self_average_rating = sum(*self.grades.values()) / len(*self.grades.values())
            other_average_rating = sum(*other.grades.values()) / len(*other.grades.values())
            return self_average_rating < other_average_rating
        else:
            return 'У одного или у обоих студентов нет оценок!'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        if self.grades:
            average_rating = sum(*self.grades.values()) / len(*self.grades.values())
            return f'Имя: {self.name} \n' \
                   f'Фамилия: {self.surname} \n' \
                   f'Средняя оценка за лекции: {average_rating: .{1}f}'
        else:
            return f'Имя: {self.name} \n' \
                   f'Фамилия: {self.surname} \n' \
                   f'Средняя оценка за лекции: Нет оценок'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Кто-то не лектор'
        elif self.grades and other.grades:
            self_average_rating = sum(*self.grades.values()) / len(*self.grades.values())
            other_average_rating = sum(*other.grades.values()) / len(*other.grades.values())
            return self_average_rating < other_average_rating
        else:
            return 'У одного или у обоих лекторов нет оценок!'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка')

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def average_students(students, course):
    all_rate = []
    for student in students:
        if not isinstance(student, Student):
            return f'{student.name} {student.surname} не студент'
        if course in student.grades:
            all_rate += student.grades[course]
    return f'Средняя оценка всех студентов за курс {course}: {sum(all_rate) / len(all_rate): .{1}f}' if all_rate \
        else f'В курсе {course} у студентов нет оценок'


def average_lecturers(lecturers, course):
    all_rate = []
    for lecturer in lecturers:
        if not isinstance(lecturer, Lecturer):
            return f'{lecturer.name} {lecturer.surname} не лектор'
        if course in lecturer.grades:
            all_rate += lecturer.grades[course]
    return f'Средняя оценка всех лекторов за курс {course}: {sum(all_rate) / len(all_rate): .{1}f}' if all_rate \
        else f'В курсе {course} у лекторов нет оценок'


first_student = Student('Leroy', 'Jankins', 'male')
first_student.courses_in_progress += ['Python', 'Git']

second_student = Student('Sylvanas', 'Windrunner', 'female')
second_student.courses_in_progress += ['Python']
second_student.add_courses('Git')

first_lecturer = Lecturer('Johnny', 'Cage')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Liu', 'Kang')
second_lecturer.courses_attached += ['Git']

first_reviewer = Reviewer('Shang', 'Tsung')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Shao', 'Kahn')
second_reviewer.courses_attached += ['Git']

first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_student.add_courses('Введение в программирование')
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 9)
first_student.rate_lecturer(first_lecturer, 'Python', 10)

# print(first_student > second_student)
# print(first_lecturer > second_lecturer)

first_reviewer.rate_hw(second_student, 'Python', 6)
first_reviewer.rate_hw(second_student, 'Python', 7)
first_reviewer.rate_hw(second_student, 'Python', 9)

second_student.rate_lecturer(second_lecturer, 'Git', 9)
second_student.rate_lecturer(second_lecturer, 'Git', 8)
second_student.rate_lecturer(second_lecturer, 'Git', 9)

print(first_student)
print(second_student)

print(first_lecturer)
print(second_lecturer)

print(first_reviewer)
print(second_reviewer)

print(first_student > second_student)
print(first_lecturer < second_lecturer)

print(average_students([first_student, second_student], 'Python'))
print(average_lecturers([first_lecturer, second_lecturer], 'Git'))
