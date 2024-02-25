from datetime import datetime

class Threat():

    __name = str()
    __add_date = str()
    __first_seen_date = str()
    __behavior = str()


    def __init__(self):
        pass


    def from_scratch(self, name, behavior, first_seen_date=None):
        self.__name = name
        self.__behavior = behavior
        self.__add_date = str(datetime.today()).split(" ")[0] # keep only date of the day
        if(first_seen_date is None):
            self.__first_seen_date = self.__add_date
        else:
            # TODO: check if date  is correctly ISO formatted
            self.__first_seen_date= first_seen_date


    def from_json(file):
        pass


    def from_xml(file):
        pass


    def get_add_date(self):
        return self.__add_date
    
    def get_first_date(self):
        return self.__first_seen_date