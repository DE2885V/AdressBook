from Program import Program, WIDTH, UI

DB = 'contacts.pkl'

def main():
    app = Program(DB)

    choise = ''
    while True:
        print(UI)
        choise = input('Choise (1 - 6): ')
        if choise.isdigit():
            choise = int(choise)
            print('-' * WIDTH)

            # show
            if choise == 1:
                app.show()

            # add
            elif choise == 2:
                app.add()

            # change
            elif choise == 3:
                changeable_name = input("Name for change: ")
                app.change(name=changeable_name)

            # delete
            elif choise == 4:
                deletable_name = tuple  (input(\
                    "Name for delete: (1 or more names)\n"
                    "example: 'Name2 Name2 Name3 ... ' "\
                    ).replace(',',' ').split())
                print('-' * WIDTH)

                app.delete(*deletable_name)

            # search
            elif choise == 5:
                searchable_name = input("Search: ")
                app.search(searchable_name)

            # reset all
            elif choise == 6:
                sure_reset = input("Are you sure you want reset all contacts? (Y/n): ")
                if sure_reset.lower() == 'y':
                    app.reset_all()
                    print('Done.')
                elif sure_reset.lower() == 'n':
                    print('Reset  canceled')
                else:
                    print('Wrong choise!')

            # exit
            elif choise == 7:
                answer = input("Are you sure? ('Y/n')")
                if answer.lower() == 'y':
                    break
        else:
            print("Wrong choise!!!")

if __name__ == '__main__':
    main()


