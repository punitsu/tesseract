import os
import glob

from modules.pdf_to_image import pdf2img
from modules.make_dir import make_temp_dir, make_entity_dir
from modules.image_to_txt import image_to_text
from modules.entity_extractor import extract_resume_info


def parse_all(docDir, txtDir, extractor):
    for doc in os.listdir(docDir):
        try:
            fileExtension = doc.split(".")[-1]
            fileName = doc.split(".")[0]

            if fileExtension == "pdf":
                temp_img_path = make_temp_dir(docDir)
                pdfFilename = docDir + "/" + doc
                pdf2img(pdfFilename, temp_img_path)
                image_to_text(temp_img_path, txtDir, fileName)

            else:
                print("Only pdf files are supported.")
        except:
            print("Error in file: " + str(doc))

        finally:
            for f in glob.glob(temp_img_path + "/*"):
                os.remove(f)

    if extractor == "regex":
        try:
            entDir = make_entity_dir(txtDir)
            extract_resume_info(txtDir, entDir)
        except:
            print("Error finding entities from : " + str(txtDir))


if __name__ == "__main__":
    docDir = f"/home/punitsureka/Desktop/talview/OCR/tesseract/data/docs_to_parse"
    txtDir = f"/home/punitsureka/Desktop/talview/OCR/tesseract/data/docs_parsed"

    extractor = "regex"  # or 'NER'

    parse_all(docDir, txtDir, extractor)
