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

#Input root trees for the two cases to be compared 

setenv OLDFILE /afs/cern.ch/user/d/dimatteo/scratch0/CMSSW_2_1_7/src/Validation/RecoEgamma/test/ElectronIDValidationRelVal214_FastZEE.root
setenv NEWFILE /afs/cern.ch/user/d/dimatteo/scratch0/CMSSW_2_1_7/src/Validation/RecoEgamma/test/ElectronIDValidationRelVal214_FullZEE.root

setenv OLDRELEASE 214Fast
setenv NEWRELEASE 214Full
setenv RELEASE    CMSSW_2_1_4
#Name of sample (affects output directory name and htmldescription only) 
setenv SAMPLE ZEE
#TYPE must be one of PixelMatchGsfElectron, Photon 
setenv TYPE PixelMatchGsfElectron
#==============END BASIC CONFIGURATION==================

#Location of output.  The default will put your output in:
#http://cmsdoc.cern.ch/Physics/egamma/www/validation/

#IF YOU WANT TO SET THE OUTPUT DIR CHANGE THE NEXT LINES!

setenv CURRENTDIR $PWD
setenv OUTPATH /afs/cern.ch/cms/Physics/egamma/www/validation
cd $OUTPATH
if (! -d $RELEASE) then
  mkdir $RELEASE
endif
setenv OUTPATH $OUTPATH/$RELEASE

setenv OUTDIR $OUTPATH/${SAMPLE}_${NEWRELEASE}_${OLDRELEASE}
if (! -d $OUTDIR) then
  cd $OUTPATH
  mkdir $OUTDIR
  cd $OUTDIR
  mkdir gifs
endif
cd $OUTDIR

#The list of histograms to be compared for each TYPE can be configured below:


if ( $TYPE == PixelMatchGsfElectron ) then

cat > scaledhistosBarrel <<EOF
  hB_ele_PoPtrue_matched_barrel  
  hB_ele_EtaMnEtaTrue_matched_barrel  
  hB_ele_PhiMnPhiTrue_matched_barrel
  hB_ele_fbremMean_matched_barrel
  hB_ele_vertexPt_matched_barrel
  hB_ele_EoP_matched_barrel
  hB_ele_eSeedOverPout_matched_barrel
  hB_ele_HoE_matched_barrel
  hB_scl_sigmaEta_matched_barrel  
  hB_ele_dEtaSc_propVtx_matched_barrel
  hB_ele_dPhiSc_propVtx_matched_barrel
  hB_scl_eSeedOverPin_matched_barrel
  hB_ele_vertexZ_matched_barrel
EOF

cat > scaledhistosEndcaps <<EOF
  hEC_ele_PoPtrue_matched_endcaps  
  hEC_ele_EtaMnEtaTrue_matched_endcaps  
  hEC_ele_PhiMnPhiTrue_matched_endcaps
  hEC_ele_fbremMean_matched_endcaps
  hEC_ele_vertexPt_matched_endcaps
  hEC_ele_EoP_matched_endcaps
  hEC_ele_eSeedOverPout_matched_endcaps
  hEC_ele_HoE_matched_endcaps
  hEC_scl_sigmaEta_matched_endcaps  
  hEC_ele_dEtaSc_propVtx_matched_endcaps
  hEC_ele_dPhiSc_propVtx_matched_endcaps
  hEC_scl_eSeedOverPin_matched_endcaps
  hEC_ele_vertexZ_matched_endcaps
EOF

cat > IDefficiencies <<EOF
  h_ele_simEta_
  h_ele_simPt_
  h_ele_simPhi_
  h_ele_simAbsEta_ 
EOF

cat > efficiencies <<EOF
  h_ele_simEta_matched
  h_ele_simPt_matched
  h_ele_simPhi_matched
  h_ele_simAbsEta_matched
EOF


else if ( $TYPE == Photon ) then

cat > scaledhistosForPhotons <<EOF
  scEta
  scPhi
  scEAll
  scEtAll
  phoDEta
  phoDPhi
  r9All
  r9Barrel
  r9Endcap
  phoEAll
  phoEtAll
  eResAll
  eResBarrel
  eResEndcap
  eResunconvAll
  eResunconvBarrel
  eResunconvEndcap
  eResconvAll
  eResconvBarrel
  eResconvEndcap

EOF


cat > scaledhistosForConvertedPhotons <<EOF

  convEta
  convPhi
  convEResAll
  convEResBarrel
  convEResEndcap
  EoverPtracksAll
  EoverPtracksBarrel 
  EoverPtracksEndcap

EOF




cat > unscaledhistosForConvertedPhotons <<EOF
pEoverEtrueVsEtaAll
pEoverPVsEtaAll

EOF

cat > efficiencyForPhotons <<EOF
  recoEffVsEta
  recoEffVsPhi

EOF

cat > efficiencyForConvertedPhotons <<EOF

  convEffVsEtaTwoTracks
  convEffVsPhiTwoTracks
  convEffVsRTwoTracks
  convEffVsZTwoTracks


EOF



cat > scaledhistosForTracks <<EOF

