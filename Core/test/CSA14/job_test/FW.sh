#lcg-ls srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/dciangot/MinBias_TuneCUETHS1_13TeV-herwigpp/RunIIWinter15GS_UE_08052015_MinBias_TuneCUETHS1_13TeV-herwigpp/150731_084856/0000 > list.txt

lcg-ls srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/dciangot/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS_UE_08052015_MinBias_TuneCUETP8M1_13TeV-pythia8/150731_084910/0000 > list.txt

sed -i 's/cms\///' list.txt

mkdir job_0
touch job_0/list_good.txt
cp CSA14_UEAna_comp.C job_0/CSA14_UEAna_comp.C

cd job_0

t=0
d=0

for i in `cat ../list.txt`;
do

if [ $t -lt 8 ]
  then
    echo $i >> list_good.txt
    t=$((t+1))
fi

if [ $t -eq 8 ]
  then	
   echo "cd /afs/cern.ch/user/d/dciangot/CMSSW_7_4_1_patch2/src/CommonFSQFramework/
export SCRAM_ARCH=slc6_amd64_gcc491
eval `scram runtime -sh`

cd /afs/cern.ch/user/d/dciangot/CMSSW_7_4_1_patch2/src/CommonFSQFramework/Core/test/CSA14/job_test/job_$d
eval `scram runtime -sh`
export X509_USER_PROXY=/afs/cern.ch/user/d/dciangot/proxy


root -l CSA14_UEAna_comp.C	
" > job.sh
    bsub -o /dev/null -q 8nh -J job_$d < job.sh

    d=$((d+1))	
    mkdir ../job_$d	
    cp CSA14_UEAna_comp.C ../job_$d/CSA14_UEAna_comp.C
    t=0    
    cd ../job_$d	
    touch list_good.txt	
fi


done

echo "cd /afs/cern.ch/user/d/dciangot/CMSSW_7_4_1_patch2/src/CommonFSQFramework/
export SCRAM_ARCH=slc6_amd64_gcc491
eval `scram runtime -sh`

cd /afs/cern.ch/user/d/dciangot/CMSSW_7_4_1_patch2/src/CommonFSQFramework/Core/test/CSA14/job_test/job_$d
eval `scram runtime -sh`
export X509_USER_PROXY=/afs/cern.ch/user/d/dciangot/proxy


root -l CSA14_UEAna_comp.C      
" > job.sh
    bsub -o /dev/null -q 8nh -J job_$d < job.sh


