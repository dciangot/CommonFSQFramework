#include "CommonFSQFramework/Core/interface/MuonView.h"
#include <DataFormats/MuonReco/interface/Muon.h>
#include "DataFormats/PatCandidates/interface/PATObject.h"
#include "DataFormats/PatCandidates/interface/Muon.h"


MuonView::MuonView(const edm::ParameterSet& iConfig, TTree * tree):
EventViewBase(iConfig,  tree)
{
    registerVecP4("p4", tree);
    registerVecFloat("dz", tree);
    registerVecFloat("d0", tree);
    registerVecFloat("dzErr", tree);
    registerVecFloat("d0Err", tree);
    registerVecFloat("vx", tree);
    registerVecFloat("vy", tree);
    registerVecFloat("vz", tree);	

    registerVecInt(  "nTrackerHits", tree);
    registerVecInt(  "nPixelHits", tree);
    registerVecInt(  "nMuonHits", tree);
    registerVecInt(  "nMatches", tree);
    registerVecFloat(  "chi2n", tree);
    
    registerVecFloat(  "Iso_beta", tree);

    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");

    m_inputCol = iConfig.getParameter<edm::InputTag>("muons");

}

void MuonView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){
    //resetLocal();


    edm::Handle<edm::View<pat::Muon> >  hIn;
    iEvent.getByLabel(m_inputCol, hIn);
    for (unsigned int i = 0; i< hIn->size();++i){

     double px = hIn->at(i).px();
     double py = hIn->at(i).py();
     double pz = hIn->at(i).pz();
     double E = px*px + py*py + pz*pz;

     if (hIn->at(i).combinedMuon().isNonnull() && hIn->at(i).pt() > m_minPt && fabs(hIn->at(i).eta()) < m_maxEta){

      if(hIn->at(i).isGlobalMuon()){
        reco::TrackRef  glbmuon = hIn->at(i).combinedMuon();
	const reco::HitPattern & glbhit = glbmuon->hitPattern();

        // Note: all fills (below) should be done consistently after all cuts are applied
        addToP4Vec("p4", reco::Candidate::LorentzVector(px,py,pz,E));
        //addToFVec("dxy", dxy);
        //addToFVec("dz", dz);
        addToFVec("dz", glbmuon->dz());
        addToFVec("dzErr", glbmuon->dzError());
        addToFVec("d0", glbmuon->d0());
        addToFVec("d0Err", glbmuon->d0Error());

        addToFVec("vx", glbmuon->vx());
        addToFVec("vy", glbmuon->vy());
        addToFVec("vz", glbmuon->vz());


        addToIVec("nTrackerHits", glbmuon->hitPattern().trackerLayersWithMeasurement());
        addToIVec("nPixelHits", glbhit.numberOfValidPixelHits());
        addToIVec("nMatches", hIn->at(i).numberOfMatches());
        addToIVec("nMuonHits", glbhit.numberOfValidMuonHits());
        addToFVec("chi2n", glbmuon->normalizedChi2());

	double Iso=(hIn->at(i).pfIsolationR04().sumChargedHadronPt+std::max(0.,hIn->at(i).pfIsolationR04().sumNeutralHadronEt+hIn->at(i).pfIsolationR04().sumPhotonEt-0.5*hIn->at(i).pfIsolationR04().sumPUPt))/hIn->at(i).pt();

        addToFVec("Iso_beta", Iso);



    }

  }  

 }

}
