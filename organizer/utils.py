from pathlib import Path 

def getCategory(extension, extension_map):
    for category, extensions in extension_map.items():
        if extension.lower() in extensions:
            return category 
    return 'Outros'

def EnsureFolder(path: Path):
    if not path.exists():
        path.mkdir(parents = True)
