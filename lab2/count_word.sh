#!/bin/bash

if [ $# -ne 2 ]; then
	echo "Usage: $0 <file_name <word>"
	exit 1
fi

FILE_NAME=$1
WORD=$2

if [ ! -f "FILE_NAME" ]; then
	echo "File '$FILE_NAME' not found!"
	exit 1
fi

	word_count=$(grep -oiw "$WORD" "FILE_NAME" | wc -l)
echo "The word '$WORD' appeared $WORD_COUNT times in the file '$FILE_NAME'."
