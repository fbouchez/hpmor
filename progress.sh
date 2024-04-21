#!/bin/bash


current=$(cat chapters/hpmor-chapter-???.tex | sed '/% STOP HERE/q' | wc -w)

total=$(cat chapters/hpmor-chapter-???.tex | wc -w)

echo "Mots revisités: $current"
echo "Mots total: $total"

# percent=$(expr $current \* 100 / $total)
percent=$(echo "scale = 2; $current * 100 / $total" | bc)

echo "Progrès: $percent %"

