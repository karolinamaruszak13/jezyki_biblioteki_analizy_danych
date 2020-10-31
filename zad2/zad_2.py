import numpy as np


class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = np.array(coefficients, dtype=np.float)

    def __add__(self, other):
        result = np.array(self.coefficients, dtype=np.float)
        result += other.coefficients
        return Polynomial(result)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        result = np.array(self.coefficients, dtype=np.float)
        result -= other.coefficients
        return Polynomial(result)

    def __rsub__(self, other):
        result = np.array(-self.coefficients, dtype=np.float)
        result -= other.coefficients
        return Polynomial(result)

    def __mul__(self, other):
        return Polynomial(other * self.coefficients)

    def __rmul__(self, other):
        return self * other

    def create_polynomial(self):
        if np.allclose(self.coefficients, 0):
            return False
        else:
            return np.poly1d(self.coefficients)

    def calculate_value(self, point):
        return np.polyval(self.coefficients, point)


##################################################################################################################################################################
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Student(Person):
    def __init__(self, name, surname, email, index_nb):
        self.email = email
        self.index_nb = index_nb
        self.grades = dict()
        super().__init__(name, surname)

    def send_email(self, message):
        return message

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        return self.grades

    def __str__(self):
        return "Dane studenta: {} {}, {}, ne indeksu: {}".format(self.name, self.surname, self.email, self.index_nb)


class Worker(Person):
    def __init__(self, name, surname, email, room_nb):
        self.room_nb = room_nb
        self.email = email
        super().__init__(name, surname)

    def send_email(self, message):
        return message

    def __str__(self):
        return "Dane pracownika: {} {}, {}, nr pokoju: {}".format(self.name, self.surname, self.email, self.room_nb)


class ScienceWorker(Worker):
    def __init__(self, name, surname, email, room_nb):
        self.publication_list = list()
        super().__init__(name, surname, email, room_nb)

    def add_to_publication_list(self, element):
        self.publication_list.append(element)
        return self.publication_list

    def __str__(self):
        return "Dane pracownika naukowego: {} {}, {}, nr pokoju: {}".format(self.name, self.surname, self.email,
                                                                            self.room_nb)


class DidacticWorker(Worker):
    def __init__(self, name, surname, email, room_nb, cons_hours):
        self.cons_hours = cons_hours
        self.subjects_list = list()
        super().__init__(name, surname, email, room_nb)

    def add_subjects(self, subject):
        self.subjects_list.append(subject)
        return self.subjects_list

    def __str__(self):
        return "Dane pracownika dydaktycznego: {} {}, {}, nr pokoju: {}, godz. konsultacji: {}".format(self.name,
                                                                                                       self.surname,
                                                                                                       self.email,
                                                                                                       self.room_nb,
                                                                                                       self.cons_hours)


#### Polynomial tests ####
f = Polynomial([1, 2, 3])
g = Polynomial([2, 1, 3])
c = Polynomial(0)

print(f.create_polynomial())
print(c.create_polynomial())
print(f.calculate_value(2))
print(f.create_polynomial() + g.create_polynomial())
print(f.create_polynomial() - g.create_polynomial())
print(f.create_polynomial() * g.create_polynomial())

### Student and Worker tests ###

# student = Student("Karolina", "Maruszak", "karolina@", 1145)
# print(student.add_grade("Analiza", 3))
# print(student.send_email("To jest email"))
# print(student)
#
# worker = Worker("Kasia", "Kowalska", "kasia@", 34)
# print(worker.send_email("Wiadomosc"))
# print(worker)
#
# science_worker = ScienceWorker("Janusz", "Heheszek", "januszek@", 15)
# print(science_worker)
# print(science_worker.add_to_publication_list("Publikacja3"))
#
# didactic_worker = DidacticWorker("Grażyna", "Kowalska", "grażynka@", 100, "10 - 12")
# print(didactic_worker)
# print(didactic_worker.subjects_list)
# print(didactic_worker.add_subjects("Python"))
