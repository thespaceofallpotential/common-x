from formulation.sanitisation.common import ISanitiser, SanitiserOptions
from formulation.sanitisation.sanitiser import Sanitiser
from formulation.sanitisation.elemental_curator import ElementalCurator


class SanitiserFactory:
    def build(self, curator: ElementalCurator, options: SanitiserOptions) -> ISanitiser:
        return Sanitiser(curator, options)


def build_sanitiser(curator: ElementalCurator, options: SanitiserOptions):
    sanitiser_factory = SanitiserFactory()

    sanitiser = sanitiser_factory.build(curator, options)

    return sanitiser
