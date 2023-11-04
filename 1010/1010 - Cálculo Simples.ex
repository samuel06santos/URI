a = IO.read(:stdio,:line) |> String.trim |> String.split(" ") |> Enum.map(fn str ->
  case Float.parse(str) do
    {number, ""} -> number
  end
end)
  
b = IO.read(:stdio,:line) |> String.trim |> String.split(" ") |> Enum.map(fn str ->
  case Float.parse(str) do
    {number, ""} -> number
  end
end)


[_, u1, v1] = a
[_, u2, v2] = b
  
IO.puts "VALOR A PAGAR: R$ #{:erlang.float_to_binary(((u1*v1)+(u2*v2)), [decimals: 2])}"
