from contact import Contact, PhoneBook


if __name__ == '__main__':
    Jhon = Contact('Jhon', 'Smith', '+71234567809', favorites=False,  telegram='@jhony', email='jhony@smith.com')
    Gleb = Contact('Gleb', 'Sevostyanov', '+7979456949', 'test', favorites=True, telegram='@gleb')

    new_book = PhoneBook('new_book')

    new_book.add_contact(Gleb)
    new_book.add_contact(Jhon)
    new_book.show_contacts()
    new_book.delete_contact('+71234567809')
    new_book.show_contact_by_name('Gleb', 'Sevostyanov')
    new_book.show_favorites()
