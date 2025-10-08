program P;
var
  x : integer

function F(a : integer) : integer
begin
  a := a + 1;
end

begin
  x := F(x);
end