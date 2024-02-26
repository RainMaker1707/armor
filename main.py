from argparse import ArgumentParser
from os import listdir

from src.threat.threat import Threat
from src.mitigation.mitigation import Mitigation
from src.util import iso_format_checker


if __name__ == "__main__":
    parser = ArgumentParser()
    args = parser.parse_args()

    json_path = "data/JSON/"
    json_list = list(filter(lambda e: e!="template.json" ,listdir(json_path)))

    xml_path = "data/XML"
    xml_list = list(filter(lambda e: e!="template.xml" ,listdir(xml_path)))

    threats = list()
    for file in json_list:
        threat = Threat()
        threat.from_json(json_path+file)
        threats.append(threat)

    for file in xml_list:
        threat = Threat()
        threat.from_json(xml_path+file)
        threats.append(threat)

    for t in threats:
        print(t)