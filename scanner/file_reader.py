class FileReader:
    def __init__(self, patch):
        self.file = open(patch, 'r')
        self.backup_line = ""
        self.load_backup_line()
        self.current_char = 0
        self.current_line = -1

    def load_backup_line(self):
        self.backup_line = self.file.readline()
        self.current_char = 0
        self.current_line += 1
        print(self.current_line)

    def forward_read(self):
        ...

    def backward_read(self):
        ...

