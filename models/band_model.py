from enums.band_fgstatus_enum import BandStatus
from repositories.band_repository import BandRepository


class BandModel:
    def get_band_genres(self, cdband):
        genres = BandRepository().get_band_genres(cdband)

        band_genres = ", ".join(genre["nmgenre"] for genre in genres)

        return band_genres

    def get_band_status(self, status):
        STATUS_MAPPING = {
            BandStatus.ACTIVE.value: "Active",
            BandStatus.SPLIT_UP.value: "Split up",
            BandStatus.CHANGED_NAME.value: "Changed name",
            BandStatus.UNKNOWN.value: "Unknown"
        }

        return STATUS_MAPPING.get(status, "Unknown")

    def get_all_bands(self):
        bands = BandRepository().get_all_bands()

        dictbands = []

        for band in bands:
            dictbands.append(
                {
                    "name": band["nmband"],
                    "country": band["nmcountry"],
                    "genre": self.get_band_genres(band["cdband"]),
                    "status": self.get_band_status(band["fgstatus"]),
                }
            )

        return dictbands
