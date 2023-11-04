{x, _} = IO.read(:stdio,:line) |> Integer.parse
{y, _} = IO.read(:stdio,:line) |> Float.parse

IO.puts "#{:erlang.float_to_binary(x/y, [decimals: 3])} km/l"
