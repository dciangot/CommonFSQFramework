#!/usr/bin/env python
import CommonFSQFramework.Core.ExampleProofReader

import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm, JetCorrectionUncertainty
from ROOT import TFile, TChain, TTree,TH1,TH2

from array import *
from array import array

import time
start = time.clock()

p1="_post"

bRec_nChg_pTLeadTrack_away = array("f",[0])
bRec_nChg_pTLeadTrack_towards = array("f",[0])
bRec_nChg_pTLeadTrack_trans = array("f",[0])
bRec_nChg_pTLeadTrack_transMin = array("f",[0])
bRec_nChg_pTLeadTrack_transMax = array("f",[0])
bRec_nChg_pTLeadTrack_transDiff = array("f",[0])
bRec_pTSum_pTLeadTrack_away = array("f",[0])
bRec_pTSum_pTLeadTrack_towards = array("f",[0])
bRec_pTSum_pTLeadTrack_trans = array("f",[0])
bRec_pTSum_pTLeadTrack_transMin = array("f",[0])
bRec_pTSum_pTLeadTrack_transMax = array("f",[0])
bRec_pTSum_pTLeadTrack_transDiff = array("f",[0])
bRec_pTLeadTrack = array("f",[0])
bRec_etaLeadTrack = array("f",[0])
bRec_phiLeadTrack = array("f",[0])

bRec_evtTrue_LeadTrack = array("f",[0]) 

bGen_nChg_pTLeadTrack_away = array("f",[0])
bGen_nChg_pTLeadTrack_towards = array("f",[0])
bGen_nChg_pTLeadTrack_trans = array("f",[0])
bGen_nChg_pTLeadTrack_transMin = array("f",[0])
bGen_nChg_pTLeadTrack_transMax = array("f",[0])
bGen_nChg_pTLeadTrack_transDiff = array("f",[0])
bGen_pTSum_pTLeadTrack_away = array("f",[0])
bGen_pTSum_pTLeadTrack_towards = array("f",[0])
bGen_pTSum_pTLeadTrack_trans = array("f",[0])
bGen_pTSum_pTLeadTrack_transMin = array("f",[0])
bGen_pTSum_pTLeadTrack_transMax = array("f",[0])
bGen_pTSum_pTLeadTrack_transDiff = array("f",[0])
bGen_pTLeadTrack = array("f",[0])
bGen_etaLeadTrack = array("f",[0])
bGen_phiLeadTrack = array("f",[0])

bGen_evtTrue_LeadTrack = array("f",[0])


