#!/bin/bash

if [ $NODE_ENV = "production" ] ; then
    yarn start:production
elif [ $NODE_ENV = "staging" ] ; then
    yarn start:staging
else
    yarn start
fi
