class Person(object):
    first_name = ""
    last_name =""
    birth_date = ""
    address = ""
    email = ""
    phone_number = ""

    def __init__(self, first_name, last_name, birth_date, address, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address
        self.email = email
        self.phone_number = phone_number

    def get_full_name(self):
        return self.first_name + " " + self.last_name