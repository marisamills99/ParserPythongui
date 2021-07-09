#TEMPLATE TO RUN PROGRAM f004
#header line 2
#header line 3


#comment1
EXECBASE=f003
EXECUTABLE=$PWD/$EXECBASE.exe
#comment
OUTPUT_DIR=$PWD/OUTPUT/
#INPUT_DIR=$PWD/INPUT/

#INPUT FILES
#INPUT=${INPUT_DIR}

echo 'No input required for f004'

#OUTPUT

echo 'Output going to ' ${OUTPUT_DIR}f004.out

$EXECUTABLE > ${OUTPUT_DIR}f004.out

echo ' '
echo 'PROGRAM f004 HAS ENDED'
#END KSH
