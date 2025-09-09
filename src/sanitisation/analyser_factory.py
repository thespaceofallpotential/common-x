from typing import cast
from sanitisation.analyser import AnalyserType, IAnalyser
from sanitisation.character_analyser import CharacterAnalyser
from sanitisation.length_analyser import LengthAnalyser
from utils.custom_exception import CustomException


class AnalyserFactory:
    def build(self, analyser_type: AnalyserType) -> IAnalyser:
        match analyser_type.value:
            case 1: #AnalyserType.LENGTH
                return cast(IAnalyser, LengthAnalyser())
            case 2: #AnalyserType.CHARACTER
                return cast(IAnalyser, CharacterAnalyser())

        raise CustomException(f"analyser factory: {analyser_type} not implemented error")
