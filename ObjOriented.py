#task 1
import numpy as np

def attach_names(data, names):
    #maybe set up a for loop which goes through the two [] in the array
    #and make an output of name: (name), data: (data) using zip
    assert len(data) == len(names)
    output = []

    for patient_data, name in zip(data, names):
        output.append({'name': name, 'data': patient_data.tolist()})
    return output



data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])

output = attach_names(data, ['Alice', 'Bob'])
print(output)

#TASK 2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self): 
        return f'{self.title} by {self.author}'

book = Book('A Book', 'Me')
print(book)

#TASK 3
# file: inflammation/models.py

class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation

class Doctor(Person):
    "A doctor with a list of patients"
    def __init__(self,name):
        super().__init__(name)
        self.patients =[]

    #add a fn to allow them to add patients
    def add_patient(self, patient):
        #just want to append with the name
        self.patients.append(patient)

        return patient 


alice = Patient('Alice')
print(alice)

obs = alice.add_observation(3)
print(obs)

bob = Person('Bob')
print(bob)

#Task 4
...
class Person:
    """A person."""
    def __init__(self, name):
        self.name = name
        self.id = None

    def __str__(self):
        return self.name

    def set_id(self, id):
        raise NotImplementedError('set_id not implemented')

    def get_id(self):
        return self.id

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return 'Patient: ' + super().__str__()

    def set_id(self, id):
        self.id = 'P' + str(id).zfill(4)


class Doctor(Person):
    """A doctor in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return 'Doctor: ' + super().__str__()

    def set_id(self, id):
        self.id = 'D' + str(id).zfill(4)
...

class Trial:
    def __init__(self):
        #create empty array of people
        self.people = []

    def add_person(self, person):
        #adds a person to the room
        # check if they are of the person type using isinstance
        # check if they have the attribute get_id?
        if isinstance(person, Person):
            self.people.append(person)
        elif hasattr(person, "get_id"):
            person_id = person.get_id()
            #if id starts with D, make doctor and if P, patient?
            # and do i make their name their ID
            if person_id[0] == "D":
                person = Doctor(person_id)
            elif person_id[0] == "P":
                person = Patient(person_id)
            else:
                raise TypeError('could not recognise person ID')
            self.people.append(person)
        else:
            raise TypeError('person must be a Person or have attribute get_id')

    def print_people(self):
        #tell the caller who is in the room
        for person in self.people:
            print(person)

    def set_ids(self):
        for number, person in enumerate(self.people):
            person.set_id(number + 1) 
             

