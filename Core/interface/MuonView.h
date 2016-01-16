#ifndef MuonView_h
#define MuonView_h

#include "CommonFSQFramework/Core/interface/EventViewBase.h"

class MuonView: public EventViewBase{
    public:
       MuonView(const edm::ParameterSet& ps, TTree * tree);

    private:
      virtual void fillSpecific(const edm::Event&, const edm::EventSetup&);
      float m_maxEta;  
      float m_minPt;
      edm::InputTag m_inputCol;


      void resetLocal();



};
#endif
