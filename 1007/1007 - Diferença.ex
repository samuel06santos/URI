{a,_} = IO.read(:stdio,:line) |> Integer.parse
{b,_} = IO.read(:stdio,:line) |> Integer.parse
{c,_} = IO.read(:stdio,:line) |> Integer.parse
{d,_} = IO.read(:stdio,:line) |> Integer.parse
r = (a*b)-(c*d)
IO.puts("DIFERENCA = #{r}")
