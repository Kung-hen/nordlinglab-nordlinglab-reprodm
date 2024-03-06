from PyPDF2 import PdfFileReader,PdfFileWriter

file_path = "input_2.pdf"
pdf = PdfFileReader(file_path)

with open("output.txt","w") as f :
    for  i in range(pdf.numPages) :
        # print("Page : {0}".format(i))
        pageobj = pdf.getPage(i)

        try : 
            txt = pageobj.extractText()
            print(" ".center(100,"-"))
        except : 
            pass
        else : 
            f.write("Page {0}\n".format(i + 1))
            f.write(" ".center(100,"-"))
            f.write(txt)

    f.close()    