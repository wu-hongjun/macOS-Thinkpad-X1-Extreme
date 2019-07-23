#!/bin/bash
OPTS="-vw 2095 -vw 2008 -vw 4089 -vi -vs"
IASL="./iasl"

cd "$(dirname "$0")"

for i in *.dsl; do
    j="${i/dsl/aml}"
    echo "Updating $j"
    $IASL $OPTS -p ../patched/$j $i >/dev/null 2>&1
done
