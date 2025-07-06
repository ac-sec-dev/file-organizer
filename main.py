from organizer.core import organize_by_extension
import sys

def main():
    if len(sys.argv) < 2:
        print('Uso: python main.py <path_to_organize>')
        return 
    path = sys.argv[1]
    
    try:
        organize_by_extension(path)
        print(f'Arquivos organizados com sucesso em: {path}')
    except Exception as error:
        print(f'Erro ao organizar arquivos: {error}')

if __name__ == '__main__':
    main() 

