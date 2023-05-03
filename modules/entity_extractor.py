import os
import re
from PIL import Image
from transformers import pipeline, GPT2Tokenizer

def extract_resume_info_regex(resumes_dir, output_dir):
    name_regex = r"([A-Z][a-z]+)\s([A-Z][a-z]+)"
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    phone_regex = r"\d{10}"
    years_of_exp_regex = (
        r"\b\d+\s*(years of experience|year of experience|years|year)\b"
    )
    education_regex = r"(?:(?<=in\s)|(?<=from\s)|(?<=at\s))([A-Za-z0-9\s,.&'-]+)(?:(?=\s[0-9]{4})|(?=$))"
    skills_regex = r"(?<=Skills)[\s\S]*(?=\n\n)"

    for filename in os.listdir(resumes_dir):
        with open(os.path.join(resumes_dir, filename), "r", encoding="latin1") as f:
            resume_text = f.read()

        name_match = re.search(name_regex, resume_text)
        if name_match:
            name = name_match.group(0)
        else:
            name = None

        email_match = re.search(email_regex, resume_text)
        if email_match:
            email = email_match.group(0)
        else:
            email = None

        phone_match = re.search(phone_regex, resume_text)
        if phone_match:
            phone = phone_match.group(0)
        else:
            phone = None

        years_of_exp_match = re.search(years_of_exp_regex, resume_text)
        if years_of_exp_match:
            years_of_exp = years_of_exp_match.group(0)
        else:
            years_of_exp = None

        education_match = re.findall(education_regex, resume_text)
        if education_match:
            education = [edu.strip() for edu in education_match]
        else:
            education = None

        skills_match = re.search(skills_regex, resume_text)
        if skills_match:
            skills = skills_match.group(0).replace("Skills", "").strip().split("\n")
        else:
            skills = None

        with open(os.path.join(output_dir, filename), "w") as f:
            f.write("Name: {}\n".format(name))
            f.write("Email: {}\n".format(email))
            f.write("Phone Number: {}\n".format(phone))
            f.write("Years of Experience: {}\n".format(years_of_exp))
            if education:
                f.write("Education Qualification: \n")
                for edu in education:
                    f.write("- {}\n".format(edu))
            else:
                f.write("Education Qualification: None\n")
            if skills:
                f.write("Skills: \n")
                for skill in skills:
                    f.write("- {}\n".format(skill))
            else:
                f.write("Skills: None\n")

        print("Resume information extracted from:", filename)


def extract_resume_info_NER(input_dir, output_dir):

    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    nlp = pipeline(
        "document-question-answering",
        model="impira/layoutlm-document-qa",
        tokenizer=tokenizer,
    )

    image_files = [
        f for f in os.listdir(input_dir) if f.endswith(".jpg") or f.endswith(".png")
    ]

    for image_file in image_files:
        print(image_file)
        image_path = os.path.join(input_dir, image_file)
        score_name, answer_name, start_name, end_name = nlp(
            image_path,
            "What is the Name in the document?",
        )
        print("Name:", answer_name)
