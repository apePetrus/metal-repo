from repositories.band_repository import BandRepository
from models.band_model import BandModel


class BandService:
    def __init__(self) -> None:
        self._repository = BandRepository()

    def get_all_bands(self):
        bands_raw = self._repository.get_all_bands()

        return [BandModel(band).to_dict() for band in bands_raw]
