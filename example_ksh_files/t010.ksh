# t010 Program badluck
#
# Program performs calculations to 
# find the Julian days for the entered
# timeset (must be from 2000 onward) to use 
# in locating Friday the 13ths with a full moon.
# Secondarily, it will perform the same 
# calculations to find Halloweens with a full moon.
#


EXECBASE=t010
EXECUTABLE=$PWD/$EXECBASE.exe

rm -f *.out

# input selected year file
ln -s years.dat fort.10

#Output file
ln -s BadLuck.out fort.9
echo $EXECUTABLE

$EXECUTABLE

rm fort.*

