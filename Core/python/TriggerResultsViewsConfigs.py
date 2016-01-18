import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    defs["SingleMuTriggerResultsView"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trgsnglMu"),
        process = cms.string("HLT"),
        triggers = cms.vstring("Iso_Mu20"),
        Iso_Mu20 = cms.vstring("HLT_IsoMu20_*")
    )

    defs["MinBiasTriggerResultsView"]  = cms.PSet(
            miniView = cms.string("TriggerResultsView"),
            branchPrefix = cms.untracked.string("trgMinB"),
            process = cms.string("HLT"),
            triggers = cms.vstring("HLT_L1MinBiasHF1OR*_*","HLT_L1MinBiasHF1AND*_*")
            )

    # ZeroBias trigger configuration
    defs["ZeroBiasTriggerResultsView"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trg"),
        process = cms.string("HLT"),
        triggers = cms.vstring("ZeroBias"),
        ZeroBias = cms.vstring("HLT_ZeroBias_*")
    )

    defs["L1GTriggerResultsView"] = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trgl1"),
        process = cms.string("HLT"),
        triggers = cms.vstring("L1GTTech","L1GTAlgo")
    )

    defs["CaloJet30TriggerResultsView"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trgJet1"),
        process = cms.string("HLT"),
        triggers = cms.vstring("AK4CaloJet30ForEndOfFill"),
        AK4CaloJet30ForEndOfFill = cms.vstring("HLT_AK4CaloJet30*")
    )

    defs["CaloJet40TriggerResultsView"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trgJet2"),
        process = cms.string("HLT"),
        triggers = cms.vstring("AK4CaloJet40ForEndOfFill"),
        AK4CaloJet40ForEndOfFill = cms.vstring("HLT_AK4CaloJet40*")
    )

    defs["CaloJet50TriggerResultsView"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trgJet3"),
        process = cms.string("HLT"),
        triggers = cms.vstring("AK4CaloJet50ForEndOfFill"),
        AK4CaloJet50ForEndOfFill = cms.vstring("HLT_AK4CaloJet50*")
    )


    defs["FullTrack12TriggerResultsView"]  = cms.PSet(
        miniView = cms.string("TriggerResultsView"),
        branchPrefix = cms.untracked.string("trgTr"),
        process = cms.string("HLT"),
        triggers = cms.vstring("FullTrack12"),
        FullTrack12 = cms.vstring("HLT_FullTrack12*")

    )


 
    # main function
    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret


