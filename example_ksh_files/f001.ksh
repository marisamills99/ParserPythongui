#TEMPLATE TO RUN PROGRAM f001

EXECBASE=f001
EXECUTABLE=$PWD/$EXECBASE.exe
OUTPUT_DIR=$PWD/OUTPUT/
#INPUT_DIR=$PWD/INPUT/

#INPUT FILES
#INPUT=${INPUT_DIR}

echo 'No input required for f001'

#OUTPUT

echo 'Output going to ' ${OUTPUT_DIR}f001.out

$EXECUTABLE > ${OUTPUT_DIR}f001.out

echo ' '
echo 'PROGRAM f001 HAS ENDED'
#END KSH
