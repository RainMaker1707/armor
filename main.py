from argparse import ArgumentParser
from os import listdir

from src.threat.threat import Threat
from src.mitigation.mitigation import Mitigation


t_json_path = "data/threats/JSON/"
m_json_path = "data/mitigation/JSON/"


def create_threat_dict(files):
    threats = dict()
    for file in files:
        threat = Threat()
        threat.from_json(t_json_path+file)
        threats[threat.get_id()] = threat
    return threats


def create_mitigations_dict(files):
    mitigations = dict()
    for file in files:
        mitigation = Mitigation()
        mitigation.from_json(m_json_path+file)
        if mitigations.get(mitigation.get_id()):
            print(f'{mitigation.get_id()} ID is aready taken by: {mitigations.get(mitigation.get_id())}')
        else:
            mitigations[mitigation.get_id()] = mitigation
    return mitigations


if __name__ == "__main__":
    parser = ArgumentParser()
    args = parser.parse_args()

    t_json_list = list(filter(lambda e: e!="template.json" ,listdir(t_json_path)))
    m_json_list = list(filter(lambda e: e!="template.json" ,listdir(m_json_path)))

    threats = create_threat_dict(t_json_list)
    mitigations = create_mitigations_dict(m_json_list)
    
    for key in threats:
        print(threats.get(key))
        print("\n")
        for m in threats.get(key).get_mitigations_ids():
            if isinstance(m, int):
                print(mitigations.get(m))