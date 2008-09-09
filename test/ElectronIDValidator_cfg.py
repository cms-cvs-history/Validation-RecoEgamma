from FWCore.ParameterSet.Config import *

process = cms.Process("TestElectronIDValidator")

process.extend(include("FWCore/MessageLogger/data/MessageLogger.cfi"))
process.extend(include("RecoEcal/EgammaClusterProducers/data/geometryForClustering.cff"))

process.load("Validation.RecoEgamma.electronIDValidator_cfi")

process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(1000)
   input = cms.untracked.int32(-1)
)

from Validation.RecoEgamma.electronIDValidator_cfi import *
#ElectronIDValidation.outputFile = 'ElectronIDValidationRelVal214_FastZEE.root'
ElectronIDValidation.outputFile = 'ElectronIDValidationRelVal214_FullZEE.root'

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#CMSSW_2_1_4 Official RelVal ZEE STARTUP_v5
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/24C809BB-7B6C-DD11-BD2F-000423D98804.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/28BFA0B5-7B6C-DD11-862C-000423D98E6C.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/2A0645B9-7B6C-DD11-9B7E-000423D98B08.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/2C25C8D8-7B6C-DD11-9170-000423D95220.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/2EDCCFF4-7B6C-DD11-A50D-000423D94AA8.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/3248F018-7C6C-DD11-8FA0-000423D94AA8.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/58F4E311-7C6C-DD11-B3F3-000423D94A20.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/66E57EBE-7B6C-DD11-B51F-000423D9870C.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/785C61E9-7B6C-DD11-BCF4-000423D94494.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/7E323EB8-7B6C-DD11-AF0F-001617C3B6C6.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/90AFA4AE-7B6C-DD11-9BBC-000423D991F0.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/DA35D7B5-7B6C-DD11-9F3C-001617C3B6CC.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/DEE028DD-7B6C-DD11-B4AB-0016177CA7A0.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/E6B7481F-7C6C-DD11-9C0A-000423D94990.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/F2742DEA-7B6C-DD11-8AD1-000423D98FBC.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0004/FCBD1C52-7C6C-DD11-B420-000423D99896.root',
    '/store/relval/CMSSW_2_1_4/RelValZEE/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/STARTUP_V5_v1/0005/0C6F68BA-AC6C-DD11-B226-001617C3B66C.root'
   ),
    secondaryFileNames = cms.untracked.vstring (
   )
)

process.p = cms.Path(process.ElectronIDValidation)
process.schedule = cms.Schedule(process.p)
