#!/usr/bin/env ruby
# Regular expression that will match the expression /hbtn/ with single or multiple t's

puts ARGV[0].scan(/hbt{1,}n/).join
