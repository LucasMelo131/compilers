from lark import Lark, Transformer, v_args

with open('pascal.lark', 'r', encoding='utf-8') as f:
    grammar = f.read()

parser = Lark(grammar, start='start', parser='lalr')

def parse_source(code: str):
    return parser.parse(code)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python parser.py <source_file>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        src = f.read()
    tree = parse_source(src)
    # Print the tree; for large input this can be big
    print(tree.pretty())