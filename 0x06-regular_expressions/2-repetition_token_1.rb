#!/usr/bin/env ruby
# Output the result of scanning the first command-line argument for the pattern /hb?tn/
# ? makes b optional

puts ARGV[0].scan(/hb?tn/).join
