[a, b, c] = IO.read(:stdio,:line) |> String.trim |> String.split(" ") |> Enum.map(fn str ->
  case Integer.parse(str) do
    {number, _} -> number
  end
end)

maior = div (a + b + abs(a - b)), 2
maior2 = div (maior + c + abs(maior - c)), 2
IO.puts "#{maior2} eh o maior"
