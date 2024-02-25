from datetime import datetime
import json

class Threat():

    __ID = str()
    __name = str()
    __fullname = str()
    __add_date = str()
    __first_seen_date = str()
    __behavior = list()
    __type = str()
    __vector = list()
    __impact = list()
    __mitigation_ids = list()


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


    def from_json(self, raw_file):
        raw_data = dict()
        with open(raw_file, 'r') as file:
            raw_data = json.load(file)
        self.__ID = raw_data["ID"]
        self.__name = raw_data["name"]
        self.__fullname = raw_data["fullname"]
        self.__first_seen_date = raw_data["first_seen"]
        self.__behavior = raw_data["behavior"]
        self.__mitigation_ids = raw_data["mitigation_ids"]
        self.__type = raw_data["type"]
        self.__vector = raw_data["vector"]
        self.__impact = raw_data["impact"]
        self.__add_date = str(datetime.today()).split(" ")[0]



    def from_xml(self, file):
        pass


    def get_add_date(self):
        return self.__add_date
    
    def get_first_date(self):
        return self.__first_seen_date
    
    def __str__(self):
        text = f'ID:          {self.__ID},\n'
        text += f'Name:        {self.__name},\n'
        text += f'FullName:    {self.__fullname},\n'
        text += f'First seen:  {self.__first_seen_date},\n'
        text += f'Added date:  {self.__add_date},\n'
        text += f'Behavior:    {self.__behavior},\n'
        text += f'Type:        {self.__type},\n'
        text += f'Vector:      {self.__vector},\n'
        text += f'Impact:      {self.__impact},\n'
        text += f'Mitigation:  {self.__mitigation_ids},\n'
        return text