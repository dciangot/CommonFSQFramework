anaType="RunII"

# root path needs proper XXX
# some stuff needed for crab configuration, e.g. blacklisting
preamble='''
cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"
'''

# point towards your list of samples you want
dsFile="CommonFSQFramework/Skim/python/ds_RunII_UE_DY_data.txt"

# define the util decorator. Functions marked with this wont turn into ds attribute
def util(func):
    setattr(func, "ignore", 1)
    return func
setattr(util, "ignore", 1) # for this function only


def DS(ds):
    return ds

def name(ds):
    split=ds.split("/") 
    if len(split) == 0: return None

    if isData(ds):
        ret = split[1]+split[2]
    else:
        ret = split[1]+split[2]
    return ret

def isData(ds):
    realData = False
    if "Run201" in ds: realData = True
    return realData

def json(ds):
    realData = isData(ds)
    # they are just MC GEN-SIM samples, no json needed here
    return ""

def crabJobs(ds):
    dsName = name(ds)
    # define to run 100 crab jobs
    # make something more clever, based on number of events in the dataset:
    # require around 50000 events to be processed per job
    return 100

def numEvents(ds):
    evts = -1
    
    # list all datasets in ds_RunIIWinterGS.txt file, get events from DAS
    
    return evts


def pathSE(ds):
     evts = ['']
     return evts


def pathTrees(ds):
      evts = ''
      return evts


def json(ds):
      evts = ''
      return evts

def pathPAT(ds):
      evts = ''
      return evts


def GT(ds):
    # no data, just get GT from GEN-SIM samples
    return "run2_mc::All"

def XS(ds):
    '''
    Note: all cross sections given in pb
    # http://iopscience.iop.org/0295-5075/96/2/21002
    LHCtotal= 73.5 mili b

    conversion factors cheatsheet:
    nano = 10^-6 mili
    nano = 10^-3 micro
    nano = 10^3 pico
    '''
    # if real data return nothing, not needed here but keep for other Templates


    dsName = name(ds)
    #if dsName in s:
    #    return s[dsName]
    #else:
    #    print "FIXME - XS missing for", dsName
    #    print '    s["'+dsName+'"] = '
    return -1

@util
def getLumi(ds, trg):
    '''
    all lumi values here should be given in picob
    '''
    
    # just do something very simple for now
    lumi = float(numEvents(ds)/XS(ds)) # pb, Nevents/XS
    return lumi

def lumiMinBias(ds):
    return getLumi(ds,"minbias")


# could useful in the future
@util
def onTheFlyCustomization():
    ret = ""

    return ret
#setattr(onTheFlyCustomization, "ignore", 1)


fun = {}
import copy,types
glob = copy.copy(globals())
for f in glob:
    if type(glob[f])==types.FunctionType:
        if hasattr(glob[f],"ignore"): 
            print "Skip", f
            continue
        #print f
        fun[f]=glob[f]
