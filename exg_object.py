import tkinter
from tkinter import filedialog

class exg():
    def __init__(self):
        root = tkinter.Tk()
        root.withdraw()
        self.raw_files = filedialog.askopenfiles(parent=root, mode='r',
                                            filetypes=[("All files", "*"),
                                                        ("BYB files","BYB_Recording*.wav"),
                                                        ("OpenBCI files", ["OpenBCI*.txt", "OpenBCI*.bdf"]),
                                                        ("Excel file","*.xls")],
                                             title='Choose an excel file')
        if len(self.raw_files) > 0:
            print("File(s): ")
            for i in range(len(self.raw_files)):
                print("\t" + self.raw_files[0].name)

    def prep_files(self):
        self.files = []
        junk = "Hi, I'm junk"
        for i in range(len(self.raw_files)):
            print('File ' + str(i+1) + ': \n\t' + self.raw_files[i].name)
            filename = self.raw_files[i].name
            this_file = {'filename': filename}
            self.files.append(this_file)



EXG = exg()
if len(EXG.raw_files) > 0:
    print("\nEXG object named 'EXG' created")
else:
    print("\nEXG object named 'EXG' created without any data files")
