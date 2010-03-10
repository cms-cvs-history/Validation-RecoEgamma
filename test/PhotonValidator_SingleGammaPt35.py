import FWCore.ParameterSet.Config as cms

process = cms.Process("TestPhotonValidator")
process.load('Configuration/StandardSequences/GeometryPilot2_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")
process.load("RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi")
process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")
process.load("RecoTracker.MeasurementDet.MeasurementTrackerESProducer_cfi")
process.load("SimGeneral.MixingModule.mixNoPU_cfi")
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load("DQMServices.Components.MEtoEDMConverter_cfi")
process.load("Validation.RecoEgamma.photonValidationSequence_cff")
process.load("Validation.RecoEgamma.photonPostprocessing_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'MC_3XY_V24::All'

process.DQMStore = cms.Service("DQMStore");
process.load("DQMServices.Components.DQMStoreStats_cfi")
from DQMServices.Components.DQMStoreStats_cfi import *
dqmStoreStats.runOnEndJob = cms.untracked.bool(True)



process.maxEvents = cms.untracked.PSet(
#input = cms.untracked.int32(10)
)



from Validation.RecoEgamma.photonValidationSequence_cff import *
from Validation.RecoEgamma.photonPostprocessing_cfi import *

photonValidation.OutputMEsInRootFile = True
photonValidation.OutputFileName = 'PhotonValidationRelVal360pre2_SingleGammaPt35.root'
photonPostprocessing.batch = cms.bool(True)
photonPostprocessing.InputFileName = photonValidation.OutputFileName

process.source = cms.Source("PoolSource",
noEventSort = cms.untracked.bool(True),
duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            
    fileNames = cms.untracked.vstring(
# official RelVal 360pre2 single Photons pt=35GeV            
        '/store/relval/CMSSW_3_6_0_pre2/RelValSingleGammaPt35/GEN-SIM-RECO/MC_3XY_V24-v1/0001/364E7B38-6F27-DF11-91A9-0026189438D4.root',
        '/store/relval/CMSSW_3_6_0_pre2/RelValSingleGammaPt35/GEN-SIM-RECO/MC_3XY_V24-v1/0000/48AE643B-0727-DF11-99FB-001731AF66F5.root'

    ),
                            
                            
    secondaryFileNames = cms.untracked.vstring(
        # official RelVal 360pre2 single Photons pt=35GeV

'/store/relval/CMSSW_3_6_0_pre2/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V24-v1/0001/74928F33-6F27-DF11-94AB-00248C55CC62.root',
        '/store/relval/CMSSW_3_6_0_pre2/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V24-v1/0000/E0534531-0727-DF11-9899-002618943900.root',
        '/store/relval/CMSSW_3_6_0_pre2/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V24-v1/0000/CEA2BC7C-0727-DF11-910E-001731AF6B77.root',
        '/store/relval/CMSSW_3_6_0_pre2/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_3XY_V24-v1/0000/14EDB930-0727-DF11-9240-003048678BE6.root'



    )
 )


photonPostprocessing.rBin = 48

## For single gamma pt = 35
photonValidation.eMax  = 300
photonValidation.etMax = 50
photonValidation.etScale = 0.20
photonValidation.dCotCutOn = False
photonValidation.dCotCutValue = 0.15

process.FEVT = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring("keep *_MEtoEDMConverter_*_*"),
    fileName = cms.untracked.string('pippo.root')
)



process.p1 = cms.Path(process.tpSelection*process.photonValidationSequence*process.photonPostprocessing*process.dqmStoreStats)
process.schedule = cms.Schedule(process.p1)
