from util.BaseRequestClass import BaseRequestClass
from typing import List
from data_classes.parental_rating import ParentalRating as ParentalRating
from data_classes.localization_option import LocalizationOption as LocalizationOption
from data_classes.culture_dto import CultureDto as CultureDto
from data_classes.country_info import CountryInfo as CountryInfo


class Localization(BaseRequestClass):
    def get_countries(
            self
    ) -> List[CountryInfo]:
        """Gets known countries.

        Http:
            <get>: /Localization/Countries

        Returns:
            <200> List[CountryInfo]: Known countries returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Localization/Countries', response_type=List[CountryInfo])

    def get_cultures(
            self
    ) -> List[CultureDto]:
        """Gets known cultures.

        Http:
            <get>: /Localization/Cultures

        Returns:
            <200> List[CultureDto]: Known cultures returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Localization/Cultures', response_type=List[CultureDto])

    def get_localization_options(
            self
    ) -> List[LocalizationOption]:
        """Gets localization options.

        Http:
            <get>: /Localization/Options

        Returns:
            <200> List[LocalizationOption]: Localization options returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Localization/Options', response_type=List[LocalizationOption])

    def get_parental_ratings(
            self
    ) -> List[ParentalRating]:
        """Gets known parental ratings.

        Http:
            <get>: /Localization/ParentalRatings

        Returns:
            <200> List[ParentalRating]: Known parental ratings returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Localization/ParentalRatings', response_type=List[ParentalRating])

