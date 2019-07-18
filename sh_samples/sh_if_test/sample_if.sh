#!/bin/bash

flag=1
if [ $flag = 1] ; then
    echo "if"
else
    echo "else"
fi

if [ $flag -ne 1 ] ; then
    echo "if"
else
    echo "else"
fi

echo "DONE"