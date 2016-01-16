#include "CommonFSQFramework/Core/interface/RecoTrackView.h"
#include <DataFormats/TrackReco/interface/Track.h>
#include <DataFormats/VertexReco/interface/Vertex.h>
#include "CommonFSQFramework/Core/interface/TestTrackData.h"



RecoTrackView::RecoTrackView(const edm::ParameterSet& iConfig, TTree * tree):
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

    registerVecInt(  "highPurity", tree);
    registerVecInt(  "algo", tree);
    registerVecInt(  "nValidHits", tree);
    registerVecInt(  "nLostHits", tree);
    registerVecInt(  "charge", tree);
    registerVecFloat(  "chi2n", tree);
    registerVecFloat(  "ptErr", tree);

    m_maxEta = iConfig.getParameter<double>("maxEta");
    m_minPt = iConfig.getParameter<double>("minPt");
    //m_maxDZ = iConfig.getParameter<double>("maxDZ");


    m_inputCol = iConfig.getParameter<edm::InputTag>("tracks");

    m_testTrackData[getPrefix()+"testTrkData"] = std::vector<tmf::TestTrackData>();
    tree->Branch((getPrefix()+"testTrkData").c_str(), "std::vector< tmf::TestTrackData >", &m_testTrackData[getPrefix()+"testTrkData"]);



    

}
void RecoTrackView::resetLocal(){
    std::map<std::string, std::vector<tmf::TestTrackData> >::iterator it, itE;
    it = m_testTrackData.begin();
    itE = m_testTrackData.end();
    for (; it!= itE; ++it){
        it->second.clear();
    }

}



void RecoTrackView::fillSpecific(const edm::Event& iEvent, const edm::EventSetup& iSetup){
    //resetLocal();

    edm::Handle<std::vector<reco::Track> > hIn;
    iEvent.getByLabel(m_inputCol, hIn);
    for (unsigned int i = 0; i< hIn->size();++i){

        double px = hIn->at(i).px();
        double py = hIn->at(i).py();
        double pz = hIn->at(i).pz();
        double E = px*px + py*py + pz*pz;

        // Note: all fills (below) should be done consistently after all cuts are applied
        addToP4Vec("p4", reco::Candidate::LorentzVector(px,py,pz,E));
        //addToFVec("dxy", dxy);
        //addToFVec("dz", dz);
        addToFVec("dz", hIn->at(i).dz());
        addToFVec("dzErr", hIn->at(i).dzError());
        addToFVec("d0", hIn->at(i).d0());
        addToFVec("d0Err", hIn->at(i).d0Error());

        addToFVec("vx", hIn->at(i).vx());
        addToFVec("vy", hIn->at(i).vy());
        addToFVec("vz", hIn->at(i).vz());

        int highpurity = 1;
        if (!hIn->at(i).quality(reco::TrackBase::highPurity)) highpurity = 0;
        addToIVec("highPurity", highpurity);
        addToIVec("algo", hIn->at(i).algo() );
        addToIVec("nValidHits", hIn->at(i).numberOfValidHits() );
        addToIVec("nLostHits", hIn->at(i).numberOfLostHits() );
        addToFVec("chi2n", hIn->at(i).normalizedChi2() );
        addToFVec("ptErr", hIn->at(i).ptError() );
        tmf::TestTrackData t;
        


    }

}
