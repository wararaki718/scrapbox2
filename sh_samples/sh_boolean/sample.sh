#!/bin/bash

flag=true
if $flag ; then
    echo "flag is true"
else
    echo "flag is not true"
fi

if ! $flag ; then
    echo "flag is not true"
else
    echo "flag is true"
fi

echo "DONE"