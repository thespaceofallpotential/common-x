from core.sink import Sink, sink_factory
from formulation.analysis.analyser import AnalyserType, IAnalyser
from formulation.analysis.analysis import Analysis
from formulation.analysis.analyser_factory import AnalyserFactory
from utils.progress import TimedProgress


class ContentAnalysisEngine[T]:
    def process(
        self,
        contents: list[str],
        processor: IAnalyser,
        sink: Sink[Analysis[T]],
    ):
        length = len(contents)

        progress = TimedProgress("content analysis", length)

        for i in range(length):
            progress.update(i)

            content = contents[i]

            processor.process(content)

            analysis = processor.get_analysis(i)

            sink.add(analysis)

        progress.complete()


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

    print(f"\n{characters}")
