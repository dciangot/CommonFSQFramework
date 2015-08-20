#if !defined(__CINT__) && !defined(__MAKECINT__)
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
#include "TChain.h"
#include "TRandom3.h"
#include "TROOT.h"
#include "TLatex.h"
#include "TFile.h"
#include "TLegend.h"
#include "TLegendEntry.h"
#include "Math/QuantFuncMathCore.h"
#include "Math/ProbFuncMathCore.h"
#include <string>
#include <iostream>
#include <cmath>
#include "DataFormats/FWLite/interface/Handle.h"
#include "DataFormats/FWLite/interface/Event.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#endif


void CSA14_UEAna_comp(){

//gROOT->Reset();



using namespace std;
using namespace edm;

//char *file_MC= (char*)"../../../Skim/config/UE/trees.root"; // output file with all MC varaibles

//char *file_MC= (char*)"root://xrootd.ba.infn.it//store/user/dciangot/HINCaloJetsOther/RunIIWinter15GS_UE_08052015_Run2015B_HINCalo/150731_085034/0000/trees_2.root";

//TFile *MC  =TFile::Open(file_MC);

TChain a_MC("UETree/data");


string z;
 ifstream aprifile;
aprifile.open("list_good.txt");

int line= count(std::istreambuf_iterator<char>(aprifile), 
             std::istreambuf_iterator<char>(), '\n');


ifstream file;
file.open("list_good.txt");

for(int i=0; i<line; i++){//DY50
                getline(file,z);
                z="root://xrootd.ba.infn.it/"+z;
		cout << z << endl;
		const char* files= z.c_str();
		a_MC.Add(files);
}



time_t timer1;
time_t timer2;

time_t timer_start;
time_t timer_end;

time(&timer1);
time(&timer_start);


struct tm * timeinfo;

timeinfo = localtime ( &timer_start);

cout << endl << "Started at:  " << asctime(timeinfo) << endl;

cout << "Entries: "<<a_MC.GetEntries() << std::endl;

std::vector<reco::Candidate::LorentzVector>* particles= new std::vector<reco::Candidate::LorentzVector>();
a_MC.SetBranchAddress("genParticlesp4",&particles);

std::vector<int>* part_charge = new std::vector<int>();
a_MC.SetBranchAddress("genParticlescharge",&part_charge);

std::vector<int>* part_status = new std::vector<int>();
a_MC.SetBranchAddress("genParticlesstatus",&part_status);

std::vector<reco::Candidate::LorentzVector>* genJets= new std::vector<reco::Candidate::LorentzVector>();
a_MC.SetBranchAddress("sisCone5ChgGenJetsp4",&genJets);

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

std::vector<float>* vtxzErr= new std::vector<float>();
a_MC.SetBranchAddress("vtxzErr",&vtxzErr);

std::vector<float>* vtxx= new std::vector<float>();
a_MC.SetBranchAddress("vtxx",&vtxx);

std::vector<float>* vtxxErr= new std::vector<float>();
a_MC.SetBranchAddress("vtxxErr",&vtxxErr);

std::vector<float>* vtxy= new std::vector<float>();
a_MC.SetBranchAddress("vtxy",&vtxy);

std::vector<float>* vtxyErr= new std::vector<float>();
a_MC.SetBranchAddress("vtxyErr",&vtxyErr);

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

std::vector<int>* jetsConst= new std::vector<int>();
a_MC.SetBranchAddress("SisCone5CHnConst",&jetsConst);

//	trgZeroBias


TH1I* h_vtxndf = new TH1I("h_vtxndf","h_vtxndf", 200, 0, 200);
TH1I* h_nvtx = new TH1I("h_nvtx","h_nvtx", 200, 0, 200);
TH1F* h_vtxdz = new TH1F("h_vtxdz","h_vtxdz", 2000,-20, 20);
TH1F* h_vtxrho = new TH1F("h_vtxrho","h_vtxrho", 400, 0, 4);

TH1F* h_pt_jet = new TH1F("h_pt_jet","h_pt_jet", 400, 0, 200);
TH1F* h_pt_jet_gen = new TH1F("h_pt_jet_gen","h_pt_jet", 400, 0, 200);

TH1F* h_eta_jet = new TH1F("h_eta_jet","h_eta_jet", 400, -2, 2);
TH1F* h_eta_jet_gen = new TH1F("h_eta_jet_gen","h_eta_jet", 400, -2, 2);

TH1F* h_phi_jet = new TH1F("h_phi_jet","h_deltaphi", 62800, -3.14, 3.14);
TH1F* h_phi_jet_gen = new TH1F("h_phi_jet_gen","h_deltaphi", 62800, -3.14, 3.14);

TH1F* h_pt_t = new TH1F("h_pt_t","h_pt_t", 400, 0, 200);
TH1F* h_pt_t_gen = new TH1F("h_pt_t_gen","h_pt_t", 400, 0, 200);

TH1F* h_eta_t = new TH1F("h_eta_t","h_eta_jet", 400, -2, 2);
TH1F* h_eta_t_gen = new TH1F("h_eta_t_gen","h_eta_jet", 400, -2, 2);

TH1F* h_phi_t = new TH1F("h_phi_t","h_deltaphi", 62800, -3.14, 3.14);
TH1F* h_phi_t_gen = new TH1F("h_phi_t_gen","h_deltaphi", 62800, -3.14, 3.14);

TH1F* h_deltaphi = new TH1F("h_deltaphi","h_deltaphi", 62800, -3.14, 3.14);
TH1F* h_deltaphi_gen = new TH1F("h_deltaphi_gen","h_deltaphi", 62800, -3.14, 3.14);

TH2F* h_nTrans_SisCone5 = new TH2F("nTrans_SisCone5",   "n_trans",  80, -0.5,79.5,400, 0, 200);
TH2F* h_ptTrans_SisCone5 = new TH2F("ptTrans_SisCone5",   "pt_trans",  400, 0.,40.,200, 0, 100);

TH2F* h_nTrans_SisCone5_gen = new TH2F("nTrans_SisCone5_gen",   "n_trans",  80, -0.5,79.5,400, 0, 200);
TH2F* h_ptTrans_SisCone5_gen = new TH2F("ptTrans_SisCone5_gen",   "pt_trans",  400, 0.,40.,200, 0, 100);

Int_t nevent = a_MC.GetEntries();
Int_t k=0;

for(Int_t i = 0; i< nevent; i++){
	k++;
	Int_t nvtx=0;

	a_MC.GetEvent(i);
	//cout << i << endl;
	
	//if(lumi>=90 && trgZeroBias){
	if(trgZeroBias){
		double pt_max=0;
		double eta_max=1000;
		double phi_max=1000;

		for(unsigned int j=0;j<genJets->size(); j++ ){
			double pt = genJets->at(j).pt();
			double eta = genJets->at(j).eta();
			double phi = genJets->at(j).phi();
			if(fabs(eta)<2. && pt>1 && pt>pt_max){
				pt_max=pt;
				eta_max=eta;
				phi_max=phi;
			}
		}

		if(pt_max>0) h_pt_jet_gen->Fill(pt_max);

                double pt_t_max=0;

		for(unsigned int j=0;j<particles->size(); j++ ){
			int charge = part_charge->at(j);
			int status = part_status->at(j);
			double pt_t=particles->at(j).pt();
			double phi_t=particles->at(j).phi();
			double eta_t=particles->at(j).eta();	
			if(status==1 && charge!=0 && particles->at(j).pt()>0.5 and fabs(particles->at(j).eta())<2.){

				if(pt_t>pt_t_max) pt_t_max=pt_t; 
			
				if(pt_max>0){
					
					double delta_phi=phi_t-phi_max;
                                        while (delta_phi > M_PI){
                                                delta_phi=delta_phi-2*M_PI;
                                        }
                                        while (delta_phi < -M_PI){
                                                delta_phi=delta_phi+2*M_PI;
                                        }
					h_deltaphi_gen->Fill(delta_phi);	
				

				}
			}

		}

		if(pt_t_max) h_pt_t_gen->Fill(pt_t_max);
		
///// END MC
		double vtxxxErr=0, vtxxyErr=0, vtxxzErr=0;
		double vtxxx=0,vtxxy=0,vtxxz=0;	
		double sumpt=0, sumpt1=0, sumpt2=0;
		double n=0, n1=0, n2=0;

		for(unsigned int j=0;j<vtxz->size(); j++ ){
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
				vtxxxErr=vtxxErr->at(j);
                                vtxxyErr=vtxyErr->at(j);
                                vtxxzErr=vtxzErr->at(j);

			}
		}


		h_nvtx->Fill(nvtx);
		if(nvtx>=1){
			//
			double ptf=0;
			double phif=0;
			double etaf=0;
			for(unsigned int t=0; t<jets->size(); t++){ // SisCone5
			    //if (jetsConst->at(t)==1) h_pt_jet->Fill(jets->at(t).pt());	
        	            if (jetsConst->at(t)>=1 && jets->at(t).pt()>ptf && jets->at(t).pt()>=1 && fabs(jets->at(t).eta())<=2){
                	        ptf=jets->at(t).pt();
                        	phif=jets->at(t).phi();
                        	etaf=jets->at(t).eta();
			    }	
			}
			
			if(ptf>0) {
				h_pt_jet->Fill(ptf);
			}
			double te=0;
			for(unsigned int t=0; t<tracks->size(); t++){			
				
				double ptt=tracks->at(t).pt();
				double pxt=tracks->at(t).px();
				double pyt=tracks->at(t).py();
				double pzt=tracks->at(t).pz();
				double phit=tracks->at(t).phi();
				double etat=tracks->at(t).eta();

				double tr_d0=tracksd0->at(t);
	                	double tr_d0Err=tracksd0Err->at(t);
        	          	double tr_dzErr=tracksdzErr->at(t);
               		   	double tr_ptErr=tracksptErr->at(t);

                  		double tr_x=tracksvx->at(t);
                  		double tr_y=tracksvy->at(t);
                  		double tr_z=tracksvz->at(t);


				tr_d0= (- (tr_x-vtxxx) * pyt + (tr_y-vtxxy) * pxt ) / ptt;

				double sigma_d0_v_2= (pyt*pyt*vtxxxErr*vtxxxErr+pxt*pxt*vtxxyErr*vtxxyErr)/(ptt*ptt);

				double sigma_d0_t=sqrt(sigma_d0_v_2+tr_d0Err*tr_d0Err);

                  		double tr_dz=  (tr_z-vtxxz) - ((tr_x-vtxxx)*pxt+(tr_y-vtxxy)*pyt)/ptt * (pzt/ptt);

				double sigma_dz_t= sqrt(tr_dzErr*tr_dzErr+vtxxzErr*vtxxzErr);

				if ( tracksisValid->at(t) && tr_d0/sigma_d0_t<3 && tr_dz/sigma_dz_t<3 && tr_ptErr/ptt <0.05 && ptt>0.5 && fabs(tracks->at(t).eta())<2 ){
					if(te<ptt) te=ptt; 
					if(ptf>0){
						double delta_phi=phit-phif;	
						while (delta_phi > M_PI){
                         				delta_phi=delta_phi-2*M_PI;
						}
                  				while (delta_phi < -M_PI){
                         				delta_phi=delta_phi+2*M_PI;
						}
						h_deltaphi->Fill(delta_phi);	

						if (delta_phi > M_PI/3. and delta_phi < 2*M_PI/3.){
			                            n=n+1.;
                       				    sumpt=sumpt+ptt;

                            		            n1=n1+1;
                            			    sumpt1=sumpt1+ptt;
						}
						if (delta_phi < -M_PI/3. and delta_phi > -2*M_PI/3.){
                                                    n=n+1.;
                                                    sumpt=sumpt+ptt;

                                                    n2=n2+1;
                                                    sumpt2=sumpt2+ptt;
						}


											
					}// I have 1 good jet	
				}// good track
	
			}// tracks cycle			

			if(ptf>0){
				h_nTrans_SisCone5->Fill(n,ptf);
                        	h_ptTrans_SisCone5->Fill(sumpt,ptf);
			}
			if(te>0){ h_pt_t->Fill(te);}
		} // >=1 good vertex 


	} // good lumi and trigger

	if(k/50000==1){
		k=0;

		time(&timer2);
		double seconds = difftime(timer1,timer2);
		cout<< "Event: " << i+1 << " speed: " << 50000*(-1.0)/seconds << " evt/s   ETA:" << (nevent-(i+1))/(50000*(-1.0)/seconds) << " s" << endl;
		timer1=timer2;
	}

} // event cycle


time(&timer_end);
timeinfo = localtime ( &timer_end);

cout << endl << "Ended at:  " << asctime(timeinfo) << endl;

cout << "Total time: " << difftime(timer_end,timer_start) << " s" << endl;

TFile* file_out;

file_out->Open("UE_test.root", "RECREATE"); 

h_vtxndf->Write();
h_vtxdz->Write();
h_vtxrho->Write();
h_nvtx->Write();

h_pt_t->Write();
h_pt_t_gen->Write();
h_eta_t->Write();
h_eta_t_gen->Write();
h_phi_t->Write();
h_phi_t_gen->Write();

h_pt_jet->Write();
h_pt_jet_gen->Write();
h_eta_jet->Write();
h_eta_jet_gen->Write();
h_phi_jet->Write();
h_phi_jet_gen->Write();

h_deltaphi->Write();
h_deltaphi_gen->Write();

h_nTrans_SisCone5->Write();
h_ptTrans_SisCone5->Write();

h_nTrans_SisCone5_gen->Write();
h_ptTrans_SisCone5_gen->Write();
}
