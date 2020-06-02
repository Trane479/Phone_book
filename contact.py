class PhoneBook:
    def __init__(self, name, contacts=[]):
        self.name = name
        self.contacts = contacts

    def show_contacts(self):
        for contact in self.contacts:
            print(contact)

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, number):
        for contact in self.contacts:
            if contact.phone_number == number:
                self.contacts.remove(contact)
                print(f'Контакт {contact.name} {contact.surname} удален')

    def show_favorites(self):
        print('Контакты в избранном:')
        for contact in self.contacts:
            if contact.favorites == 'да':
                print(contact)

    def show_contact_by_name(self, name, surname):
        for contact in self.contacts:
            if contact.name == name and contact.surname == surname:
                print(contact)




class Contact:
    def __init__(self, name, surname, phone_number,  *args, favorites=False, **kwargs, ):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        if favorites == 1:
            self.favorites = 'да'
        else:
            self.favorites = 'нет'
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        ad_info = []
        ad_info_dict ={}
        if len(self.args) > 0:
            for args in self.args:
                ad_info.append(args)
        if len(self.kwargs) > 0:
            for key, value in self.kwargs.items():
                ad_info_dict.setdefault(key, value)
        additional_info = ''
        for item in ad_info:
            additional_info += item + '\n'
        for key, value in ad_info_dict.items():
            additional_info += key + ' - ' + value + '\n'
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Телефон: {self.phone_number}\n' \
               f'В избранных: {self.favorites}\n' \
               f'Дополнительная информация: \n{additional_info}'


