import mimetypes
import magic

extension_key = {
'.blend': ('3D Modeling File',
'Blender 3D File'), '.max': ('3D Modeling File',
'3D Studio Max File'), 
'.mb': ('3D Modeling File', 
'Autodesk Maya File'), 
'.fbx': ('3D Modeling File', 'FBX File'), 
'.obj': ('3D Modeling File', '3D Object File'), 
'.stl': ('3D Modeling File', 'STL File'), 
'.gltf': ('3D Modeling File', 'GLTF Model'), 
'.dae': ('3D Modeling File', '3D Collada File'), 
'.tar': ('Archive', 'TAR Archive'), 
'.ogg': ('Audio Files', 'OGG Audio'), 
'.flac': ('Audio Files', 'FLAC Audio'), 
'.m4a': ('Audio Files', 'M4A Audio'), 
'.midi': ('Audio Files', 'MIDI File'), 
'.aiff': ('Audio Files', 'AIFF Audio File'), 
'.m4b': ('Audio Files', 'M4B Audiobook'), 
'.bak': ('Backup Files', 'Backup File'), 
'.dwg': ('CAD Files', 'AutoCAD Drawing'), 
'.dxf': ('CAD Files', 'DXF File'), 
'.step': ('CAD Files', 'STEP File'), 
'.iges': ('CAD Files', 'IGES File'), 
'.crt': ('Certificate and Keys', 'SSL Certificate'), 
'.pgp': ('Certificate and Keys', 'PGP Key'), 
'.pem': ('Certificate and Keys', 'SSH Private Key'), 
'.o': ('Compiled Files', 'Object File'), 
'.so': ('Compiled Files', 'Shared Object (Linux)'), 
'.class': ('Compiled Files', 'Java Bytecode'), 
'.pyc': ('Compiled Files', 'Python Bytecode'), 
'.zip': ('Compressed Files', 'ZIP Archive'), 
'.rar': ('Compressed Files', 'RAR Archive'), 
'.7z': ('Compressed Files', '7-Zip Archive'), 
'.bz2': ('Compressed Files', 'BZIP2 Archive'), 
'.gz': ('Compressed Files', 'GZIP Archive'), 
'.tf': ('Configuration Files', 'Terraform Configuration'), 
'.json': ('Configuration Files', 'JSON'), 
'.yaml': ('Configuration Files', 'YAML'), 
'.xml': ('Configuration Files', 'XML'), 
'.ini': ('Configuration Files', 'INI'), 
'.properties': ('Configuration Files', 'Properties'), 
'.toml': ('Configuration Files', 'TOML'), 
'.env': ('Configuration Files', 'ENV File'), 
'.yml': ('Configuration Files', 'YAML File'), 
'.csv': ('Data Files', 'CSV File'), 
'.parquet': ('Data Files', 'Parquet File'), 
'.sas7bdat': ('Data Files', 'SAS File'), 
'.avro': ('Data Files', 'AVRO File'), 
'.avsc': ('Data Files', 'AVRO File'), 
'.avdl': ('Data Files', 'AVRO File'), 
'.orc': ('Data Files', 'ORC File'), 
'.xlsb': ('Data Files', 'Excel Binary Workbook'), 
'.psd': ('Design Files', 'Photoshop PSD File'), 
'.ai': ('Design Files', 'Adobe Illustrator File'), 
'.sketch': ('Design Files', 'Sketch File'), 
'.fig': ('Design Files', 'Figma Design File'), 
'.cdr': ('Design Files', 'CorelDRAW File'), 
'.xcf': ('Design Files', 'GIMP File'), 
'.iso': ('Disk Image Files', 'ISO Disk Image'), 
'.bin': ('Disk Image Files', 'Bin/Cue Disk Image'), 
'.dmg': ('Disk Image Files', 'DMG Disk Image'), 
'.vhd': ('Disk Image Files', 'VHD Disk Image'), 
'.epub': ('Document Files', 'ePub eBook'), 
'.mobi': ('Document Files', 'Mobipocket eBook'), 
'.djvu': ('Document Files', 'DjVu File'), 
'.cbr': ('Document Files', 'Comic Book Archive'), 
'.tex': ('Document Files', 'LaTeX Source File'), 
'.pst': ('Email Files', 'Outlook PST'), 
'.ost': ('Email Files', 'Outlook OST'), 
'.eml': ('Email Files', 'MIME Email'), 
'.mbox': ('Email Files', 'MBOX Email'), 
'.gpg': ('Encrypted Files', 'GPG Encrypted File'), 
'.enc': ('Encrypted Files', 'Encrypted File'), 
'.msi': ('Executable Files', 'Windows Executable File'), 
'.exe': ('Executable Files', 'Windows Executable'), 
'.out': ('Executable Files', 'Linux Executable'), 
'.elf': ('Executable Files', 'ELF Executable'), 
'.bat': ('Executable Files', 'Windows Batch File'), 
'.cmd': ('Executable Files', 'Windows Command Script'), 
'.ps1': ('Executable Files', 'PowerShell Script'), 
'.qbb': ('Financial Data Files', 'QuickBooks Backup'), 
'.qbw': ('Financial Data Files', 'QuickBooks Company File'), 
'.ttf': ('Font Files', 'TrueType Font'), 
'.otf': ('Font Files', 'OpenType Font'), 
'.woff': ('Font Files', 'WOFF Font'), 
'.woff2': ('Font Files', 'WOFF2 Font'), 
'.eot': ('Font Files', 'EOT Font File'), 
'.rom': ('Game Files', 'ROM File'), 
'.sav': ('Game Files', 'Game Save File'), 
'.gba': ('Game Files', 'Game Boy Advance ROM'), 
'.nds': ('Game Files', 'Nintendo DS ROM'), 
'.shp': ('Geospatial Files', 'Shapefile'), 
'.geojson': ('Geospatial Files', 'GeoJSON'), 
'.kml': ('Geospatial Files', 'KML File'), 
'.gpx': ('Geospatial Files', 'GPX File'), 
'.gif': ('Image File', 'GIF Image'), 
'.bmp': ('Image File', 'BMP Image'), 
'.tiff': ('Image File', 'TIFF Image'), 
'.heic': ('Image File', 'HEIC Image'), 
'.heif': ('Image File', 'HEIF Image'), 
'.jpeg': ('Image File', 'JPEG Image'), 
'.png': ('Image File', 'PNG Image'), 
'.ico': ('Image File', 'Icon File'), 
'.svg': ('Image File', 'Scalable Vector Graphic'), 
'.eps': ('Image File', 'Encapsulated PostScript'), 
'.log': ('Log Files', 'Log File'), 
'.syslog': ('Log Files', 'System Log'), 
'.evtx': ('Log Files', 'Windows Event Log'), 
'.perf': ('Log Files', 'Performance Log'), 
'.dcm': ('Medical Files', 'DICOM Image'), 
'.nii': ('Medical Files', 'NIfTI Image'), 
'.hdr': ('Medical Files', 'Analyze 7.5'), 
'.vmr': ('Medical Files', 'BrainVoyager File'), 
'.audit': ('Monitoring Files', 'Audit File'), 
'.mib': ('Monitoring Files', 'SNMP MIB File'), 
'.docx': ('MS Office Documents', 'Word Document'), 
'.xlsx': ('MS Office Documents', 'Excel Spreadsheet'), 
'.pptx': ('MS Office Documents', 'PowerPoint Presentation'), 
'.mdb': ('MS Office Documents', 'Access Database'), 
'.vsdx': ('MS Office Documents', 'Visio Diagram'), 
'.jpg': ('Multimedia Files', 'JPEG Image'), 
'.mp4': ('Multimedia Files', 'MP4 Video'), 
'.wav': ('Multimedia Files', 'WAV Audio'), 
'.mp3': ('Multimedia Files', 'MP3 Audio'), 
'.avi': ('Multimedia Files', 'AVI Video'), 
'.mkv': ('Multimedia Files', 'MKV Video'), 
'.pdf': ('PDF', 'PDF'), 
'.webp': ('Image File', 'WebP Image'), 
'.h5': ('Scientific Data Files', 'HDF5 File'), 
'.nc': ('Scientific Data Files', 'NetCDF File'), 
'.grib': ('Scientific Data Files', 'GRIB File'), 
'.mat': ('Scientific Data Files', 'MAT File (MATLAB)'), 
'.jks': ('Security Files', 'Key Store'), 
'.pfx': ('Security Files', 'PKCS12 Certificate'), 
'.asc': ('Security Files', 'PGP Private Key'), 
'.sig': ('Security Files', 'PGP Signature'), 
'.crl': ('Security Files', 'Certificate Revocation List'), 
'.cer': ('Security Files', 'X.509 Certificate'), 
'.der': ('Security Files', 'DER Encoded Certificate'), 
'.key': ('Source Code', 'Keynote Presentation'), 
'.odp': ('Source Code', 'OpenDocument Presentation'), 
'.php': ('Web Files', 'PHP File'), 
'.rb': ('Source Code', 'Ruby Code'), 
'.swift': ('Source Code', 'Swift Code'), 
'.kt': ('Source Code', 'Kotlin Code'), 
'.rs': ('Source Code', 'Rust Code'), 
'.dart': ('Source Code', 'Dart Code'), 
'.pl': ('Source Code', 'Perl Script'), 
'.r': ('Source Code', 'R Script'), 
'.m': ('Source Code', 'MATLAB Script'), 
'.f': ('Source Code', 'FORTRAN Code'), 
'.cob': ('Source Code', 'COBOL Code'), 
'.hs': ('Source Code', 'Haskell Code'), 
'.lua': ('Source Code', 'Lua Code'), 
'.scala': ('Source Code', 'Scala Code'), 
'.ts': ('Source Code', 'TypeScript Code'), 
'.jl': ('Source Code', 'Julia Code'), 
'.pas': ('Source Code', 'Pascal Code'), 
'.bash': ('Source Code', 'Bash Script'), 
'.groovy': ('Source Code', 'Groovy Script'), 
'.py': ('Source Code', 'Python Code'), 
'.java': ('Source Code', 'Java Code'), 
'.c': ('Source Code', 'C Code'), 
'.cpp': ('Source Code', 'C++ Code'), 
'.h': ('Source Code', 'C Header File'), 
'.sh': ('Source Code', 'Shell Script'), 
'Makefile': ('Source Code', 'Makefile'), 
'Dockerfile': ('Source Code', 'Dockerfile'), 
'.js': ('Web Files', 'JavaScript File'), 
'.go': ('Source Code', 'Go Code'), 
'.jar': ('Source Code Archives', 'JAR File'), 
'.war': ('Source Code Archives', 'WAR File'), 
'.ear': ('Source Code Archives', 'EAR File'), 
'.ods': ('Spreadsheet Files', 'OpenDocument Spreadsheet'), 
'.pgsql': ('SQL and Database Files', 'PostgreSQL Dump'), 
'.dbf': ('SQL and Database Files', 'Oracle Database File'), 
'.sql': ('SQL and Database Files', 'SQL Script'), 
'.sqlite': ('SQL and Database Files', 'SQLite Database'), 
'.dll': ('System Files', 'Windows DLL'), 
'.ko': ('System Files', 'Linux Kernel Module'), 
'.sys': ('System Files', 'Windows System File'), 
'.init': ('System Files', 'Linux Init Script'), 
'.reg': ('System Files', 'Windows Registry File'), 
'.lnk': ('System Files', 'Windows Shortcut'), 
'.apk': ('System Files', 'Android Package'), 
'.ipa': ('System Files', 'iOS App Archive'), 
'.cab': ('System Files', 'Windows Cabinet File'), 
'.md': ('Text Files', 'Markdown File'), 
'.rtf': ('Text Files', 'Rich Text Format'), 
'.textile': ('Text Files', 'Textile File'), 
'.svn': ('Version Control Files', 'Subversion Commit'), 
'.patch': ('Version Control Files', 'Git Patch'), 
'.git': ('Version Control Files', 'Git Repository'), 
'.hg': ('Version Control Files', 'Mercurial Repository'), 
'.gitignore': ('Version Control Files', 'Git Ignore File'), 
'.gitattributes': ('Version Control Files', 'Git Attributes File'), 
'.ova': ('Virtualization Files', 'OVA (Virtual Appliance)'), 
'.qcow2': ('Virtualization Files', 'QCOW2 Disk Image'), 
'.vdi': ('Virtualization Files', 'VirtualBox Disk Image'), 
'.vmdk': ('Virtualization Files', 'VMware Disk Image'), 
'.vhdx': ('Virtualization Files', 'Hyper-V Disk Image'), 
'.html': ('Web Files', 'HTML File'), 
'.css': ('Web Files', 'CSS File'), 
'.aspx': ('Web Files', 'ASPX File')
}

