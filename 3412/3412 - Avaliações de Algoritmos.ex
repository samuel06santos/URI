defmodule Modulo do

  def calcula_nota([a]), do: a/2
  def calcula_nota(lista) when length(lista) in 2..3 do
    Enum.sum(lista) / length(lista)
  end
  def calcula_nota([a, b, c, d]) do
    lista_notas = [a, b, c]
    minimo_valor = Enum.min(lista_notas)
    minimo_valor_indx = Enum.find_index(lista_notas, fn n -> n == minimo_valor end)
    
    if d > minimo_valor do
      lista_notas = List.replace_at(lista_notas, minimo_valor_indx, d)
      media = (Enum.sum(lista_notas) / length(lista_notas))
      Float.round(media, 1)
    else
      media = (Enum.sum(lista_notas) / length(lista_notas))
      Float.round(media, 1)
    end
  end

  def ler_entradas(0), do: []
  def ler_entradas(c) when c > 0 do
    nome = IO.read(:stdio,:line) |> String.trim
    
    notas = IO.read(:stdio,:line) |> String.trim |> String.split(" ") |> Enum.map(fn str ->
      case Float.parse(str) do
        {number, _} -> number
      end
    end)
    
    nota_final = :erlang.float_to_binary(calcula_nota(notas), [decimals: 1])
    IO.puts("#{nome}: #{nota_final}")
    
    ler_entradas(c - 1)
  end
  
end

{c, _} = IO.read(:stdio,:line) |> Integer.parse

Modulo.ler_entradas(c)
