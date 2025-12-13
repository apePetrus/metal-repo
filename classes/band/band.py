from enums.band_fgstatus_enum import BandStatus
from repositories.band_repository import BandRepository


class Band:
    def getBandGenres(self, cdband):
        genres = BandRepository().get_band_genres(cdband)

        band_genres = []
        for genre in genres:
            band_genres.append(genre["nmgenre"])

        genres_str = ", ".join(band_genres)

        return genres_str

    def getBandStatus(self, status):
        match status:
            case BandStatus.ACTIVE.value:
                return "Active"
            case BandStatus.SPLIT_UP.value:
                return "Split up"
            case BandStatus.CHANGED_NAME.value:
                return "Changed name"
            case BandStatus.UNKNOWN.value:
                return "Unknown"

    def getBands(self):
        bands = BandRepository().get_all_bands()

        dictbands = []

        for idx, band in enumerate(bands):
            dictbands.append({})
            dictbands[idx]["name"] = band["nmband"]
            dictbands[idx]["country"] = band["nmcountry"]
            dictbands[idx]["genre"] = self.getBandGenres(band["cdband"])
            dictbands[idx]["status"] = self.getBandStatus(band["fgstatus"])

        return dictbands
