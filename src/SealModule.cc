#include "PluginManager/ModuleDef.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "Validation/RecoEgamma/interface/EgammaObjects.h"
#include "Validation/RecoEgamma/interface/EgammaObjectsDQMLoader.h"


DEFINE_SEAL_MODULE();

DEFINE_ANOTHER_FWK_MODULE(EgammaObjects);
DEFINE_ANOTHER_FWK_MODULE(DQMReadFileExample);
