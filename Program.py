from Person import Person
import pickle
import time
import os

VERSION = 3.0
WIDTH = 117
UI = \
'''
----------------
Adress Book {VERSION}
----------------
1. show list
2. add contact
3. change [name]
4. delete [name]
5. search [name]
6. reset all contacts
7. exit
    '''.format(VERSION=VERSION)

UI_LIST = '''
----------------
How to show?
1. list
2. cards
3. don`t show
----------------
'''

TABLE_FORM = '| {:<30}| {:<18}| {:<10}| {:<15}| {:<15}| {:<12} \t|'
DIR_DB = 'data/'

#### Program ####
class Program(object):

    def __init__(self, pkl):
        self.data_pkl = DIR_DB + pkl
        self.data_dict = dict()

        self.logg = 'Last launch:\t' + time.strftime('%d.%m.%Y %H:%M:%S.\n')

        if not os.path.exists(DIR_DB):
            os.system('mkdir ' + DIR_DB)

        ### create new file pickle if it not exist
        if not os.path.exists(self.data_pkl):

            with open(self.data_pkl, 'wb') as pf:
                pickle.dump(self.data_dict, pf)

        ### ...or load exist pickle file
        else:
            with open(self.data_pkl, 'rb') as pf:
                self.data_dict = pickle.load(pf)
        ### ###

    ### show ###
    def show(self):
        if self.data_dict:
            while True:
                how_show = input(UI_LIST)
                if how_show.isdigit():
                    how_show = int(how_show)

                    # like list
                    if how_show == 1:
                        # header
                        print(TABLE_FORM.format('name','phone','adress', 'email', 'telegram', 'whatsapp'))
                        print('-' * WIDTH)

                        for cnt in self.data_dict.values():
                            a = tuple([x for x in cnt.__dict__.values()])
                            print(TABLE_FORM.format(*a))

                        print('-' * WIDTH)
                        break

                    # like cards
                    elif how_show == 2:
                        for cnt in self.data_dict.values():
                            print(cnt)
                        break

                    elif how_show == 3:
                        break
                    else:
                        print('Wrong choise! (only 1, 2 or 3)')

        else:
            print("Database './{}' is empty".format(self.data_pkl))

    ### add ###
    def add(self):
        print("Fill form please!")
        name = ''
        while name == '':
            name = input("Your Name: ")

        if not name in self.data_dict.keys():

            phone = str(input('Phone: '))
            adress = input('Adress: ')
            email = str(input('Email: '))
            telegram = input('Telegram: ')
            whatsapp = str(input('Whatsapp: '))

            self.data_dict.update({name : Person(
                name=name,
                phone=phone,
                adress=adress,
                email = email,
                telegram = telegram,
                whatsapp = whatsapp
            )})
        else:
            print('Contact with name: {} already exists!'.format(name))
            answer = input("Change this contacts? ('Y/n') ")
            if answer.lower() == 'y':
                self.change(name)


    ### ### ###

    def change(self, name):
        if name not in self.data_dict.keys():
            print("Contact with name: {} doesn`t exist in the database.".format(name))
        else:
            print('Change the contact data' , name)

            old_phone = self.data_dict[name].phone
            print("Old phone: {}".format(old_phone))
            phone = str(input("New phone: "))

            old_adress = self.data_dict[name].adress
            print("Old phone: {}".format(old_adress))
            adress = input("New adress: ")

            self.data_dict.update({name : Person(name=name,phone=phone, adress=adress)})

    ### delete ###
    def delete(self, *names):
        for name in names:

            if name not in self.data_dict.keys():
                print("Contact with name: {} doesn`t exist in the database.".format(name))
            else:
                print('Deleteable contact', name)
                self.data_dict.pop(name)
                print('Contact {} has been deleted!'.format(name), end='\n' + '-' * WIDTH + '\n')

    ### ### ###

    ### search ###
    def search(self, name):
        if name in self.data_dict.keys():
            print(self.data_dict[name])
        else:
            print("Contact with name: {} doesn`t exist in the database.".format(name))
    ### ### ###

    ### resset all ###
    def reset_all(self):
        self.data_dict = dict()
    ### ### ###

    def __del__(self):
        with open(self.data_pkl, 'wb') as pf:
            pickle.dump(self.data_dict, pf)
            print("Contacts database saved in './{}'".format(self.data_pkl))
            print('Goodbye!')

        # experiment: save like text
        self.logg += 'Stop programm:\t' + time.strftime('%d.%m.%Y %H:%M:%S.')

        with open(self.data_pkl + '.log', 'w') as f:
            f.write(self.logg)

