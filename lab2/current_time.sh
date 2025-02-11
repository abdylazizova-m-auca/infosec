#!/bin/bash

END_H=17
END_M=00

CURRENT_H=$(date +%H)
CURRENT_M=$(date +%M)

CURRENT_TOTAL_M=$((CURRENT_H * 60 + CURRENT_M))
END_TOTAL_M=$((END_H * 60 + END_M))

TIME_REMAINING=$((END_TOTAL_M - CURRENT_TOTAL_M))

if [ "$TIME_REMAINING" -gt 0 ]; then
	HOUR_LEFT=$((TIME_REMAINING / 60))
	MIN_LEFT=$((TIME_REMAINING % 60))

	echo "Current time: $(date +%H:%M). Work day ends after $HOUR_LEFT hours and $MINUTES_LEFT minutes."
else
	echo "Current time: $(date +%H:%M). The work day has ended!"
fi
