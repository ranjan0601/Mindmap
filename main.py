
from PyPDF2 import PdfReader, PdfWriter


chap1 =  list(range(17,31))
chap2 = list(range(31, 44))
chap3 = list(range(44, 64))
chap4 = list(range(64, 88))

with open("NISM_IA_Lev1_Mar_25.pdf", "rb") as f:
    reader = PdfReader(f)
    c1writer = PdfWriter()
    c2writer = PdfWriter()
    c3writer = PdfWriter()
    c4writer = PdfWriter()

    for page_number in range(len(reader.pages)):
        if page_number in chap1:
            c1writer.add_page(reader.pages[page_number])
        elif page_number in chap2:
            c2writer.add_page(reader.pages[page_number])
        elif page_number in chap3:
            c3writer.add_page(reader.pages[page_number])
        elif page_number in chap4:
            c4writer.add_page(reader.pages[page_number])
        

        with open("chap1.pdf", "wb") as f2:
            c1writer.write(f2)

        with open("chap2.pdf", "wb") as f2:
            c2writer.write(f2)

        with open("chap3.pdf", "wb") as f2:
            c3writer.write(f2)

        with open("chap4.pdf", "wb") as f2:
            c4writer.write(f2)
