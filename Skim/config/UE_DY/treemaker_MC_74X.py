import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.patTemplate_cfg import *

from RecoTracker.Configuration.customiseForRunI import customiseForRunI

## switch to uncheduled mode
#process.options.allowUnscheduled = cms.untracked.bool(True)
#runOnData(process)
#process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

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

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

#'/store/mc/RunIISpring15DR74/MinBias_TuneCUETP8M1_13TeV-pythia8/AODSIM/NoPU_MCRUN2_74_V8-v3/70000/B0BF8704-8407-E511-AB55-D4AE526567E2.root',
#'/store/mc/RunIISpring15DR74/MinBias_TuneCUETP8M1_13TeV-pythia8/AODSIM/NoPU_MCRUN2_74_V8-v3/70000/86653091-8207-E511-99B9-C81F66B73F37.root'
#'/store/mc/RunIISpring15DR74/MinBias_TuneEE5C_13TeV-herwigpp/AODSIM/NoPURaw_castor_MCRUN2_74_V8-v1/60000/14555D3C-26FA-E411-9DD0-001E67397F71.root'
#)
'/store/mc/RunIISpring15DR74/MinBias_TuneCUETHS1_13TeV-herwigpp/AODSIM/NoPU_castor_MCRUN2_74_V8-v1/00000/00E15C10-85FA-E411-8D14-00259059649C.root'
))

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.load("Configuration.StandardSequences.MagneticField_cff")


process.charged = cms.Path(
        pfParticleSelectionForIsoSequence *
            muonPFIsolationPATSequence *
             muonMatch *
              patMuons*
               selectedPatMuons*
                cleanPatMuons
)
##### stop from Diego
#process = customiseForRunI(process)

process.out.outputCommands.append( 'keep *_*_*_*' )
# Here starts the CFF specific part

#process = customiseForRunI(process)


import CommonFSQFramework.Core.customizePAT


process = CommonFSQFramework.Core.customizePAT.customize(process)
#process.TFileService = cms.Service("TFileService", fileName = cms.string("trees_.root") )
# GT customization
#process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
import CommonFSQFramework.Core.MuonViewsConfigs
import CommonFSQFramework.Core.GenLevelViewsConfigs
import CommonFSQFramework.Core.JetViewsConfigs
import CommonFSQFramework.Core.RecoTrackViewsConfigs
import CommonFSQFramework.Core.VerticesViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs

process.UETree= cms.EDAnalyzer("CFFTreeProducer")

process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(
        ["GenPartView"]))

process.UETree._Parameterizable__setParameters(
	CommonFSQFramework.Core.RecoTrackViewsConfigs.get(["RecoTrackView"]) 
)
process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView"])
)

process.UETree._Parameterizable__setParameters(
  CommonFSQFramework.Core.MuonViewsConfigs.get(["MuonView" ]))

process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["SingleMuTriggerResultsView"])
)




process = CommonFSQFramework.Core.customizePAT.addPath(process,process.charged)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.UETree)
process = CommonFSQFramework.Core.customizePAT.removeEdmOutput(process)


