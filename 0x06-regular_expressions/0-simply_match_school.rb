#!/usr/bin/env ruby

# ARGV[0] contains the command-line argument
# the `scan` method is used in finding all occurences of the pattern in the input
# the 'join` method is used to concatenate them into a string

puts ARGV[0].scan(/School/).join