tkChi2AllTracks
hTkPtPullAll
hTkPtPullBarrel
hTkPtPullEndcap
hDPhiTracksAtVtxAll
hDCotTracksAll
hDEtaTracksAtEcalAll
hDPhiTracksAtEcalAll
eBcOverTkPoutAll
eBcOverTkPoutBarrel
eBcOverTkPoutEndcap
zPVFromTracks
dzPVFromTracks

EOF

cat > unscaledhistosForTracks <<EOF
h_nHitsVsEtaAllTracks
h_nHitsVsRAllTracks


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


foreach i (`cat scaledhistosBarrel`)
  cat > temp$N.C <<EOF
TCanvas *c${i} = new TCanvas("c${i}");
c${i}->SetFillColor(10);
file_old->cd();
${i}->SetStats(0);
${i}->SetMinimum(0.);
${i}->SetLineColor(4);
${i}->SetLineWidth(3);
${i}->SetTitle( "${i}");
${i}->Draw();
Double_t nold=${i}->GetEntries();
file_new->cd();
Double_t nnew=${i}->GetEntries();
${i}->SetStats(0);
${i}->SetLineColor(2);
${i}->SetLineWidth(3);
${i}->Scale(nold/nnew);
${i}->SetTitle( "${i}");
${i}->Draw("same");
c${i}->SaveAs("gifs/${i}.gif");

EOF
  setenv N `expr $N + 1`
end

foreach i (`cat scaledhistosEndcaps`)
  cat > temp$N.C <<EOF
TCanvas *c${i} = new TCanvas("c${i}");
c${i}->SetFillColor(10);
file_old->cd();
${i}->SetStats(0);
${i}->SetMinimum(0.);
${i}->SetLineColor(4);
${i}->SetLineWidth(3);
${i}->SetTitle( "${i}") ;
${i}->Draw();
Double_t nold=${i}->GetEntries();
file_new->cd();
Double_t nnew=${i}->GetEntries();
${i}->SetStats(0);
${i}->SetLineColor(2);
${i}->SetLineWidth(3);
${i}->Scale(nold/nnew);
${i}->SetTitle( "${i}") ;
${i}->Draw("same");
c${i}->SaveAs("gifs/${i}.gif");

EOF
  setenv N `expr $N + 1`
end


cat > temp$N.C <<EOF

//Reinitialize Histos and declare MC variables==========================

TFile *file_old = TFile::Open("$OLDFILE");
TFile *file_new = TFile::Open("$NEWFILE");

EOF
setenv N `expr $N + 1`

set DEN = ( h_ele_simEta_matched h_ele_simPt_matched h_ele_simPhi_matched h_ele_simAbsEta_matched )

foreach j ( robustL robustT loose tight )

setenv k 1

foreach i (`cat IDefficiencies`)
  cat > temp$N.C <<EOF
TCanvas *c${i}${j} = new TCanvas("c${i}${j}");
c${i}${j}->SetFillColor(10);
file_old->cd();

TH1F *${i}Eff_${j};

${i}Eff_${j}  = (TH1F*) ${i}${j} -> Clone ( "${i}Eff_${j}" );

${i}Eff_${j}->SetStats(0);
${i}Eff_${j}->SetLineColor(4);
${i}Eff_${j}->SetLineWidth(3);

${i}Eff_${j} ->Sumw2();
$DEN[$k]->Sumw2();

${i}Eff_${j}->Divide(${i}Eff_${j}, $DEN[$k] ,1.,1.,"b");

${i}Eff_${j}->SetMinimum(0.);
${i}Eff_${j}->SetMaximum(1.);
${i}Eff_${j}->GetYaxis()->SetTitle("Efficiency") ;
${i}Eff_${j}->Draw("e1");

file_new->cd();

${i}Eff_${j}  = (TH1F*) ${i}${j} -> Clone ( "${i}Eff_${j}" );

${i}Eff_${j}->SetStats(0);
${i}Eff_${j}->SetLineColor(2);
${i}Eff_${j}->SetLineWidth(3);
${i}Eff_${j} ->Sumw2();
$DEN[$k]->Sumw2();

${i}Eff_${j}->Divide(${i}Eff_${j}, $DEN[$k] ,1.,1.,"b");

${i}Eff_${j}->SetMinimum(0.);
${i}Eff_${j}->SetMaximum(1.);
${i}Eff_${j}->GetYaxis()->SetTitle("Efficiency") ;
${i}Eff_${j}->Draw("same e1");

c${i}${j}->SaveAs("gifs/${i}Eff_${j}.gif");

EOF
 setenv N `expr $N + 1`
 setenv k `expr $k + 1`
end
end


set DEN = ( h_mc_eta h_mc_Pt h_mc_Phi h_mc_AbsEta )

setenv k 1

foreach i (`cat efficiencies`)
   cat > temp$N.C <<EOF
TCanvas *c${i} = new TCanvas("c${i}");
c${i}->SetFillColor(10);
file_old->cd();

TH1F *${i}_Eff;

${i}_Eff  = (TH1F*) ${i} -> Clone ( "${i}_Eff" );

${i}_Eff->SetStats(0);
${i}_Eff->SetLineColor(4);
${i}_Eff->SetLineWidth(3);


