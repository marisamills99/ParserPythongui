#unclassified
#TEMPLATE TO RUN PROGRAM f004
#this program does x.y,z
#header line 3


EXECBASE=f004
EXECUTABLE=$PWD/$EXECBASE.exe
OUTPUT_DIR=$PWD/OUTPUT/
#added a comment2
INPUT_DIR=$HOME/USER/INPUT/

#INPUT FILES
#INPUT=${INPUT_DIR}

echo 'No input required for f004'

#OUTPUT

echo 'Output going to ' ${OUTPUT_DIR}f004.out

$EXECUTABLE > ${OUTPUT_DIR}f004.out

echo ' '
echo 'PROGRAM f004 HAS ENDED'
#END KSH