# https://codeforces.com/contest/4/problem/A

input = gets.chomp.to_i

if input <= 2
  puts "No"
  exit
end

out = input % 2

if out == 0
  puts "Yes"
else
  puts "No"
end

