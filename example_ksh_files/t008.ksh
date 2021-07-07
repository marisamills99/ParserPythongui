# t008.ksh 
# Program uses altitude.dat for input and 
# creates two output files

EXECBASE=t008
EXECUTABLE=$PWD/$EXECBASE.exe

rm -f *.txt
#Input file
ln -s ALTITUDE.DAT fort.15

#Output files
ln -s TIME_TRIALS.OUT fort.10
ln -s VELOCITY.DAT fort.16
ln -s ACCEL.DAT fort.17

echo $EXECUTABLE

$EXECUTABLE

rm fort.*

