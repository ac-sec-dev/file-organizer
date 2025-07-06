# 📁 File Organizer 
Automatically organize your files by **extension** with just one command!<br>
Simple, efficient, with **simulation** support, **verbose mode**, and ready to expand with new filters (like date, size, and recursive organization).


## 🚀 Funcionalidades

✅ File organization by **extension**<br>
✅ **CLI supporte** using `argparse`<br>
✅ **Dry-run mode** to test without moving files<br> 
✅ **Verbose:** Logs detailed execution steps<br> 
✅ Modular structure, test-ready<br> 
✅ Automated tests with `pytest`

📦 Ready for future updates

## 📦 Instalação
Clone the repository:
```bash
git clone https://github.com/ac-sec-dev/file-organizer.git
cd file-organizer
```

Install the required modules:
```bash
pip install -r requirements.txt
```
> *ℹ️ Since this version only uses `pytest` as an external library, there are no mandatory dependencies if you won't run tests*

## 🧠 Uso 
Run the program pointing to the folder you want to organize:

```bash 
python main.py <path> [options]
```

## 🔧 Opções Disponíveis 

|   Opção    | Descrição |
|------------|-----------|
|`-m, --mode` | Organization mode (default: extension)|
|`-s, --simulate` | Simulates reorganization without moving files |
|`-v, --verbose` | Shows detailed file processing |
| `-V, --version` | Displays program version |

## 📌 Exemplos 
```bash
python main.py C:/MyFiles --mode extension --verbose
```

## 🛠️ File Tree
```
file-organizer/
├── main.py
├── organizar/
│   ├── __init__.py
│   ├── core.py
│   ├── config.py
│   ├── utils.py
│   └── __version.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── README.md
├── .gitignore
├── LICENSE
└── requirements.txt
```

## 📄 License
This project is licensed under the MIT License. Feel free to use, modify and distribute it.

## 🤝 Contributing 
Contributions are welcome! Some ideas for future features:

📂 Recursive organization (subfolders)<br>
⏱️ Filter by modification date<br> 
📏 Filter by file size<br> 
📑 Action logging<br>
⏪ Undo organization<br> 
🖼️ Graphical interface (GUI)

Open an *issue* with suggestions or submit a *pull request* 

## ✨ Author 
**Alecsander Moraes Santos de Oliveira**<br>
[GitHub](https://github.com/ac-sec-dev) • [Instagram](https://instagram.com/ac.dev) • `ac.dev`
