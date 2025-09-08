from typing import cast
from sanitisation.analyser import AnalyserType, IAnalyser
from sanitisation.character_analyser import CharacterAnalyser
from utils.custom_exception import CustomException


class AnalyserFactory:
    def build(self, analyser_type: AnalyserType) -> IAnalyser:
        match analyser_type.value:
            case 1:
                return cast(IAnalyser, CharacterAnalyser())

        raise CustomException(f"analyser factory: {type} not implemented error")
