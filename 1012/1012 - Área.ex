[a, b, c] = IO.read(:stdio,:line) |> String.trim |> String.split(" ") |> Enum.map(fn str ->
  case Float.parse(str) do
    {number, _} -> number
  end
end)

pi = 3.14159

triangulo = (a * c) / 2 |> :erlang.float_to_binary([decimals: 3])
circulo = (pi * :math.pow c, 2) |> :erlang.float_to_binary([decimals: 3])
trapezio = ((a + b) * c) / 2 |> :erlang.float_to_binary([decimals: 3])
quadrado = (:math.pow b, 2) |> :erlang.float_to_binary([decimals: 3])
retangulo = a * b |> :erlang.float_to_binary([decimals: 3])

IO.puts "TRIANGULO: #{triangulo}\nCIRCULO: #{circulo}\nTRAPEZIO: #{trapezio}\nQUADRADO: #{quadrado}\nRETANGULO: #{retangulo}"
