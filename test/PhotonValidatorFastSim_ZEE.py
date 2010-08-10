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
process.GlobalTag.globaltag = 'MC_38Y_V8::All'

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
photonValidation.OutputFileName = 'PhotonValidationRelVal390pre1_ZEE.root'

photonPostprocessing.batch = cms.bool(True)
photonPostprocessing.InputFileName = photonValidation.OutputFileName

process.source = cms.Source("PoolSource",
noEventSort = cms.untracked.bool(True),
duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            
    fileNames = cms.untracked.vstring(
# official RelVal 390pre1 single Photons pt=35GeV
 '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/FCF2D664-EA9A-DF11-86FD-003048678F6C.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/F8EAA0CC-EC9A-DF11-A245-00261894391D.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/F88CE04D-EE9A-DF11-8A39-001A928116DE.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/F806226D-EB9A-DF11-983C-002618943836.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/EEAA4FC4-EA9A-DF11-8A06-002618FDA287.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/D281315A-EA9A-DF11-B4A9-0026189437FA.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/C816BC66-EB9A-DF11-96DA-00261894384F.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/B658F66A-EB9A-DF11-8D6D-002618943852.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/B0F30BE1-ED9A-DF11-8E52-001A92810AD2.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/B0E2CADD-ED9A-DF11-A076-0018F3D096AE.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/B0AC2ACE-EC9A-DF11-A4C5-002354EF3BE1.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/A6EB81DC-ED9A-DF11-925D-0026189438CF.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/A6E0E468-EB9A-DF11-92AC-00261894398C.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/A44295D8-ED9A-DF11-916C-002618943821.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/9EDA80C3-E99A-DF11-A5BB-0026189438F5.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/9ECB86D9-EB9A-DF11-A5F6-0026189437F5.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/9A814ADA-ED9A-DF11-9B81-003048678FEA.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/964D2DD7-EB9A-DF11-B98A-003048678B0C.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/94F4C76A-EB9A-DF11-A983-00261894387A.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/88C9486C-EB9A-DF11-BF79-002618943826.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/868B6067-EB9A-DF11-BC5F-00261894390A.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/8258F159-EA9A-DF11-BF7A-0018F3D095F2.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/8245D768-EA9A-DF11-B343-00261894394F.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/80CDD9CE-EC9A-DF11-914E-0030486790FE.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/7EC36B6D-EB9A-DF11-B839-001A92811728.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/7A3CD3DE-ED9A-DF11-AE29-0018F3D096E0.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/789C194E-EE9A-DF11-9220-001A92971B8C.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/782501DE-ED9A-DF11-A0EB-001A92810ADE.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/767A08D9-ED9A-DF11-B68D-003048678FC4.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/6CE8EA67-EB9A-DF11-8598-002618943926.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/6A221ACA-EF9A-DF11-8984-0018F3D0960A.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/682B5565-EA9A-DF11-A6FD-002354EF3BD0.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/66D58543-ED9A-DF11-8375-002618943944.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/666EFD66-EB9A-DF11-BCF8-0026189437F5.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/64B58ADD-ED9A-DF11-9D18-00261894387B.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/52FC1058-EA9A-DF11-B300-0026189438AA.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/5261376C-EB9A-DF11-9D5D-0026189438A5.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/3C7F7A5E-EA9A-DF11-80FE-0030486791F2.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/36ADA768-EA9A-DF11-AE7D-003048678B70.root',
        '/store/relval/CMSSW_3_9_0_pre1/RelValZEE/GEN-SIM-DIGI-RECO/MC_38Y_V8_FastSim-v1/0008/34E1BE69-EB9A-DF11-898E-002618943880.root'

    )
     )


photonPostprocessing.rBin = 48

## For single gamma pt = 35
photonValidation.eMax  = 300
photonValidation.etMax = 50
photonValidation.etScale = 0.20
photonValidation.dCotCutOn = False
photonValidation.dCotCutValue = 0.15
photonValidation.fastSim = True

process.FEVT = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring("keep *_MEtoEDMConverter_*_*"),
    fileName = cms.untracked.string('pippo.root')
)



process.p1 = cms.Path(process.tpSelection*process.photonValidationSequence*process.photonPostprocessing*process.dqmStoreStats)
process.schedule = cms.Schedule(process.p1)
