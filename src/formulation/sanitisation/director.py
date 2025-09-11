from typing import Dict

from formulation.sanitisation.sanitisation_types import SanitisationTypes


class Director:
    structured_sanitisation: Dict[SanitisationTypes, str]

    def __init__(self) -> None:
        self.structured_sanitisation = {}