mime_key = {
'application/x-blender': ('3D Modeling File', 'Blender 3D File'),
'application/octet-stream': ('Virtualization Files', 'Hyper-V Disk Image'), 
'application/sla': ('3D Modeling File', 'STL File'), 
'model/gltf+json': ('3D Modeling File', 'GLTF Model'), 
'model/vnd.collada+xml': ('3D Modeling File', '3D Collada File'), 
'application/x-tar': ('Archive', 'TAR Archive'), 
'audio/ogg': ('Audio Files', 'OGG Audio'), 
'audio/flac': ('Audio Files', 'FLAC Audio'), 
'audio/mp4': ('Audio Files', 'M4B Audiobook'), 
'audio/midi': ('Audio Files', 'MIDI File'), 
'audio/x-aiff': ('Audio Files', 'AIFF Audio File'), 
'application/acad': ('CAD Files', 'AutoCAD Drawing'), 
'image/vnd.dxf': ('CAD Files', 'DXF File'), 
'application/step': ('CAD Files', 'STEP File'), 
'application/iges': ('CAD Files', 'IGES File'), 
'application/x-x509-ca-cert': ('Security Files', 'DER Encoded Certificate'), 
'application/pgp-encrypted': ('Security Files', 'PGP Private Key'), 
'application/x-pem-file': ('Certificate and Keys', 'SSH Private Key'), 
'application/x-object': ('Compiled Files', 'Object File'), 
'application/x-sharedlib': ('Compiled Files', 'Shared Object (Linux)'),
'application/java-vm': ('Compiled Files', 'Java Bytecode'), 
'application/x-python-code': ('Compiled Files', 'Python Bytecode'), 
'application/zip': ('Compressed Files', 'ZIP Archive'), 
'application/x-rar-compressed': ('Compressed Files', 'RAR Archive'), 
'application/x-7z-compressed': ('Compressed Files', '7-Zip Archive'), 
'application/x-bzip2': ('Compressed Files', 'BZIP2 Archive'), 
'application/gzip': ('Compressed Files', 'GZIP Archive'), 
'text/plain': ('Version Control Files', 'Git Attributes File'), 
'application/json': ('Geospatial Files', 'GeoJSON'), 
'application/x-yaml': ('Configuration Files', 'YAML File'), 
'application/xml': ('Configuration Files', 'XML'), 
'text/csv': ('Data Files', 'CSV File'), 
'application/x-sas-data': ('Data Files', 'SAS File'), 
'application/vnd.ms-excel.sheet.binary.macroenabled.12': ('Data Files', 'Excel Binary Workbook'), 
'image/vnd.adobe.photoshop': ('Design Files', 'Photoshop PSD File'), 
'application/postscript': ('Image File', 'Encapsulated PostScript'), 
'application/x-coreldraw': ('Design Files', 'CorelDRAW File'), 
'application/x-gimp': ('Design Files', 'GIMP File'), 
'application/x-iso9660-image': ('Disk Image Files', 'ISO Disk Image'), 
'application/x-apple-diskimage': ('Disk Image Files', 'DMG Disk Image'), 
'application/epub+zip': ('Document Files', 'ePub eBook'), 
'application/x-mobipocket-ebook': ('Document Files', 'Mobipocket eBook'), 
'image/vnd.djvu': ('Document Files', 'DjVu File'), 
'application/x-cbr': ('Document Files', 'Comic Book Archive'), 
'application/x-tex': ('Document Files', 'LaTeX Source File'), 
'application/vnd.ms-outlook': ('Email Files', 'Outlook OST'), 
'message/rfc822': ('Email Files', 'MIME Email'), 
'application/mbox': ('Email Files', 'MBOX Email'), 
'application/x-msi': ('Executable Files', 'Windows Executable File'), 
'application/x-msdownload': ('System Files', 'Windows System File'), 
'application/x-executable': ('Executable Files', 'ELF Executable'), 
'application/x-bat': ('Executable Files', 'Windows Batch File'), 
'application/x-msdos-program': ('Executable Files', 'Windows Command Script'), 
'application/x-powershell': ('Executable Files', 'PowerShell Script'), 
'application/vnd.intu.qbo': ('Financial Data Files', 'QuickBooks Company File'), 
'font/ttf': ('Font Files', 'TrueType Font'), 
'font/otf': ('Font Files', 'OpenType Font'), 
'font/woff': ('Font Files', 'WOFF Font'), 
'font/woff2': ('Font Files', 'WOFF2 Font'), 
'application/vnd.ms-fontobject': ('Font Files', 'EOT Font File'), 
'application/vnd.google-earth.kml+xml': ('Geospatial Files', 'KML File'), 
'application/gpx+xml': ('Geospatial Files', 'GPX File'), 
'image/gif': ('Image File', 'GIF Image'), 
'image/bmp': ('Image File', 'BMP Image'), 
'image/tiff': ('Image File', 'TIFF Image'), 
'image/heic': ('Image File', 'HEIC Image'), 
'image/jpeg': ('Multimedia Files', 'JPEG Image'), 
'image/png': ('Image File', 'PNG Image'), 
'image/x-icon': ('Image File', 'Icon File'), 
'image/svg+xml': ('Image File', 'Scalable Vector Graphic'), 
'application/dicom': ('Medical Files', 'DICOM Image'), 
'application/nifti': ('Medical Files', 'NIfTI Image'), 
'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ('MS Office Documents', 'Word Document'), 
'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ('MS Office Documents', 'Excel Spreadsheet'), 
'application/vnd.openxmlformats-officedocument.presentationml.presentation': ('MS Office Documents', 'PowerPoint Presentation'), 
'application/vnd.ms-access': ('MS Office Documents', 'Access Database'), 
'application/vnd.visio': ('MS Office Documents', 'Visio Diagram'),
'video/mp4': ('Multimedia Files', 'MP4 Video'), 
'audio/wav': ('Multimedia Files', 'WAV Audio'), 
'audio/mpeg': ('Multimedia Files', 'MP3 Audio'), 
'video/x-msvideo': ('Multimedia Files', 'AVI Video'), 
'video/x-matroska': ('Multimedia Files', 'MKV Video'), 
'application/pdf': ('PDF', 'PDF'), 
'image/webp': ('Image File', 'WebP Image'), 
'application/x-hdf5': ('Scientific Data Files', 'HDF5 File'), 
'application/x-netcdf': ('Scientific Data Files', 'NetCDF File'), 
'application/x-grib': ('Scientific Data Files', 'GRIB File'), 
'application/x-matlab-data': ('Scientific Data Files', 'MAT File (MATLAB)'), 
'application/x-java-keystore': ('Security Files', 'Key Store'), 
'application/x-pkcs12': ('Security Files', 'PKCS12 Certificate'), 
'application/pgp-signature': ('Security Files', 'PGP Signature'), 
'application/pkix-crl': ('Security Files', 'Certificate Revocation List'), 
'application/pkix-cert': ('Security Files', 'X.509 Certificate'), 
'application/vnd.apple.keynote': ('Source Code', 'Keynote Presentation'), 
'application/vnd.oasis.opendocument.presentation': ('Source Code', 'OpenDocument Presentation'), 
'application/x-php': ('Source Code', 'PHP Code'), 
'application/x-ruby': ('Source Code', 'Ruby Code'), 
'application/x-swift': ('Source Code', 'Swift Code'), 
'application/x-kotlin': ('Source Code', 'Kotlin Code'), 
'text/x-rust': ('Source Code', 'Rust Code'), 
'application/x-dart': ('Source Code', 'Dart Code'), 
'text/x-perl': ('Source Code', 'Perl Script'), 
'text/x-matlab': ('Source Code', 'MATLAB Script'), 
'text/x-fortran': ('Source Code', 'FORTRAN Code'), 
'text/x-cobol': ('Source Code', 'COBOL Code'), 
'text/x-haskell': ('Source Code', 'Haskell Code'), 
'text/x-lua': ('Source Code', 'Lua Code'), 
'text/x-scala': ('Source Code', 'Scala Code'), 
'application/x-typescript': ('Source Code', 'TypeScript Code'), 
'application/julia': ('Source Code', 'Julia Code'), 
'text/x-pascal': ('Source Code', 'Pascal Code'), 
'application/x-sh': ('Source Code', 'Shell Script'), 
'application/x-groovy': ('Source Code', 'Groovy Script'), 
'text/x-python': ('Source Code', 'Python Code'), 
'text/x-java-source': ('Source Code', 'Java Code'), 
'text/x-c': ('Source Code', 'C Code'), 
'text/x-cpp': ('Source Code', 'C++ Code'), 
'text/x-chdr': ('Source Code', 'C Header File'), 
'application/javascript': ('Web Files', 'JavaScript File'), 
'text/x-go': ('Source Code', 'Go Code'), 
'application/java-archive': ('Source Code Archives', 'EAR File'), 
'application/vnd.oasis.opendocument.spreadsheet': ('Spreadsheet Files', 'OpenDocument Spreadsheet'), 
'application/sql': ('SQL and Database Files', 'SQL Script'), 
'application/vnd.sqlite3': ('SQL and Database Files', 'SQLite Database'), 
'application/vnd.microsoft.portable-executable': ('System Files', 'Windows DLL'), 
'application/x-ko': ('System Files', 'Linux Kernel Module'), 
'application/x-ms-shortcut': ('System Files', 'Windows Shortcut'), 
'application/vnd.android.package-archive': ('System Files', 'Android Package'), 
'application/vnd.ms-cab-compressed': ('System Files', 'Windows Cabinet File'), 
'text/markdown': ('Text Files', 'Markdown File'), 
'application/rtf': ('Text Files', 'Rich Text Format'), 
'text/x-textile': ('Text Files', 'Textile File'), 
'application/x-subversion': ('Version Control Files', 'Subversion Commit'), 
'text/x-diff': ('Version Control Files', 'Git Patch'), 
'application/x-git': ('Version Control Files', 'Git Repository'), 
'application/x-mercurial': ('Version Control Files', 'Mercurial Repository'), 
'application/x-virtualbox-ova': ('Virtualization Files', 'OVA (Virtual Appliance)'), 
'application/x-qcow2': ('Virtualization Files', 'QCOW2 Disk Image'), 
'application/x-virtualbox-vdi': ('Virtualization Files', 'VirtualBox Disk Image'), 
'application/x-vmdk': ('Virtualization Files', 'VMware Disk Image'), 
'text/html': ('Web Files', 'HTML File'), 
'text/css': ('Web Files', 'CSS File'), 
'application/x-httpd-php': ('Web Files', 'PHP File'), 
'application/x-aspx': ('Web Files', 'ASPX File')
}

