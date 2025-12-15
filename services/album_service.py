from repositories.album_repository import AlbumRepository
from utils.date_utils import format_epoch_to_str
from models.album_model import AlbumModel


class AlbumService:
    def __init__(self):
        self._repository = AlbumRepository()

    def get_all_albums(self):
        albums_raw = self._repository.get_all_albums()

        return [
            {
                "album_name": album["nmalbum"],
                "release": format_epoch_to_str(album["dtrelease"]),
                "type": AlbumModel._get_album_type(album["fgtype"]),
                "band_name": album["nmband"],
            }
            for album in albums_raw
        ]
