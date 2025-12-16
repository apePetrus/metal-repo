from enums.band_fgstatus_enum import BandStatus
from repositories.band_repository import BandRepository


class BandModel:
    def __init__(self, data) -> None:
        self.cdband = data["cdband"]
        self.nmband = data["nmband"]
        self.nmcountry = data["nmcountry"]
        self.fgstatus = data["fgstatus"]

    @staticmethod
    def _get_band_genres(cdband):
        genres = BandRepository().get_band_genres(cdband)

        band_genres = ", ".join(genre["nmgenre"] for genre in genres)

        return band_genres

    @staticmethod
    def _get_band_status(status):
        STATUS_MAPPING = {
            BandStatus.ACTIVE.value: "Active",
            BandStatus.SPLIT_UP.value: "Split up",
            BandStatus.CHANGED_NAME.value: "Changed name",
            BandStatus.UNKNOWN.value: "Unknown"
        }

        return STATUS_MAPPING.get(status, "Unknown")

    @property
    def band_genre(self):
        return BandModel._get_band_genres(self.cdband)

    @property
    def band_status(self):
        return BandModel._get_band_status(self.fgstatus)

    def to_dict(self):
        return {
            "name": self.nmband,
            "country": self.nmcountry,
            "genre": self.band_genre,
            "status": self.band_status
        }
