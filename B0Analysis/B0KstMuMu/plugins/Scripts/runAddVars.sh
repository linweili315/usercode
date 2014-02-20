source InitAnalysis.sh

echo @@@ Directory with data: $DATADIR @@@
echo @@@ Adding single canditate GEN variables @@@

Qsub -l lnxfarm -e -o AddVarsSignGEN.log  -N SignGEN  .././AddVarsToCandidates addSingleCandGENvars $DATADIR/MonteCarlo2012/GENcands/B0ToKstMuMu_GEN_NoFilter_MC_NTuples.root  $DATADIR/MonteCarlo2012/ForEfficiency/B0ToKstMuMu_GEN_NoFilter_MC_NTuples_addGENvars.root  1
Qsub -l lnxfarm -e -o AddVarsJPsiGEN.log  -N JPsiGEN  .././AddVarsToCandidates addSingleCandGENvars $DATADIR/MonteCarlo2012/GENcands/B0ToJPsiKst_GEN_NoFilter_MC_NTuples.root  $DATADIR/MonteCarlo2012/ForEfficiency/B0ToJPsiKst_GEN_NoFilter_MC_NTuples_addGENvars.root  3
Qsub -l lnxfarm -e -o AddVarsPsi2SGEN.log -N Psi2SGEN .././AddVarsToCandidates addSingleCandGENvars $DATADIR/MonteCarlo2012/GENcands/B0ToPsi2SKst_GEN_NoFilter_MC_NTuples.root $DATADIR/MonteCarlo2012/ForEfficiency/B0ToPsi2SKst_GEN_NoFilter_MC_NTuples_addGENvars.root 5

Qsub -l lnxfarm -e -o AddVarsSignRECO.log  -N SignRECO  .././AddVarsToCandidates addSingleCandGENvars $DATADIR/MonteCarlo2012/RECOcands/B0ToKstMuMu_MC_NTuple.root  $DATADIR/MonteCarlo2012/ForEfficiency/B0ToKstMuMu_MC_NTuple_addGENvars.root  1
Qsub -l lnxfarm -e -o AddVarsJPsiRECO.log  -N JPsiRECO  .././AddVarsToCandidates addSingleCandGENvars $DATADIR/MonteCarlo2012/RECOcands/B0ToJPsiKst_MC_NTuple.root  $DATADIR/MonteCarlo2012/ForEfficiency/B0ToJPsiKst_MC_NTuple_addGENvars.root  3
Qsub -l lnxfarm -e -o AddVarsPsi2SRECO.log -N Psi2SRECO .././AddVarsToCandidates addSingleCandGENvars $DATADIR/MonteCarlo2012/RECOcands/B0ToPsi2SKst_MC_NTuple.root $DATADIR/MonteCarlo2012/ForEfficiency/B0ToPsi2SKst_MC_NTuple_addGENvars.root 5
