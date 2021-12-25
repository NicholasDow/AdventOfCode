#!/bin/bash
for i in {1..25}
do
    folder_name="Day${i}"
    mkdir "${folder_name}"
    cd "${folder_name}"
    for j in 1 2
    do
        part="Part${j}"
        mkdir "${part}"
        cd "${part}"
        touch "${part}.py"
        cd ..
    done
    cd ..
done