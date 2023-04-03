{v1, _} = IO.read(:stdio,:line) |> Integer.parse
{v2, _} = IO.read(:stdio,:line) |> Integer.parse
IO.puts("X = #{v1+v2}")
