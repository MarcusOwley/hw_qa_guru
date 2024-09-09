import zipfile
import os

def create_test_files():
    files_content = {
        'pdf.pdf': b'This is PDF file',
        'csv.csv': b'This is CSV file',
        'xlsx.xlsx': b'This is XLSX file'
    }
    for filename, content in files_content.items():
        with open(filename, 'wb') as f:
            f.write(content)
    return list(files_content.keys())

def test_zip_file(add_in_zip_fixture, read_file_content_in_zip_fixture, delete_zip_fixture):
    name_files = create_test_files()
    zip_file_name = 'zip_with_files.zip'
    add_in_zip_fixture(zip_file_name, name_files)

    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        zip_content = zipf.namelist()
        assert sorted(zip_content) == sorted(name_files)

    content_files = []

    for item in name_files:
        content = read_file_content_in_zip_fixture(zip_file_name, item)
        content_files.append(content)
        if item == 'csv.csv':
            assert content == 'This is CSV file'
        elif item == 'pdf.pdf':
            assert content == 'This is PDF file'
        elif item == 'xlsx.xlsx':
            assert content == 'This is XLSX file'

    delete_zip_fixture(zip_file_name)
    for file in name_files:
        if os.path.exists(file):
            os.remove(file)