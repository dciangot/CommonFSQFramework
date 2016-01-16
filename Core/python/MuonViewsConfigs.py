import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    defs["MuonView"]  = cms.PSet(
        miniView = cms.string("MuonView"),
        branchPrefix = cms.untracked.string("patMuons"),
        maxEta = cms.double(5.),
        minPt = cms.double(-1),
        muons = cms.InputTag("cleanPatMuons")
    )

 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


