#!/bin/bash

for ((i=0; i<20; i++))
do
  echo $i
  python abc301/d.py < abc301/dsample$i.txt
  python abc301/d_01.py < abc301/dsample$i.txt
  echo ""
done
