import tkinter
from tkinter import filedialog

class exg():
    def __init__(self):
        root = tkinter.Tk()
        root.withdraw()
        self.files = filedialog.askopenfiles(parent=root, mode='r',
                                            filetypes=[("All files", "*"),
                                                        ("BYB files","BYB_Recording*.wav"),
                                                        ("OpenBCI files", ["OpenBCI*.txt", "OpenBCI*.bdf"]),
                                                        ("Excel file","*.xls")],
                                             title='Choose an excel file')
        if len(self.files) > 0:
            print("File(s): ")
            for i in range(len(self.files)):
                print("\t" + self.files[0].name)


EXG = exg()
if len(EXG.files) > 0:
    print("\nEXG object named 'EXG' created")
else:
    print("\nEXG object named 'EXG' created without any data files")
