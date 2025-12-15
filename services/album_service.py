from repositories.album_repository import AlbumRepository
from models.album_model import AlbumModel


class AlbumService:
    def __init__(self):
        self._repository = AlbumRepository()

    def get_all_albums(self):
        albums_raw = self._repository.get_all_albums()

        return [
            {
                "album_name": album["nmalbum"],
                "release": AlbumModel._format_date(album["dtrelease"]),
                "type": AlbumModel._get_album_type(album["fgtype"]),
                "band_name": album["nmband"],
            }
            for album in albums_raw
        ]
