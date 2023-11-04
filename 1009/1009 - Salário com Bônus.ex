_ = IO.read(:stdio,:line)
{b, _} = IO.read(:stdio,:line) |> Float.parse
{c, _} = IO.read(:stdio,:line) |> Float.parse

IO.puts("TOTAL = R$ #{:erlang.float_to_binary((c*0.15)+b, [decimals: 2])}")
