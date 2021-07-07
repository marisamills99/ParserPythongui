#add more here
#TEMPLATE TO RUN PROGRAM f004
#header
#include this
EXECBASE=f004
EXECUTABLE=$PWD/$EXECBASE.exe
OUTPUT_DIR=$PWD/OUTPUT/

#INPUT FILES
#INPUT=${INPUT_DIR}

echo 'No input required for f004'

#OUTPUT

echo 'Output going to ' ${OUTPUT_DIR}f004.out

$EXECUTABLE > ${OUTPUT_DIR}f004.out

echo ' '
echo 'PROGRAM f004 HAS ENDED'
#END KSH
