{raio, _} = IO.read(:stdio,:line) |> Float.parse
IO.puts("A=#{:erlang.float_to_binary(:math.pow(raio,2)*3.14159,[decimals: 4])}")
