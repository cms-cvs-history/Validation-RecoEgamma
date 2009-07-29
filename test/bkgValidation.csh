#!/bin/csh

#This script can be used to generate a web page to compare histograms from 
#two input root files produced using the EDAnalyzers in RecoEgamma/Examples,
#by running one of:
#
#  
#  
#  "Validation/RecoEgamma/test/PhotonValidator_cfg.py
#
# The default list of histograms (configurable) is based on version VXX-XX-XX
# of Validation/RecoEgamma
#
#Two files are created by this script: validation.C and validation.html.
#validation.C should be run inside root to greate a set of gif images
#which can then be viewed in a web browser using validation.html.

#=============BEGIN CONFIGURATION=================
setenv TYPE Photons
setenv CMSSWver1 3_1_1
setenv CMSSWver2 3_1_2
setenv OLDRELEASE 311
setenv NEWRELEASE 312
setenv OLDPRERELEASE 
setenv NEWPRERELEASE 

setenv OLDRELEASE ${OLDRELEASE}${OLDPRERELEASE}
setenv NEWRELEASE ${NEWRELEASE}${NEWPRERELEASE}


#Name of sample (affects output directory name and htmldescription only) 

setenv SAMPLE QCD_Pt_80_120STARTUP
#TYPE must be one ofPixelMatchGsfElectron, Photon 

#==============END BASIC CONFIGURATION==================


#Input root trees for the two cases to be compared 



#setenv OLDFILE /afs/cern.ch/user/n/nancy/scratch0/PreProductionValidation/CMSSW_3_1_1/src/Validation/RecoEgamma/test/results/${SAMPLE}_total.root
#setenv NEWFILE /afs/cern.ch/user/n/nancy/scratch0/PreProductionValidation/CMSSW_3_1_1/src/Validation/RecoEgamma/test/results/${SAMPLE}_total.root

if ($SAMPLE == QCD_Pt_80_120STARTUP) then 

setenv OLDFILE /data/test/CMSSW_${CMSSWver2}/src/Validation/RecoEgamma/test/PhotonValidationRelVal${NEWRELEASE}_QCD_Pt_80_120.root
setenv NEWFILE /data/test/CMSSW_${CMSSWver2}/src/Validation/RecoEgamma/test/PhotonValidationRelVal${NEWRELEASE}_QCD_Pt_80_120.root


endif



#Location of output.  The default will put your output in:
#http://cmsdoc.cern.ch/Physics/egamma/www/validation/

setenv CURRENTDIR $PWD
setenv OUTPATH /afs/cern.ch/cms/Physics/egamma/www/validation
cd $OUTPATH
if (! -d $NEWRELEASE) then
  mkdir $NEWRELEASE
endif
setenv OUTPATH $OUTPATH/$NEWRELEASE
cd $OUTPATH
if (! -d ${TYPE}_vs${OLDRELEASE}) then
  mkdir ${TYPE}_vs${OLDRELEASE}
endif
setenv OUTPATH $OUTPATH/${TYPE}_vs${OLDRELEASE}

setenv OUTDIR $OUTPATH/${SAMPLE}
if (! -d $OUTDIR) then
  cd $OUTPATH
  mkdir $OUTDIR
  cd $OUTDIR
  mkdir gifs
endif
cd $OUTDIR


#The list of histograms to be compared for each TYPE can be configured below:


if ( $TYPE == Photons ) then




cat > scaledhistosForBkg <<EOF

  scBkgEta
  scBkgPhi
  scBkgEAll
  scBkgEtAll
  phoBkgEta
  phoBkgPhi
  r9BkgAll
  r9BkgBarrel
  r9BkgEndcap
  hOverEBkgAll
  hOverEBkgBarrel
  hOverEBkgEndcap
  ecalRecHitSumEtConeDR04BkgBarrel
  ecalRecHitSumEtConeDR04BkgEndcap

EOF

cat > unscaledhistosForBkg <<EOF
  pEcalRecHitSumEtConeDR04VsEtBkgBarrel
  pEcalRecHitSumEtConeDR04VsEtBkgEndcap
  pEcalRecHitSumEtConeDR04VsEtaBkgAll




EOF


endif

#=================END CONFIGURATION=====================

