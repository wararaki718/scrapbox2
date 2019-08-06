#!/bin/bash

if [ -z $HELLO ]; then
    HELLO=test
fi

: ${WORLD:=test}

echo $HELLO, $WORLD
