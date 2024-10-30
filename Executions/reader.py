import os
import re
import fitz
import pdfbox
import shutil
import zipfile
import pytesseract
import pandas as pd
from PIL import Image
from tika import parser
import pyarrow.parquet as pq


class ReadPDF:
    """
    A class to read text from PDF files using PDFBox and OCR.

    Methods:
        read(path, pages): Reads text from the specified pages of a PDF.
    """

    def read(self, path, pages):
        """
        Reads text from a PDF file.

        Args:
            path (str): The path to the PDF file.
            pages (int): The number of pages to read.

        Returns:
            str: The extracted text from the PDF.
        """
        file_content = self._pdfbox_read(path, pages)
        if file_content is None or not file_content.isalnum():
            file_content = self._ocr_read(path, pages)
        return file_content
    
    def _pdfbox_read(self, path, pages):
        """
        Reads text from a PDF file using PDFBox.

        Args:
            path (str): The path to the PDF file.
            pages (int): The number of pages to read.

        Returns:
            str: The extracted text from the PDF.
        """
        p = pdfbox.PDFBox()
        out = "file/pdf.txt"
        p.extract_text(input_path=path, output_path=out, end_page=pages)
        with open(out, 'rb') as file:
            pdf_text = str(file.read())
        os.remove(out)
        return pdf_text
    
    def _ocr_read(self, path, pages):
        """
        Reads text from a PDF file using OCR.

        Args:
            path (str): The path to the PDF file.
            pages (int): The number of pages to read.

        Returns:
            str: The extracted text from the PDF.
        """
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pdf_document = fitz.open(path)
        extracted_text = ""
        for page_num in range(min(pages, pdf_document.page_count)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(image)
            extracted_text += text + "\n" 
        pdf_document.close()
        return extracted_text


class ReadExcel:
    """
    A class to read text from Excel files.

    Methods:
        read(path, buffer): Reads text from an Excel file.
    """

    def read(self, path, buffer):
        """
        Reads text from an Excel file.

        Args:
            path (str): The path to the Excel file.
            buffer (int): A multiplier for the amount of text to read.

        Returns:
            str: The extracted text from the Excel file.
        """
        with zipfile.ZipFile(path, 'r') as zip:
            zip.extractall("/temp/")
            with open("/temp/xl/sharedStrings.xml", "r", encoding="utf-8", errors='ignore') as xml:
                a = str(xml.read(buffer * 3))
            zip.close()
        shutil.rmtree("/temp")

        results = re.findall(r'>(.*?)<', a)
        output = ' '.join(results)
        return output


class ReadWord:
    """
    A class to read text from Word documents.

    Methods:
        read(path, buffer): Reads text from a Word document.
    """

    def read(self, path, buffer):
        """
        Reads text from a Word document.

        Args:
            path (str): The path to the Word document.
            buffer (int): A multiplier for the amount of text to read.

        Returns:
            str: The extracted text from the Word document.
        """
        with zipfile.ZipFile(path, 'r') as zip:
            zip.extractall("/temp/")
            with open("/temp/word/document.xml", "r", encoding="utf-8", errors='ignore') as xml:
                a = str(xml.read(buffer * 15))
            zip.close()
        shutil.rmtree("/temp")

        results = re.findall(r'>(.*?)<', a)
        output = ' '.join(results)
        return output


class ReadPPT:
    """
    A class to read text from PowerPoint presentations.

    Methods:
        read(path, buffer): Reads text from a PowerPoint presentation.
    """

    def read(self, path, buffer):
        """
        Reads text from a PowerPoint presentation.

        Args:
            path (str): The path to the PowerPoint file.
            buffer (int): A multiplier for the amount of text to read.

        Returns:
            str: The extracted text from the PowerPoint presentation.
        """
        with zipfile.ZipFile(path, 'r') as zip:
            zip.extractall("temp/")
            with open("temp/ppt/slides/slide1.xml", "r", encoding="utf-8", errors='ignore') as xml:
                a = str(xml.read())
            zip.close()
        shutil.rmtree("temp")

        results = re.findall(r'>(.*?)<', a)
        output = ' '.join(results)
        return output


class ReadMSG:
    """
    A class to read text from MSG files.

    Methods:
        read(path, buffer): Reads text from an MSG file.
    """

    def read(self, path, buffer):
        """
        Reads text from an MSG file.

        Args:
            path (str): The path to the MSG file.
            buffer (int): A multiplier for the amount of text to read.

        Returns:
            str: The extracted text from the MSG file.
        """
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            file.seek(1165)
            msg = str(file.read(buffer * 20))
        return msg


class ReadAvro:
    """
    A class to read text from Avro files.

    Methods:
        read(path, buffer): Reads text from an Avro file.
    """

    def read(self, path, buffer):
        """
        Reads text from an Avro file.

        Args:
            path (str): The path to the Avro file.
            buffer (int): A multiplier for the amount of text to read.

        Returns:
            str: The extracted text from the Avro file.
        """
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            file.seek(0)
            msg = str(file.read(buffer * 10))
        return msg


class ReadParquet:
    """
    A class to read data from Parquet files.

    Methods:
        read(path, records): Reads records from a Parquet file.
    """

    def read(self, path, records):
        """
        Reads records from a Parquet file.

        Args:
            path (str): The path to the Parquet file.
            records (int): The number of records to read.

        Returns:
            str: A string representation of the records from the Parquet file.
        """
        parquet_file = pq.ParquetFile(path)
        for batch in parquet_file.iter_batches(batch_size=records):
            lst = batch.to_pandas()
            break
        return str(lst)


class ReadSAS:
    """
    A class to read data from SAS files.

    Methods:
        read(path, records): Reads records from a SAS file.
    """

    def read(self, path, records):
        """
        Reads records from a SAS file.

        Args:
            path (str): The path to the SAS file.
            records (int): The number of records to read.

        Returns:
            str: A string representation of the records from the SAS file.
        """
        df = pd.read_sas(path, chunksize=records)
        msg = str(df.read())
        return msg


class FileReader:
    """
    A class to determine file type and read content based on file type.

    Args:
        path (str): The file path.
        pages (int): Number of pages for PDF reading.
        buffer (int): Buffer size for reading text from various formats.
        records (int): Number of records to read for data files.

    Attributes:
        body (str): The extracted content from the file.
    """

    def __init__(self, path, pages, buffer, records):
        self.type = self._find_type(path)
        self.excel_ext = ['xlsx', 'xlsm', 'xltx']
        self.word_ext = ['docx', 'docm', 'dotx']
        self.ppt_ext = ['pptx', 'pptm', 'potx']
        self.avro_ext = ['avro', 'avsc', 'avdl']
        self.parquet_ext = ['parquet', 'pq']
        self.sas_ext = ['sas7bdat', 'xpt']

        self.body = ""

        if self.type == 'pdf':
            pdf_reader = ReadPDF()
            self.body = pdf_reader.read(path, pages)
        
        elif self.type in self.excel_ext:
            excel_reader = ReadExcel()
            self.body = excel_reader.read(path, buffer)
        
        elif self.type in self.word_ext:
            word_reader = ReadWord()
            self.body = word_reader.read(path, buffer)

        elif self.type in self.ppt_ext:
            ppt_reader = ReadPPT()
            self.body = ppt_reader.read(path, buffer)

        elif self.type == "msg":
            msg_reader = ReadMSG()
            self.body = msg_reader.read(path, buffer)

        elif self.type in self.parquet_ext:
            parquet_reader = ReadParquet()
            self.body = parquet_reader.read(path, records)

        elif self.type in self.sas_ext:
            sas_reader = ReadSAS()
            self.body = sas_reader.read(path, records)
        
        elif self.type in self.avro_ext:
            avro_reader = ReadAvro()
            self.body = avro_reader.read(path, buffer)

        else:
            parsed_file = parser.from_file(path)
            self.body = parsed_file['content']
    
    def _find_type(self, path: str):
        """
        Determines the file type based on the file extension.

        Args:
            path (str): The file path.

        Returns:
            str: The file extension/type.
        """
        lst = path.split(".")
        return lst[-1]
