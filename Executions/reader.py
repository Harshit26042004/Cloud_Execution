import os
import re
import fitz
import pdfbox
import shutil
import opendal
import zipfile
import pytesseract
import pandas as pd
from PIL import Image
from tika import parser
import pyarrow.parquet as pq


class ReadPDF:
    def read(self, path, pages):
        file_content = self._pdfbox_read(path, pages)
        if file_content is None or not file_content.isalnum():
            file_content = self._ocr_read(path,pages)
        return (file_content)
    
    def _pdfbox_read(self, path, pages):
        p = pdfbox.PDFBox()
        out = "file/pdf.txt"
        p.extract_text(input_path=path, output_path=out, end_page=pages)
        with open(out, 'rb') as file:
            pdf_text = str(file.read())
        os.remove(out)
        return pdf_text
    
    def _ocr_read(self, path, pages):
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
    def read(self,path,buffer):
        with zipfile.ZipFile(path,'r')as zip:
            zip.extractall("/temp/")
            with open("/temp/xl/sharedStrings.xml", "r", encoding="utf-8", errors='ignore')as xml:
                a = str(xml.read(buffer*3))
                xml.close()
            zip.close()
        shutil.rmtree("/temp")

        results = re.findall(r'>(.*?)<', a)
        output = ' '.join(results)
        return (output)

class ReadWord:
    def read(self,path,buffer):
        with zipfile.ZipFile(path,'r')as zip:
            zip.extractall("/temp/")
            with open("/temp/word/document.xml", "r", encoding="utf-8", errors='ignore')as xml:
                a = str(xml.read(buffer*15))
                xml.close()
            zip.close()
        shutil.rmtree("/temp")

        results = re.findall(r'>(.*?)<', a)
        output = ' '.join(results)
        return (output)

class ReadPPT:
    def read(self,path,buffer):
        with zipfile.ZipFile(path,'r')as zip:
            zip.extractall("temp/")
            with open("temp/ppt/slides/slide1.xml", "r", encoding="utf-8", errors='ignore')as xml:
                a = str(xml.read())
                xml.close()
            zip.close()
        shutil.rmtree("temp")

        results = re.findall(r'>(.*?)<', a)
        output = ' '.join(results)
        return output

class ReadMSG:
    def read(self,path,buffer):
        with open(path,"r",encoding="utf-8",errors="ignore")as file:
            file.seek(1165)
            msg = str(file.read(buffer*20))
        file.close()
        return msg

class ReadAvro:
    def read(self,path,buffer):
        with open(path,"r",encoding="utf-8",errors="ignore")as file:
            file.seek(0)
            msg = str(file.read(buffer*10))
        file.close()
        return msg

class ReadParquet:
    def read(self,path,records):
        parquet_file = pq.ParquetFile(path)
        for batch in parquet_file.iter_batches(batch_size=records):
            lst = batch.to_pandas()
            break
        parquet_file.close()
        return str(lst)
    
class ReadSAS:
    def read(self,path,records):
        df = pd.read_sas(path, chunksize=records)
        msg =  str(df.read())
        df.close()
        return msg

class FileReader:
    def __init__(self, path, pages, buffer, records):

        self.type = self._find_type(path)
        self.excel_ext = ['xlsx','xlsm','xltx']
        self.word_ext = ['docx','docm','dotx']
        self.ppt_ext = ['pptx','pptm','potx']
        self.avro_ext = ['avro','avsc','avdl']
        self.parquet_ext = ['parquet','pq']
        self.sas_ext = ['sas7bdat','xpt']

        self.body = ""

        if self.type == 'pdf':
            pdf_reader = ReadPDF()
            self.body = pdf_reader.read(path, pages)
        
        elif self.type in self.excel_ext:
            excel_reader = ReadExcel()
            self.body = excel_reader.read(path,buffer)
        
        elif self.type in self.word_ext:
            word_reader = ReadWord()
            self.body = word_reader.read(path,buffer)

        elif self.type in self.ppt_ext:
            ppt_reader = ReadPPT()
            self.body = ppt_reader.read(path,buffer)

        elif self.type == "msg":
            msg_reader = ReadMSG()
            self.body = msg_reader.read(path,buffer)

        elif self.type in self.parquet_ext:
            parquet_reader = ReadParquet()
            self.body = parquet_reader.read(path,records)

        elif self.type in self.sas_ext:
            sas_reader = ReadSAS()
            self.body = sas_reader.read(path,records)
        
        elif self.type in self.avro_ext:
            avro_reader = ReadAvro()
            self.body = avro_reader.read(path,buffer)

        else:
            print("Activating Tika")
            parsed_file = parser.from_file(path)
            self.body = parsed_file['content']
    
    def _find_type(self, path: str):
        lst = path.split(".")
        return lst[len(lst) - 1]
