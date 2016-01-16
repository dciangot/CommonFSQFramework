import FWCore.ParameterSet.Config as cms


process = cms.Process("analysis")

#process.options.allowUnscheduled = cms.untracked.bool(True)
#runOnData(process)
#process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")


from PhysicsTools.PatAlgos.patTemplate_cfg import *
from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.jetTools import *
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.cleaningLayer1.cleanPatCandidates_cff import *
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
from PhysicsTools.PatAlgos.producersLayer1.muonProducer_cff import *
from PhysicsTools.PatAlgos import *
import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.muonMatch_cfi import *
from TrackingTools.TransientTrack.TransientTrackBuilder_cfi import *
from PhysicsTools.PatAlgos.producersLayer1.muonProducer_cfi import *

from PhysicsTools.PatAlgos.recoLayer0.pfParticleSelectionForIso_cff import *
from PhysicsTools.PatAlgos.recoLayer0.pfMuonIsolationPAT_cff import *


process.load("PhysicsTools.PatAlgos.patSequences_cff")
runOnData(process)


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

#'/store/mc/RunIISpring15DR74/MinBias_TuneCUETP8M1_13TeV-pythia8/AODSIM/NoPU_MCRUN2_74_V8-v3/70000/B0BF8704-8407-E511-AB55-D4AE526567E2.root',
#'/store/mc/RunIISpring15DR74/MinBias_TuneCUETP8M1_13TeV-pythia8/AODSIM/NoPU_MCRUN2_74_V8-v3/70000/86653091-8207-E511-99B9-C81F66B73F37.root'
#'/store/mc/RunIISpring15DR74/MinBias_TuneEE5C_13TeV-herwigpp/AODSIM/NoPURaw_castor_MCRUN2_74_V8-v1/60000/14555D3C-26FA-E411-9DD0-001E67397F71.root'
#)
#'/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/0071FA3B-5738-E511-8E71-20CF3027A59F.root'
#'/store/data/Run2015D/DoubleMuon/AOD/PromptReco-v4/000/258/159/00000/0823175D-D16B-E511-90DC-02163E0139B5.root'
#'/store/data/Run2015D/SingleMuon/AOD/PromptReco-v4/000/258/159/00000/0C2C8F20-246C-E511-B27C-02163E0143D6.root'
'/store/data/Run2015D/DoubleMuon/AOD/PromptReco-v4/000/258/159/00000/2A133FB7-B56B-E511-9D56-02163E011F4E.root',
#'/store/data/Run2015D/DoubleMuon/AOD/PromptReco-v4/000/258/159/00000/0823175D-D16B-E511-90DC-02163E0139B5.root',
#'/store/data/Run2015D/DoubleMuon/AOD/PromptReco-v4/000/258/159/00000/0823175D-D16B-E511-90DC-02163E0139B5.root'
))

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data')
process.load("Configuration.StandardSequences.MagneticField_cff")



process.charged = cms.Path(
                  #       process.UEAnalysisParticles *
    pfParticleSelectionForIsoSequence *
    muonPFIsolationPATSequence *
    patMuons*
    selectedPatMuons*
    cleanPatMuons
                                 )

process.out.outputCommands.append( 'keep *_*_*_*' )

import CommonFSQFramework.Core.customizePAT

process = CommonFSQFramework.Core.customizePAT.customize(process)
process.TFileService = cms.Service("TFileService", fileName = cms.string("trees_.root") )
# GT customization
#process = CommonFSQFramework.Core.customizePAT.customizeGT(process)


# define treeproducer
#import CommonFSQFramework.Core.GenLevelViewsConfigs
import CommonFSQFramework.Core.MuonViewsConfigs
import CommonFSQFramework.Core.RecoTrackViewsConfigs
import CommonFSQFramework.Core.VerticesViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs

process.UETree= cms.EDAnalyzer("CFFTreeProducer")

#process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(
#        ["GenPartView"]))

process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.MuonViewsConfigs.get(["MuonView" ]))

process.UETree._Parameterizable__setParameters(
	CommonFSQFramework.Core.RecoTrackViewsConfigs.get(["RecoTrackView"]) 
)
process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView"])
)

process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["SingleMuTriggerResultsView"])
######################################################
### qui dovrebbe essere DoubleMuTrigerResultsView ####
######################################################

)


#process = CommonFSQFramework.Core.customizePAT.addPath(process,process.chargedgenjets)

process = CommonFSQFramework.Core.customizePAT.addPath(process,process.charged)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.UETree)
process = CommonFSQFramework.Core.customizePAT.removeEdmOutput(process)

