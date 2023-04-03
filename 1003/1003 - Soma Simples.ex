{a, _} = IO.read(:stdio,:line) |> Integer.parse
{b, _} = IO.read(:stdio,:line) |> Integer.parse
IO.puts("SOMA = #{a+b}")
