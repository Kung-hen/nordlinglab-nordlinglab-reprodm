import pdftotext

# Load your PDF
with open("input.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
#with open("secure.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f, "secret")

# How many pages?
print("There are {} pages.".format(len(pdf)))

# Iterate over all the pages


with open("outputtext.txt", "w") as o:
    for page in pdf:
        print(page)
        o.write(page)
    o.close()
# Read some individual pages
# print(pdf[0])
# print(pdf[1])

# Read all the text into one string
# print("\n\n".join(pdf))