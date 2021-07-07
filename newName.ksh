#added attempt 2
#TEMPLATE TO RUN PROGRAM f003
#header line 2
#header line 3


#yes
EXECBASE=f004
EXECUTABLE=$PWD/$EXECBASE.exe
#hi
OUTPUT_DIR=$PWD/OUTPUT/hi
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
