from enums.album_fgtype_enum import AlbumType


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