class Classifier:
    """
    A class for classifying files based on their extension and MIME type.

    Attributes:
        extension_key (dict): A mapping of file extensions to their (main_type, sub_type).
        mime_key (dict): A mapping of MIME types to their (main_type, sub_type).
    """

    def classify(self, path):
        """
        Classifies a file based on its path.

        Args:
            path (str): The file path to classify.

        Returns:
            tuple: A tuple containing two lists:
                - main_type: A list of main types derived from the file's extension and MIME type.
                - sub_type: A list of sub types derived from the file's extension and MIME type.
        """
        file_ext = []
        lst = path.split(".")

        file_ext.append("." + str(lst[-1]))
        mime_type = self.get_mime_type_from_magic(path)
        file_ext.extend(mimetypes.guess_all_extensions(mime_type))
        
        print(mime_type)
        file_type = set()

        if mime_type in mime_key:
            file_type.add(mime_key[mime_type])

        for i in file_ext:
            if i in extension_key:
                file_type.add(extension_key[i])

        main_type = []
        sub_type = []

        for i in file_type:
            main_type.append(i[0])
            sub_type.append(i[1])

        return main_type, sub_type

    @staticmethod
    def get_mime_type_from_magic(file_path):
        """
        Gets the MIME type of a file using the file's contents.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The determined MIME type of the file. If the MIME type cannot be determined,
                  it returns None.
        """
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type is not None:
            return mime_type
        mime = magic.Magic(mime=True)
        mime_type = mime.from_file(file_path)
        return mime_type
