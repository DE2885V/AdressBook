CARD = '''
******************************************
|                                         |
|     Name:\t{name:<30}|
|    Phone:\t{phone:<30}|
|   Adress:\t{adress:<30}|
|   E-mail:\t{email:<30}|
| Telegram:\t{telegram:<30}|
| Whatsapp:\t{whatsapp:<30}|
|                                         |
******************************************
'''

class Person(object):

    def __init__(self, **kwargs):
        self.name       = '-'
        self.phone      = '-'
        self.adress     = '-'
        self.email      = '-'
        self.telegram   = '-'
        self.whatsapp   = '-'

        self.__dict__.update(**kwargs)

    def __str__(self):
        return CARD.format(**self.__dict__)