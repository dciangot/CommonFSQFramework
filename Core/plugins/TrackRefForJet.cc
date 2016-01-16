#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/ObjectSelectorStream.h"

#include "CommonTools/UtilAlgos/interface/SingleElementCollectionSelectorPlusEvent.h"
#include "CommonFSQFramework/Core/interface/TrackRefForJet.h"

namespace reco { 
  namespace modules {

typedef ObjectSelectorStream<
  SingleElementCollectionSelectorPlusEvent<
          reco::TrackCollection,
          ::TrackRefForJet,
          reco::TrackRefVector 
          >,
  reco::TrackRefVector > TrackRefForJet;

DEFINE_FWK_MODULE(TrackRefForJet);

} }


/*
#include "FWCore/Framework/interface/MakerMacros.h"

#include "CommonTools/RecoAlgos/interface/TrackFullCloneSelectorBase.h"
#include "CommonFSQFramework/Core/interface/TrackRefForJet.h"

namespace reco { 
  namespace modules {

    typedef TrackFullCloneSelectorBase< ::TrackRefForJet > TrackRefForJet;

    DEFINE_FWK_MODULE(TrackRefForJet);

} }
*/
