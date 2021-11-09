import PyPDF2
a = PyPDF2.PdfFileReader('SodaPDF-compressed-DLD PRAC. FILE-compressed_reduce.pdf')
#print(a.documentInfo)
x = a.getNumPages()
str = ""
for i in range(1,x):
    str += a.getPage(i).extractText()

with open("text.txt","w" , encoding='utf-8') as f:
    f.write(str)