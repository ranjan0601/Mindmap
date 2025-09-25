
from PyPDF2 import PdfReader, PdfWriter


chap5 =  list(range((90 -1) ,(105 -1)))
chap6 = list(range((105-1), (127-1)))
chap7 = list(range((128-1), (135-1)))
chap8 = list(range((135-1), (153-1)))

with open("NISM_IA_Lev1_Mar_25.pdf", "rb") as f:
    reader = PdfReader(f)
    c1writer = PdfWriter()
    c2writer = PdfWriter()
    c3writer = PdfWriter()
    c4writer = PdfWriter()

    for page_number in range(len(reader.pages)):
        if page_number in chap5:
            c1writer.add_page(reader.pages[page_number])
        elif page_number in chap6:
            c2writer.add_page(reader.pages[page_number])
        elif page_number in chap7:
            c3writer.add_page(reader.pages[page_number])
        elif page_number in chap8:
            c4writer.add_page(reader.pages[page_number])
        

        with open("chap5.pdf", "wb") as f2:
            c1writer.write(f2)

        with open("chap6.pdf", "wb") as f2:
            c2writer.write(f2)

        with open("chap7.pdf", "wb") as f2:
            c3writer.write(f2)

        with open("chap8.pdf", "wb") as f2:
            c4writer.write(f2)
