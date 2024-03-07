import os
from tkinter.filedialog import askdirectory

directory = askdirectory(title="Select a directory")

list_arquives = os.listdir(directory)

locals = {
    "images": [".png", ".jpg", ".hev"],
    "sheets": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": ["csv"],
    "icons": [".svg"],
    "installer": [".exe"],
    "compact": [".zip", ".rar"]
}

for arquive in list_arquives:
    print(arquive)
    name, extension = os.path.splitext(f"{directory}/{arquive}")
    for folder in locals:
        if extension in locals[folder]:
            if not os.path.exists(f"{directory}/{folder}"):
                os.mkdir(f"{directory}/{folder}")
            os.rename(f"{directory}/{arquive}", f"{directory}/{folder}/{arquive}")