[a, b, c, d] = IO.read(:stdio,:line) |> String.trim |> String.split |> Enum.map(fn str ->
  case Float.parse str  do
    {number, _} -> number
  end
end)

media1 = (a*2 + b*3 + c*4 + d) / Enum.sum [2, 3, 4, 1]
IO.puts "Media: #{:erlang.float_to_binary(media1, [decimals: 1])}"

if media1 >= 7.0, do: IO.puts "Aluno aprovado."
if media1 < 5.0, do: IO.puts "Aluno reprovado."
if media1 >= 5.0 && media1 <= 6.9 do
  IO.puts("Aluno em exame.")
  {n, _} = IO.read(:stdio,:line) |> String.trim |> Float.parse
  IO.puts "Nota do exame: #{:erlang.float_to_binary(n, [decimals: 1])}"
  
  media2 = (media1+n)/2
  if media2 >= 5.0, do: IO.puts "Aluno aprovado."
  if media2 <= 4.9, do: IO.puts "Aluno reprovado."
    IO.puts "Media final: #{:erlang.float_to_binary(media2, [decimals: 1])}"
end
