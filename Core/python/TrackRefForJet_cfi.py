import FWCore.ParameterSet.Config as cms

from CommonFSQFramework.Core.TrackRefForJetParams_cff import *

TrackRefForJet = cms.EDFilter("TrackRefForJet",
    TrackRefForJetParams
)

