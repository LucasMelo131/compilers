import sys
from lark import Lark

# Verifica se foi passado o nome do arquivo
if len(sys.argv) < 2:
    print("Uso: python parser.py <arquivo.sp>")
    sys.exit(1)

arquivo_entrada = sys.argv[1]

# Carrega a gramática
with open('simple_pascal_grammar.lark', 'r') as f:
    grammar = f.read()

parser = Lark(grammar, start='programa', parser='lalr')

try:
    with open(arquivo_entrada, 'r') as fi:
        teste = fi.read()
    tree = parser.parse(teste)
    print("Análise sintática bem-sucedida!")
    print("\nÁrvore sintática:")
    print(tree.pretty())
except FileNotFoundError:
    print(f"Erro: arquivo '{arquivo_entrada}' não encontrado.")
    sys.exit(1)
except Exception as e:
    print(f"Erro na análise: {e}")
    sys.exit(1)