import os
from pdf2image import convert_from_path


def pdf2img(pdfpath, temp_img_path):
    try:
        pages = convert_from_path(pdfpath, 500)

        image_counter = 0

        for page in pages:
            filename = "page_" + str(image_counter + 1) + ".jpg"

            page.save(os.path.join(temp_img_path, filename), "JPEG")
            image_counter = image_counter + 1
    except:
        print("Error in converting doc to img: " + str(pdfpath))