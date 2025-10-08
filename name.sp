program P;
type
  V := array[5] of integer;
  R := record
    c : integer
  end
var
  a : V;
  r : R
begin
  a[2] := 3;
  r.c := a[2];
end