import argparse
from eductools.math_tools import add, subtract  # Ajustez l'import selon votre structure de package

def calcul_cli():
    parser = argparse.ArgumentParser(description="Effectue des opérations mathématiques simples.")
    parser.add_argument('a', type=int, help="Le premier nombre")
    parser.add_argument('b', type=int, help="Le second nombre")
    parser.add_argument('--operation', type=str, help="L'opération à effectuer: add ou subtract", choices=['add', 'subtract'])
    
    args = parser.parse_args()
    
    if args.operation == 'add':
        result = add(args.a, args.b)
    elif args.operation == 'subtract':
        result = subtract(args.a, args.b)
    else:
        parser.error("Opération non supportée.")
        return

    print(f'Résultat: {result}')

if __name__ == "__main__":
    calcul_cli()
