import os
import zipfile
import pytest


@pytest.fixture
def create_tmp_dir():
    tmp_dir = 'tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    return tmp_dir


@pytest.fixture
def create_test_files(create_tmp_dir):
    tmp_dir = create_tmp_dir

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


@pytest.fixture
def add_in_zip():
    def add_in_zip(zip_name, files):
        with zipfile.ZipFile(zip_name, 'a') as zip_write:
            for file in files:
                zip_write.write(file)

    return add_in_zip


@pytest.fixture
def read_file_content_in_zip():
    def read_file_content_in_zip(zip_name, file):
        with zipfile.ZipFile(zip_name, 'r') as zip_read:
            with zip_read.open(file) as file:
                file_content = file.read()
                return file_content.decode('utf-8')

    return read_file_content_in_zip


@pytest.fixture
def delete_zip():
    def delete_zip(zip_name):
        if os.path.exists(zip_name):
            os.remove(zip_name)

    return delete_zip


###