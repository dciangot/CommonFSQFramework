#ifndef CommonFSQFramework_Core_TrackRefForJet_H
#define CommonFSQFramework_Core_TrackRefForJet_H

// Original Author:  Giovanni Petrucciani
//         Created:  Fri May 25 10:06:02 CEST 2007
// $Id: TrackRefForJet.h,v 1.4 2010/04/07 08:56:18 gpetrucc Exp $


#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

class TrackRefForJet {
   public:
      explicit TrackRefForJet(const edm::ParameterSet& iConfig, edm::ConsumesCollector && iC) :
        TrackRefForJet(iConfig, iC) {}
      explicit TrackRefForJet(const edm::ParameterSet& iConfig, edm::ConsumesCollector & iC);
      ~TrackRefForJet();
      bool operator()(const reco::Track &t, const edm::Event &iEvent) const ;
      bool operator()(const reco::Track &t, const reco::VertexCollection &vtxs) const;
      bool testTrack(const reco::Track &t) const ;
      bool testVertices(const reco::Track &t, const reco::VertexCollection &vtxs, const reco::BeamSpot &hBs) const ;
   private:
      uint32_t numberOfValidHits_;
      uint32_t numberOfValidPixelHits_;
      uint32_t numberOfLostHits_;
      double   normalizedChi2_;
      double   ptMin_, ptMax_, etaMin_, etaMax_;
      double   dzMax_,   d0Max_;
      double   ptErrorCut_;
      std::string quality_;

      uint32_t      nVertices_;
      edm::EDGetTokenT<reco::VertexCollection> vertexToken_;
      edm::EDGetTokenT<reco::BeamSpot> bsToken_;
      bool          vtxFallback_;
      double        zetaVtx_, rhoVtx_;

      typedef math::XYZPoint Point;
};

#endif
