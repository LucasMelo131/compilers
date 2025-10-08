import sys
from lark import Lark


def load_grammar(path='simple_pascal_grammar.lark'):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erro: gramática '{path}' não encontrada.")
        sys.exit(1)


def print_lexical(parser, text):
    print("ANÁLISE LÉXICA:")
    print(f"{'Token':<15} {'Lexema':<15} {'Linha':<10}")
    print("-" * 40)
    for token in parser.lex(text):
        # token has attributes: type, value, line
        print(f"{token.type:<15} {token.value:<15} {token.line:<10}")


def print_syntax_tree(parser, text):
    try:
        tree = parser.parse(text)
        print("Análise sintática bem-sucedida!")
        print("\nÁrvore sintática:")
        print(tree.pretty())
    except Exception as e:
        print(f"Erro na análise sintática: {e}")


def interactive_menu(parser, text):
    while True:
        print("\nEscolha uma opção:")
        print("1) Análise léxica")
        print("2) Árvore sintática")
        print("3) Sair")
        escolha = input("Opção: ").strip()
        if escolha == '1':
            print_lexical(parser, text)
        elif escolha == '2':
            print_syntax_tree(parser, text)
        elif escolha == '3':
            print("Saindo.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    # se o usuário passou o arquivo como argumento, usa-o; senão pede via input
    if len(sys.argv) >= 2:
        arquivo_entrada = sys.argv[1]
    else:
        arquivo_entrada = input('Digite o caminho do arquivo .sp: ').strip()

    grammar = load_grammar()
    parser = Lark(grammar, start='programa', parser='lalr')

    try:
        with open(arquivo_entrada, 'r') as fi:
            texto = fi.read()
    except FileNotFoundError:
        print(f"Erro: arquivo '{arquivo_entrada}' não encontrado.")
        sys.exit(1)

    interactive_menu(parser, texto)


if __name__ == '__main__':
    main()
