a, b = gets.split(' ').map(&:to_i)
ans = 0
while a != b
  a, b = b, a if b > a

  mod = a % b
  if mod == 0
    ans += (a - b) / b
    break
  else
    ans += a / b
    a = mod
  end
end

puts ans
