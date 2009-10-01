
import sys
import os
import dbs_discovery
import FWCore.ParameterSet.Config as cms


process = cms.Process("electronMcValidation")

process.DQMStore = cms.Service("DQMStore")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(),secondaryFileNames = cms.untracked.vstring())
process.source.fileNames.extend(dbs_discovery.search())

process.load("Validation.RecoEgamma.ElectronMcValidator_cfi")
process.electronMcValidator.outputFile = cms.string(os.environ['TEST_OUTPUT_FILE'])
#from RecoEgamma.Examples.mcAnalyzerFineBiningParameters_cff import *
#process.electronMcValidator.HistosConfigurationMC = cms.PSet(mcAnalyzerFineBiningParameters)

process.p = cms.Path(process.electronMcValidator)


