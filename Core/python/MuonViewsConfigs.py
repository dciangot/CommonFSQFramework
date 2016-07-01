import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    # RecoTrackView
    defs["MuonView"]  = cms.PSet(
        miniView = cms.string("MuonView"),
        branchPrefix = cms.untracked.string("recoMuon"),
        maxEta = cms.double(2.5),
        maxDZ  = cms.double(15),
        minPt = cms.double(10),
        tracks = cms.InputTag("muons")
    )

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


