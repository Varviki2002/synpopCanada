#!/bin/bash

provinces=( 10 11 12 13 24 35 46 47 48 59 60 61 62 )
da_nb=( 1073 295 1658 1454 13658 20160 2183 2474 5803 7617 67 98 50 )
years=( 2016 2021 2022 2030 )

index=0
for p in "${provinces[@]}"
do
  nb=("${da_nb[$index]}")
	nb=$((nb+1000))
	for i in $(eval echo "{0..$nb..1000}")
	do
    for j in "${years[@]}"
    do
        qsub launch_assign_hhtype.sh /nobackup/geompr/Canada $p $i $j
    done
  done
	index=$((index+1))
done
