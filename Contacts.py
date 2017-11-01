from Person import Person
                                    # Kako dodane, spremenjene ali izbrisane podatke shranim in kam? ... 
                                    # da se program ob zagonu ne zacne znova, temvec tam, ker se je urejanje koncalo? Odgovor na to 
                                    # vprasanje ze imam in je vključen v kodo.. me pa zanima, zakaj se pri shranjevanju pojavi razmak  
class Contacts(object):             # med vrsticami v txt.file? .. ta razmak pri edit contact in delete contact izgine.....
    contact_book = []

    def __init__(self, contact_book):
        self.contact_book = contact_book


    def output_contacts(self):
        for index, person in enumerate(self.contact_book, start = 1):
            print "ID number: " + str(index) + "."
            print "First name: " + person.first_name
            print "Last name: " + person.last_name
            print "Birth date: " + person.birth_date
            print "Address: " + person.address
            print "Email: " + person.email
            print "Phone number: " + person.phone_number
            print ""

        if not self.contact_book:
            print "Your contact book is empty."

    def add_new_contact(self):
        first_name = raw_input("Enter first name: ")
        last_name = raw_input("Enter last name: ")
        birth_date = raw_input("Enter date of birth (dd.mm.yyyy): ")
        address = raw_input("Enter address: ")
        email = raw_input("Enter email: ")
        phone_number = raw_input("Enter phone number: ")

        new_contact = Person(first_name=first_name, last_name=last_name, birth_date=birth_date, address=address,email=email, phone_number=phone_number)
        self.contact_book.append(new_contact)

        print ""
        print "New contact " + new_contact.get_full_name() + " was successfully added to your contact book."
        print ""

    def edit_contacts(self):
        print "Select ID number of person you would like to edit."
        print ""
        for index, person in enumerate(self.contact_book, start=1):
            print str(index) + " " + person.get_full_name()

        print ""
        select_ID = int(raw_input("Enter ID number of person you would like to edit: "))
        selected_contact = self.contact_book[select_ID - 1]

        print ""
        print("You are editing %s: " % selected_contact.get_full_name())
        print ""

        edit_first_name = raw_input("Edit first name: ")    # tu bi zelela, da se vse moznosti za edit pokazejo naenkrat in bi se spreminjale samo tiste, ki bi jih zelel...
        selected_contact.first_name = edit_first_name       # npr. ime bi se prikazalo kot placeholder, ki ga spremenis, ce zelis, ce ne ostane isto... enako naprej za spodnje podatke..
                                                            # da ni treba vedno znova vnasati vse podatke... naredim to z def in if / else ali obstaja krajsa moznost?
        edit_last_name = raw_input("Edit last name: ")
        selected_contact.last_name = edit_last_name

        edit_birth_date = raw_input("Edit birth date: ")
        selected_contact.birth_date = edit_birth_date

        edit_address = raw_input("Edit address: ")
        selected_contact.address = edit_address

        edit_email = raw_input("Edit email: ")
        selected_contact.email = edit_email

        edit_phone_number = raw_input("Edit phone number: ")
        selected_contact.phone_number = edit_phone_number

    def delete_contact(self):
        print "Select ID number of person you would like to delete."
        for index, person in enumerate(self.contact_book, start=1):
            print str(index) + " " + person.get_full_name()

        print ""
        select_ID_to_delete = int(raw_input("Enter ID number of person you would like to delete: "))
        selected_contact_to_delete = self.contact_book[select_ID_to_delete - 1]

        print ""
        print "Your contact " + selected_contact_to_delete.get_full_name() + " was seccessully deleted."
        print ""

        self.contact_book.pop(select_ID_to_delete - 1)

    def save_to_disk(self):
        with open("contacts.txt", "w+") as conct_file:
            for contact in self.contact_book:
                conct_file.write("%s,%s,%s,%s,%s,%s\n" % (contact.first_name, contact.last_name, contact.birth_date, contact.address, contact.email, contact.phone_number))

