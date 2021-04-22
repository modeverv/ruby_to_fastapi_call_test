require 'net/http'

begin
    Net::HTTP.get(URI.parse('http://localhost:8000/newmail?foo=bar'))
rescue => ex
    puts "ok"
end
puts "end of program"
