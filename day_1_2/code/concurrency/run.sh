#!/bin/bash

set -e
n=$1

for i in $(seq 1 ${n})
do
    cmd="mcreate /concurrent-services{dev$i}"
    ncs_cmd -u admin -c "$cmd" &
    worker_pid=$!
    echo "Service: create dev$i, worker $worker_pid"
done
wait