if (-e validation.C) rm validation.C
touch validation.C
cat > begin.C <<EOF
{
TFile *file_old = TFile::Open("$OLDFILE");
TFile *file_new = TFile::Open("$NEWFILE");

EOF
cat begin.C >>& validation.C
rm begin.C

setenv N 1




foreach i (`cat scaledhistosForBkg`)
  cat > temp$N.C <<EOF
TCanvas *c$i = new TCanvas("c$i");
c$i->SetFillColor(10);
file_new->cd("DQMData/EgammaV/PhotonValidator/Background");
Double_t mnew=$i->GetMaximum();
Double_t nnew=$i->GetEntries();
file_old->cd("DQMData/EgammaV/PhotonValidator/Background");
Double_t mold=$i->GetMaximum();
Double_t nold=$i->GetEntries();
$i->SetStats(0);
$i->SetMinimum(0.);
//if ( mnew > mold) 
// $i->SetMaximum(mnew+mnew*0.2);
//else 
//$i->SetMaximum(mold+mold*0.2);
//$i->SetMaximum(mold+mold*0.2);
$i->SetLineColor(kPink+8);
$i->SetFillColor(kPink+8);
//$i->SetLineWidth(3);
$i->Draw();
file_new->cd("DQMData/EgammaV/PhotonValidator/Background");
Double_t nnew=$i->GetEntries();
$i->SetStats(0);
$i->SetLineColor(kBlack);
$i->SetMarkerColor(kBlack);
$i->SetMarkerStyle(20);
$i->SetMarkerSize(1);
//$i->SetLineWidth(1);
$i->Scale(nold/nnew);
$i->Draw("esame");
c$i->SaveAs("gifs/$i.gif");

EOF
  setenv N `expr $N + 1`
end



foreach i (`cat unscaledhistosForBkg`)
  cat > temp$N.C <<EOF
TCanvas *c$i = new TCanvas("c$i");
c$i->SetFillColor(10);
file_old->cd("DQMData/EgammaV/PhotonValidator/Background");
$i->SetStats(0);
if ( $i==pEcalRecHitSumEtConeDR04VsEtaBkgAll ) {  
$i->GetYaxis()->SetRangeUser(0.,5.);
} else if ( $i==pEcalRecHitSumEtConeDR04VsEtBkgBarrel ) 
{ $i->GetYaxis()->SetRangeUser(0.,20.); 
} else if ( $i==pEcalRecHitSumEtConeDR04VsEtBkgEndcap  ) 
{
$i->GetYaxis()->SetRangeUser(0.,20.);
} else  {
$i->SetMinimum(0.8);
$i->SetMaximum(1.1);
}
$i->SetLineColor(kPink+8);
$i->SetMarkerColor(kPink+8);
$i->SetMarkerStyle(20);
$i->SetMarkerSize(1);
$i->SetLineWidth(1);
$i->Draw();
file_new->cd("DQMData/EgammaV/PhotonValidator/Background");
$i->SetStats(0);
$i->SetLineColor(kBlack);
$i->SetMarkerColor(kBlack);
$i->SetMarkerStyle(20);
$i->SetMarkerSize(1);
$i->SetLineWidth(1);
$i->Draw("esame");
c$i->SaveAs("gifs/$i.gif");

EOF
  setenv N `expr $N + 1`
end



setenv NTOT `expr $N - 1`
setenv N 1
while ( $N <= $NTOT )
  cat temp$N.C >>& validation.C
  rm temp$N.C
  setenv N `expr $N + 1`
end

cat > end.C <<EOF
}
EOF
cat end.C >>& validation.C
rm end.C


if ( $TYPE == PixelMatchGsfElectron ) then
  setenv ANALYZER PixelMatchGsfElectronAnalyzer
  setenv CFG read_gsfElectrons
else if ( $TYPE == Photons ) then
  setenv ANALYZER PhotonValidator
  setenv CFG PhotonValidator_cfg
endif

if (-e validation.html) rm validation.html
if (-e bkgValidationPlotsTemplate.html) rm bkgValidationPlotsTemplate.html
cp ${CURRENTDIR}/bkgValidationPlotsTemplate.html bkgValidationPlotsTemplate.html
touch validation.html
cat > begin.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<title>$NEWRELEASE vs $OLDRELEASE $TYPE validation</title>
</head>

<h1>$NEWRELEASE vs $OLDRELEASE $TYPE validation
<br>
 $SAMPLE 
</h1>

<p>The following plots were made using <a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/CMSSW/Validation/RecoEgamma/src/$ANALYZER.cc">Validation/RecoEgamma/src/$ANALYZER</a>, 
using <a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/CMSSW/Validation/RecoEgamma/test/$CFG.py">Validation/RecoEgamma/test/$CFG.py</a>
<p>The script used to make the plots is <a href="validation.C">here</a>.
<br>
In all plots below, $OLDRELEASE is in purple , $NEWRELEASE in black. 
<br>
Click on the plots to see them enlarged.
<br>
Responsible: N. Marinelli
<br>
<br>



EOF
cat begin.html >>& validation.html
rm begin.html
cat  bkgValidationPlotsTemplate.html >>& validation.html
rm   bkgValidationPlotsTemplate.html 

rm scaledhistosForBkg
rm unscaledhistosForBkg

#echo "Now paste the following into your terminal window:"
#echo ""
echo "cd $OUTDIR"
#echo " root -b"
#echo ".x validation.C"
#echo ".q"
#echo "cd $CURRENTDIR"
#echo ""


root -b -l -q validation.C
cd $CURRENTDIR
echo "Then you can view your valdation plots here:"
echo "http://cmsdoc.cern.ch/Physics/egamma/www/$OUTPATH/validation.html"
