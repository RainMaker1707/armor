from datetime import datetime
from src.util import from_json_to_dict, from_xml_to_dict, iso_format_checker

class Threat():

    __ID = str()
    __name = str()
    __fullname = str()
    __add_date = str()
    __last_modified = str()
    __first_seen_date = str()
    __behavior = list()
    __type = str()
    __vector = list()
    __impact = list()
    __mitigation_ids = list()
    __CVE = str()


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


    def from_json(self, file):
        raw_data = from_json_to_dict(file)
        self.assign(raw_data)


    def from_xml(self, file):
        raw_data = from_xml_to_dict(file)
        self.assign(raw_data)


    def from_stix(file):
        pass


    def assign(self, dic):
        self.__ID = dic.get("ID")
        self.__name = dic.get("name")
        self.__fullname = dic.get("fullname")
        if not iso_format_checker(dic.get("first_seen")):
            return ValueError("ISO format date error in first_seen: excepted -> YYYY-MM-DD  has -> " + dic.get("first_seen"))
        self.__first_seen_date = dic.get("first_seen")
        if not iso_format_checker(dic.get("last_modified")):
            return ValueError("ISO format date error last_modified: excepted -> YYYY-MM-DD  has -> " + dic.get("last_modified"))
        self.__last_modified = dic.get("last_modified")
        self.__behavior = dic.get("behavior")
        self.__mitigation_ids = dic.get("mitigation_ids")
        # TODO: Type must be type object
        self.__type = dic.get("type")
        # TODO: Vector must be vector object
        self.__vector = dic.get("vector")
        self.__impact = dic.get("impact")
        self.__add_date = str(datetime.today()).split(" ")[0]
        self.__CVE = dic.get("CVE")


    def get_id(self):
        return self.__ID

    def get_add_date(self):
        return self.__add_date


    def get_first_date(self):
        return self.__first_seen_date
    

    def get_behavior(self):
        return self.__behavior


    def get_name(self):
        return self.__name
    

    def get_type(self):
        return self.__type
    

    def get_cve(self):
        return self.__CVE
    

    def get_vector(self):
        return  self.__vector
    

    def get_impact(self):
        return self.__impact
    

    def get_mitigations_ids(self):
        return self.__mitigation_ids


    def __str__(self):
        text = f'ID:            {self.__ID},\n'
        text += f'Name:          {self.__name},\n'
        text += f'FullName:      {self.__fullname},\n'
        text += f'First seen:    {self.__first_seen_date},\n'
        text += f'Last modified: {self.__last_modified}\n'
        text += f'Added date:    {self.__add_date},\n'
        text += f'Behavior:      {self.__behavior},\n'
        text += f'Type:          {self.__type},\n'
        text += f'Vector:        {self.__vector},\n'
        text += f'Impact:        {self.__impact},\n'
        text += f'Mitigation:    {self.__mitigation_ids},\n'
        text += f'CVE:           {self.__CVE}\n'
        return text