class universal_UEAnalyzer(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):
    def init( self):

        self.jetMode = False #DR
        self.dataMode = False #DR for lumi and trigger at the moment

        #TODO: *************BEAMSPOT IS NOT IMPLEMENTED RIGHT NOW****************
        #TODO: *************NEED SWITCHES FOR MONTE CARLO RECO+GEN OR JUST GEN AND DATA****************
        #TODO: *************JET (ESPECIALLY) AND TRACK NEEDS TO BE VALIDATED****************
        #TODO: *************NOTE THAT I HAVE DISABLED NORMALIZATION OF PROFILES AND HISTOGRAMS*********

        self.tree = ROOT.TTree("tree","ueAnalysis")
        self.tree.Branch('bRec_pTLeadTrack',   bRec_pTLeadTrack,'bRec_pTLeadTrack/F')
        self.tree.Branch('bRec_etaLeadTrack',   bRec_etaLeadTrack,'bRec_etaLeadTrack/F')
        self.tree.Branch('bRec_phiLeadTrack',   bRec_phiLeadTrack,'bRec_phiLeadTrack/F')
        self.tree.Branch('bRec_evtTrue_LeadTrack',   bRec_evtTrue_LeadTrack,'bRec_evtTrue_LeadTrack/F')
        self.tree.Branch('bGen_evtTrue_LeadTrack',   bGen_evtTrue_LeadTrack,'bGen_evtTrue_LeadTrack/F')
        self.tree.Branch('bGen_pTLeadTrack',   bGen_pTLeadTrack,'bGen_pTLeadTrack/F')
        self.tree.Branch('bGen_etaLeadTrack',   bGen_etaLeadTrack,'bGen_etaLeadTrack/F')
        self.tree.Branch('bGen_phiLeadTrack',   bGen_phiLeadTrack,'bGen_phiLeadTrack/F')
        self.tree.Branch('bRec_nChg_pTLeadTrack_away',   bRec_nChg_pTLeadTrack_away,'bRec_nChg_pTLeadTrack_away/F')
        self.tree.Branch('bRec_nChg_pTLeadTrack_towards',   bRec_nChg_pTLeadTrack_towards,'bRec_nChg_pTLeadTrack_towards/F')
        self.tree.Branch('bRec_nChg_pTLeadTrack_trans',   bRec_nChg_pTLeadTrack_trans,'bRec_nChg_pTLeadTrack_trans/F')
        self.tree.Branch('bRec_nChg_pTLeadTrack_transMin',   bRec_nChg_pTLeadTrack_transMin,'bRec_nChg_pTLeadTrack_transMin/F')
        self.tree.Branch('bRec_nChg_pTLeadTrack_transMax',   bRec_nChg_pTLeadTrack_transMax,'bRec_nChg_pTLeadTrack_transMax/F')
        self.tree.Branch('bRec_nChg_pTLeadTrack_transDiff',   bRec_nChg_pTLeadTrack_transDiff,'bRec_nChg_pTLeadTrack_transDiff/F')
        self.tree.Branch('bRec_pTSum_pTLeadTrack_away',   bRec_pTSum_pTLeadTrack_away,'bRec_pTSum_pTLeadTrack_away/F')
        self.tree.Branch('bRec_pTSum_pTLeadTrack_towards',   bRec_pTSum_pTLeadTrack_towards,'bRec_pTSum_pTLeadTrack_towards/F')
        self.tree.Branch('bRec_pTSum_pTLeadTrack_trans',   bRec_pTSum_pTLeadTrack_trans,'bRec_pTSum_pTLeadTrack_trans/F')
        self.tree.Branch('bRec_pTSum_pTLeadTrack_transMin',   bRec_pTSum_pTLeadTrack_transMin,'bRec_pTSum_pTLeadTrack_transMin/F')
        self.tree.Branch('bRec_pTSum_pTLeadTrack_transMax',   bRec_pTSum_pTLeadTrack_transMax,'bRec_pTSum_pTLeadTrack_transMax/F')
        self.tree.Branch('bRec_pTSum_pTLeadTrack_transDiff',   bRec_pTSum_pTLeadTrack_transDiff,'bRec_pTSum_pTLeadTrack_transDiff/F')
        self.tree.Branch('bGen_nChg_pTLeadTrack_away',   bGen_nChg_pTLeadTrack_away,'bGen_nChg_pTLeadTrack_away/F')
        self.tree.Branch('bGen_nChg_pTLeadTrack_towards',   bGen_nChg_pTLeadTrack_towards,'bGen_nChg_pTLeadTrack_towards/F')
        self.tree.Branch('bGen_nChg_pTLeadTrack_trans',   bGen_nChg_pTLeadTrack_trans,'bGen_nChg_pTLeadTrack_trans/F')
        self.tree.Branch('bGen_nChg_pTLeadTrack_transMin',   bGen_nChg_pTLeadTrack_transMin,'bGen_nChg_pTLeadTrack_transMin/F')
        self.tree.Branch('bGen_nChg_pTLeadTrack_transMax',   bGen_nChg_pTLeadTrack_transMax,'bGen_nChg_pTLeadTrack_transMax/F')
        self.tree.Branch('bGen_nChg_pTLeadTrack_transDiff',   bGen_nChg_pTLeadTrack_transDiff,'bGen_nChg_pTLeadTrack_transDiff/F')
        self.tree.Branch('bGen_pTSum_pTLeadTrack_away',   bGen_pTSum_pTLeadTrack_away,'bGen_pTSum_pTLeadTrack_away/F')
        self.tree.Branch('bGen_pTSum_pTLeadTrack_towards',   bGen_pTSum_pTLeadTrack_towards,'bGen_pTSum_pTLeadTrack_towards/F')
        self.tree.Branch('bGen_pTSum_pTLeadTrack_trans',   bGen_pTSum_pTLeadTrack_trans,'bGen_pTSum_pTLeadTrack_trans/F')
        self.tree.Branch('bGen_pTSum_pTLeadTrack_transMin',   bGen_pTSum_pTLeadTrack_transMin,'bGen_pTSum_pTLeadTrack_transMin/F')
        self.tree.Branch('bGen_pTSum_pTLeadTrack_transMax',   bGen_pTSum_pTLeadTrack_transMax,'bGen_pTSum_pTLeadTrack_transMax/F')
        self.tree.Branch('bGen_pTSum_pTLeadTrack_transDiff',   bGen_pTSum_pTLeadTrack_transDiff,'bGen_pTSum_pTLeadTrack_transDiff/F')
        self.GetOutputList().Add(self.tree)
	self.hist = {}
        self.hist_vertex = {}
	self.hist_pre = {}
	self.hist_post = {}
	self.hist_gen = {}
        self.hist_jet = {}
	self.hist_gent = {}
	self.hist_trans = {}
	self.hist_tow = {}
	self.hist_away = {}
	self.hist_gentow = {}
        self.hist_genaway = {}
	self.hist_full_jet = {}
	self.hist_full_tracks = {}
	self.hist_full_genjet = {}
        self.hist_full_gentracks = {}
        self.Trans_SisCon5 = {}
        self.other_SisCon5 = {}
     
	self.hist_full_genjet["fgen_ptSisCone5"] =  ROOT.TH1F("fgen_pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        self.hist_full_genjet["fgen_etaSisCone5"] =  ROOT.TH1F("fgen_eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        self.hist_full_genjet["fgen_phiSisCone5"] =  ROOT.TH1F("fgen_phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14)

        self.hist_full_gentracks["fgen_trackPt"] =  ROOT.TH1F("fgen_tracksPt",   "tracksPt",  5000, 0, 500)

        self.hist_full_jet["f_ptSisCone5"] =  ROOT.TH1F("f_pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        self.hist_full_jet["f_etaSisCone5"] =  ROOT.TH1F("f_eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        self.hist_full_jet["f_phiSisCone5"] =  ROOT.TH1F("f_phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14
)

        self.hist_full_tracks["f_trackPt"] =  ROOT.TH1F("f_trackPt",   "tracksPt",  5000, 0, 500)


        #p = "_central_B" # a placeholder for different triggers ("B") and uncertainty variations
                         #  "central" means this is a central value (ie no variations were applied)
        self.hist_vertex["nVtx"] =  ROOT.TH1F("nVtx",   "nVtx",  100, 0, 100)
        self.hist_vertex["ndfVtx"] =  ROOT.TH1F("ndfVtx",   "ndfVtx",  100, 0, 100)
	self.hist_vertex["gen_nJets"] = ROOT.TH1F("gen_nJets",   "nJets",  100, 0, 100)
	self.hist_vertex["nJets"] = ROOT.TH1F("nJets",   "nJets",  100, 0, 100)
#######        
	self.hist_pre["trackD0"] =  ROOT.TH1F("tracksD0",   "tracksD0",  2000, -10, 10)
 	self.hist_pre["trackD0Err"] =  ROOT.TH1F("tracksD0Err",   "tracksD0Err",  1000, 0, 10)
        self.hist_pre["trackD0Significance"] =  ROOT.TH1F("tracksD0Significance",   "tracksD0Sig",  2000, -100, 100)
	self.hist_pre["trackDz"] =  ROOT.TH1F("tracksDz",   "tracksDz",  20000, -100 , 100)
        self.hist_pre["trackDzErr"] =  ROOT.TH1F("tracksDzErr",   "tracksDzErr",  1000, 0, 10)
        self.hist_pre["trackDzSignificance"] =  ROOT.TH1F("tracksDzSignificance",   "tracksDzSig",  2000, -100, 100)

        self.hist_pre["trackPt"] =  ROOT.TH1F("tracksPt",   "tracksPt",  5000, 0, 500) 
	self.hist_pre["trackPtErr"] =  ROOT.TH1F("tracksPtErr",   "tracksPtErr",  5000, 0, 50)	
        self.hist_pre["trackPtSigma"] =  ROOT.TH1F("tracksPtSigma",   "tracksPtSigma",  5000, 0, 50)

	self.hist_pre["trackEta"] =  ROOT.TH1F("tracksEta",   "tracksEta",  100, -5, 5)
	self.hist_pre["trackPhi"] =  ROOT.TH1F("tracksPhi",   "tracksPhi",  628, -3.14, 3.14)
        self.hist_pre["trackDeltaPhi"] =  ROOT.TH1F("tracksDeltaPhi",   "tracksDeltaPhi",  62800, -3.14, 3.14)

	self.hist_pre["purity"] =  ROOT.TH1F("purity",   "purity",  2, 0., 2)
	self.hist_pre["imp0"] =  ROOT.TH1F("imp0",   "imp0",  2, 0., 2)
	self.hist_pre["impz"] =  ROOT.TH1F("impz",   "impz",  2, 0., 2)
	self.hist_pre["dpt"] =  ROOT.TH1F("dpt",   "dpt",  2, 0., 2)
	self.hist_pre["kin"] =  ROOT.TH1F("kin",   "kin",  2, 0., 2)
######
        self.hist_post["trackD0"+p1] =  ROOT.TH1F("tracksD0"+p1,   "tracksD0",  2000, -10, 10)
        self.hist_post["trackD0Err"+p1] =  ROOT.TH1F("tracksD0Err"+p1,   "tracksD0Err",  1000, 0, 10)
        self.hist_post["trackD0Significance"+p1] =  ROOT.TH1F("tracksD0Significance"+p1,   "tracksD0Sig",  2000, -100, 100)
        self.hist_post["trackDz"+p1] =  ROOT.TH1F("tracksDz"+p1,   "tracksD0",  20000, -100 , 100)
        self.hist_post["trackDzErr"+p1] =  ROOT.TH1F("tracksDzErr"+p1,   "tracksDzErr",  1000, 0, 10)
        self.hist_post["trackDzSignificance"+p1] =  ROOT.TH1F("tracksDzSignificance"+p1,   "tracksDzSig",  2000, -100, 100)

        self.hist_post["trackPt"+p1] =  ROOT.TH1F("tracksPt"+p1,   "tracksPt",  5000, 0, 500) 
        self.hist_post["trackPtErr"+p1] =  ROOT.TH1F("tracksPtErr"+p1,   "tracksPtErr",  5000, 0, 50)      
        self.hist_post["trackPtSigma"+p1] =  ROOT.TH1F("tracksPtSigma"+p1,   "tracksPtSigma",  5000, 0, 50)

        self.hist_post["trackEta"+p1] =  ROOT.TH1F("tracksEta"+p1,   "tracksEta",  100, -5, 5)
        self.hist_post["trackPhi"+p1] =  ROOT.TH1F("tracksPhi"+p1,   "tracksPhi",  628, -3.14, 3.14)
        self.hist_post["trackDeltaPhi"+p1] =  ROOT.TH1F("tracksDeltaPhi"+p1,   "tracksDeltaPhi",  62800, -3.14, 3.14)

	self.hist_gen["gen_trackDeltaPhi"] =  ROOT.TH1F("gen_tracksDeltaPhi",   "tracksDeltaPhi",  62800, -3.14, 3.14)
        self.hist_gen["gen_trackPt"] =  ROOT.TH1F("gen_tracksPt",   "tracksPt",  5000, 0, 500)
	self.hist_gen["gen_trackEta"] =  ROOT.TH1F("gen_tracksEta",   "tracksEta",  100, -5, 5)
        self.hist_gen["gen_trackPhi"] =  ROOT.TH1F("gen_tracksPhi",   "tracksPhi",  628, -3.14, 3.14)

######
	self.hist["gen_ptSisCone5"] =  ROOT.TH1F("gen_pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        self.hist["gen_etaSisCone5"] =  ROOT.TH1F("gen_eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        self.hist["gen_phiSisCone5"] =  ROOT.TH1F("gen_phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14)

        self.hist_jet["ptSisCone5"] =  ROOT.TH1F("pt_SisCone5",   "ptTrackJets",  200, 0, 200)
	self.hist_jet["etaSisCone5"] =  ROOT.TH1F("eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
	self.hist_jet["phiSisCone5"] =  ROOT.TH1F("phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14)
	self.hist_jet["nTracksSisCone5"] =  ROOT.TH1F("nTracks_SisCone5",   "nTracks_TracksJets",  100 , 0, 100)

	self.hist["gen_nJetTracks"] =  ROOT.TH1F("gen_nJetTracks",   "nTracks_TracksJets",  100 , 0, 100)

#	self.hist["ptSisCone7"] =  ROOT.TH1F("pt_SisCone7",   "ptTrackJets",  20, 0, 20)

#        self.hist["ptak5"] =  ROOT.TH1F("pt_ak5",   "ptTrackJets",  20, 0, 20)
#        self.hist["ptak7"] =  ROOT.TH1F("pt_ak7",   "ptTrackJets",  20, 0, 20) 
  
	self.hist["gen_nTot_SisCone5"] = ROOT.TH2F("gen_nTot_SisCone5",   "n_tot",  800, -0.5,799.5,400, 0, 200)
	self.hist_gent["gen_nTrans_SisCone5"] = ROOT.TH2F("gen_nTrans_SisCone5",   "n_trans",  80,-0.5,79.5,400, 0, 200)
        self.hist_gent["gen_ptTrans_SisCone5"] = ROOT.TH2F("gen_ptTrans_SisCone5",   "n_trans",  400, 0.,40.,400, 0, 200)
	self.hist_gent["gen_nTransMax_SisCone5"] = ROOT.TH2F("gen_nTransMax_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_gent["gen_ptTransMax_SisCone5"] = ROOT.TH2F("gen_ptTransMax_SisCone5",   "n_trans",  400, 0.,40.,400, 0, 200)

        self.hist_gent["gen_nTransMin_SisCone5"] = ROOT.TH2F("gen_nTransMin_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_gent["gen_ptTransMin_SisCone5"] = ROOT.TH2F("gen_ptTransMin_SisCone5",   "n_trans",  400, 0.,40.,200, 0, 100) 

        self.hist_gent["gen_nTransDiff_SisCone5"] = ROOT.TH2F("gen_nTransDiff_SisCone5",   "n_trans",  160, -80.5,79.5,400, 0, 200)
        self.hist_gent["gen_ptTransDiff_SisCone5"] = ROOT.TH2F("gen_ptTransDiff_SisCone5",   "n_trans",  160, -80.5,79.5,200, 0, 100)


        self.hist_genaway["gen_nAway_SisCone5"] = ROOT.TH2F("gen_nAway_SisCone5",   "n_away",  80, -0.5,79.5,200, 0, 100)
        self.hist_genaway["gen_ptAway_SisCone5"] = ROOT.TH2F("gen_ptAway_SisCone5",   "pt_away",  1000, 0.,10.,200, 0, 100)

        self.hist_gentow["gen_nTow_SisCone5"] = ROOT.TH2F("gen_nTow_SisCone5",   "n_tow",  80, -0.5,79.5,200, 0, 100)
        self.hist_gentow["gen_ptTow_SisCone5"] = ROOT.TH2F("gen_ptTow_SisCone5",   "pt_tow",  80, -0.5,79.5,200, 0, 100)


        self.hist_jet["nTot_SisCone5"] = ROOT.TH2F("nTot_SisCone5",   "n_tot",  800, -0.5,799.5,400, 0, 200)

	self.hist_trans["nTrans_SisCone5"] = ROOT.TH2F("nTrans_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_trans["ptTrans_SisCone5"] = ROOT.TH2F("ptTrans_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100)
	
	self.hist_trans["nTransMax_SisCone5"] = ROOT.TH2F("nTransMax_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_trans["ptTransMax_SisCone5"] = ROOT.TH2F("ptTransMax_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100)
	
	self.hist_trans["nTransMin_SisCone5"] = ROOT.TH2F("nTransMin_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        self.hist_trans["ptTransMin_SisCone5"] = ROOT.TH2F("ptTransMin_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100)		

        self.hist_trans["nTransDiff_SisCone5"] = ROOT.TH2F("nTransDiff_SisCone5",   "n_trans",  160, -80.5,79.5,400, 0, 200)
        self.hist_trans["ptTransDiff_SisCone5"] = ROOT.TH2F("ptTransDiff_SisCone5",   "pt_trans",  160, -80.,80.,200, 0, 100)

        self.hist_away["nAway_SisCone5"] = ROOT.TH2F("nAway_SisCone5",   "n_away",  80, -0.5,79.5,200, 0, 100)
        self.hist_away["ptAway_SisCone5"] = ROOT.TH2F("ptAway_SisCone5",   "pt_away",  1000, 0.,10.,200, 0, 100)

        self.hist_tow["nTow_SisCone5"] = ROOT.TH2F("nTow_SisCone5",   "n_tow",  80, -0.5,79.5,200, 0, 100)
        self.hist_tow["ptTow_SisCone5"] = ROOT.TH2F("ptTow_SisCone5",   "pt_tow",  1000, 0.,10.,200, 0, 100)

        for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])
	for h in self.hist_vertex:
            self.hist_vertex[h].Sumw2()
            self.GetOutputList().Add(self.hist_vertex[h])
	for h in self.hist_gen:
            self.hist_gen[h].Sumw2()
            self.GetOutputList().Add(self.hist_gen[h])
	for h in self.hist_gent:
            self.hist_gent[h].Sumw2()
            self.GetOutputList().Add(self.hist_gent[h])
	for h in self.hist_trans:
            self.hist_trans[h].Sumw2()
            self.GetOutputList().Add(self.hist_trans[h])
	for h in self.hist_pre:
            self.hist_pre[h].Sumw2()
            self.GetOutputList().Add(self.hist_pre[h])
	for h in self.hist_post:
            self.hist_post[h].Sumw2()
            self.GetOutputList().Add(self.hist_post[h])	
	for h in self.hist_jet:
            self.hist_jet[h].Sumw2()
            self.GetOutputList().Add(self.hist_jet[h])
	for h in self.hist_tow:
            self.hist_tow[h].Sumw2()
            self.GetOutputList().Add(self.hist_tow[h])
	for h in self.hist_away:
            self.hist_away[h].Sumw2()
            self.GetOutputList().Add(self.hist_away[h])
	for h in self.hist_gentow:
            self.hist_gentow[h].Sumw2()
            self.GetOutputList().Add(self.hist_gentow[h])
        for h in self.hist_genaway:
            self.hist_genaway[h].Sumw2()
            self.GetOutputList().Add(self.hist_genaway[h])
	for h in self.hist_full_genjet:
            self.hist_full_genjet[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_genjet[h])	
	for h in self.hist_full_gentracks:
            self.hist_full_gentracks[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_gentracks[h])
	for h in self.hist_full_jet:
            self.hist_full_jet[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_jet[h])
        for h in self.hist_full_tracks:
            self.hist_full_tracks[h].Sumw2()
            self.GetOutputList().Add(self.hist_full_tracks[h])


	 	

        self.Trans_SisCon5["nTransDensity"] = ROOT.TProfile("nTransDensity_SisCon5",   "n_trans",  200, 0, 100)
        self.Trans_SisCon5["ptTransDensity"] = ROOT.TProfile("ptTransDensity_SisCon5",   "pt_trans",  200, 0, 100)
	self.Trans_SisCon5["nTow"] = ROOT.TProfile("nTow_SisCon5",   "n_tow",  200, 0, 100)
        self.Trans_SisCon5["nAway"] = ROOT.TProfile("nAway_SisCon5",   "n_away",  200, 0, 100)
        self.Trans_SisCon5["ptTow"] = ROOT.TProfile("ptTow_SisCon5",   "pt_tow",  200, 0, 100)
        self.Trans_SisCon5["ptAway"] = ROOT.TProfile("ptAway_SisCon5",   "pt_away",  200, 0, 100)
        self.Trans_SisCon5["nTot"] = ROOT.TProfile("nTot_SisCon5",   "pt_away",  200, 0, 100)
        self.Trans_SisCon5["ptTot"] = ROOT.TProfile("ptTot_SisCon5",   "pt_away",  200, 0, 100)

	for h in self.Trans_SisCon5:
            self.Trans_SisCon5[h].Sumw2()
            self.GetOutputList().Add(self.Trans_SisCon5[h])	

        self.other_SisCon5["nTransMax"] = ROOT.TProfile("nTransMax_SisCon5",   "n_trans",  200, 0, 100)
        self.other_SisCon5["nTransMin"] = ROOT.TProfile("nTransMin_SisCon5",   "n_trans",  200, 0, 100)
	self.other_SisCon5["ptTransMax"] = ROOT.TProfile("ptTransMax_SisCon5",   "pt_trans",  200, 0, 100)
        self.other_SisCon5["ptTransMin"] = ROOT.TProfile("ptTransMin_SisCon5",   "pt_trans",  200, 0, 100)
	self.other_SisCon5["nDiff"] = ROOT.TProfile("nDiff_SisCon5",   "pt_diff",  200, 0, 100)
        self.other_SisCon5["ptDiff"] = ROOT.TProfile("ptDiff_SisCon5",   "pt_diff",  200, 0, 100)	

        for h in self.other_SisCon5:
            self.other_SisCon5[h].Sumw2()
            self.GetOutputList().Add(self.other_SisCon5[h])
         
        #self.eventCounter = 0

    def analyze(self):
        # note: use printTTree.py asamplename in order to learn what tries/branches are avaliable

        weight = 1 # 
        num = 0
        #self.hist["numGenTracks"].Fill(num, weight)
        #for t in self.fChain.genParticlesp4: # this collection contains four-momenta of charged genparticles
        #    self.hist["etaGenTracks"].Fill(t.eta(), weight)

        # consistency xcheck
        ''' - disabled
        sizes = set()
        sizes.add(self.fChain.dxy.size())
        sizes.add(self.fChain.dz.size())
        sizes.add(self.fChain.recoTracks.size())
        sizes.add(self.fChain.testTrkData.size())
        if len(sizes)!= 1:
            print "Wrong collection lengths:", sizes
            raise Exception("Inonsistent data")
        # '''

        #for i in xrange(0, self.fChain.dz.size()):
        #for i in xrange(0, self.fChain.testTrkData.size()):
        #for i in xrange(0, self.fChain.recoTracksp4.size()):
         #   self.hist["etaRecoTracks"].Fill(self.fChain.recoTracksp4.at(i).eta())
            
        sumpt_gen=0.
        pt_gen=-1.
        dphi_gen=999
	phi_gen=0
        eta_gen=999
        n_gen=0.
        ntracks_gen=0
        n_tow_gen=0.
        sumpt_tow_gen=0.
        n_away_gen=0.
        sumpt_away_gen=0.
	n_tot_gen=0.

        sumpt1_gen=0
        sumpt2_gen=0
        n1_gen=0
        n2_gen=0
        sumpt_max_gen=0
        sumpt_min_gen=0
        n_max_gen=0
        n_min_gen=0

        nconst=0


        weight = 1  
        num = 0

        numgoodvtx = 0
	nu=0

        vtx_x=0
        vtx_y=0
	vtx_z=0

        #SUNIL
        bGen_pTLeadTrack[0] = -999
        bGen_etaLeadTrack[0] = -999
        bGen_phiLeadTrack[0] = -999
        bGen_evtTrue_LeadTrack[0] = -100

        bGen_nChg_pTLeadTrack_away[0]         = 0
        bGen_nChg_pTLeadTrack_towards[0]      = 0
        bGen_nChg_pTLeadTrack_trans[0]        = 0
        bGen_nChg_pTLeadTrack_transMin[0]     = 0
        bGen_nChg_pTLeadTrack_transMax[0]     = 0
        bGen_nChg_pTLeadTrack_transDiff[0]    = 0
        bGen_pTSum_pTLeadTrack_away[0]        = 0
        bGen_pTSum_pTLeadTrack_towards[0]     = 0
        bGen_pTSum_pTLeadTrack_trans[0]       = 0
        bGen_pTSum_pTLeadTrack_transMin[0]    = 0
        bGen_pTSum_pTLeadTrack_transMax[0]    = 0
        bGen_pTSum_pTLeadTrack_transDiff[0]   = 0
        #/SUNIL

        #SUNIL
        bRec_pTLeadTrack[0] = -999
        bRec_etaLeadTrack[0] = -999
        bRec_phiLeadTrack[0] = -999
        bRec_evtTrue_LeadTrack[0] = -100

        bRec_nChg_pTLeadTrack_away[0]         = 0
        bRec_nChg_pTLeadTrack_towards[0]      = 0
        bRec_nChg_pTLeadTrack_trans[0]        = 0
        bRec_nChg_pTLeadTrack_transMin[0]     = 0
        bRec_nChg_pTLeadTrack_transMax[0]     = 0
        bRec_nChg_pTLeadTrack_transDiff[0]    = 0
        bRec_pTSum_pTLeadTrack_away[0]        = 0
        bRec_pTSum_pTLeadTrack_towards[0]     = 0
        bRec_pTSum_pTLeadTrack_trans[0]       = 0
        bRec_pTSum_pTLeadTrack_transMin[0]    = 0
        bRec_pTSum_pTLeadTrack_transMax[0]    = 0
        bRec_pTSum_pTLeadTrack_transDiff[0]   = 0
        #/SUNIL
















        #GEN
        #if True:  
         #self.eventCounter += 1
         #if self.eventCounter == 100: sys.exit("You have set the program to exit at 10000 events!")
        
        sumpt=0.
        pt=-1.
        dphi=999
	phi=0
        eta=999
        n=0.
        ntracks=0
        n_tow=0.
        sumpt_tow=0.
        n_away=0.
        sumpt_away=0.

	sumpt1=0
	sumpt2=0
	n1=0
	n2=0
	sumpt_max=0
	sumpt_min=0
	n_max=0
	n_min=0
	
	ptf=0
	phif=0
	etaf=0

        #DR DR DR: Can add a check to initialize these only if not self.jetMode
        l_trd0Err=[]
	l_trdzErr=[]
        l_trptErr=[]

	l_trx=[]
	l_try=[]		
	l_trz=[]

	l_trd0= []
	l_trdz=  []

        l_trHighPurity = []

        l_trGood = []


	#self.hist_vertex["nJets"].Fill(self.fChain.SisCone5CHp4.size())
        

        sumpt_gen=0.
        pt_gen=-1.
        dphi_gen=999
	phi_gen=0
        eta_gen=999
        n_gen=0.
        ntracks_gen=0
        n_tow_gen=0.
        sumpt_tow_gen=0.
        n_away_gen=0.
        sumpt_away_gen=0.
	n_tot_gen=0.

        sumpt1_gen=0
        sumpt2_gen=0
        n1_gen=0
        n2_gen=0
        sumpt_max_gen=0
        sumpt_min_gen=0
        n_max_gen=0
        n_min_gen=0

        nconst=0


        weight = 1  
        num = 0

        numgoodvtx = 0
	nu=0

        vtx_x=0
        vtx_y=0
	vtx_z=0

        #DR
        #JET MODE
        if self.jetMode:
            leadObjSize = self.fChain.sisCone5ChgGenJetsp4.size()
            leadObjp4 = self.fChain.sisCone5ChgGenJetsp4
            nJetTracks = self.fChain.sisCone5ChgGenJetsnConst
            ptMin = 1
        #TRACK MODE
        else:
            leadObjSize = self.fChain.genParticlesp4.size()
            leadObjp4 = self.fChain.genParticlesp4
            nJetTracks = self.fChain.genParticlespdg #This is a bit of an awkward placeholder for an observable tracks don't need.
            ptMin = 0.5

	#LEADING OBJECT LOOP
	for i in xrange(0, leadObjSize): #DR

                    #JET MODE   BUG? SHOULD THIS CHECK KINEMATICS?
                    if self.jetMode:
                        trackp4 = leadObjp4.at(i) #DR
                        if trackp4.pt()>ptf:
                            ptf=trackp4.pt()
                            phif=trackp4.phi()
                            etaf=trackp4.eta()

                    #TRACK MODE
                    if not self.jetMode:
                        track = leadObjp4.at(i) #DR
                        if track.pt()>0.5 and math.fabs(track.eta())<2. and not self.fChain.genParticlescharge == 0:
                            if track.pt()>ptf:
                                ptf=track.pt()
                                phif=track.phi()
                                etaf=track.eta()

        #/LEADING OBJECT LOOP



	self.hist_full_jet["f_ptSisCone5"].Fill(ptf)
        self.hist_full_jet["f_phiSisCone5"].Fill(phif)
        self.hist_full_jet["f_etaSisCone5"].Fill(etaf)

        #print "one", ptf

        if True:
            iptf = -1
            ptf = 0

            ###
	    for i in xrange(0, leadObjp4.size()): #DR # SisCone5
                    trackp4 = leadObjp4.at(i) #DR

                    if True:  #DR
                     if trackp4.pt()>ptf: #DR BIG "thought it was a BUG" WAS HERE!!!
                        ptf=trackp4.pt()
                        phif=trackp4.phi()
			etaf=trackp4.eta()
			ntracks=nJetTracks.at(i) #DR
                        iptf = i

            if not ptf < ptMin and math.fabs(etaf)<2.:
                self.hist_jet["ptSisCone5"].Fill(ptf)
		self.hist_jet["phiSisCone5"].Fill(phif)
		self.hist_jet["etaSisCone5"].Fill(etaf)
		self.hist_jet["nTracksSisCone5"].Fill(ntracks)

                #SUNIL
                bGen_pTLeadTrack[0] = ptf
                bGen_etaLeadTrack[0] = etaf
                bGen_phiLeadTrack[0] = phif
                #/SUNIL

	    #if True:	
		#print self.fChain.recoTracksd0Err.size()
                #print "SPOT 1"

                ###
                for i in xrange(0, self.fChain.genParticlesp4.size()):
		  track= self.fChain.genParticlesp4.at(i)

		  dphi_gen=track.phi()-phif #"thought it was a BUG" phi ===> phif
                  while dphi_gen > math.pi:
                         dphi_gen=dphi_gen-2*math.pi
                  while dphi_gen < -math.pi:
                         dphi_gen=dphi_gen+2*math.pi

		
		  self.hist_gen["gen_trackPt"].Fill(track.pt())
		  self.hist_gen["gen_trackEta"].Fill(track.eta())
		  self.hist_gen["gen_trackPhi"].Fill(track.phi())
		  self.hist_gen["gen_trackDeltaPhi"].Fill(dphi_gen)

                  #print "two", ptf

		  if track.pt()>0.5 and math.fabs(track.eta())<2.:	
			if not ptf < ptMin and math.fabs(etaf)<2.:
			   
                           if (dphi_gen > math.pi/3. and dphi_gen < 2*math.pi/3.):
                            n_gen=n_gen+1.
			    sumpt_gen=sumpt_gen+track.pt()

			    n1_gen=n1_gen+1
			    sumpt1_gen=sumpt1_gen+track.pt()		    			   

			   if (dphi_gen < -math.pi/3. and dphi_gen > -2*math.pi/3.):	
			    n_gen=n_gen+1.
                            sumpt_gen=sumpt_gen+track.pt()				   
	 		
			    n2_gen=n2_gen+1
			    sumpt2_gen=sumpt2_gen+track.pt()

			   if (dphi_gen < math.pi/3. and dphi_gen > -math.pi/3):
			    n_tow_gen=n_tow_gen+1
			    sumpt_tow_gen=sumpt_tow_gen+track.pt()	

			   if (dphi_gen > 2*math.pi/3. or dphi_gen < -2*math.pi/3):
			    n_away_gen=n_away_gen+1
                            sumpt_away_gen=sumpt_away_gen+track.pt()

                #print "individual n", n_gen, n_tow_gen, n_away_gen
                #print "total n", n_gen+n_tow_gen+n_away_gen
		if n_gen+n_tow_gen+n_away_gen>-1:
                 #print "FILL 3"
  	    	 self.hist_jet["nTot_SisCone5"].Fill(n_gen+n_tow_gen+n_away_gen,ptf)
                 self.Trans_SisCon5["nTot"].Fill(ptf,n_gen+n_tow_gen+n_away_gen)

                 self.Trans_SisCon5["ptTot"].Fill(ptf,sumpt_gen+sumpt_away_gen+sumpt_tow_gen)
	         #if n+n_tow+n_away>0:
                 self.hist_trans["nTrans_SisCone5"].Fill(n_gen,ptf)
		 self.Trans_SisCon5["nTransDensity"].Fill(ptf,n_gen)

                 self.Trans_SisCon5["ptTransDensity"].Fill(ptf,sumpt_gen)
                 self.hist_trans["ptTrans_SisCone5"].Fill(sumpt_gen,ptf)	
		 if sumpt1_gen>sumpt2_gen:
			sumpt_max_gen=sumpt1_gen
			sumpt_min_gen=sumpt2_gen
		 else :
			sumpt_max_gen=sumpt2_gen
                        sumpt_min_gen=sumpt1_gen
		 if n1_gen>n2_gen:
                        n_max_gen=n1_gen
                        n_min_gen=n2_gen
                 else :
                        n_max_gen=n2_gen
                        n_min_gen=n1_gen
  
		 self.hist_trans["nTransMax_SisCone5"].Fill(n_max_gen,ptf)
                 self.other_SisCon5["nTransMax"].Fill(ptf,n_max_gen)
		  	
                 self.hist_trans["ptTransMax_SisCone5"].Fill(sumpt_max_gen,ptf)
	         self.other_SisCon5["ptTransMax"].Fill(ptf,sumpt_max_gen)  

                 self.hist_trans["nTransMin_SisCone5"].Fill(n_min_gen,ptf)
		 self.other_SisCon5["nTransMin"].Fill(ptf,n_min_gen)  
			
                 self.hist_trans["ptTransMin_SisCone5"].Fill(sumpt_min_gen,ptf)	
		 self.other_SisCon5["ptTransMin"].Fill(ptf,sumpt_min_gen)

		 self.hist_trans["nTransDiff_SisCone5"].Fill(-n_min_gen+n_max_gen,ptf)
		 self.other_SisCon5["nDiff"].Fill(ptf,-n_min_gen+n_max_gen)

                 self.hist_trans["ptTransDiff_SisCone5"].Fill(-sumpt_min_gen+sumpt_max_gen,ptf)
		 self.other_SisCon5["ptDiff"].Fill(ptf,-sumpt_min_gen+sumpt_max_gen)	

		 self.hist_tow["nTow_SisCone5"].Fill(n_tow_gen,ptf)
		 self.Trans_SisCon5["nTow"].Fill(ptf,n_tow_gen)
			
                 self.hist_tow["ptTow_SisCone5"].Fill(sumpt_tow_gen,ptf)
		 self.Trans_SisCon5["ptTow"].Fill(ptf,sumpt_tow_gen)	

		 self.hist_away["nAway_SisCone5"].Fill(n_away_gen,ptf)
		 self.Trans_SisCon5["nAway"].Fill(ptf,n_away_gen)

                 self.hist_away["ptAway_SisCone5"].Fill(sumpt_away_gen,ptf)
		 self.Trans_SisCon5["ptAway"].Fill(ptf,sumpt_away_gen)	

                 #SUNIL
                 bGen_nChg_pTLeadTrack_away[0]         = n_away_gen
                 bGen_nChg_pTLeadTrack_towards[0]      = n_tow_gen
                 bGen_nChg_pTLeadTrack_trans[0]        = n_gen
                 bGen_nChg_pTLeadTrack_transMin[0]     = n_min_gen
                 bGen_nChg_pTLeadTrack_transMax[0]     = n_max_gen
                 bGen_nChg_pTLeadTrack_transDiff[0]    = -n_min_gen + n_max_gen
                 bGen_pTSum_pTLeadTrack_away[0]        = sumpt_away_gen
                 bGen_pTSum_pTLeadTrack_towards[0]     = sumpt_tow_gen
                 bGen_pTSum_pTLeadTrack_trans[0]       = sumpt_gen
                 bGen_pTSum_pTLeadTrack_transMin[0]    = sumpt_min_gen
                 bGen_pTSum_pTLeadTrack_transMax[0]    = sumpt_max_gen
                 bGen_pTSum_pTLeadTrack_transDiff[0]   = -sumpt_min_gen + sumpt_max_gen
                 bGen_evtTrue_LeadTrack[0]             = 100


































        #RECO
        goAhead = False
        if self.dataMode: 
            goAhead = self.fChain.lumi >= 90 and self.fChain.trgZeroBias == 1
        else:
            goAhead = True

        if goAhead:  
         #self.eventCounter += 1
         #if self.eventCounter == 100: sys.exit("You have set the program to exit at 10000 events!")

         for i in xrange(0, self.fChain.vtxisFake.size()):
                    
                    vtxrho = math.sqrt(self.fChain.vtxx.at(i)*self.fChain.vtxx.at(i) + self.fChain.vtxy.at(i)*self.fChain.vtxy.at(i))

		    nu=nu+1	

                    #DR: WE MUST REMEMBER TO ADD BEAMSPOT FOR DATA/NEW MONTE CARLO
                    if not self.fChain.vtxisFake.at(i) and abs(self.fChain.vtxz.at(i)) <= 10 and self.fChain.vtxndof.at(i) > 4 and vtxrho <= 2: # count only good primary vertices
                        numgoodvtx+=1
			if numgoodvtx==1:
			 vtx_x=self.fChain.vtxx.at(i)
			 vtx_y=self.fChain.vtxy.at(i)
			 vtx_z=self.fChain.vtxz.at(i)
			self.hist_vertex["ndfVtx"].Fill(self.fChain.vtxndof.at(i))	
        self.hist_vertex["nVtx"].Fill(numgoodvtx) 

        #print "Event", self.eventCounter
        #print "good vertex?", numgoodvtx
        sumpt=0.
        pt=-1.
        dphi=999
	phi=0
        eta=999
        n=0.
        ntracks=0
        n_tow=0.
        sumpt_tow=0.
        n_away=0.
        sumpt_away=0.

	sumpt1=0
	sumpt2=0
	n1=0
	n2=0
	sumpt_max=0
	sumpt_min=0
	n_max=0
	n_min=0
	
	ptf=0
	phif=0
	etaf=0

        #DR DR DR: Can add a check to initialize these only if not self.jetMode
        l_trd0Err=[]
	l_trdzErr=[]
        l_trptErr=[]

	l_trx=[]
	l_try=[]		
	l_trz=[]

	l_trd0= []
	l_trdz=  []

        l_trHighPurity = []

        l_trGood = []


	self.hist_vertex["nJets"].Fill(self.fChain.SisCone5CHp4.size())

        #DR
        #JET MODE
        if self.jetMode:
            leadObjSize = self.fChain.SisCone5CHp4.size()
            leadObjp4 = self.fChain.SisCone5CHp4
            nJetTracks = self.fChain.SisCone5CHnConst
            ptMin = 1
        #TRACK MODE
        else:
            leadObjSize = self.fChain.recoTracksp4.size()
            leadObjp4 = self.fChain.recoTracksp4
            nJetTracks = self.fChain.recoTracksnValidHits #This is a bit of an awkward placeholder for an observable tracks don't need.
            ptMin = 0.5

	#LEADING OBJECT LOOP
	for i in xrange(0, leadObjSize): #DR

                    #JET MODE
                    if self.jetMode:
                        trackp4 = leadObjp4.at(i) #DR
                        if trackp4.pt()>ptf:  
                            ptf=trackp4.pt()
                            phif=trackp4.phi()
                            etaf=trackp4.eta()

                    #TRACK MODE
                    if not self.jetMode:
		        track = self.fChain.recoTracksp4.at(i)
                        l_trd0Err.append( self.fChain.recoTracksd0Err.at(i) )
	                l_trdzErr.append( self.fChain.recoTracksdzErr.at(i) )	
                        l_trptErr.append( self.fChain.recoTracksptErr.at(i) )

	                l_trx.append( self.fChain.recoTracksvx.at(i) )
	                l_try.append( self.fChain.recoTracksvy.at(i) )	
	                l_trz.append( self.fChain.recoTracksvz.at(i) )

		        tr_x=self.fChain.recoTracksvx.at(i)
		        tr_y=self.fChain.recoTracksvy.at(i)		
		        tr_z=self.fChain.recoTracksvz.at(i) 

	                l_trd0.append( (- (tr_x-vtx_x) * track.py() + (tr_y-vtx_y) * track.px() ) / track.pt()  )

	                l_trdz.append(  (tr_z-vtx_z) - ((tr_x-vtx_x)*track.px()+(tr_y-vtx_y)*track.py())/track.pt() * (track.pz()/track.pt())	 )

                        l_trHighPurity.append( self.fChain.recoTrackshighPurity.at(i) )

                        l_trGood.append( 0 )

		        if math.fabs(l_trd0[i]/l_trd0Err[i])<3:
		            if math.fabs(l_trdz[i]/l_trdzErr[i])<3:
		                if l_trptErr[i]/track.pt()<0.05:
		                    if track.pt()>0.5 and math.fabs(track.eta())<2.:	#DR: I have to be careful with this!
                                        l_trGood[i] = 1

                        if l_trGood[i]:
                            if track.pt()>ptf:
                                ptf=track.pt()
                                phif=track.phi()
                                etaf=track.eta()

        #print "ptMax", ptf
                        
                        

        #END LEADING OBJECT LOOP



	self.hist_full_jet["f_ptSisCone5"].Fill(ptf)
        self.hist_full_jet["f_phiSisCone5"].Fill(phif)
        self.hist_full_jet["f_etaSisCone5"].Fill(etaf)
        if numgoodvtx >= 1:
            iptf = -1
            ptf = 0
            ###
	    for i in xrange(0, leadObjp4.size()): #DR # SisCone5
                    trackp4 = leadObjp4.at(i) #DR

                    proceed = False  #DR

                    if self.jetMode and self.fChain.SisCone5CHnConst.at(i) > 1: proceed = True  #DR
                    if not self.jetMode and l_trGood[i]: proceed = True  #DR

                    #print "proceed?", proceed
                    if proceed:  #DR
                     if trackp4.pt()>ptf: #DR BIG "thought it was a BUG" WAS HERE!!! "pt <==> ptf"
                        ptf=trackp4.pt()
                        phif=trackp4.phi()
			etaf=trackp4.eta()
			ntracks=nJetTracks.at(i) #DR
                        iptf = i
			#d0
			#d0err	

            ###
            #print "SPOT 0"
            #print "pt, ptMin, math.fabs(eta)", ptf, ptMin, math.fabs(eta)
            #print "ptMax", ptf
            #print "sigs", math.fabs(l_trd0[iptf]/l_trd0Err[iptf]), math.fabs(l_trdz[iptf]/l_trdzErr[iptf]), l_trptErr[iptf]/ptf, l_trHighPurity[iptf], l_trGood[iptf]
            if not ptf < ptMin and math.fabs(etaf)<2.:
                self.hist_jet["ptSisCone5"].Fill(ptf)
		self.hist_jet["phiSisCone5"].Fill(phif)
		self.hist_jet["etaSisCone5"].Fill(etaf)
		self.hist_jet["nTracksSisCone5"].Fill(ntracks)

                #SUNIL
                bRec_pTLeadTrack[0] = ptf
                bRec_etaLeadTrack[0] = etaf
                bRec_phiLeadTrack[0] = phif
                #/SUNIL

	    #if True:	
		#print self.fChain.recoTracksd0Err.size()
                #print "SPOT 1"

                ###
                for i in xrange(0, self.fChain.recoTracksd0Err.size()):
		  track= self.fChain.recoTracksp4.at(i)

                  #JET MODE
                  if self.jetMode:
		      tr_d0Err=self.fChain.recoTracksd0Err.at(i)
		      tr_dzErr=self.fChain.recoTracksdzErr.at(i) 	
		      tr_ptErr=self.fChain.recoTracksptErr.at(i)	

		      tr_x=self.fChain.recoTracksvx.at(i)
		      tr_y=self.fChain.recoTracksvy.at(i)		
		      tr_z=self.fChain.recoTracksvz.at(i) 

		      tr_d0= (- (tr_x-vtx_x) * track.py() + (tr_y-vtx_y) * track.px() ) / track.pt() 

	              tr_dz=  (tr_z-vtx_z) - ((tr_x-vtx_x)*track.px()+(tr_y-vtx_y)*track.py())/track.pt() * (track.pz()/track.pt())	

                  #TRACK MODE
                  if not self.jetMode:
		      #tr_d0=self.fChain.recoTracksd0.at(i)
		      tr_d0Err=l_trd0Err[i]
		      tr_dzErr=l_trdzErr[i]	
		      tr_ptErr=l_trptErr[i]	

		      tr_x=l_trx[i]
		      tr_y=l_try[i]		
		      tr_z=l_trz[i]

		      tr_d0=l_trd0[i]

	              tr_dz=l_trdz[i]



		  purity=0
        	  imp0= 0
        	  impz= 0
                  dpt= 0
                  kin= 0
		  dphi=track.phi()-phif #"thought it was a BUG" WAS HERE "phi"
                  while dphi > math.pi:
                         dphi=dphi-2*math.pi
                  while dphi < -math.pi:
                         dphi=dphi+2*math.pi

                  #print "FILL 1"	
		  self.hist_pre["trackD0"].Fill(tr_d0)
		  self.hist_pre["trackD0Err"].Fill(tr_d0Err)
		  self.hist_pre["trackD0Significance"].Fill(tr_d0/tr_d0Err)	
		  self.hist_pre["trackDz"].Fill(tr_dz)
                  self.hist_pre["trackDzErr"].Fill(tr_dzErr)
                  self.hist_pre["trackDzSignificance"].Fill(tr_dz/tr_dzErr)	
		  self.hist_pre["trackPt"].Fill(track.pt())
		  self.hist_pre["trackPtErr"].Fill(tr_ptErr)
		  self.hist_pre["trackPtSigma"].Fill(tr_ptErr/track.pt())
		  self.hist_pre["trackEta"].Fill(track.eta())
		  self.hist_pre["trackPhi"].Fill(track.phi())
		  self.hist_pre["trackDeltaPhi"].Fill(dphi)
		  if self.fChain.recoTrackshighPurity.at(i):
		   #purity=1	
		   if math.fabs(tr_d0/tr_d0Err)<3:
		    # imp0=1	
		     if math.fabs(tr_dz/tr_dzErr)<3:
		     # impz=1	
		      if tr_ptErr/track.pt()<0.05:
		       #dpt=1	
		       if track.pt()>0.5 and math.fabs(track.eta())<2.:	
		  	kin=1
			if not ptf < ptMin and math.fabs(etaf)<2.:# and ntracks > 1:
                           #print "FILL 2"	 		
			   self.hist_post["trackD0"+p1].Fill(tr_d0)
                 	   self.hist_post["trackD0Err"+p1].Fill(tr_d0Err)
                 	   self.hist_post["trackD0Significance"+p1].Fill(tr_d0/tr_d0Err)
                 	   self.hist_post["trackDz"+p1].Fill(tr_dz)
                 	   self.hist_post["trackDzErr"+p1].Fill(tr_dzErr)
                  	   self.hist_post["trackDzSignificance"+p1].Fill(tr_dz/tr_dzErr)
                  	   self.hist_post["trackPt"+p1].Fill(track.pt())
                  	   self.hist_post["trackPtErr"+p1].Fill(tr_ptErr)
                  	   self.hist_post["trackPtSigma"+p1].Fill(tr_ptErr/track.pt())
                  	   self.hist_post["trackEta"+p1].Fill(track.eta())
                  	   self.hist_post["trackPhi"+p1].Fill(track.phi())	
                           self.hist_post["trackDeltaPhi"+p1].Fill(dphi)	
			   
                           if (dphi > math.pi/3. and dphi < 2*math.pi/3.):
                            n=n+1.
			    sumpt=sumpt+track.pt()

			    n1=n1+1
			    sumpt1=sumpt1+track.pt()		    			   

			   if (dphi < -math.pi/3. and dphi > -2*math.pi/3.):	
			    n=n+1.
                            sumpt=sumpt+track.pt()				   
	 		
			    n2=n2+1
			    sumpt2=sumpt2+track.pt()

			   if (dphi < math.pi/3. and dphi > -math.pi/3):
			    n_tow=n_tow+1
			    sumpt_tow=sumpt_tow+track.pt()	

			   if (dphi > 2*math.pi/3. or dphi < -2*math.pi/3):
			    n_away=n_away+1
                            sumpt_away=sumpt_away+track.pt()

                  self.hist_pre["purity"].Fill(purity)
        	  self.hist_pre["imp0"].Fill(imp0)
        	  self.hist_pre["impz"].Fill(impz)
                  self.hist_pre["dpt"].Fill(dpt)
                  self.hist_pre["kin"].Fill(kin)
                #print "individual n", n, n_tow, n_away
                #print "total n", n+n_tow+n_away
		if n+n_tow+n_away>-1:
                 #print "FILL 3"
  	    	 self.hist_jet["nTot_SisCone5"].Fill(n+n_tow+n_away,ptf)
                 self.Trans_SisCon5["nTot"].Fill(ptf,n+n_tow+n_away)

                 self.Trans_SisCon5["ptTot"].Fill(ptf,sumpt+sumpt_away+sumpt_tow)
	         #if n+n_tow+n_away>0:
                 self.hist_trans["nTrans_SisCone5"].Fill(n,ptf)
		 self.Trans_SisCon5["nTransDensity"].Fill(ptf,n)

                 self.Trans_SisCon5["ptTransDensity"].Fill(ptf,sumpt)
                 self.hist_trans["ptTrans_SisCone5"].Fill(sumpt,ptf)	
		 if sumpt1>sumpt2:
			sumpt_max=sumpt1
			sumpt_min=sumpt2
		 else :
			sumpt_max=sumpt2
                        sumpt_min=sumpt1
		 if n1>n2:
                        n_max=n1
                        n_min=n2
                 else :
                        n_max=n2
                        n_min=n1
  
		 self.hist_trans["nTransMax_SisCone5"].Fill(n_max,ptf)
                 self.other_SisCon5["nTransMax"].Fill(ptf,n_max)
		  	
                 self.hist_trans["ptTransMax_SisCone5"].Fill(sumpt_max,ptf)
	         self.other_SisCon5["ptTransMax"].Fill(ptf,sumpt_max)  

                 self.hist_trans["nTransMin_SisCone5"].Fill(n_min,ptf)
		 self.other_SisCon5["nTransMin"].Fill(ptf,n_min)  
			
                 self.hist_trans["ptTransMin_SisCone5"].Fill(sumpt_min,ptf)	
		 self.other_SisCon5["ptTransMin"].Fill(ptf,sumpt_min)

		 self.hist_trans["nTransDiff_SisCone5"].Fill(-n_min+n_max,ptf)
		 self.other_SisCon5["nDiff"].Fill(ptf,-n_min+n_max)

                 self.hist_trans["ptTransDiff_SisCone5"].Fill(-sumpt_min+sumpt_max,ptf)
		 self.other_SisCon5["ptDiff"].Fill(ptf,-sumpt_min+sumpt_max)	

		 self.hist_tow["nTow_SisCone5"].Fill(n_tow,ptf)
		 self.Trans_SisCon5["nTow"].Fill(ptf,n_tow)
			
                 self.hist_tow["ptTow_SisCone5"].Fill(sumpt_tow,ptf)
		 self.Trans_SisCon5["ptTow"].Fill(ptf,sumpt_tow)	

		 self.hist_away["nAway_SisCone5"].Fill(n_away,ptf)
		 self.Trans_SisCon5["nAway"].Fill(ptf,n_away)

                 self.hist_away["ptAway_SisCone5"].Fill(sumpt_away,ptf)
		 self.Trans_SisCon5["ptAway"].Fill(ptf,sumpt_away)	

                 #SUNIL
                 bRec_nChg_pTLeadTrack_away[0]         = n_away
                 bRec_nChg_pTLeadTrack_towards[0]      = n_tow
                 bRec_nChg_pTLeadTrack_trans[0]        = n
                 bRec_nChg_pTLeadTrack_transMin[0]     = n_min
                 bRec_nChg_pTLeadTrack_transMax[0]     = n_max
                 bRec_nChg_pTLeadTrack_transDiff[0]    = -n_min + n_max
                 bRec_pTSum_pTLeadTrack_away[0]        = sumpt_away
                 bRec_pTSum_pTLeadTrack_towards[0]     = sumpt_tow
                 bRec_pTSum_pTLeadTrack_trans[0]       = sumpt
                 bRec_pTSum_pTLeadTrack_transMin[0]    = sumpt_min
                 bRec_pTSum_pTLeadTrack_transMax[0]    = sumpt_max
                 bRec_pTSum_pTLeadTrack_transDiff[0]   = -sumpt_min + sumpt_max
                 bRec_evtTrue_LeadTrack[0]             = 100
                 #/SUNIL

                 #print "Hopefully filling tree with ptMax", ptf
                 

                 if (bRec_evtTrue_LeadTrack[0] == 100 or bGen_evtTrue_LeadTrack[0] == 100): 
                     self.tree.Fill()
                     #print "Filling tree because", bRec_evtTrue_LeadTrack[0], bGen_evtTrue_LeadTrack[0]
                     #print "entry for GenpTlead should be", bGen_pTLeadTrack[0]

        return 1

    def finalize(self):
        #tree.Write()
        #outfile.Write()
        #outfile.Close()      
        end = time.clock()

        print "Finalize:"
        normFactor = self.getNormalizationFactor()
        print "  applying norm", normFactor


        #DR DR DR DR commented out to test as my analysis does not scale
        """
	for h in self.Trans_SisCon5:
           self.Trans_SisCon5[h].Scale(3/(2*4*math.pi))
	for h in self.other_SisCon5:
           self.other_SisCon5[h].Scale(3/(4*math.pi))

        for h in self.hist:
            self.hist[h].Scale(normFactor)
        """

    def finalizeWhenMerged(self):
        #
        # you can save further histograms to the output file by calling:
        #self.GetOutputList().Add(myNewHisto)
        #
        pass

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None
    maxFilesMC = None
    maxFilesData = None
    nWorkers = None # Use all

    # debug config:
    #'''
    # Run printTTree.py alone to get the samples list
    #sampleList = []
    #sampleList.append("QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6")
    #maxFilesMC = 1
    #maxFilesData = 1
    #nWorkers = 1
    maxNevents = -1
    #maxFilesData = 1
    #nWorkers =12 
    # '''


    slaveParams = {}
    #slaveParams["maxEta"] = 2.


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    universal_UEAnalyzer.runAll(treeName="UETree",
                               slaveParameters=slaveParams,
                               sampleList=sampleList,
                               maxFilesMC = maxFilesMC,
                               maxFilesData = maxFilesData,
                               maxNevents = maxNevents,
                               nWorkers=nWorkers,
				outFile = "MC_universal_tracks_8-14-15.root" )


