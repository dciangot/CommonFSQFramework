anaVersion="RunIIWinter15GS_UE_08052015"
anaType="RunIIWinter15GS"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"

sam = {}

sam["Run2015B"]={}
sam["Run2015B"]["crabJobs"]=20
sam["Run2015B"]["GT"]='MCRUN2_71_V0::All'
sam["Run2015B"]["name"]='ZeroBias'
sam["Run2015B"]["isData"]=False
sam["Run2015B"]["numEvents"]=1000000
sam["Run2015B"]["pathSE"]=['srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/dciangot/ZeroBias/RunIIWinter15GS_UE_08052015_Run2015B/150729_094437/0000/']

sam["Run2015B"]["pathTrees"]=['/scratch/osg/rankdw/Run2015B_2/0/',
'/scratch/osg/rankdw/Run2015B_2/1/',
'/scratch/osg/rankdw/Run2015B_2/2/',
'/scratch/osg/rankdw/Run2015B_2/3/',
'/scratch/osg/rankdw/Run2015B_2/4/',
'/scratch/osg/rankdw/Run2015B_2/5/',
'/scratch/osg/rankdw/Run2015B_2/6/',
'/scratch/osg/rankdw/Run2015B_2/7/',
'/scratch/osg/rankdw/Run2015B_2/8/']

sam["Run2015B"]["json"]=''
sam["Run2015B"]["lumiMinBias"]=2.7427317608337905e-05
sam["Run2015B"]["XS"]=36460000000.0
sam["Run2015B"]["pathPAT"]='asd'
sam["Run2015B"]["DS"]='/ZeroBias/Run2015B-PromptReco-v1/RECO'





"""
sam["Run2015B_FullTrack"]={}
sam["Run2015B_FullTrack"]["crabJobs"]=20
sam["Run2015B_FullTrack"]["GT"]='MCRUN2_71_V0::All'
sam["Run2015B_FullTrack"]["name"]='ZeroBias8'
sam["Run2015B_FullTrack"]["isData"]=False
sam["Run2015B_FullTrack"]["numEvents"]=1000000
sam["Run2015B_FullTrack"]["pathSE"]='srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/dciangot/FullTrack/RunIIWinter15GS_UE_08052015_Run2015B_FullTrack/150731_085247/0000/'

sam["Run2015B_FullTrack"]["pathTrees"]='/scratch/osg/rankdw/Run2015B_2/FullTrack/'

sam["Run2015B_FullTrack"]["json"]=''
sam["Run2015B_FullTrack"]["lumiMinBias"]=2.7427317608337905e-05
sam["Run2015B_FullTrack"]["XS"]=36460000000.0
sam["Run2015B_FullTrack"]["pathPAT"]='asd'
sam["Run2015B_FullTrack"]["DS"]='/FullTrack/Run2015B-PromptReco-v1/RECO'


sam["Run2015B_HINCalo"]={}
sam["Run2015B_HINCalo"]["crabJobs"]=20
sam["Run2015B_HINCalo"]["GT"]='MCRUN2_71_V0::All'
sam["Run2015B_HINCalo"]["name"]='ZeroBias8'
sam["Run2015B_HINCalo"]["isData"]=False
sam["Run2015B_HINCalo"]["numEvents"]=1000000
sam["Run2015B_HINCalo"]["pathSE"]='srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/dciangot/HINCaloJetsOther/RunIIWinter15GS_UE_08052015_Run2015B_HINCalo/150731_085034/0000/'

sam["Run2015B_HINCalo"]["pathTrees"]='/scratch/osg/rankdw/Run2015B_2/HINCalo/'

sam["Run2015B_HINCalo"]["json"]=''
sam["Run2015B_HINCalo"]["lumiMinBias"]=2.7427317608337905e-05
sam["Run2015B_HINCalo"]["XS"]=36460000000.0
sam["Run2015B_HINCalo"]["pathPAT"]='asd'
sam["Run2015B_HINCalo"]["DS"]='/HINCaloJetsOther/Run2015B-PromptReco-v1/RECO'
"""


def fixLocalPaths(sam):
        import os,imp
        if "SmallXAnaDefFile" not in os.environ:
            print "Please set SmallXAnaDefFile environment variable:"
            print "export SmallXAnaDefFile=FullPathToFile"
            raise Exception("Whooops! SmallXAnaDefFile env var not defined")

        anaDefFile = os.environ["SmallXAnaDefFile"]
        mod_dir, filename = os.path.split(anaDefFile)
        mod, ext = os.path.splitext(filename)
        f, filename, desc = imp.find_module(mod, [mod_dir])
        mod = imp.load_module(mod, f, filename, desc)

        localBasePathPAT = mod.PATbasePATH
        localBasePathTrees = mod.TTreeBasePATH

        #for s in sam:
            #if "pathPAT" in sam[s]:
                #sam[s]["pathPAT"] = sam[s]["pathPAT"].replace("XXXTMFPAT", localBasePathPAT)
            #if "pathTrees" in sam[s]:
                #sam[s]["pathTrees"] = sam[s]["pathTrees"].replace("XXXTMFTTree", localBasePathTrees)
            #print sam[s]["pathPAT"]
            #print sam[s]["pathTrees"]
        return sam
sam = fixLocalPaths(sam)
