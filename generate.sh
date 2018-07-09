# /bin/bash

for n in {1..10}; do
    echo $(( RANDOM % 10 )) >> test_files/file_"$n".txt.ignore
done
