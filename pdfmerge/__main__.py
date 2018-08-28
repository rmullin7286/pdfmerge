import sys

from PyPDF2 import PdfFileReader, PdfFileMerger

def main():
    files = sys.argv [1:]
    merger = PdfFileMerger()
    for f in files:
        merger.append(PdfFileReader(f), 'rb')
    merger.write('merged.pdf')



if __name__ == "__main__":
    main()