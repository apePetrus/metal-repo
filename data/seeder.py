import yaml

class Seeder:
    def __init__(self) -> None:
        pass

    def _load_yaml_by_key(self, key: str):
        with open("data/seeder.yaml") as stream:
            try:
                return yaml.safe_load(stream)[key]
            except yaml.YAMLError as exc:
                return exc

    def yaml_test(self):
        print(self._load_yaml_by_key('genres')[0])
