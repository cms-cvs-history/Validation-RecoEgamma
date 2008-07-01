import FWCore.ParameterSet.Config as cms

photonValidation = cms.EDAnalyzer("PhotonValidator",
    OutputMEsInRootFile = cms.bool(True),
    dEtaTracksMin = cms.double(-0.2),
    eMin = cms.double(0.0),
    hcalIsolExtR = cms.double(0.3),
    dEtaTracksMax = cms.double(0.2),
    hcalIsolInnR = cms.double(0.0),
    scEndcapProducer = cms.string('correctedMulti5x5SuperClustersWithPreshower'),
    conversionOITrackProducer =cms.string('ckfOutInTracksFromConversions'),
    outInTrackCollection =cms.string(''),
    conversionIOTrackProducer =cms.string('ckfInOutTracksFromConversions'),
    inOutTrackCollection =cms.string(''),
    minTrackPtCut = cms.double(1.5),
    minBcEtCut = cms.double(0.0),
    etBin = cms.int32(100),
    etaMax = cms.double(2.5),
    phiMax = cms.double(3.14),
    r9Max = cms.double(1.1),
    phiMin = cms.double(-3.14),
    lipCut = cms.double(2.0),
    eMax = cms.double(100.0),
    OutputFileName = cms.string('PhotonValidationHistos.root'),
    photonCollection = cms.string(''),
    etaBin = cms.int32(100),
    etaBin2 = cms.int32(100),
    dEtaTracksBin = cms.int32(100),
    hbheInstance = cms.string(''),
    endcapEcalHits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    barrelEcalHits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    dPhiTracksMax = cms.double(0.5),
    hbheModule = cms.string('hbhereco'),
    trackProducer = cms.InputTag("generalTracks"),
    Verbosity = cms.untracked.int32(2),
    trkIsolInnR = cms.double(0.03),
    r9Min = cms.double(0.0),
    ecalIsolR = cms.double(0.35),
    dPhiTracksMin = cms.double(-0.5),
    phiBin = cms.int32(100),
    r9Bin = cms.int32(100),
    etMin = cms.double(0.0),
    trkIsolExtR = cms.double(0.3),
    eBin = cms.int32(100),
    maxNumOfTracksInCone = cms.int32(3),
    etMax = cms.double(100.0),
    hcalEtSumCut = cms.double(6.0),
    phoProducer = cms.string('photons'),
    minHcalHitEtCut = cms.double(0.0),
    etaMin = cms.double(-2.5),
    minPhoEtCut = cms.double(20.0),
    dPhiTracksBin = cms.int32(100),
    scBarrelProducer = cms.string('correctedHybridSuperClusters'),
    Name = cms.untracked.string('photonValidation'),
    trkPtSumCut = cms.double(9999.0),
    ecalEtSumCut = cms.double(5.0),
    dEtaMin = cms.double(-0.2),
    dEtaMax = cms.double(0.2),
    dEtaBin = cms.int32(100),
    dPhiMin = cms.double(-0.05),
    dPhiMax = cms.double(0.05),
    dPhiBin = cms.int32(100),
    rMin = cms.double(0.),
    rMax = cms.double(120),
    rBin = cms.int32(24),
    zMin = cms.double(-220.),
    zMax = cms.double(220),
    zBin = cms.int32(100)

                                  
                                   
)