${i}_Eff ->Sumw2();
$DEN[$k]  ->Sumw2();

${i}_Eff->Divide(${i}_Eff, $DEN[$k] ,1.,1.,"b");

${i}_Eff->SetMinimum(0.);
${i}_Eff->SetMaximum(1.);
${i}_Eff->GetYaxis()->SetTitle("Efficiency") ;
${i}_Eff->Draw("e1");

file_new->cd();

${i}_Eff  = (TH1F*) ${i} -> Clone ( "${i}_Eff" );

${i}_Eff->SetStats(0);
${i}_Eff->SetLineColor(2);
${i}_Eff->SetLineWidth(3);
${i}_Eff ->Sumw2();
$DEN[$k]->Sumw2();

${i}_Eff->Divide(${i}_Eff, $DEN[$k] ,1.,1.,"b");

${i}_Eff->SetMinimum(0.);
${i}_Eff->SetMaximum(1.);
${i}_Eff->GetYaxis()->SetTitle("Efficiency") ;
${i}_Eff->Draw("same e1");

c${i}->SaveAs("gifs/${i}_Eff.gif");

EOF
 setenv N `expr $N + 1`
 setenv k `expr $k + 1`
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
  setenv ANALYZER ElectronIDValidator.cc
  setenv CFG ElectronIDValidator_cfg
else if ( $TYPE == Photon ) then
  setenv ANALYZER PhotonValidator
  setenv CFG PhotonValidator_cfg
endif

if (-e validation.html) rm validation.html
touch validation.html
cat > begin.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<title>$NEWRELEASE vs $OLDRELEASE $TYPE $SAMPLE validation</title>
</head>

<h1>$NEWRELEASE vs $OLDRELEASE $TYPE $SAMPLE validation</h1>

<p>The following plots were made using <a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/CMSSW/Validation/RecoEgamma/src/$ANALYZER.cc">Validation/RecoEgamma/src/$ANALYZER</a>, 
using <a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/CMSSW/Validation/RecoEgamma/test/$CFG.py">Validation/RecoEgamma/test/$CFG.py</a>, using $SAMPLE as input.
<p>The script used to make the plots is <a href="validation.C">here</a>.

<p>In all plots below, $OLDRELEASE is in blue, $NEWRELEASE in red.

EOF
cat begin.html >>& validation.html
rm begin.html

setenv N 1

  cat > temp$N.html <<EOF
<p>Barrel Histos.
EOF
  setenv N `expr $N + 1`
  setenv NTOT `expr $NTOT + 1`

foreach i (`cat scaledhistosBarrel`)
  cat > temp$N.html <<EOF
<br>
<p><img class="image" width="500" src="gifs/${i}.gif">
EOF
  setenv N `expr $N + 1`
end

  cat > temp$N.html <<EOF
<p>Endcaps Histos.
EOF
  setenv N `expr $N + 1`
  setenv NTOT `expr $NTOT + 1`

foreach i (`cat scaledhistosEndcaps`)
  cat > temp$N.html <<EOF
<br>
<p><img class="image" width="500" src="gifs/${i}.gif">
EOF
  setenv N `expr $N + 1`
end

  cat > temp$N.html <<EOF
<p>ElectronID efficiencies: #MatchedEle which have passed EleID/#Matched Ele
EOF
  setenv N `expr $N + 1`
  setenv NTOT `expr $NTOT + 1`

foreach j ( robustL robustT loose tight )

foreach i (`cat IDefficiencies`)
  cat > temp$N.html <<EOF
<br>
<p><img class="image" width="500" src="gifs/${i}Eff_${j}.gif">
EOF
  setenv N `expr $N + 1`
end

end

  cat > temp$N.html <<EOF
<p>Efficiencies: #MatchedEle/#MonteCarloEle
EOF
  setenv N `expr $N + 1`
  setenv NTOT `expr $NTOT + 1`

foreach i (`cat efficiencies`)
  cat > temp$N.html <<EOF
<br>
<p><img class="image" width="500" src="gifs/${i}_Eff.gif">
EOF
  setenv N `expr $N + 1`
end

setenv N 1

while ( $N < $NTOT )
  cat temp$N.html >>& validation.html
  rm temp$N.html
  setenv N `expr $N + 1`
end

cat > end.html <<EOF

</html>
EOF
cat end.html >>& validation.html
rm end.html

rm scaledhistosBarrel
rm scaledhistosEndcaps
rm IDefficiencies
rm efficiencies
rm scaledhistosForConvertedPhotons
rm unscaledhistos
rm efficiencyForPhotons
rm efficiencyForConvertedPhotons
rm scaledhistosForTracks
rm unscaledhistosForTracks


echo "Now paste the following into your terminal window:"
echo ""
echo "cd $OUTDIR"
echo " root -b"
echo ".x validation.C"
echo ".q"
echo "cd $CURRENTDIR"
echo ""
echo "Then you can view your valdation plots here:"
echo "http://cmsdoc.cern.ch/Physics/egamma/www/validation/${RELEASE}/${SAMPLE}_${NEWRELEASE}_${OLDRELEASE}/validation.html"

