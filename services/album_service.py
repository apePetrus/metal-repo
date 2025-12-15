from repositories.album_repository import AlbumRepository
from models.album_model import AlbumModel


class AlbumService:
    def __init__(self):
        self._repository = AlbumRepository()

    def get_all_albums(self):
        albums_raw = self._repository.get_all_albums()

        return [AlbumModel(album).to_dict() for album in albums_raw]
