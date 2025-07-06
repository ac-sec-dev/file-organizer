from pathlib import Path 
import subprocess 
import tempfile 
import shutil 
import sys 

def create_test_file(path: Path, name: str):
    (path / name).write_text('File Test')

def test_cli_organize_by_extension():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)
        
        create_test_file(tmp_path, 'photo.jpg')
        create_test_file(tmp_path, 'document.pdf')
        create_test_file(tmp_path, 'script.py')
        create_test_file(tmp_path, 'unknown.xxx')

        result = subprocess.run(
            [sys.executable, 'main.py', str(tmp_path), '--mode', 'extension', '--verbose'],
            capture_output = True, 
            text = True
        )
        
        assert result.returncode == 0 
        assert 'photo.jpg' in result.stdout 
        assert 'document.pdf' in result.stdout 
        assert 'script.py' in result.stdout 
        assert 'unknown.xxx' in result.stdout
        
        assert (tmp_path / 'Images' / 'photo.jpg').exists()
        assert (tmp_path / 'Documents' / 'document.pdf').exists()
        assert (tmp_path / 'Python' / 'script.py').exists()
        assert (tmp_path / 'Outros' / 'unknown.xxx').exists()

def test_cli_simulate_dry_run():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)
        
        create_test_file(tmp_path, 'music.mp3')
        
        result = subprocess.run(
            [sys.executable, 'main.py', str(tmp_path), '--mode', 'extension', '--simulate', '--verbose'],
            capture_output = True, 
            text = True
        )
        
        assert result.returncode == 0 
        assert 'music.mp3' in result.stdout 
        
        assert (tmp_path / 'music.mp3').exists()
        assert not (tmp_path / 'Audios').exists()
