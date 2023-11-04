{a, _} = IO.read(:stdio,:line) |> Integer.parse
{b, _} = IO.read(:stdio,:line) |> Integer.parse
{c, _} = IO.read(:stdio,:line) |> Float.parse

IO.puts("NUMBER = #{a}\nSALARY = U$ #{:erlang.float_to_binary(b*c, [decimals: 2])}")
