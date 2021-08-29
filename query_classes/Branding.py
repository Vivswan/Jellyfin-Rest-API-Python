from data_classes.branding_options import BrandingOptions as BrandingOptions
from util.BaseRequestClass import BaseRequestClass


class Branding(BaseRequestClass):
    def get_branding_options(
            self
    ) -> BrandingOptions:
        """Gets branding configuration.

        Http:
            <get>: /Branding/Configuration

        Returns:
            <200> BrandingOptions: Branding configuration returned.
        """
        return self._get(path='/Branding/Configuration', response_type=BrandingOptions)

    def get_branding_css(
            self
    ) -> str:
        """Gets branding css.

        Http:
            <get>: /Branding/Css

        Returns:
            <200> str: Branding css returned.
            <204> str: No branding css configured.
        """
        return self._get(path='/Branding/Css', response_type=str)

    def get_branding_css_2(
            self
    ) -> str:
        """Gets branding css.

        Http:
            <get>: /Branding/Css.css

        Returns:
            <200> str: Branding css returned.
            <204> str: No branding css configured.
        """
        return self._get(path='/Branding/Css.css', response_type=str)

