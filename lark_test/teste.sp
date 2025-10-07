program funcoes;
const TAM := 10;
type
vetor := array[15] of integer;
aluno := record

nota1, nota2 : real;
end

var
A, B, C, D : integer;
E : vetor;
F : aluno;
function fatorial(a:integer) : integer
var i : integer;
begin
i := 1;
result:=1;
while i < a
begin
result:=result*i;
i:=i+1;
end;
end
function exp(a: real; b: real) : real
var i : integer;
begin
i := 1;
result := a;
if b = 0 then
result := 1
else
while i < b
begin
result := a * a;
i := i + 1;
end;

end
function lerDados() : aluno
begin
write “digite as notas do aluno”;
read result.nota1;
read result.nota2;
end