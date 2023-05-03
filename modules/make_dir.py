import os


def make_temp_dir(dir_path):
    try:
        if not os.path.exists(os.path.join(dir_path, "temp_img")):
            os.makedirs(os.path.join(dir_path, "temp_img"))
        return os.path.join(dir_path, "temp_img")
    except:
        print("Error in making temp dir: " + str(dir_path))

def make_entity_dir(dir_path):
    try:
        parent_dir = os.path.dirname(dir_path)
        if not os.path.exists(os.path.join(parent_dir, "regex_entity")):
            os.makedirs(os.path.join(parent_dir, "regex_entity"))
        return os.path.join(parent_dir, "regex_entity")
    except:
        print("Error in making entity dir: " + str(dir_path))
