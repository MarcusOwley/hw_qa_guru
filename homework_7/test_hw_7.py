import zipfile
import os

def create_tmp_dir():
    tmp_dir = 'tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    return tmp_dir

def create_test_files():
    tmp_dir = create_tmp_dir()

    files_content = {
        'pdf.pdf': b'This is PDF file',
        'csv.csv': b'This is CSV file',
        'xlsx.xlsx': b'This is XLSX file'
    }
    file_paths = []
    for filename, content in files_content.items():
        file_path = os.path.join(tmp_dir, filename)
        with open(file_path, 'wb') as f:
            f.write(content)
        file_paths.append(file_path)

    return file_paths

def test_zip_file(add_in_zip_fixture, read_file_content_in_zip_fixture, delete_zip_fixture):
    # Создание тестовых файлов
    name_files = create_test_files()

    # Название для zip файла в папке tmp
    zip_file_name = os.path.join('tmp', 'zip_with_files.zip')

    # Вызов добавления файлов в zip
    add_in_zip_fixture(zip_file_name, name_files)

    # Проверка корректности добавления файлов
    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        zip_content = zipf.namelist()
        # Приведение путей из архива к именам файлов без директории
        zip_content_files = [os.path.basename(file) for file in zip_content]
        expected_files = [os.path.basename(file) for file in name_files]
        assert sorted(zip_content_files) == sorted(expected_files)

    # Проверка содержимого файлов относительно самих файлов
    content_files = []
    for item in name_files:
        # Находим полный путь файла в архиве
        full_path_in_zip = [file for file in zip_content if os.path.basename(file) == os.path.basename(item)]
        if full_path_in_zip:
            content = read_file_content_in_zip_fixture(zip_file_name, full_path_in_zip[0])
            content_files.append(content)
            if os.path.basename(item) == 'csv.csv':
                assert content == 'This is CSV file'
            elif os.path.basename(item) == 'pdf.pdf':
                assert content == 'This is PDF file'
            elif os.path.basename(item) == 'xlsx.xlsx':
                assert content == 'This is XLSX file'

    # Общая проверка содержимого всех файлов
    assert content_files == ['This is PDF file', 'This is CSV file', 'This is XLSX file']

    # Удаление zip файла и тестовых файлов после проверки
    delete_zip_fixture(zip_file_name)
    for file in name_files:
        if os.path.exists(file):
            os.remove(file)