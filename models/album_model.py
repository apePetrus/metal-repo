from datetime import datetime
from enums.album_fgtype_enum import AlbumType
from repositories.album_repository import AlbumRepository


class AlbumModel:
    def get_album_type(self, type):
        TYPE_MAPPING = {
            AlbumType.FULL_LENGTH.value: "Full length",
            AlbumType.EP.value: "EP",
            AlbumType.SINGLE.value: "Single",
            AlbumType.DEMO.value: "Demo",
            AlbumType.LIVE.value: "Live",
            AlbumType.COMPILATION.value: "Compilation",
            AlbumType.BOXED_SET.value: "Boxed set",
            AlbumType.VIDEO.value: "Video",
            AlbumType.UNKNOWN.value: "Unknown",
        }

        return TYPE_MAPPING.get(type, "Unknown")

    def _format_date(self, date):
        return datetime.fromtimestamp(date).strftime("%Y-%m-%d")

    def get_all_albums(self):
        albums = AlbumRepository().get_all_albums()

        return [
            {
                "album_name": album["nmalbum"],
                "release": self._format_date(album["dtrelease"]),
                "type": self.get_album_type(album["fgtype"]),
                "band_name": album["nmband"],
            } for album in albums
        ]
