# Дана строка, содержащая полное имя файла. Выделить из этой строки название
# последнего каталога (без символов «\»). Если файл содержится в корневом каталоге,
# то вывести символ «\ ».
import os
def get_last_directory(file_path):
  try:
    directory = os.path.dirname(file_path)
    if not directory:
      return "\\"
    else:
        last_directory = os.path.basename(directory)
        return last_directory
  except:
    return None
