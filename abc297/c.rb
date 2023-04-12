h, w = gets.split(' ').map(&:to_i)
sarr = []
h.times do
  sarr.push(gets.chomp)
end

(0...h).each do |i|
  (0...w-1).each do |j|
    if sarr[i][j] == 'T' && sarr[i][j+1] == 'T'
      sarr[i][j] = 'P'
      sarr[i][j+1] = 'C'
    end
  end
end

sarr.each do |s|
  puts s
end
