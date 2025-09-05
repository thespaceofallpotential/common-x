from sanitisation.sanitiser import Sanitiser


class SanitiserFactory:
    def build(self) -> Sanitiser | None:
        return Sanitiser()
