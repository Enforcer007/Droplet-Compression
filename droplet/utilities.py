import os



class Directories:

    def __init__(self,path):
        self.path = path
        self.directories = os.walk(self.path)

    def traverse_directories(self):
        files_list = []
        for i in self.directories:
            for j in i[2]:
                files_list.append(i[0]+'/'+j)
        return files_list

    @staticmethod
    def determine_format(path_file):
        path , file = os.path.split(path_file)
        return file.split('.')[-1]

    @staticmethod
    def _get_rootdir(path_file):
        while True:
            path , file = os.path.split(path_file)
            print(path, file)
            if file == path_file:
                return '.'
            elif path == path_file:
                return path
            else:
                path_file = path

    @classmethod
    def get_output_path(cls,path_file):
        path, file = os.path.split(path_file)
        path_root = cls._get_rootdir(path_file)
        file_name, format = file.split('.')
        return path+'/'+file_name+'_compress.'+format, path_root

if __name__ == '__main__':
    directories = Directories('./Test_Folder')
    #print(list(directories.traverse_directories()))
    print(Directories.get_output_path('./Test_Folder/books/Foundations of DS.pdf'))