#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage: $0 <directory>"
	exit 1
fi

DIRECTORY=$1
if [ ! -d "DIRECTORY" ]; then
	echo "Directory 'DIRECTORY' not found."
	exit 2
fi

find "$DIRECTORY" -type f -empty -print -exec rm {} \;
echo "Empty files were deleted from 'DIRECTORY'."
