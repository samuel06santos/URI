{r, _} = IO.read(:stdio,:line) |> Float.parse
IO.puts "VOLUME = #{:erlang.float_to_binary(((4/3) * 3.14159 * :math.pow r, 3), [decimals: 3])}"
