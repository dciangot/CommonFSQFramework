#ifndef MuonView_h
#define MuonView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"
#include "CommonFSQFramework/Core/interface/TestTrackData.h"

class MuonView: public EventViewBase{
    public:
       MuonView(const edm::ParameterSet& ps, TTree * tree, edm::ConsumesCollector && iC);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float m_maxEta; // 
      float m_maxDZ; // 
      float m_minPt;
      int   m_charge; // -1 - take all, 0 - neutral, +1 - charged  
      edm::InputTag m_inputCol;


      std::map<std::string, std::vector<tmf::TestTrackData> > m_testTrackData;
      void resetLocal();



};
#endif
