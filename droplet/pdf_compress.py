from droplet.utilities import Directories


class ConvertPDF(Directories):
    pdf_command = 'gs'
    minimal_configuration = {
        '-sDEVICE':'pdfwrite',
        '-dCompatibility':'1.4',
        '-dPDFSETTINGS':'/screen',
        '-dNOPAUSE':None,
        '-dQUIET':None,
        '-dBATCH':None,
        '-sOutputFile':'{}'
    }
    optional_configuration = {
        '-sColorConversionStrategy':'Gray',
        '-dProcessColorModel':'/DeviceGray'
    }
    @classmethod
    def convert_pdf(cls, path_file):
        compress_path = Directories.get_output_path(path_file)
        parameters = ['='.join(i) if i[1] else i[0] for i in cls.minimal_configuration.items()]
        parameters[-1]=parameters[-1].format(compress_path)
        parameters = [cls.pdf_command] + parameters + [path_file]
        return parameters


if __name__=='__main__':
    print(ConvertPDF.convert_pdf('./Test_Folder/books/Foundations of DS.pdf'))







