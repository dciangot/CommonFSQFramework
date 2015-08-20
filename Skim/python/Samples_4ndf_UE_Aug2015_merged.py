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
sam["Run2015B"]["numEvents"]=11000000
sam["Run2015B"]["pathSE"]='srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/dciangot/ZeroBias/RunIIWinter15GS_UE_08052015_Run2015B/150729_094437/0000/'
sam["Run2015B"]["pathTrees"]='/scratch/osg/rankdw/Run2015B_2Merged/'
sam["Run2015B"]["json"]=''
sam["Run2015B"]["lumiMinBias"]=0.000301700493692
sam["Run2015B"]["XS"]=36460000000.0
sam["Run2015B"]["pathPAT"]='asd'
sam["Run2015B"]["DS"]='/ZeroBias/Run2015B-PromptReco-v1/RECO'


















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

        for s in sam:
            if "pathPAT" in sam[s]:
                sam[s]["pathPAT"] = sam[s]["pathPAT"].replace("XXXTMFPAT", localBasePathPAT)
            if "pathTrees" in sam[s]:
                sam[s]["pathTrees"] = sam[s]["pathTrees"].replace("XXXTMFTTree", localBasePathTrees)
            #print sam[s]["pathPAT"]
            #print sam[s]["pathTrees"]
        return sam
sam = fixLocalPaths(sam)
