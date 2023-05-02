import os


def make_temp_dir(dir_path):
    try:
        if not os.path.exists(os.path.join(dir_path, "temp_img")):
            os.makedirs(os.path.join(dir_path, "temp_img"))
        return os.path.join(dir_path, "temp_img")
    except:
        print("Error in making temp dir: " + str(dir_path))
