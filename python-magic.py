import magic
from Executions.classify import Classifier

file_paths = [r"D:\Cloud\Localstack\file\contacts_to_import.xlsx",
             r'D:\Cloud\Localstack\file\message_files\Convert your PDFs quickly and easily.eml',
             r'D:\Cloud\Localstack\file\Structured\Person.avsc',
             r"D:\Images\IMG_20230119_185104.jpg",
             r"D:\movies\LYAL\archive.zip"
             ]
classifier = Classifier()
for file_path in file_paths:
    main_type,subtype = classifier.classify(file_path)
    print(f'\nThe File type of "{file_path}" :\n\t File Type -> {main_type}\n\t Subtype -> {subtype}\n')
