require 'net/http'
require 'uri'
require 'json'

def main(argv)
  q = argv[0]
  uri = URI.parse('http://challenge-server.code-check.io/api/hash')
  uri.query = URI.encode_www_form({q: q})
  response = Net::HTTP.get_response(uri)
  body = response.body
  json = JSON.parse(body)
  puts json['hash']
end

main(ARGV)
