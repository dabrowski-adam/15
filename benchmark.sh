#!/usr/bin/env bash

# If a file is given, print there
# Otherwise, use /dev/stdout
file=${1:-/dev/stdout}

printf "Benchmark\n\n" > "$file"

printf "8\n\n" >> "$file"

{
  printf -- "--bfs R\n"
  ./puzzle.py --input=sample_input.txt --bfs R --verbose
  printf "\n\n"
} >> "$file"

{
  printf -- "--dfs R\n"
  ./puzzle.py --input=sample_input.txt --dfs R --verbose
  printf "\n\n"
} >> "$file"

{
  printf -- "--idfs R\n"
  ./puzzle.py --input=sample_input.txt --idfs R --verbose
  printf "\n\n"
} >> "$file"

{
  printf -- "--astar 0\n"
  ./puzzle.py --input=sample_input.txt --astar 0 --verbose
  printf "\n\n"
} >> "$file"

{
  printf -- "--astar 1\n"
  ./puzzle.py --input=sample_input.txt --astar 1 --verbose
  printf "\n\n"
} >> "$file"

{
  printf -- "--astar 2\n"
  ./puzzle.py --input=sample_input.txt --astar 2 --verbose
  printf "\n\n"
} >> "$file"

printf "\n" >> "$file"

#printf "15\n\n" >> "$file"
#
#{
#  printf -- "--bfs R\n"
#  ./puzzle.py --input=sample_input_15.txt --bfs R --verbose
#  printf "\n\n"
#} >> "$file"
#
#{
#  printf -- "--dfs R\n"
#  ./puzzle.py --input=sample_input_15.txt --dfs R --verbose
#  printf "\n\n"
#} >> "$file"
#
#{
#  printf -- "--idfs R\n"
#  ./puzzle.py --input=sample_input_15.txt --idfs R --verbose
#  printf "\n\n"
#} >> "$file"
#
#{
#  printf -- "--astar 0\n"
#  ./puzzle.py --input=sample_input_15.txt --astar 0 --verbose
#  printf "\n\n"
#} >> "$file"
#
#{
#  printf -- "--astar 1\n"
#  ./puzzle.py --input=sample_input_15.txt --astar 1 --verbose
#  printf "\n\n"
#} >> "$file"
#
#{
#  printf -- "--astar 2\n"
#  ./puzzle.py --input=sample_input_15.txt --astar 2 --verbose
#  printf "\n\n"
#} >> "$file"