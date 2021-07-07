# t009.ksh 
# Program uses loops through variety
# of calculations (trig, random deviant,
# random number generator and writes to 
# one output file for calculations and
# a time_trial to be used with optimizaiton

EXECBASE=t009
EXECUTABLE=$PWD/$EXECBASE.exe

rm -f *.out

#Output files
ln -s time_trials.out fort.10
ln -s calculations.out fort.16

echo $EXECUTABLE

$EXECUTABLE

rm fort.*

