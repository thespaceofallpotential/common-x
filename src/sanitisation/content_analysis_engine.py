from core.sink import Sink, sink_factory
from sanitisation.analyser import AnalyserType, IAnalyser
from sanitisation.analysis import Analysis
from sanitisation.analyser_factory import AnalyserFactory


class ContentAnalysisEngine[T]:
    def process(
        self,
        contents: list[str],
        processor: IAnalyser,
        sink: Sink[Analysis[T]],
    ):
        length = len(contents)

        for i in range(length):
            print("{'progress [%d%%]\r'}" % ((i + 1) / length * 100), end="")

            content = contents[i]

            processor.process(content)

            analysis = processor.get_analysis(i)

            sink.add(analysis)

        print("")  # move cursor to next line


def content_analysis_runner(
    analyser_type: AnalyserType,
    contents: list[str],
    # sink: Sink[Analysis[T]],
) -> list[Analysis]:
    factory = AnalyserFactory()

    processor = factory.build(analyser_type)

    engine = ContentAnalysisEngine()

    sink = sink_factory()

    engine.process(contents, processor, sink)

    return sink.items


def run_and_print(analyser_type: AnalyserType, contents: list[str]):
    characters = content_analysis_runner(analyser_type, contents)

    print(f"{characters}")
