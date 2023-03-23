import os
from datetime import datetime, timedelta

def remove_old_files(directory, age_threshold, keep_days, exclude_dirs):
    current_time = datetime.now()

    for root, dirs, files in os.walk(directory):
        # Проверяем, является ли текущая директория исключенной
        if any(exclude_dir.lower() in root.lower() for exclude_dir in exclude_dirs):
            continue

        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Получаем время изменения файла (mtime)
            mtime = os.path.getmtime(file_path)
            file_mtime = datetime.fromtimestamp(mtime)

            # Проверяем возраст файла и сохраняем файлы за 1-е и 15-е число
            if (current_time - file_mtime) > age_threshold and file_mtime.day not in keep_days:
                os.remove(file_path)
                print(f"Удален файл: {file_path}")

if __name__ == "__main__":
    directory = "path/to/your/test/folder"  # Укажите путь к папке с тестовыми файлами
    age_threshold = timedelta(days=45)  # Удаляем файлы старше 45 дней (полтора месяца)
    keep_days = [1, 15]  # Оставляем файлы за 1-е и 15-е число каждого месяца
    exclude_dirs = ["exclude_folder1", "exclude_folder2"]  # Укажите папки, которые следует исключить

    remove_old_files(directory, age_threshold, keep_days, exclude_dirs)
