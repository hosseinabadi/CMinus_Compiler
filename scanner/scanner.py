from .file_reader import FileReader

fr = FileReader(patch="input.txt")
while True:
    fr.load_backup_line()

