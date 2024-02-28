from src.util import from_json_to_dict, from_xml_to_dict, iso_format_checker

class Mitigation:

    __ID = str()
    __name = str()
    __fullname = str()
    __type = str() # network / software / hardware
    __related_threat = list()
    __add_date = str()
    __last_modification = str()
    __object = dict() # oject explaining the mitigation technique
    

    def __init__(self):
        pass


    def from_scratch(self):
        pass


    def from_json(self, file):
        data = from_json_to_dict(file)
        self.__ID = data.get("ID")
        self.__name = data.get("name")
        self.__fullname = data.get("fullname")
        self.__type = data.get("type")
        self.__related_threat = data.get("related_threat")
        if not iso_format_checker(data.get("add_date")):
            return ValueError("ISO format date error in add_date: excepted -> YYYY-MM-DD  has -> " + data.get("add_date"))
        self.__add_date = data.get("add_date")
        if not iso_format_checker(data.get("last_modification")):
            return ValueError("ISO format date error in last_modification: excepted -> YYYY-MM-DD  has -> " + data.get("last_modification"))
        self.__last_modification = data.get("last_modification")
        self.__object = data.get("object")


    def from_xml(file):
        data = from_xml_to_dict(file)
        pass


    def get_id(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_fullname(self):
        return self.__fullname

    def get_type(self):
        return self.__type
    
    def get_related_threat(self):
        return self.__related_threat
    
    def get_add_date(self):
        return  self.__add_date
    
    def get_last_modification(self):
        return self.__last_modification
    
    def get_object(self):
        return self.__object


    def __str__(self):
        text = f'ID:                {self.__ID},\n'
        text += f'Name:              {self.__name},\n'
        text += f'FullName:          {self.__fullname},\n'
        text += f'Add date:          {self.__add_date},\n'
        text += f'Last modified:     {self.__last_modification}\n'
        text += f'Type:              {self.__type},\n'
        text += f'Related Threat:    {self.__related_threat},\n'
        text += f'Object:            {self.__object}\n'
        return text