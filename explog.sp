program P;
var
  x : integer
begin
  if x > 0 then
    x := x + 1
  else
    x := 0;

  while x < 10 begin
    x := x + 1;
  end;
end