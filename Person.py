CARDS = '''
******************************
|
|    Name:\t{name}
|   Phone:\t{phone}
|  Adress:\t{adress}
|
******************************
'''

class Person(object):
    def __init__(self, name = 'no name', phone = None, adress = None):
        self.name = name
        self.phone = phone
        self.adress = adress

    def __str__(self):
        return CARDS.format(**self.__dict__)