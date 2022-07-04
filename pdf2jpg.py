# install
# pip install pdf2image
# import module
from pdf2image import convert_from_path
from sys import argv


if len(argv) > 1:
    pdf_file = argv[1]
else:
    pdf_file = input('pdf file path>>> ')

try:
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_file)
    #print(pdf_file)
    #exit()
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(pdf_file + str(i) + '.jpg', 'JPEG')

except FileNotFoundError:
    print(f'{argv[1]} not found')

except TypeError as error:
    print(error)


