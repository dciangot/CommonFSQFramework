#include "time.h"
#include "TBox.h"
#include "TArrow.h"
#include "TCanvas.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TTree.h"
#include "TLine.h"
#include "TMath.h"
#include "TCanvas.h"
#include "TRandom3.h"
#include "TROOT.h"
#include "TLatex.h"
#include "TFile.h"
#include "TLegend.h"
#include "TLegendEntry.h"
#include "Math/QuantFuncMathCore.h"
#include "Math/ProbFuncMathCore.h"
#include <string>
#include <vector>

#if !defined(__CINT__) && !defined(__MAKECINT__)
#include "DataFormats/FWLite/interface/Handle.h"
#include "DataFormats/FWLite/interface/Event.h"
#endif

void CSA14_UEAna_test(){

gROOT->Reset();

using namespace std;
using namespace edm;

//char *file_MC= (char*)"../../../Skim/config/UE/trees.root"; // output file with all MC varaibles

//char *file_MC= (char*)"root://xrootd.ba.infn.it//store/user/dciangot/HINCaloJetsOther/RunIIWinter15GS_UE_08052015_Run2015B_HINCalo/150731_085034/0000/trees_2.root";

//TFile *MC  =TFile::Open(file_MC);

TChain a_MC("UETree/data");

a_MC.Add("/scratch/osg/rankdw/Run2015B_2/0/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/0/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/0/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/1/trees_9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/2/trees_9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/3/trees_9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/4/trees_9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/5/trees_9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/6/trees_9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/7/trees_9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/8/trees_9.root");
/*
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/FullTrack/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/FullTrack/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/HINCalo/trees_1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/HINCalo/trees_2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/HINCalo/trees_3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/HINCalo/trees_4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2/HINCalo/trees_5.root");
*/
/*
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_10_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_10_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_10_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_10_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_10_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_10_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_10_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_10_sam9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam11.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_1_sam9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam11.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_2_sam9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam3.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_3_sam9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_4_sam1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_4_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_4_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_4_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_4_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_4_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_4_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_4_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_4_sam9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_5_sam1.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_5_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_5_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_5_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_5_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_5_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_5_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_5_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_5_sam9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_6_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_6_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_6_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_6_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_6_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_6_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_6_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_6_sam9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_7_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_7_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_7_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_7_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_7_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_7_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_7_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_7_sam9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_8_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_8_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_8_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_8_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_8_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_8_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_8_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_8_sam9.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_9_sam10.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_9_sam2.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_9_sam4.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_9_sam5.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_9_sam6.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_9_sam7.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_9_sam8.root");
a_MC.Add("/scratch/osg/rankdw/Run2015B_2Merged/trees_9_sam9.root");
*/


time_t timer1;
time_t timer2;

time_t timer_start;
time_t timer_end;

time(&timer1);
time(&timer_start);
//TTree *a_MC = (TTree*)MC->Get("UETree/data");

cout << "Entries: "<<a_MC.GetEntries() << std::endl;

TBranch *tracks_ = a_MC.GetBranch("recoTracksp4");
std::vector<reco::Candidate::LorentzVector>* test;

std::vector<reco::Candidate::LorentzVector>* tracks= new std::vector<reco::Candidate::LorentzVector>();
a_MC.SetBranchAddress("recoTracksp4",&tracks);

std::vector<float>* tracksd0= new std::vector<float>();
a_MC.SetBranchAddress("recoTracksd0",&tracksd0);

std::vector<float>* tracksd0Err= new std::vector<float>();
a_MC.SetBranchAddress("recoTracksd0Err",&tracksd0Err);

std::vector<float>* tracksdz= new std::vector<float>();
a_MC.SetBranchAddress("recoTracksdz",&tracksdz);

std::vector<float>* tracksdzErr= new std::vector<float>();
a_MC.SetBranchAddress("recoTracksdzErr",&tracksdzErr);

std::vector<float>* tracksptErr= new std::vector<float>();
a_MC.SetBranchAddress("recoTracksptErr",&tracksptErr);

std::vector<float>* tracksvz= new std::vector<float>();
a_MC.SetBranchAddress("recoTracksvz",&tracksvz);

std::vector<float>* tracksvx= new std::vector<float>();
a_MC.SetBranchAddress("recoTracksvx",&tracksvx);

std::vector<float>* tracksvy= new std::vector<float>();
a_MC.SetBranchAddress("recoTracksvy",&tracksvy);

std::vector<int>* tracksisValid=new std::vector<int>();
a_MC.SetBranchAddress("recoTrackshighPurity",&tracksisValid);


int lumi;
a_MC.SetBranchAddress("lumi",&lumi);


std::vector<float>* vtxz= new std::vector<float>();
a_MC.SetBranchAddress("vtxz",&vtxz);

std::vector<float>* vtxx= new std::vector<float>();
a_MC.SetBranchAddress("vtxx",&vtxx);

std::vector<float>* vtxy= new std::vector<float>();
a_MC.SetBranchAddress("vtxy",&vtxy);

std::vector<float>* vtxzBS=new std::vector<float>();
a_MC.SetBranchAddress("vtxzBS",&vtxzBS);

std::vector<float>* vtxxBS=new std::vector<float>();
a_MC.SetBranchAddress("vtxxBS",&vtxxBS);

std::vector<float>* vtxyBS=new std::vector<float>();
a_MC.SetBranchAddress("vtxyBS",&vtxyBS);

std::vector<int>* vtxisValid=new std::vector<int>();
a_MC.SetBranchAddress("vtxisValid",&vtxisValid);

std::vector<int>* vtxisFake=new std::vector<int>();
a_MC.SetBranchAddress("vtxisFake",&vtxisFake);

std::vector<int>* vtxndf=new std::vector<int>();
a_MC.SetBranchAddress("vtxndof",&vtxndf);

int trgZeroBias;
a_MC.SetBranchAddress("trgZeroBias",&trgZeroBias);

std::vector<reco::Candidate::LorentzVector>* jets= new std::vector<reco::Candidate::LorentzVector>();
a_MC.SetBranchAddress("SisCone5CHp4",&jets);

std::vector<float>* jetsConst= new std::vector<float>();
a_MC.SetBranchAddress("SisCone5CHnConst",&jetsConst);

//	trgZeroBias


TH1I* h_vtxndf = new TH1I("h_vtxndf","h_vtxndf", 200, 0, 200);
TH1I* h_nvtx = new TH1I("h_nvtx","h_nvtx", 200, 0, 200);


TH1F* h_vtxdz = new TH1F("h_vtxdz","h_vtxdz", 2000,-20, 20);
TH1F* h_vtxrho = new TH1F("h_vtxrho","h_vtxrho", 400, 0, 4);

TH1F* h_pt_jet = new TH1F("h_pt_jet","h_pt_jet", 400, 0, 200);

TH1F* h_pt_t = new TH1F("h_pt_t","h_pt_t", 400, 0, 200);




Int_t nevent = a_MC.GetEntries();
Int_t k=0;

for(Int_t i = 0; i< nevent; i++){
	k++;
	Int_t nvtx=0;

	a_MC.GetEvent(i);

	//cout << i << endl;
	if(lumi>=90 && trgZeroBias){
		double vtxxx,vtxxy,vtxxz;	
		for(int j=0;j<vtxz->size(); j++ ){
			double vx= vtxx->at(j)-vtxxBS->at(j);
			double vy= vtxy->at(j)-vtxyBS->at(j);
			double vtxrho = sqrt(vx*vx + vy*vy);

			h_vtxndf->Fill(vtxndf->at(j));
			h_vtxdz->Fill(vtxz->at(j)-vtxzBS->at(j));
			h_vtxrho->Fill(vtxrho);

			if(vtxisValid->at(j) && !vtxisFake->at(j) && fabs(vtxz->at(j)-vtxzBS->at(j))<10 && vtxndf->at(j)>4 && vtxrho<2 ){ 
				nvtx++;
				vtxxx=vtxx->at(j);
				vtxxy=vtxy->at(j);
				vtxxz=vtxz->at(j);	
			}
		}


		h_nvtx->Fill(nvtx);
		if(nvtx>0){
			//
			double ptf=0;
			double phif=0;
			double etaf=0;
			for(Int_t t=0; t<jets->size(); t++){ // SisCone5
			    //if (jetsConst->at(t)==1) h_pt_jet->Fill(jets->at(t).pt());	
        	            if (jets->at(t).pt()>ptf && jets->at(t).pt()>=1 && fabs(jets->at(t).eta())<=2){
                	        ptf=jets->at(t).pt();
                        	phif=jets->at(t).phi();
                        	etaf=jets->at(t).eta();
			    }	
			}
			
			if(ptf>0) {
				h_pt_jet->Fill(ptf);
			}
			double te=0;
			for(Int_t t=0; t<tracks->size(); t++){			
				
				double ptt=tracks->at(t).pt();
				double pxt=tracks->at(t).px();
				double pyt=tracks->at(t).py();
				double pzt=tracks->at(t).pz();
				double tr_d0=tracksd0->at(t);
	                	double tr_d0Err=tracksd0Err->at(t);
        	          	double tr_dzErr=tracksdzErr->at(t);
               		   	double tr_ptErr=tracksptErr->at(t);

                  		double tr_x=tracksvx->at(t);
                  		double tr_y=tracksvy->at(t);
                  		double tr_z=tracksvz->at(t);

				tr_d0= (- (tr_x-vtxxx) * pyt + (tr_y-vtxxy) * pxt ) / ptt;

                  		double tr_dz=  (tr_z-vtxxz) - ((tr_x-vtxxx)*pxt+(tr_y-vtxxy)*pyt)/ptt * (pzt/ptt);
				if ( tracksisValid->at(t) && tr_d0/tr_d0Err<3 && tr_dz/tr_dzErr<3 && tr_ptErr/ptt <0.05 && ptt>0.5 && fabs(tracks->at(t).eta())<2 ){
					if(te<ptt) te=ptt; 
				}
	
			}			
			if(te>0){ h_pt_t->Fill(te);}
		} 


	}

	if(k/100000==1){
		k=0;

		time(&timer2);
		double seconds = difftime(timer1,timer2);
		cout<< "Event: " << i+1 << " speed: " << 100000*(-1.0)/seconds << "evt/s" << endl;
		timer1=timer2;
	}

}


time(&timer_end);
cout << "Entries: "<<a_MC.GetEntries() << std::endl;

cout << "Total time: " << difftime(timer_end,timer_start) << " s" << endl;

//TFile* file_out;

//file_out->Open("test2.root", "RECREATE"); 

TFile *file_out = new TFile("test3.root", "RECREATE"); //DR

h_vtxndf->Write();
h_vtxdz->Write();
h_vtxrho->Write();
h_nvtx->Write();
h_pt_t->Write();
h_pt_jet->Write();
}

