import yaml

from data.seeder_repository import SeederRepository

class Seeder:
    def __init__(self) -> None:
        pass

    def _load_yaml_by_key(self, key: str):
        with open("data/seeder.yaml") as stream:
            try:
                return yaml.safe_load(stream)[key]
            except yaml.YAMLError as exc:
                raise exc

    def insert_genres(self):
        genres = self._load_yaml_by_key('genres')
        names = [genre["name"] for genre in genres]

        for name in names:
            SeederRepository().save_genre_ref(name)

    def yaml_test(self):
        pass
        # self.insert_genres()
