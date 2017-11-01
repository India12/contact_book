from Person import Person
from Contacts import Contacts


def main():
    person1 = Person(first_name = "Tanja", last_name = "Fink", birth_date = "01.02.1973", address = "Kersnikova 4, 1000 Ljubljana", email = "tanja.fink@gmail.com", phone_number = "030 222 333")
    person2 = Person(first_name = "Mateja", last_name = "Kuznar", birth_date = "06.12.1999", address = "Brezovnik 11, 2000 Maribor", email = "mateja.kuznar@gmail.com", phone_number = "051 555 666")
    person3 = Person(first_name = "Toni", last_name = "Potocnik", birth_date = "23.10.1980", address = "Krajnceva ulica 9, 1000 Ljubljana", email = "toni.potocnik@gmail.com", phone_number = "040 111 444")
    person4 = Person(first_name = "Marko", last_name = "Makovec", birth_date = "08.09.1985", address = "Gornji dol 15 a, 3000 Celje", email = "marko.makovec@gmail.com", phone_number = "031 444 888")
    person5 = Person(first_name = "Sanja", last_name = "Lah", birth_date = "17.05.1983", address = "Ravnik 6, 1236 Trzin", email = "sanja.lah@gmail.com", phone_number = "030 999 777")

    contact_book = [person1, person2, person3, person4, person5]

    manager = Contacts(contact_book)

    with open("contacts.txt","r") as c_file:
        for line in c_file:
            try:
                first_name, last_name, birth_date, address, email, phone_number = line.split(",")
                contact = Person(first_name=first_name, last_name=last_name, birth_date=birth_date, address=address,email=email, phone_number=phone_number)
                contact_book.append(contact)
            except ValueError:
                continue

    while True:
        print "Choose: (1 - 5):"
        print ""
        print "1. Contacts"
        print "2. Add new contact"
        print "3. Edit contacts"
        print "4. Delete contacts"
        print "5. Save changes"
        print "6. Close"
        print ""

        choice = raw_input("Enter your choice: ")

        print ""

        if choice == "1":
            manager.output_contacts()
        elif choice == "2":
            manager.add_new_contact()
        elif choice == "3":
            manager.edit_contacts()
        elif choice == "4":
            manager.delete_contact()
        elif choice == "5":
            manager.save_to_disk()
        elif choice == "6":
            print "Closing program ..."
            break
        else:
            print ("Enter one of the presented options: ")
            print ""


if __name__ == "__main__":
    main()
