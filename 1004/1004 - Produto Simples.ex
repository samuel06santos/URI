{a, _} = IO.read(:stdio,:line) |> Integer.parse
{b, _} = IO.read(:stdio,:line) |> Integer.parse
IO.puts("PROD = #{a*b}")
