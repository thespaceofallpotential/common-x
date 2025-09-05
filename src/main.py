# see generation_1.py & batch_example.py
from data.file import FileHelper
from sanitisation.sanitiser_factory import SanitiserFactory
from sanitisation.sanitiser import SanitiserOptions

file_helper = FileHelper("../data/example_1")

a_clean = file_helper.get_file("a-clean.txt")
b_clean = file_helper.get_file("b-clean.txt")

a_file = file_helper.get_file("a.txt")
b_file = file_helper.get_file("b.txt")

sanitiser_factory = SanitiserFactory()

sanitiser_options = SanitiserOptions()

stopwords_file = file_helper.get_file("stopwords.txt")

sanitiser_options.stopwords = stopwords_file.content

sanitiser = sanitiser_factory.build(sanitiser_options)

a_sanitised = sanitiser.sanitise(a_file.content)
b_sanitised = sanitiser.sanitise(b_file.content)

if a_sanitised != a_clean.content:
    print("err")

print(a_clean)
