from sanitisation import sanitiser_factory
from sanitisation.sanitiser import SanitiserOptions
from utils.file_helper import FileHelper
from data.source import Source, SourceHelper

source_helper = SourceHelper("data/example_1")

source_helper.add("a.txt")
source_helper.add("b.txt")

source = Source(source_helper)

sanitised = source.get_sanitised()

file_helper = FileHelper("data/example_1")

a_clean = file_helper.get_file("a-clean.txt")
b_clean = file_helper.get_file("b-clean.txt")

if sanitised[0] != a_clean.content:
    print("err: a")
    print(sanitised[0])
    print(a_clean.content)

if sanitised[1] != b_clean.content:
    print("err: b")
    print(sanitised[1])
    print(b_clean.content)

text = """---
aliases:
  - clean-knowledge
---
# clean knowledge
> see: [[clean code]]

michael

---
> [!definition]+
> - 

    """

options = SanitiserOptions()


sanitiser = sanitiser_factory.build_sanitiser(options)

result = sanitiser.sanitise(text)

print(result)
