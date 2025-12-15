from enums.album_fgtype_enum import AlbumType
from utils.date_utils import format_epoch_to_str


class AlbumModel:
    def __init__(self, data):
        self.cdalbum = data["cdalbum"]
        self.nmalbum = data["nmalbum"]
        self.dtrelease = data["dtrelease"]
        self.fgtype = data["fgtype"]
        self.nmband = data["nmband"]

    @staticmethod
    def _get_album_type(type):
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

    @property
    def release_date(self):
        return format_epoch_to_str(self.dtrelease)

    @property
    def type_description(self):
        return AlbumModel._get_album_type(self.fgtype)

    def to_dict(self):
        return {
            "album_name": self.nmalbum,
            "release": self.release_date,
            "type": self.type_description,
            "band_name": self.nmband
        }
