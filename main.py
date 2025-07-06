from organizer.core import organize_by_extension
from organizer.__version__ import __version__
from argparse import ArgumentParser 

def main():
    parser = ArgumentParser(prog = 'File Organizer', description = 'Organizes folder files by extension')
    parser.add_argument('path', help = 'Path of folder to be organized')
    parser.add_argument('-m', '--mode', choices = ['extension'], default = 'extension', help = 'Organization mode (default: extension)')
    parser.add_argument('-s', '--simulate', action = 'store_true', help = 'Simulates organization without actually moving files')
    parser.add_argument('-V', '--version', action = 'version', version = f'%(prog)s {__version__}')
    parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Shows files being organized')

    args = parser.parse_args() 
    
    try:
        if args.mode == 'extension':
            organize_by_extension(args.path, simulate = args.simulate, verbose = args.verbose)
        else:
            print(f"Invalid Organization Mode: '{args.mode}'")
    except Exception as error:
        print(f'[ERROR] {error}')

if __name__ == '__main__':
    main() 
