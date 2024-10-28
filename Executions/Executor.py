"""
Main module for interacting with S3 using opendal.
"""

import logging
import opendal
import pandas as pd
from reader import *
from classify import *
from tika import parser

"""Initializing Logging capability"""
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class AccessException(Exception):
    """Custom exception for access-related errors."""
    pass

class S3Executor:
    """Class to handle S3 operations using opendal."""

    def __init__(self, bucket: str, region: str, endpoint: str,
                 access_key_id: str | None, secret_access_key: str | None,
                 session_token: str | None) -> None:
        """
        Initialize the S3Executor with credentials.

        Args:
            bucket (str): The name of the S3 bucket.
            region (str): The region of the S3 bucket.
            endpoint (str): The S3 endpoint URL.
            access_key_id (str | None): Access key ID for authentication.
            secret_access_key (str | None): Secret access key for authentication.
            session_token (str | None): Session token for authentication.
        """
        print("Bucket name : ",bucket)
        try:
            if session_token is not None:
                self.op = opendal.Operator(
                    "s3",
                    root="/",
                    bucket=bucket,
                    region=region,
                    session_token=session_token,
                    endpoint=endpoint
                )
                logger.info("\tAuthenticating with session token!\t")
                logger.info("\tAuthentication Successful!\t")
            elif access_key_id is not None and secret_access_key is not None:
                self.op = opendal.Operator(
                    "s3",
                    root="/",
                    bucket=bucket,
                    region=region,
                    access_key_id=access_key_id,
                    secret_access_key=secret_access_key,
                    endpoint=endpoint
                )
                logger.info("\tAuthenticating with access key and secret access!\t")
                logger.info("\tAuthentication Successful!\t")
            else:
                logger.error("\tSome Authentication Problem!\t")

        except AccessException:
            logger.critical("\tInvalid Token or Denied Access\t")

    def load_sample(self):
        """Load a sample file into the S3 bucket.This is for testing purpose"""
        self.op.write("/test.py", b"print(\"hello world\")")
        self.op.create_dir("/tmp/subs/")
        self.op.create_dir("/sub/")
        logger.info("\tdirectory created!\n")

    def list_directory(self, path="/"):
        """List the contents of a directory in the S3 bucket.

        Args:
            path (str): The directory path to list.
        """
        logger.info("\tScanning files...")
        entries = self.op.scan(path)
        for entry in entries:
            print(entry)

    def get_meta_data(self, entry):
        """Get metadata for a specific entry.

        Args:
            entry: The entry object to retrieve metadata for.

        Returns:
            dict: A dictionary containing metadata information.
        """
        stat = self.op.stat(entry.path)
        return {
            "Content-size": stat.content_length,
            "E-tag": stat.etag,
            "Content type": stat.content_type,
            "Content mode": stat.mode,
            "Disposition": stat.content_disposition,
            "md5": stat.content_md5
        }

    def discover(self):
        """Discover and print metadata for all entries in the S3 bucket."""
        entries = self.op.scan("/")
        schema = {}
        for entry in entries:
            schema[entry.path] = self.get_meta_data(entry)
        for _key, _values in schema.items():
            print("\n", _key)
            print("Meta-data are:")
            for k, v in _values.items():
                print("\t", k, ":", v)

    def file_read(self, path,max_buffer,pages,records,skip_file_type):
        """Read a file from the S3 bucket and process its content.

        Args:
            path (str): The path of the file to read.
        """
        logger.info("\tReading files\n")
        with self.op.open(path, "rb") as file:
            content = ["txt", "csv", "log", "md", "xml", "json", "html", "css", "tsv", "ini", "conf", "sh", "py", "sql", "yaml", "yml", "properties", "bat", "cmd", "pl", "rb", "r", "asp", "jsp", "tex", "txt2", "diff", "patch", "xml.gz", "jsonl", "m3u", "m3u8", "svg", "txt.gz", "csv.gz", "srt", "ts", "vbs", "java", "eml", "mbox", "svgz", "log.gz", "note", "cfg", "pmd", "plist", "dtd", "xsl", "kml", "gpx", "f90", "f95", "h", "c", "cpp", "pas", "cs", "asm", "d", "swift", "ml", "makefile", "cmake", "rc", "pfx", "json5"]

            lst = path.split(".")
            ext = lst[len(lst) - 1]
            if ext in content:
                file.seek(0, 0)
                print("Reading : \n", file.read(max_buffer))
            else:
                print("reading...")
                print(FileReader(path, pages, max_buffer, records).body)
                
            # print("\nMeta Data:\n", parsed_pdf['metadata'])

    def read_all(self,max_buffer,pages,row_limit,file_size,skip_file_type):
        """Reading all the files that are available with certain filters
        
        Args:
            row_limit (int): No. of rows to be returned.
            file_size (int): Maximum size allowed.
        """
        logger.info("\tRetrieving all files\n")
        entries = self.op.scan("/")
        for entry in entries:
            stat = self.op.stat(entry.path)
            size = stat.content_length
            size /= (1024*1024)
            file_check = stat.mode
            if file_check.is_file():
                print("\n\tFile name : ",entry.path)
                if size<=file_size:
                    path = entry.path
                    with self.op.open(path,'rb')as reader:
                        lpath = path
                        with open(lpath,'wb')as f:
                            f.write(reader.read())

                        self.file_read(lpath,max_buffer,pages,row_limit,skip_file_type)
                        print("\nFile type: ",Classifier().classify(lpath))
                        f.close()
                        reader.close()
                        os.remove(lpath)
                else:
                    print("File skipped (size filter)")
