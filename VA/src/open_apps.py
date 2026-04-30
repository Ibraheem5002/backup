import os

def open_app(app_name):
    try:
        os.startfile(app_name)
        # subprocess.Popen(app_name)

    except FileNotFoundError:
        print("ERROR: no such app exists")