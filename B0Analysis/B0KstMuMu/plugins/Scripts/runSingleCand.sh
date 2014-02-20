source InitAnalysis.sh

echo @@@ Directory with data: $DATADIR @@@
echo @@@ Single candidate production @@@

Qsub -l lnxfarm -e -o SingleCandData.log -N SCData .././SingleCandB0KstMuMu singlecand $DATADIR/Data2012/B0ToKstMuMu_Data2012ABCD_NTuples.root $DATADIR/Data2012/SingleCand/singleCand_B0ToKstMuMu_Data2012ABCD_NTuples.root

Qsub -l lnxfarm -e -o SingleCandKstMuMu.log  -N SCKstMuMu  .././SingleCandB0KstMuMu singlecand $DATADIR/MonteCarlo2012/RECOcands/B0ToKstMuMu_MC_NTuple.root  $DATADIR/MonteCarlo2012/SingleCand/singleCand_B0ToKstMuMu_MC_NTuple.root  1
Qsub -l lnxfarm -e -o SingleCandJPsiKst.log  -N SCJPsiKst  .././SingleCandB0KstMuMu singlecand $DATADIR/MonteCarlo2012/RECOcands/B0ToJPsiKst_MC_NTuple.root  $DATADIR/MonteCarlo2012/SingleCand/singleCand_B0ToJPsiKst_MC_NTuple.root  3
Qsub -l lnxfarm -e -o SingleCandPsi2SKst.log -N SCPsi2SKst .././SingleCandB0KstMuMu singlecand $DATADIR/MonteCarlo2012/RECOcands/B0ToPsi2SKst_MC_NTuple.root $DATADIR/MonteCarlo2012/SingleCand/singleCand_B0ToPsi2SKst_MC_NTuple.root 5

Qsub -l lnxfarm -e -o SingleCandBsKst.log   -N SCBsKst   .././SingleCandB0KstMuMu singlecand $DATADIR/MonteCarlo2012/RECOcands/BsToKstMuMu_MC_NTuple.root      $DATADIR/MonteCarlo2012/SingleCand/singleCand_BsToKstMuMu_MC_NTuple.root
Qsub -l lnxfarm -e -o SingleCandB0PsiX.log  -N SCB0PsiX  .././SingleCandB0KstMuMu singlecand $DATADIR/MonteCarlo2012/RECOcands/B0ToPsiMuMu_MC_NTuple.root      $DATADIR/MonteCarlo2012/SingleCand/singleCand_B0ToPsiMuMu_MC_NTuple.root
Qsub -l lnxfarm -e -o SingleCandBpPsiX.log  -N SCBpPsiX  .././SingleCandB0KstMuMu singlecand $DATADIR/MonteCarlo2012/RECOcands/BpToPsiMuMu_MC_NTuple.root      $DATADIR/MonteCarlo2012/SingleCand/singleCand_BpToPsiMuMu_MC_NTuple.root
Qsub -l lnxfarm -e -o SingleCandBsPsiX.log  -N SCBsPsiX  .././SingleCandB0KstMuMu singlecand $DATADIR/MonteCarlo2012/RECOcands/BsToPsiMuMu_MC_NTuple.root      $DATADIR/MonteCarlo2012/SingleCand/singleCand_BsToPsiMuMu_MC_NTuple.root
Qsub -l lnxfarm -e -o SingleCandLamPsiX.log -N SCLamPsiX .././SingleCandB0KstMuMu singlecand $DATADIR/MonteCarlo2012/RECOcands/LambdaBToPsiMuMu_MC_NTuple.root $DATADIR/MonteCarlo2012/SingleCand/singleCand_LambdaBToPsiMuMu_MC_NTuple.root
