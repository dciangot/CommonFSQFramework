import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.patTemplate_cfg import *

from RecoTracker.Configuration.customiseForRunI import customiseForRunI

## switch to uncheduled mode
#process.options.allowUnscheduled = cms.untracked.bool(True)
#runOnData(process)
#process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(2000))

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
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.load("Configuration.StandardSequences.MagneticField_cff")


##### from Diego
# load low-pt charged GenJet configuration here
# get charged genParticles
process.load('QCDAnalysis.UEAnalysis.UEAnalysisParticles_cfi')

from RecoJets.JetProducers.sc5GenJets_cfi import sisCone5GenJets
from RecoJets.JetProducers.ak5GenJets_cfi import ak5GenJets
from RecoJets.JetProducers.FastjetParameters_cfi import *

process.load("RecoJets.Configuration.GenJetParticles_cff")

process.chargeParticles.cut = cms.string('charge != 0 & pt > 0.5 & status = 1')

process.sisCone5ChgGenJets = sisCone5GenJets.clone(rParam = 0.5, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5) )
process.sisCone7ChgGenJets = sisCone5GenJets.clone(rParam = 0.7, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5) )

process.ak5ChgGenJets = ak5GenJets.clone(rParam = 0.5, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5)  )
process.ak4ChgGenJets = ak5GenJets.clone(rParam = 0.4, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5)  )
process.ak7ChgGenJets = ak5GenJets.clone(rParam = 0.7, jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5)  )
process.ak10ChgGenJets = ak5GenJets.clone(rParam = 1., jetPtMin=1.0, src = cms.InputTag("chargeParticles"), inputEtMin     = cms.double(0.5)  )




#from CommonFSQFramework.Core.TrackWithVertexRefSelector2_cfi import *
from CommonFSQFramework.Core.TrackRefForJet_cfi import *
#from CommonTools.RecoAlgos.TrackWithVertexRefSelector_cfi import *
from RecoJets.JetProducers.TracksForJets_cff import *
#process.load("CommonTools.RecoAlgos.TrackWithVertexRefSelector_cfi")
#process.load("RecoJets.JetProducers.TracksForJets_cff")

process.TrackRefForJet=TrackRefForJet.clone()


process.TrackRefForJet.src=cms.InputTag('generalTracks') 
process.TrackRefForJet.ptMin=0.5
process.TrackRefForJet.etaMin=-2.5
process.TrackRefForJet.etaMax=2.5
process.TrackRefForJet.ptErrorCut=0.05
process.TrackRefForJet.nVertices=1
process.TrackRefForJet.vtxFallback = cms.bool(False)
process.TrackRefForJet.rhoVtx = 3
process.TrackRefForJet.zetaVtx = 3



process.trackRefsForJets=trackRefsForJets.clone()

process.trackRefsForJets.src=cms.InputTag('TrackRefForJet')

from RecoJets.JetProducers.sc5TrackJets_cfi import sisCone5TrackJets
from RecoJets.JetProducers.ak5TrackJets_cfi import ak5TrackJets


process.sisCone5TrackJets = sisCone5TrackJets.clone( rParam = 0.5, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))
process.sisCone7TrackJets = sisCone5TrackJets.clone(rParam = 0.7, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))


process.ak5TrackJets = ak5TrackJets.clone( rParam = 0.5, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))
process.ak4TrackJets = ak5TrackJets.clone( rParam = 0.4, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))
process.ak7TrackJets = ak5TrackJets.clone( rParam = 0.7, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))
process.ak10TrackJets = ak5TrackJets.clone( rParam = 1.0, jetPtMin=1.0, UseOnlyVertexTracks=True, UseOnlyOnePV=True, src = cms.InputTag("trackRefsForJets"), inputEtMin     = cms.double(0.5))



process.chargedjets = cms.Path(  
					process.UEAnalysisParticles*process.sisCone5ChgGenJets*
                                        process.sisCone7ChgGenJets*process.ak4ChgGenJets
                                        *process.ak5ChgGenJets*process.ak7ChgGenJets*process.ak10ChgGenJets*	
					process.TrackRefForJet*
					process.trackRefsForJets*
					process.sisCone5TrackJets
                                        *process.sisCone7TrackJets*process.ak4TrackJets
                                        *process.ak5TrackJets*process.ak7TrackJets*process.ak10TrackJets)

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
import CommonFSQFramework.Core.GenLevelViewsConfigs
import CommonFSQFramework.Core.JetViewsConfigs
import CommonFSQFramework.Core.RecoTrackViewsConfigs
import CommonFSQFramework.Core.VerticesViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs

process.UETree= cms.EDAnalyzer("CFFTreeProducer")

process.UETree._Parameterizable__setParameters(CommonFSQFramework.Core.GenLevelViewsConfigs.get(
        ["GenPartView","ak4ChgGenJetView","ak5ChgGenJetView","ak7ChgGenJetView","ak10ChgGenJetView","sisCone5ChgGenJetView","sisCone7ChgGenJetView"]))

process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.JetViewsConfigs.get(["JetViewSisCone5TrackJets","JetViewAk5TrackJets" ]))

process.UETree._Parameterizable__setParameters(
	CommonFSQFramework.Core.RecoTrackViewsConfigs.get(["RecoTrackView"]) 
)
process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView"])
)

process.UETree._Parameterizable__setParameters(
        CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["ZeroBiasTriggerResultsView","FullTrack12TriggerResultsView","CaloJet30TriggerResultsView","CaloJet40TriggerResultsView","CaloJet50TriggerResultsView"])
)



#process = CommonFSQFramework.Core.customizePAT.addPath(process,process.chargedgenjets)

process = CommonFSQFramework.Core.customizePAT.addPath(process,process.chargedjets)
process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.UETree)
process = CommonFSQFramework.Core.customizePAT.removeEdmOutput(process)


