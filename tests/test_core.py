from organizer.core import organize_by_extension
from organizer.config import EXTENSION_MAP 
from pathlib import Path 
import tempfile, shutil 

def create_test_file(path: Path, name: str):
    (path / name).write_text('Test File')

def test_organize_by_extension():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)

        create_test_file(tmp_path, 'photo.jpg')
        create_test_file(tmp_path, 'document.pdf')
        create_test_file(tmp_path, 'table.xlsx')
        create_test_file(tmp_path, 'script.txt')
        create_test_file(tmp_path, 'music.mp3')
        create_test_file(tmp_path, 'code.py')
        create_test_file(tmp_path, 'strange.file')
        
        organize_by_extension(tmp_path)
        
        assert (tmp_path / 'Images' / 'photo.jpg').exists()
        assert (tmp_path / 'Documents' / 'document.pdf').exists()
        assert (tmp_path / 'Spreadsheets' / 'table.xlsx').exists()
        assert (tmp_path / 'Documents' / 'script.txt').exists()
        assert (tmp_path / 'Audios' / 'music.mp3').exists()
        assert (tmp_path / 'Python' / 'code.py').exists()
        assert (tmp_path / 'Outros' / 'strange.file').exists()

        assert not (tmp_path / 'photo.jpg').exists()
