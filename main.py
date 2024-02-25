from argparse import ArgumentParser
from src.threat import Threat
from src.mitigation import Mitigation


if __name__ == "__main__":
    parser = ArgumentParser()
    args = parser.parse_args()

    test = Threat()
    test.from_scratch(name="test", behavior="test")
    print(test.get_add_date())