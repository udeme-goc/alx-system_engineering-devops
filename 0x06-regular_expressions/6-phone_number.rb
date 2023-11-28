#!/usr/bin/env ruby
# 10 digit phone number validator

puts ARGV[0].scan(/^[0-9]{10}$/).join
