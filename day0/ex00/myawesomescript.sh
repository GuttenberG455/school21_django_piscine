#!/bin/sh

if [ $1 ] ; then
	curl --silent $1 | grep "moved here" | cut -d \" -f 2
fi
