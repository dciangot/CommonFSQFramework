#!/usr/bin/python
import os,sys,stat
import shutil
import re
from subprocess import call

readFiles=open('data_');
outputFile="data";
cfgFile="data";
bsubFile="data";
dirCfgFile="cfgFiles/";
dirBsubFile="bsubFiles/";
dirRootFile="rootFiles/";
type = "FALSE"# 0 for MC, 1 for data
homeDir="/afs/cern.ch/user/d/dciangot/CMSSW_7_4_1_patch2/src/CommonFSQFramework/Core/test/CSA14/Analyzer_Sunil_MC/";
nf=0;
for line in readFiles:   #Loop over LHE files
  line=line[:-1]
  nf=nf+1;
  outputFile_i=outputFile+str(nf)+".root";
  cfgFile_i=cfgFile+str(nf)+".py"
  bsubFile_i=bsubFile+str(nf)+".sh"

  namefile=dirCfgFile+cfgFile_i;
  shutil.copyfile("tmp_Analyzer.py", namefile);
  with open(namefile) as f:   # To make changes in config file
   data=f.read();
  with open(namefile, "w") as f:
   data=re.sub("inputFile", line, data);
   data=re.sub("outputFile", outputFile_i, data);
   data = re.sub("runtype", type, data);
   f.write(data);
  f.close();

  shfile=dirBsubFile+bsubFile_i;
  outfile=open(shfile, "w"); # To make a bsub script

  outfile.write("#!/bin/sh \n");
  namefile="cd "+str(homeDir)+str("\n");
  outfile.write(namefile);
  outfile.write("eval `scramv1 runtime -sh`\n");
  outfile.write("export X509_USER_PROXY=/afs/cern.ch/user/d/dciangot/proxy\n"); 
# outfile.write("export SmallXAnaDefFile=/afs/cern.ch/work/s/subansal/CMS/CMSSW_7_4_3/src/setup/MyAnalysis.py\n");
#  outfile.write("export SmallXAnaVersion=CommonFSQFramework.Skim.Samples_CSA14_Tracks_20140904_new\n");
#  outfile.write("eval `scramv1 runtime -sh`\n");
  #outfile.write("cd -\n");   
  namefile="python "+homeDir+dirCfgFile+cfgFile_i+str("\n");
  outfile.write(namefile);
  namefile="mv "+ outputFile_i+" "+homeDir+str(dirRootFile)+str("\n");#str("/afs/cern.ch/work/d/dciangot/MC_rootFiles_PU/")+str("\n"); #+homeDir+str(dirRootFile)+str("\n");
  outfile.write(namefile);
  outfile.close();


  st = os.stat(shfile);
  os.chmod(shfile,st.st_mode |stat.S_IRWXU|stat.S_IRWXO|stat.S_IRWXG);

  cfgfile=dirCfgFile+cfgFile_i;
  st = os.stat(cfgfile);
  os.chmod(cfgfile,st.st_mode |stat.S_IRWXU|stat.S_IRWXO|stat.S_IRWXG);
  namefile=homeDir+shfile;
  bsubcommand="bsub -q 1nh -u /dev/null  -o /dev/null " + namefile;
  child   = os.system(bsubcommand);
  print "submitted batch job on file %%", line;

print "job submission finished";
print "Cfg location = ", homeDir+dirCfgFile;
print "script location = ", homeDir+dirRootFile;
print "root file location = ",homeDir+dirRootFile;
 
