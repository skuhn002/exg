import tkinter
from tkinter import filedialog
from scipy.io import wavfile

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

    def get_data(self, filepath, format='BYB', debug=False):
        if format == 'BYB':
            if 'BYB_Recording' not in filepath:
                print('This may not be in BYB format')
            sample_rate, Y = wavfile.read(filepath)
            if debug:
                print('Sample Rate: ' + str(sample_rate))
                print("First 10 Samples: " + str(Y[0:10]))
            return sample_rate, Y

    def prep_files(self):
        self.files = []
        for i in range(len(self.raw_files)):
            print('File ' + str(i+1) + ': \n\t' + self.raw_files[i].name)
            filename = self.raw_files[i].name
            sample_rate, data = self.get_data(filename, format='BYB', debug=True)
            this_file = {'filename': filename, 'sample_rate': sample_rate, 'data': data}
            self.files.append(this_file)




EXG = exg()
if len(EXG.raw_files) > 0:
    print("\nEXG object named 'EXG' created")
else:
    print("\nEXG object named 'EXG' created without any data files")

EXG.prep_files()
