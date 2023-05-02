import os
import glob
from pdf2image import convert_from_path

from modules.pdf_to_image import pdf2img
from modules.make_temp_dir import make_temp_dir
from modules.image_to_txt import image_to_text


def parse_all(docDir, txtDir):
    for doc in os.listdir(docDir):
        try:
            fileExtension = doc.split(".")[-1]

            if fileExtension == "pdf":
                temp_img_path = make_temp_dir(docDir)
                pdfFilename = docDir + "/" + doc
                pdf2img(pdfFilename, temp_img_path)
                image_to_text(temp_img_path, txtDir)

            else:
                print("Only pdf files are supported.")
        except:
            print("Error in file: " + str(doc))

        finally:
            for f in glob.glob(temp_img_path + "/*"):
                os.remove(f)


docDir = f"/home/punitsureka/Desktop/talview/OCR/tesseract/data/docs_to_parse"
txtDir = f"/home/punitsureka/Desktop/talview/OCR/tesseract/data/docs_parsed"

parse_all(docDir, txtDir)
