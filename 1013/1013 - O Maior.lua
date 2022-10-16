abc = {}
for i in string.gmatch(io.read() , "%S+") do
  table.insert(abc, tonumber(i))
end
maior = (abc[1] + abc[2] + math.abs(abc[1] - abc[2]))/2
maior2 = (maior + abc[3] + math.abs(maior - abc[3]))/2
print(string.format("%.0f eh o maior", maior2))
