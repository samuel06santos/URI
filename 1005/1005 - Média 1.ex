{a, _} = IO.read(:stdio,:line) |> Float.parse
{b, _} = IO.read(:stdio,:line) |> Float.parse
a = a * 3.5
b = b * 7.5
IO.puts("MEDIA = #{:erlang.float_to_binary((a+b)/11,[decimals: 5])}")
