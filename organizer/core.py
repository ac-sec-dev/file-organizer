from .utils import getCategory, EnsureFolder
from .config import EXTENSION_MAP 
from pathlib import Path 
import shutil 

def organize_by_extension(base_path, simulate = False, verbose = False):
    base_path = Path(base_path)
    
    if not base_path.exists() or not base_path.is_dir():
        raise ValueError(f'Caminho Inválido: {base_path}')

    for file in base_path.iterdir():
        if file.is_file():
            ext = file.suffix 
            category = getCategory(ext, EXTENSION_MAP)
            target_folder = base_path / category
            target_path = target_folder / file.name 
            
            if verbose:
                print(f"[INFO] '{file.name}' -> '{category}/'")
            
            if not simulate:
                EnsureFolder(target_folder)
                if target_path.exists():
                    target_path = target_folder / f'{file.stem}_copy{file.suffix}'
                shutil.move(str(file), str(target_path))
