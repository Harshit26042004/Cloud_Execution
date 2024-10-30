import magic
from Executions.classify import Classifier

file_path = r'D:\Cloud\Localstack\file\Structured\intel.sas7bdat'
classifier = Classifier()
main_type,subtype = classifier.classify(file_path)
print(f'\nThe MIME type of "{file_path}" :\n\t File Type -> {main_type}\n\t Subtype -> {subtype}\n')
