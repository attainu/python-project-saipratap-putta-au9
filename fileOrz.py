import os
import shutil
from datetime import datetime
import time
from stat import ST_SIZE


class Junk_file_organizer:
    # recursively list out all the files.
    def get_Data(self, path):
        file_Data = []
        for file in os.scandir(path):
            if not file.is_dir():
                fileName = file.name
                filePath = file.path
                fileExtension = fileName.split('.')[-1]
                fileSize = os.stat(filePath)[ST_SIZE]
                file_Data.append([fileName, filePath, fileExtension, fileSize])
            else:
                file_Data + [data for data in (self.get_Data(file.path))]

        return file_Data

    # For organize files by their extension
    def byExtension(self, path, Data, organizedPath):
        for data in Data:
            fileName = data[0]
            filePath = data[1]
            extension = data[2]

            if not os.path.exists(organizedPath + extension):
                os.makedirs(organizedPath + extension)

            shutil.move(filePath, organizedPath + extension + '/' + fileName)
    
    # For organize files by size
    def bySize(self, path, Data, organizedPath):
        for data in Data:
            fileName = data[0]
            filePath = data[1]
            size = data[3]

            if 0 <= size < 1000:  # bytes
                if not os.path.exists(organizedPath + 'BYTES'):
                    os.makedirs(organizedPath + 'BYTES')

                shutil.move(filePath, organizedPath + 'BYTES/' + fileName)

            elif 1000 < size < 1000000:  # KiloBytes
                if not os.path.exists(organizedPath + 'KB'):
                    os.makedirs(organizedPath + 'KB')

                shutil.move(filePath, organizedPath + 'KB/' + fileName)

            elif 1000000 < size < 100000000:  # MegaBytes
                if not os.path.exists(organizedPath + 'MB'):
                    os.makedirs(organizedPath + 'MB')

                shutil.move(filePath, organizedPath + 'MB/' + fileName)

            # If any file more than 100 MB
            else:
                if not os.path.exists(organizedPath + 'more than MB'):
                    os.makedirs(organizedPath + 'more than MB')

                shutil.move(filePath, organizedPath +
                'more than MB/' + fileName)

    # For organize files by date
 
    def bydate(self, path, Data, organizedPath):

        name = os.listdir(path)
        name.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
        files = [f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))]

        os.chdir(path)

        for x in files:

            # Get the creation time

            create_time = time.ctime(os.path.getmtime(os.path.join(path, x)))
            create_dt = datetime.strptime(create_time, '%a %b %d %H:%M:%S %Y')
            modified_date = str(create_dt.day) + '-' + str(
                            create_dt.month) + '-' + str(create_dt.year)

            if(os.path.isdir(organizedPath + modified_date)):
                shutil.move(os.path.join(path, x),
                organizedPath + modified_date)

            else:

                os.makedirs(organizedPath + modified_date)
                shutil.move(os.path.join(path, x),
                organizedPath + modified_date)

    def organize(self):
        path = input('Enter the Path: ')
        organizeBy = input('Enter the option(ext or size or date): ')

        # For exception handling during wrong path input
        try:
            Data = self.get_Data(path)
        except FileNotFoundError:
            print('Invalid path directory')
            return

        if not os.path.exists(path + '/organized'):
            os.makedirs(path + '/organized')
        organizedPath = path + '/organized/'

        if organizeBy == 'ext':
            self.byExtension(path, Data, organizedPath)
        elif organizeBy == 'size':
            self.bySize(path, Data, organizedPath)
        elif organizeBy == 'date':
            self.bydate(path, Data, organizedPath)


if __name__ == "__main__":

    junk_file_orz = Junk_file_organizer()
    junk_file_orz.organize()
