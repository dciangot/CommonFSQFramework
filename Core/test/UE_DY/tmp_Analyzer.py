#!/usr/bin/env python
import sys, os, time, math
import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import TFile, TChain, TTree,TH1,TH2
#from ROOT import edm, JetCorrectionUncertainty

from array import *
from array import array
val_PI = math.pi 
val2_PI3 = 2*val_PI/3.
val_PI3 = val_PI/3.
boolFillHist = "TRUE"
import time
start = time.clock()
datatype = "runtype"
if datatype == "TRUE":
   isData = 1
else:
   isData = 0  
outfile = TFile("outputFile","recreate")
tree = ROOT.TTree("tree","ueAnalysis")

p1="_post"

if boolFillHist == "TRUE": 
        TH1.SetDefaultSumw2(True) 
        hist = {}
        hist_vertex = {}
        hist_pre = {}
        hist_post = {}
        hist_gen = {}
        hist_jet = {}
        hist_gent = {}
        hist_trans = {}
        hist_tow = {}
        hist_away = {}
        hist_gentow = {}
        hist_genaway = {}
        hist_full_jet = {}
        hist_full_tracks = {}
        hist_full_genjet = {}
        hist_full_gentracks = {}
        Trans_SisCon5 = {}
        other_SisCon5 = {}
	noScale_SisCon5 = {}



        hist_full_genjet["fgen_ptSisCone5"] =  ROOT.TH1F("fgen_pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        hist_full_genjet["fgen_etaSisCone5"] =  ROOT.TH1F("fgen_eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        hist_full_genjet["fgen_phiSisCone5"] =  ROOT.TH1F("fgen_phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14)

        hist_full_gentracks["fgen_trackPt"] =  ROOT.TH1F("fgen_tracksPt",   "tracksPt",  5000, 0, 500)

        hist_full_jet["f_ptSisCone5"] =  ROOT.TH1F("f_pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        hist_full_jet["f_etaSisCone5"] =  ROOT.TH1F("f_eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        hist_full_jet["f_phiSisCone5"] =  ROOT.TH1F("f_phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14
)

        hist_full_tracks["f_trackPt"] =  ROOT.TH1F("f_trackPt",   "tracksPt",  5000, 0, 500)


        #p = "_central_B" # a placeholder for different triggers ("B") and uncertainty variations
                         #  "central" means this is a central value (ie no variations were applied)
        hist_vertex["nVtx"] =  ROOT.TH1F("nVtx",   "nVtx",  100, 0, 100)
        hist_vertex["ndfVtx"] =  ROOT.TH1F("ndfVtx",   "ndfVtx",  100, 0, 100)
        hist_vertex["gen_nJets"] = ROOT.TH1F("gen_nJets",   "nJets",  100, 0, 100)
        hist_vertex["nJets"] = ROOT.TH1F("nJets",   "nJets",  100, 0, 100)
#######        
        hist_pre["trackD0"] =  ROOT.TH1F("tracksD0",   "tracksD0",  2000, -10, 10)
        hist_pre["trackD0Err"] =  ROOT.TH1F("tracksD0Err",   "tracksD0Err",  1000, 0, 10)
        hist_pre["trackD0Significance"] =  ROOT.TH1F("tracksD0Significance",   "tracksD0Sig",  2000, -100, 100)
        hist_pre["trackDz"] =  ROOT.TH1F("tracksDz",   "tracksDz",  20000, -100 , 100)

	hist_pre["trackDzErr"] =  ROOT.TH1F("tracksDzErr",   "tracksDzErr",  1000, 0, 10)
        hist_pre["trackDzSignificance"] =  ROOT.TH1F("tracksDzSignificance",   "tracksDzSig",  2000, -100, 100)

        hist_pre["trackPt"] =  ROOT.TH1F("tracksPt",   "tracksPt",  5000, 0, 500)
        hist_pre["trackPtErr"] =  ROOT.TH1F("tracksPtErr",   "tracksPtErr",  5000, 0, 50)
        hist_pre["trackPtSigma"] =  ROOT.TH1F("tracksPtSigma",   "tracksPtSigma",  5000, 0, 50)

        hist_pre["trackEta"] =  ROOT.TH1F("tracksEta",   "tracksEta",  100, -5, 5)
        hist_pre["trackPhi"] =  ROOT.TH1F("tracksPhi",   "tracksPhi",  628, -3.14, 3.14)
        hist_pre["trackDeltaPhi"] =  ROOT.TH1F("tracksDeltaPhi",   "tracksDeltaPhi",  62800, -3.14, 3.14)

        hist_pre["purity"] =  ROOT.TH1F("purity",   "purity",  2, 0., 2)
        hist_pre["imp0"] =  ROOT.TH1F("imp0",   "imp0",  2, 0., 2)
        hist_pre["impz"] =  ROOT.TH1F("impz",   "impz",  2, 0., 2)
        hist_pre["dpt"] =  ROOT.TH1F("dpt",   "dpt",  2, 0., 2)
        hist_pre["kin"] =  ROOT.TH1F("kin",   "kin",  2, 0., 2)
######
        hist_post["trackD0"+p1] =  ROOT.TH1F("tracksD0"+p1,   "tracksD0",  2000, -10, 10)
        hist_post["trackD0Err"+p1] =  ROOT.TH1F("tracksD0Err"+p1,   "tracksD0Err",  1000, 0, 10)
        hist_post["trackD0Significance"+p1] =  ROOT.TH1F("tracksD0Significance"+p1,   "tracksD0Sig",  2000, -100, 100)
        hist_post["trackDz"+p1] =  ROOT.TH1F("tracksDz"+p1,   "tracksD0",  20000, -100 , 100)
        hist_post["trackDzErr"+p1] =  ROOT.TH1F("tracksDzErr"+p1,   "tracksDzErr",  1000, 0, 10)
        hist_post["trackDzSignificance"+p1] =  ROOT.TH1F("tracksDzSignificance"+p1,   "tracksDzSig",  2000, -100, 100)

        hist_post["trackPt"+p1] =  ROOT.TH1F("tracksPt"+p1,   "tracksPt",  5000, 0, 500)
        hist_post["trackPtErr"+p1] =  ROOT.TH1F("tracksPtErr"+p1,   "tracksPtErr",  5000, 0, 50)
        hist_post["trackPtSigma"+p1] =  ROOT.TH1F("tracksPtSigma"+p1,   "tracksPtSigma",  5000, 0, 50)

        hist_post["trackEta"+p1] =  ROOT.TH1F("tracksEta"+p1,   "tracksEta",  100, -5, 5)
        hist_post["trackPhi"+p1] =  ROOT.TH1F("tracksPhi"+p1,   "tracksPhi",  628, -3.14, 3.14)
        hist_post["trackDeltaPhi"+p1] =  ROOT.TH1F("tracksDeltaPhi"+p1,   "tracksDeltaPhi",  62800, -3.14, 3.14)

        hist_gen["gen_trackDeltaPhi"] =  ROOT.TH1F("gen_tracksDeltaPhi",   "tracksDeltaPhi",  62800, -3.14, 3.14)
        hist_gen["gen_trackPt"] =  ROOT.TH1F("gen_tracksPt",   "tracksPt",  5000, 0, 500)
        hist_gen["gen_trackEta"] =  ROOT.TH1F("gen_tracksEta",   "tracksEta",  100, -5, 5)
        hist_gen["gen_trackPhi"] =  ROOT.TH1F("gen_tracksPhi",   "tracksPhi",  628, -3.14, 3.14)

######
        hist["gen_ptSisCone5"] =  ROOT.TH1F("gen_pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        hist["gen_etaSisCone5"] =  ROOT.TH1F("gen_eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        hist["gen_phiSisCone5"] =  ROOT.TH1F("gen_phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14)

        hist_jet["ptSisCone5"] =  ROOT.TH1F("pt_SisCone5",   "ptTrackJets",  200, 0, 200)
        hist_jet["etaSisCone5"] =  ROOT.TH1F("eta_SisCone5",   "etaTrackJets",  100 , -5, 5)
        hist_jet["phiSisCone5"] =  ROOT.TH1F("phi_SisCone5",   "phiTrackJets",  628 , -3.14, 3.14)
        hist_jet["nTracksSisCone5"] =  ROOT.TH1F("nTracks_SisCone5",   "nTracks_TracksJets",  100 , 0, 100)

        hist["gen_nJetTracks"] =  ROOT.TH1F("gen_nJetTracks",   "nTracks_TracksJets",  100 , 0, 100)

#       hist["ptSisCone7"] =  ROOT.TH1F("pt_SisCone7",   "ptTrackJets",  20, 0, 20)

#        hist["ptak5"] =  ROOT.TH1F("pt_ak5",   "ptTrackJets",  20, 0, 20)
#        hist["ptak7"] =  ROOT.TH1F("pt_ak7",   "ptTrackJets",  20, 0, 20) 

        hist["gen_nTot_SisCone5"] = ROOT.TH2F("gen_nTot_SisCone5",   "n_tot",  800, -0.5,799.5,400, 0, 200)
        hist_gent["gen_nTrans_SisCone5"] = ROOT.TH2F("gen_nTrans_SisCone5",   "n_trans",  80,-0.5,79.5,400, 0, 200)
        hist_gent["gen_ptTrans_SisCone5"] = ROOT.TH2F("gen_ptTrans_SisCone5",   "n_trans",  400, 0.,40.,400, 0, 200)
        hist_gent["gen_nTransMax_SisCone5"] = ROOT.TH2F("gen_nTransMax_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        hist_gent["gen_ptTransMax_SisCone5"] = ROOT.TH2F("gen_ptTransMax_SisCone5",   "n_trans",  400, 0.,40.,400, 0, 200)

        hist_gent["gen_nTransMin_SisCone5"] = ROOT.TH2F("gen_nTransMin_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        hist_gent["gen_ptTransMin_SisCone5"] = ROOT.TH2F("gen_ptTransMin_SisCone5",   "n_trans",  400, 0.,40.,200, 0, 100)

        hist_gent["gen_nTransDiff_SisCone5"] = ROOT.TH2F("gen_nTransDiff_SisCone5",   "n_trans",  160, -80.5,79.5,400, 0, 200)
        hist_gent["gen_ptTransDiff_SisCone5"] = ROOT.TH2F("gen_ptTransDiff_SisCone5",   "n_trans",  160, -80.5,79.5,200, 0, 100)


        hist_genaway["gen_nAway_SisCone5"] = ROOT.TH2F("gen_nAway_SisCone5",   "n_away",  80, -0.5,79.5,200, 0, 100)
        hist_genaway["gen_ptAway_SisCone5"] = ROOT.TH2F("gen_ptAway_SisCone5",   "pt_away",  1000, 0.,10.,200, 0, 100)

        hist_gentow["gen_nTow_SisCone5"] = ROOT.TH2F("gen_nTow_SisCone5",   "n_tow",  80, -0.5,79.5,200, 0, 100)
        hist_gentow["gen_ptTow_SisCone5"] = ROOT.TH2F("gen_ptTow_SisCone5",   "pt_tow",  80, -0.5,79.5,200, 0, 100)


        hist_jet["nTot_SisCone5"] = ROOT.TH2F("nTot_SisCone5",   "n_tot",  800, -0.5,799.5,400, 0, 200)

        hist_trans["nTrans_SisCone5"] = ROOT.TH2F("nTrans_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        hist_trans["ptTrans_SisCone5"] = ROOT.TH2F("ptTrans_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100)

        hist_trans["nTransMax_SisCone5"] = ROOT.TH2F("nTransMax_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        hist_trans["ptTransMax_SisCone5"] = ROOT.TH2F("ptTransMax_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100)

        hist_trans["nTransMin_SisCone5"] = ROOT.TH2F("nTransMin_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200)
        hist_trans["ptTransMin_SisCone5"] = ROOT.TH2F("ptTransMin_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100)

        hist_trans["nTransDiff_SisCone5"] = ROOT.TH2F("nTransDiff_SisCone5",   "n_trans",  160, -80.5,79.5,400, 0, 200)
        hist_trans["ptTransDiff_SisCone5"] = ROOT.TH2F("ptTransDiff_SisCone5",   "pt_trans",  160, -80.,80.,200, 0, 100)

        hist_away["nAway_SisCone5"] = ROOT.TH2F("nAway_SisCone5",   "n_away",  80, -0.5,79.5,200, 0, 100)
        hist_away["ptAway_SisCone5"] = ROOT.TH2F("ptAway_SisCone5",   "pt_away",  1000, 0.,10.,200, 0, 100)

        hist_tow["nTow_SisCone5"] = ROOT.TH2F("nTow_SisCone5",   "n_tow",  80, -0.5,79.5,200, 0, 100)
        hist_tow["ptTow_SisCone5"] = ROOT.TH2F("ptTow_SisCone5",   "pt_tow",  1000, 0.,10.,200, 0, 100)
	
	Trans_SisCon5["nTransDensity"] = ROOT.TProfile("nTransDensity_SisCon5",   "n_trans",  200, 0, 100)
        Trans_SisCon5["ptTransDensity"] = ROOT.TProfile("ptTransDensity_SisCon5",   "pt_trans",  200, 0, 100)


        other_SisCon5["nTransMax"] = ROOT.TProfile("nTransMax_SisCon5",   "n_trans",  200, 0, 100)
        other_SisCon5["nTransMin"] = ROOT.TProfile("nTransMin_SisCon5",   "n_trans",  200, 0, 100)
        other_SisCon5["ptTransMax"] = ROOT.TProfile("ptTransMax_SisCon5",   "pt_trans",  200, 0, 100)
        other_SisCon5["ptTransMin"] = ROOT.TProfile("ptTransMin_SisCon5",   "pt_trans",  200, 0, 100)
        other_SisCon5["nTow"] = ROOT.TProfile("nTow_SisCon5",   "n_tow",  200, 0, 100)
        other_SisCon5["nAway"] = ROOT.TProfile("nAway_SisCon5",   "n_away",  200, 0, 100)
        other_SisCon5["ptTow"] = ROOT.TProfile("ptTow_SisCon5",   "pt_tow",  200, 0, 100)
        other_SisCon5["ptAway"] = ROOT.TProfile("ptAway_SisCon5",   "pt_away",  200, 0, 100)
        other_SisCon5["nDiff"] = ROOT.TProfile("nDiff_SisCon5",   "pt_diff",  200, 0, 100)
        other_SisCon5["ptDiff"] = ROOT.TProfile("ptDiff_SisCon5",   "pt_diff",  200, 0, 100)


	noScale_SisCon5["ptAveTrans"] = ROOT.TProfile("ptAveTrans",   "pt_away",  200, 0, 100)
        noScale_SisCon5["ptAveTow"] = ROOT.TProfile("ptAveTow",   "pt_away",  200, 0, 100)
	noScale_SisCon5["ptAveAway"] = ROOT.TProfile("ptAveAway",   "pt_away",  200, 0, 100)

	hist_tow["ptAVETow_SisCone5"] = ROOT.TH2F("ptAVETow_SisCone5",   "ptAVE_tow",  1000, 0.,100.,200, 0, 100)
        hist_away["ptAVEAway_SisCone5"] = ROOT.TH2F("ptAVEAway_SisCone5",   "ptAVE_away",  1000, 0.,100.,200, 0, 100)        
        hist_trans["ptAVETrans_SisCone5"] = ROOT.TH2F("ptAVETrans_SisCone5",   "ptAVE_trans",  1000, 0.,100.,200, 0, 100)
	hist_jet["ptAVETot_SisCone5"] = ROOT.TH2F("ptAVETot_SisCone5",   "ptAVE_tot",  1000, 0.,100.,200, 0, 100)


	Trans_SisCon5["nTransDensity"] = ROOT.TProfile("nTransDensity_SisCon5",   "n_trans",  200, 0, 100)
        Trans_SisCon5["ptTransDensity"] = ROOT.TProfile("ptTransDensity_SisCon5",   "pt_trans",  200, 0, 100)
	Trans_SisCon5["nTow"] = ROOT.TProfile("nTow_SisCon5",   "n_tow",  200, 0, 100)
        Trans_SisCon5["nAway"] = ROOT.TProfile("nAway_SisCon5",   "n_away",  200, 0, 100)
        Trans_SisCon5["ptTow"] = ROOT.TProfile("ptTow_SisCon5",   "pt_tow",  200, 0, 100)
        Trans_SisCon5["ptAway"] = ROOT.TProfile("ptAway_SisCon5",   "pt_away",  200, 0, 100)
        Trans_SisCon5["nTot"] = ROOT.TProfile("nTot_SisCon5",   "pt_away",  200, 0, 100)
        Trans_SisCon5["ptTot"] = ROOT.TProfile("ptTot_SisCon5",   "pt_away",  200, 0, 100)


fChain = TChain("UETree/data")
inputFile


nentry = fChain.GetEntries()
print nentry
for i in range(0,nentry):
   fChain.GetEntry(i)
   if isData == 0:  
	weight = 1 # 
        num = 0
        num = fChain.genParticlesp4.size()
        #hist["numGenTracks"].Fill(num, weight)
        #for t in fChain.genParticlesp4: # this collection contains four-momenta of charged genparticles
        #    hist["etaGenTracks"].Fill(t.eta(), weight)

        # consistency xcheck
        ''' - disabled
        sizes = set()
        sizes.add(fChain.dxy.size())
        sizes.add(fChain.dz.size())
        sizes.add(fChain.recoTracks.size())
        sizes.add(fChain.testTrkData.size())
        if len(sizes)!= 1:
            print "Wrong collection lengths:", sizes
            raise Exception("Inonsistent data")
        # '''

        #for i in xrange(0, fChain.dz.size()):
        #for i in xrange(0, fChain.testTrkData.size()):
        #for i in xrange(0, fChain.recoTracksp4.size()):
         #   hist["etaRecoTracks"].Fill(fChain.recoTracksp4.at(i).eta())

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
           
        #Loop over tracks ends
 
	nconst=0

        hist_vertex["gen_nJets"].Fill(fChain.sisCone5ChgGenJetsp4.size())


        for track in fChain.genParticlesp4:
                  hist_full_gentracks["fgen_trackPt"].Fill(track.pt())

        #print tracks.getSize()
        #for tracksg in tracks.get(""):
        #          track=tracksg.p4
        #          hist_full_tracks["f_trackPt"].Fill(track.pt())

        for i in  xrange(0, fChain.sisCone5ChgGenJetsp4.size()): # SisCone5
                trackp4=fChain.sisCone5ChgGenJetsp4.at(i)
                if fChain.sisCone5ChgGenJetsnConst.at(i)>1:
                  hist["gen_nJetTracks"].Fill(fChain.sisCone5ChgGenJetsnConst.at(i))
                  if trackp4.pt()>pt_gen:

                        pt_gen=trackp4.pt()
                        phi_gen=trackp4.phi()
                        eta_gen=trackp4.eta()

        hist_full_genjet["fgen_ptSisCone5"].Fill(pt_gen)
        hist_full_genjet["fgen_phiSisCone5"].Fill(phi_gen)
        hist_full_genjet["fgen_etaSisCone5"].Fill(eta_gen)
#       hist_full_genjet["gen_nTracks_SisCone5"].Fill(trackjetg.s_number_of_tracks) TO DO
        if not pt_gen < 1. and math.fabs(eta_gen)<2.: # and trackjetg._genJets_number_of_tracks>1 :
               hist["gen_ptSisCone5"].Fill(pt_gen)
               hist["gen_phiSisCone5"].Fill(phi_gen)
               hist["gen_etaSisCone5"].Fill(eta_gen)
        #if True:
               for i in xrange(0,fChain.genParticlescharge.size()):
                  track=fChain.genParticlesp4.at(i)
                  dphi_gen=track.phi()-phi_gen
                  charge=fChain.genParticlescharge.at(i)
                  while dphi_gen > math.pi:
                         dphi_gen=dphi_gen-2*math.pi
                  while dphi_gen < -math.pi:
                         dphi_gen=dphi_gen+2*math.pi

                  if track.pt()>0.5 and math.fabs(track.eta())<2. and not charge==0: #and genTracks.getSize()>4:
                     hist_gen["gen_trackDeltaPhi"].Fill(dphi_gen)
                     hist_gen["gen_trackPt"].Fill(track.pt())
                     hist_gen["gen_trackEta"].Fill(track.eta())
                     hist_gen["gen_trackPhi"].Fill(track.phi())
		     if not pt_gen < 1. and math.fabs(eta_gen)<2. :
                      n_tot_gen=n_tot_gen+1

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

         #     if n_tot_gen > 0:
               hist["gen_nTot_SisCone5"].Fill(n_tot_gen,pt_gen)
        #       if n_gen>0:
               hist_gent["gen_ptTrans_SisCone5"].Fill(sumpt_gen,pt_gen)
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

               hist_gent["gen_nTrans_SisCone5"].Fill(n_max_gen+n_min_gen,pt_gen)
##### 3./(2.*4*math.pi)
               hist_gent["gen_nTransMax_SisCone5"].Fill(n_max_gen,pt_gen)		
 
    	       hist_gent["gen_ptTransMax_SisCone5"].Fill(sumpt_max_gen,pt_gen)
               hist_gent["gen_nTransMin_SisCone5"].Fill(n_min_gen,pt_gen)
               hist_gent["gen_ptTransMin_SisCone5"].Fill(sumpt_min_gen,pt_gen)
               hist_gent["gen_nTransDiff_SisCone5"].Fill(-n_min_gen+n_max_gen,pt_gen)
               hist_gent["gen_ptTransDiff_SisCone5"].Fill(-sumpt_min_gen+sumpt_max_gen,pt_gen)
        #       if n_tow_gen>0:
               hist_gentow["gen_nTow_SisCone5"].Fill(n_tow_gen,pt_gen)
               hist_gentow["gen_ptTow_SisCone5"].Fill(sumpt_tow_gen,pt_gen)
         #     if n_away_gen>0:
               hist_genaway["gen_nAway_SisCone5"].Fill(n_away_gen,pt_gen)
               hist_genaway["gen_ptAway_SisCone5"].Fill(sumpt_away_gen,pt_gen)	 
   ####################Gen distributions filled Now go for reco###########################
  
   runreco = 0
   if isData == 1 and fChain.lumi >= 90 and fChain.trgZeroBias:
     runreco = 1
   elif isData == 0 and fChain.trgZeroBias:
     runreco = 1

   if runreco == 1:
	weight = 1  
        num = 0

        numgoodvtx = 0
	nu=0

        vtx_x=0
        vtx_y=0
	vtx_z=0

        trig=False 

	 
        for i in xrange(0, fChain.vtxisFake.size()):
                    
                    vtxrho = math.sqrt(fChain.vtxx.at(i)*fChain.vtxx.at(i) + fChain.vtxy.at(i)*fChain.vtxy.at(i))

		    nu=nu+1	
                    if fChain.vtxisValid.at(i)  and not fChain.vtxisFake.at(i) and math.fabs(fChain.vtxz.at(i) - fChain.vtxzBS.at(i)) <= 10 and fChain.vtxndof.at(i) > 4 and vtxrho <= 2: # count only good primary vertices
                        numgoodvtx+=1
			if numgoodvtx==1:
			 vtx_x=fChain.vtxx.at(i)
			 vtx_y=fChain.vtxy.at(i)
			 vtx_z=fChain.vtxz.at(i)
		    hist_vertex["ndfVtx"].Fill(fChain.vtxndof.at(i))	
        hist_vertex["nVtx"].Fill(numgoodvtx) 

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

	hist_vertex["nJets"].Fill(fChain.SisCone5CHp4.size())

		
	for i in xrange(0, fChain.SisCone5CHp4.size()): # SisCone5
                    trackp4 = fChain.SisCone5CHp4.at(i)
                    if trackp4.pt()>ptf:
                        ptf=trackp4.pt()
                        phif=trackp4.phi()
                        etaf=trackp4.eta()
	hist_full_jet["f_ptSisCone5"].Fill(ptf)
        hist_full_jet["f_phiSisCone5"].Fill(phif)
        hist_full_jet["f_etaSisCone5"].Fill(etaf)
        if numgoodvtx >= 1:
	    for i in xrange(0, fChain.SisCone5CHp4.size()): # SisCone5
                   trackp4 = fChain.SisCone5CHp4.at(i)	
                   #if fChain.SisCone5CHnConst.at(i)>1:
                   if trackp4.pt()>pt and not trackp4.pt() < 1 and math.fabs(trackp4.eta())<2.:
                        pt=trackp4.pt()
                        phi=trackp4.phi()
			eta=trackp4.eta()
			ntracks=fChain.SisCone5CHnConst.at(i)
			#d0
			#d0err	
            if not pt < 1 and math.fabs(eta)<2.:
                hist_jet["ptSisCone5"].Fill(pt)
		hist_jet["phiSisCone5"].Fill(phi)
		hist_jet["etaSisCone5"].Fill(eta)
		hist_jet["nTracksSisCone5"].Fill(ntracks)
	    #if True:	
	#	#print fChain.recoTracksd0Err.size()
                for i in xrange(0, fChain.recoTracksd0Err.size()):
		  track= fChain.recoTracksp4.at(i)
		  #tr_d0=fChain.recoTracksd0.at(i)
		  tr_d0Err=fChain.recoTracksd0Err.at(i)
		  tr_dzErr=fChain.recoTracksdzErr.at(i) 	
		  tr_ptErr=fChain.recoTracksptErr.at(i)	

		  tr_x=fChain.recoTracksvx.at(i)
		  tr_y=fChain.recoTracksvy.at(i)		
		  tr_z=fChain.recoTracksvz.at(i) 

		  tr_d0= (- (tr_x-vtx_x) * track.py() + (tr_y-vtx_y) * track.px() ) / track.pt() 

	          tr_dz=  (tr_z-vtx_z) - ((tr_x-vtx_x)*track.px()+(tr_y-vtx_y)*track.py())/track.pt() * (track.pz()/track.pt())		 

		  purity=0
        	  imp0= 0
        	  impz= 0
                  dpt= 0
                  kin= 0
		  dphi=track.phi()-phi
                  while dphi > math.pi:
                         dphi=dphi-2*math.pi
                  while dphi < -math.pi:
                         dphi=dphi+2*math.pi	
		  hist_pre["trackD0"].Fill(tr_d0)
		  hist_pre["trackD0Err"].Fill(tr_d0Err)
		  hist_pre["trackD0Significance"].Fill(tr_d0/tr_d0Err)	
		  hist_pre["trackDz"].Fill(tr_dz)
                  hist_pre["trackDzErr"].Fill(tr_dzErr)
                  hist_pre["trackDzSignificance"].Fill(tr_dz/tr_dzErr)	
		  hist_pre["trackPt"].Fill(track.pt())
		  hist_pre["trackPtErr"].Fill(tr_ptErr)
		  hist_pre["trackPtSigma"].Fill(tr_ptErr/track.pt())
		  hist_pre["trackEta"].Fill(track.eta())
		  hist_pre["trackPhi"].Fill(track.phi())
		  hist_pre["trackDeltaPhi"].Fill(dphi)
		  if fChain.recoTrackshighPurity.at(i):
		   #purity=1	
		   if math.fabs(tr_d0/tr_d0Err)<3:
		    # imp0=1	
		     if math.fabs(tr_dz/tr_dzErr)<3:
		     # impz=1	
		      if tr_ptErr/track.pt()<0.05:
		       #dpt=1	
		       if track.pt()>0.5 and math.fabs(track.eta())<2.:	
		  	kin=1
			if not pt < 1 and math.fabs(eta)<2.:# and ntracks > 1:	 		
			   hist_post["trackD0"+p1].Fill(tr_d0)
                 	   hist_post["trackD0Err"+p1].Fill(tr_d0Err)
                 	   hist_post["trackD0Significance"+p1].Fill(tr_d0/tr_d0Err)
                 	   hist_post["trackDz"+p1].Fill(tr_dz)
                 	   hist_post["trackDzErr"+p1].Fill(tr_dzErr)
                  	   hist_post["trackDzSignificance"+p1].Fill(tr_dz/tr_dzErr)
                  	   hist_post["trackPt"+p1].Fill(track.pt())
                  	   hist_post["trackPtErr"+p1].Fill(tr_ptErr)
                  	   hist_post["trackPtSigma"+p1].Fill(tr_ptErr/track.pt())
                  	   hist_post["trackEta"+p1].Fill(track.eta())
                  	   hist_post["trackPhi"+p1].Fill(track.phi())	
                           hist_post["trackDeltaPhi"+p1].Fill(dphi)	
			   
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

                  hist_pre["purity"].Fill(purity)
        	  hist_pre["imp0"].Fill(imp0)
        	  hist_pre["impz"].Fill(impz)
                  hist_pre["dpt"].Fill(dpt)
                  hist_pre["kin"].Fill(kin)
		if n+n_tow+n_away>0:
  	    	 hist_jet["nTot_SisCone5"].Fill(n+n_tow+n_away,pt)
                 Trans_SisCon5["nTot"].Fill(pt,n+n_tow+n_away)

                 Trans_SisCon5["ptTot"].Fill(pt,sumpt+sumpt_away+sumpt_tow)
	         #if n+n_tow+n_away>0:
                 hist_trans["nTrans_SisCone5"].Fill(n,pt)
		 Trans_SisCon5["nTransDensity"].Fill(pt,n)

                 if not n==0:
		  noScale_SisCon5["ptAveTrans"].Fill(pt,sumpt*1.0/(n*1.0)) 
		  hist_trans["ptAVETrans_SisCone5"].Fill(sumpt/n,pt)
		  	
                 if not n_tow==0:
		  hist_tow["ptAVETow_SisCone5"].Fill(sumpt_tow/n_tow,pt)
		  noScale_SisCon5["ptAveTow"].Fill(pt,sumpt_tow*1.0/(n_tow*1.0))	
 
                 if not n_away==0:
		  noScale_SisCon5["ptAveAway"].Fill(pt,sumpt_away*1.0/(n_away*1.0))
		  hist_away["ptAVEAway_SisCone5"].Fill(sumpt_away/n_away,pt)

                 if not n_away+n_tow+n==0:  
		  noScale_SisCon5["ptAveAway"].Fill(pt,(sumpt_away+sumpt_tow+sumpt)*1.0/((n_away+n_tow+n)*1.0)) 
		  hist_jet["ptAVETot_SisCone5"].Fill((sumpt_away+sumpt_tow+sumpt)*1.0/((n_away+n_tow+n)*1.0),pt)	
                 

                 Trans_SisCon5["ptTransDensity"].Fill(pt,sumpt)
                 hist_trans["ptTrans_SisCone5"].Fill(sumpt,pt)	
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

  
		 hist_trans["nTransMax_SisCone5"].Fill(n_max,pt)
                 other_SisCon5["nTransMax"].Fill(pt,n_max)
		  	
                 hist_trans["ptTransMax_SisCone5"].Fill(sumpt_max,pt)
	         other_SisCon5["ptTransMax"].Fill(pt,sumpt_max)  

                 hist_trans["nTransMin_SisCone5"].Fill(n_min,pt)
		 other_SisCon5["nTransMin"].Fill(pt,n_min)  
			
                 hist_trans["ptTransMin_SisCone5"].Fill(sumpt_min,pt)	
		 other_SisCon5["ptTransMin"].Fill(pt,sumpt_min)

		 hist_trans["nTransDiff_SisCone5"].Fill(-n_min+n_max,pt)
		 other_SisCon5["nDiff"].Fill(pt,-n_min+n_max)

                 hist_trans["ptTransDiff_SisCone5"].Fill(-sumpt_min+sumpt_max,pt)
		 other_SisCon5["ptDiff"].Fill(pt,-sumpt_min+sumpt_max)	

		 hist_tow["nTow_SisCone5"].Fill(n_tow,pt)
		 Trans_SisCon5["nTow"].Fill(pt,n_tow)
			
                 hist_tow["ptTow_SisCone5"].Fill(sumpt_tow,pt)
		 Trans_SisCon5["ptTow"].Fill(pt,sumpt_tow)	

		 hist_away["nAway_SisCone5"].Fill(n_away,pt)
		 Trans_SisCon5["nAway"].Fill(pt,n_away)

                 hist_away["ptAway_SisCone5"].Fill(sumpt_away,pt)
		 Trans_SisCon5["ptAway"].Fill(pt,sumpt_away)		

    

for h in Trans_SisCon5:
           Trans_SisCon5[h].Scale(3/(2*4*math.pi))
for h in other_SisCon5:
           other_SisCon5[h].Scale(3/(4*math.pi))

outfile.Write()
outfile.Close()      
end = time.clock()
print "%.2gs" % (end-start)
