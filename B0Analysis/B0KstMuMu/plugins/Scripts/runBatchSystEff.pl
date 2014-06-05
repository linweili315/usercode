#!/usr/bin/perl

####################################################################
# Program to fit with different pre-generated efficiency functions #
####################################################################

if (@ARGV == 6)
{
    $dirEffRndGen = @ARGV[0] ;

    $listcmd = "ls " . $dirEffRndGen ;
    @list = `$listcmd` ;

    $q2BinIndx = @ARGV[4] ;
    
    $cmd .= "unset DISPLAY\n" ;
    $cmd .= "rm FitSystematics_q2Bin_" . $q2BinIndx . ".txt" . "\n" ;
    
    $listStart = 0 ;
    $listEnd   = @list - 1 ;
    $listIndx  = 1 ;
    foreach $file (@list[$listStart..$listEnd])
    {
	chomp $file ;
	$execProg = ".././ExtractYield " . @ARGV[1] . " " . @ARGV[2] . " " . @ARGV[3] . " " . $q2BinIndx . " " . $dirEffRndGen . $file . " " . $listIndx . "\n" ;

	if (@ARGV[5] eq "false")
	{
	    $toRun = $execProg ;
	}
	else
	{
	    $toRun = "Qsub -l lnxfarm -e -o EffSys" . @ARGV[3] . "_" . $q2BinIndx . "_" . $listIndx . ".log -N ESYS" . $q2BinIndx . $listIndx . " " . $execProg ;
	}

	$cmd .= "echo " . $toRun ;
	$cmd .= $toRun ;
	$listIndx++ ;
    }


    open(OUT, ">runMultiExtractYield_q2Bin_" . $q2BinIndx . ".sh") ;
    print OUT "$cmd" ;
    print OUT "\n" ;
    close(OUT) ;
}
else
{
    print "Parameter missing:\n" ;
    print "./runBatchSystEff.pl [DirEffRndGen] [FitType] [File.root] [FitEff] [q^2 bin to fit (0 - ...)] [runJobs[true / false]]\n" ;
}
