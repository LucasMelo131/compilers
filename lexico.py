import ply.lex as lex

# Palavras reservadas
reserved = {
    'program': 'PROGRAM',
    'begin': 'BEGIN',
    'end': 'END',
    'const': 'CONST',
    'type': 'TYPE',
    'integer': 'INTEGER',
    'real': 'REAL',
    'array': 'ARRAY',
    'of': 'OF',
    'record': 'RECORD',
    'var': 'VAR',
    'function': 'FUNCTION',
    'while': 'WHILE',
    'if': 'IF',
    'then': 'THEN',
    'write': 'WRITE',
    'read': 'READ',
    'else': 'ELSE',
}

# Lista de tokens
tokens = [
    # Constantes e identificadores
    'STRING',
    'ID',
    'NUMERO',

    # Delimitadores
    'PV',         # ;
    'ABRE_COL',   # [
    'FECHA_COL',  # ]
    'DP',         # :
    'VIRG',       # ,
    'ABRE_PAR',   # (
    'FECHA_PAR',  # )

    # Operadores
    'ATRIB',      # :=
    'OP_LOG',     # operadores lógicos/relacionais
    'OP_MAT',     # + - * /
] + list(set(reserved.values()))

# Regras simples (tokens de 1-2 chars que não conflitam)
t_PV        = r';'
t_ABRE_COL  = r'\['
t_FECHA_COL = r'\]'
t_DP        = r':'
t_VIRG      = r','
t_ABRE_PAR  = r'\('
t_FECHA_PAR = r'\)'

# Operador de atribuição := (precisa vir antes de DP e =)
t_ATRIB     = r':='

# Operadores matemáticos
t_OP_MAT    = r'[\+\-\*/]'

# Operadores lógicos/relacionais:
# cobre: <= >= <> == = < > !
# Nota: muitas gramáticas Pascal-like usam <> para “diferente”.
def t_OP_LOG(t):
    r'(<=|>=|<>|==|=|<|>|!)'
    return t

# String entre aspas duplas, aceita caracteres alfanuméricos e espaços simples
# Caso precise aceitar escape, estenda a regex/lógica.
def t_STRING(t):
    r'"[^"\n]*"'
    # Remova aspas se desejar: t.value = t.value[1:-1]
    return t

# Número: dígitos com no máximo um ponto
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    # Pode converter para float/int, conforme desejado:
    # t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Identificadores e palavras reservadas
def t_ID(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    lower = t.value.lower()
    tok = reserved.get(lower)
    if tok:
        # Para integer/real, ambos viram TIPO_NUM
        t.type = tok
    else:
        t.type = 'ID'
    return t

# Comentários:
# 1) Estilo // até fim da linha
def t_COMMENT_LINE(t):
    r'//[^\n]*'
    pass

# 2) Estilo { ... }
def t_COMMENT_BRACES(t):
    r'\{[^}]*\}'
    # Se quiser contabilizar linhas dentro do comentário, faça:
    t.lexer.lineno += t.value.count('\n')
    pass

# Ignorar espaços e tabs
t_ignore = ' \t'

# Contar novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Erros léxicos
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

def build_lexer(**kwargs):
    return lex.lex(**kwargs)
 
def print_tokens_table(source_code: str):
    lexer = build_lexer()
    lexer.input(source_code)

    # Cabeçalho
    col1, col2, col3 = "Linha", "Token", "Lexema"
    # Larguras mínimas para alinhamento
    w1, w2, w3 = 7, 14, 30

    def fmt(s, w):
        s = str(s)
        if len(s) > w:
            return s[: w - 1] + "…"
        return s

    header = f"{col1:<{w1}} | {col2:<{w2}} | {col3}"
    sep = "-" * len(header)
    print(header)
    print(sep)

    for t in lexer:
        line = t.lineno
        tok_type = t.type
        lexema = t.value
        print(f"{str(line):<{w1}} | {fmt(tok_type, w2):<{w2}} | {lexema}")

if __name__ == '__main__':
    with open('teste.sp', 'r', encoding='utf-8', errors='replace') as f:
        data = f.read()
    print_tokens_table(data)