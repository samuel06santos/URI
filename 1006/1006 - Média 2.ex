{a, _} = IO.read(:stdio,:line) |> Float.parse
{b, _} = IO.read(:stdio,:line) |> Float.parse
{c, _} = IO.read(:stdio,:line) |> Float.parse
IO.puts("MEDIA = #{:erlang.float_to_binary(((a*2)+(b*3)+(c*5))/10,[decimals: 1])}")
