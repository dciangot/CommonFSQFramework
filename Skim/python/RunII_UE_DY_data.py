anaVersion="RunIIWinter16_UE_11012016"
anaType="RunIIWinter15GS"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"

sam = {}

/DoubleMuon/Run2015D-PromptReco-v4/AOD


sam["DoubleMuon_Run2015D"]={}
sam["DoubleMuon_Run2015D"]["crabJobs"]=20
sam["DoubleMuon_Run2015D"]["GT"]='auto_run2::All'
sam["DoubleMuon_Run2015D"]["name"]='DoubleMuon_Run2015D'
sam["DoubleMuon_Run2015D"]["isData"]=False
sam["DoubleMuon_Run2015D"]["numEvents"]=1000000
sam["DoubleMuon_Run2015D"]["pathSE"]=['']
sam["DoubleMuon_Run2015D"]["pathTrees"]=''
sam["DoubleMuon_Run2015D"]["json"]=''
sam["DoubleMuon_Run2015D"]["lumiMinBias"]=2.7427317608337905e-05
sam["DoubleMuon_Run2015D"]["XS"]=36460000000.0
sam["DoubleMuon_Run2015D"]["pathPAT"]=''
sam["DoubleMuon_Run2015D"]["DS"]='/DoubleMuon/Run2015D-PromptReco-v4/AOD'


sam["DoubleMuon_Run2015C"]={}
sam["DoubleMuon_Run2015C"]["crabJobs"]=20
sam["DoubleMuon_Run2015C"]["GT"]='auto_run2::All'
sam["DoubleMuon_Run2015C"]["name"]='DoubleMuon_Run2015C'
sam["DoubleMuon_Run2015C"]["isData"]=False
sam["DoubleMuon_Run2015C"]["numEvents"]=1000000
sam["DoubleMuon_Run2015C"]["pathSE"]=['']
sam["DoubleMuon_Run2015C"]["pathTrees"]=''
sam["DoubleMuon_Run2015C"]["json"]=''
sam["DoubleMuon_Run2015C"]["lumiMinBias"]=2.7427317608337905e-05
sam["DoubleMuon_Run2015C"]["XS"]=36460000000.0
sam["DoubleMuon_Run2015C"]["pathPAT"]=''
sam["DoubleMuon_Run2015C"]["DS"]='/DoubleMuon/Run2015C-PromptReco-v4/AOD'



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
