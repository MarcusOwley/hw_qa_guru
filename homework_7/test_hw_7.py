import zipfile
import os

def test_zip_file(add_in_zip, read_file_content_in_zip, delete_zip, create_test_files):

    name_files = create_test_files

    zip_file_name = os.path.join('tmp', 'zip_with_files.zip')

    add_in_zip(zip_file_name, name_files)

    # Проверка корректности добавления файлов
    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        zip_content = zipf.namelist()
        # Приведение путей из архива к именам файлов без директории
        zip_content_files = [os.path.basename(file) for file in zip_content]
        expected_files = [os.path.basename(file) for file in name_files]
        assert sorted(zip_content_files) == sorted(expected_files)

    content_files = []
    for item in name_files:
        # Находим полный путь файла в архиве
        full_path_in_zip = [file for file in zip_content if os.path.basename(file) == os.path.basename(item)]
        if full_path_in_zip:
            content = read_file_content_in_zip(zip_file_name, full_path_in_zip[0])
            content_files.append(content)
            if os.path.basename(item) == 'csv.csv':
                assert content == 'This is CSV file'
            elif os.path.basename(item) == 'pdf.pdf':
                assert content == 'This is PDF file'
            elif os.path.basename(item) == 'xlsx.xlsx':
                assert content == 'This is XLSX file'

    assert content_files == ['This is PDF file', 'This is CSV file', 'This is XLSX file']

    delete_zip(zip_file_name)
    for file in name_files:
        if os.path.exists(file):
            os.remove(file)