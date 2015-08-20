



	//	#include "MZ_Selector_test_11_09_10.h"
	#include "TROOT.h"
	#include "TH2.h"
	#include "TH1.h"
	#include "TProfile.h"
	#include <TStyle.h>
	#include <iostream>
	#include <iomanip>
	#include "math.h" 
	#include "TCanvas.h"
	#include "TFile.h"
	#include "TTree.h"
	#include "TChain.h"
	#include "TProfile.h"
	#include "TPaveText.h"
	//	#include "TCanvas.h"
	#include "TLegend.h"
	#include <stdio.h>
	#include <stdlib.h>
	#include "TMath.h"
	#include "TInterpreter.h"
	#include "Print.h"
	#include "TDCacheFile.h"
	#include "TMatrixD.h"
	#include "TVectorD.h"
	#include "TMatrixDEigen.h"
	//	#include "TestFunc.h"
	#include <fstream>
	#include <time.h>
	#include <string.h>


	using namespace std;



	void printHistos_DATA ()
	{



	TFile *fhist = new TFile("DATA_8-10-15_eta08_vtxs.root");


	fhist->cd("Run2015B");

	//TCanvas *c1 = new TCanvas("c1","c1",600,400);




	//TH2F *HIST_CUT_TFF_TTF_NchMB;
	//gDirectory->GetObject("HIST_CUT_TFF_TTF_NchMB",HIST_CUT_TFF_TTF_NchMB);
	//gStyle->SetPalette(1);
	//HIST_CUT_TFF_TTF_NchMB->Draw("COLZ");
	//c1->Update();
	//c1->Print();

TH1F *HIST_nEventsVTXS;
gDirectory->GetObject("HIST_nEventsVTXS",HIST_nEventsVTXS);
PrintHistogram(HIST_nEventsVTXS,1,1,"text/DATA/HIST_nEventsVTXS.txt");

TH1F *HIST_nEventsVTX1;
gDirectory->GetObject("HIST_nEventsVTX1",HIST_nEventsVTX1);
PrintHistogram(HIST_nEventsVTX1,1,1,"text/DATA/HIST_nEventsVTX1.txt");


TH1F *HIST_delzVtx;
gDirectory->GetObject("HIST_delzVtx",HIST_delzVtx);
PrintHistogram(HIST_delzVtx,1,1,"text/DATA/HIST_delzVtx.txt");

TH1F *HIST_delzVtxVTX;
gDirectory->GetObject("HIST_delzVtxVTX",HIST_delzVtxVTX);
PrintHistogram(HIST_delzVtxVTX,1,1,"text/DATA/HIST_delzVtxVTX.txt");

TH1F *HIST_nVtx;
gDirectory->GetObject("HIST_nVtx",HIST_nVtx);
PrintHistogram(HIST_nVtx,1,1,"text/DATA/HIST_nVtx.txt");

TH1F *HIST_nVtxVTX;
gDirectory->GetObject("HIST_nVtxVTX",HIST_nVtxVTX);
PrintHistogram(HIST_nVtxVTX,1,1,"text/DATA/HIST_nVtxVTX.txt");


TProfile *towardTotalAvg_b4;
gDirectory->GetObject("towardTotalAvg_b4",towardTotalAvg_b4);
PrintProfile(towardTotalAvg_b4,1,1,"text/DATA/towardTotalAvg_b4.txt");

TProfile *towardNch_b4;
gDirectory->GetObject("towardNch_b4",towardNch_b4);
PrintProfile(towardNch_b4,1,1,"text/DATA/towardNch_b4.txt");

TProfile *trans_b4;
gDirectory->GetObject("trans_b4",trans_b4);
PrintProfile(trans_b4,1,1,"text/DATA/trans_b4.txt");

TProfile *toward_b4;
gDirectory->GetObject("toward_b4",toward_b4);
PrintProfile(toward_b4,1,1,"text/DATA/toward_b4.txt");

TProfile *overallTotal_b4;
gDirectory->GetObject("overallTotal_b4",overallTotal_b4);
PrintProfile(overallTotal_b4,1,1,"text/DATA/overallTotal_b4.txt");

TProfile *transMaxNch_b4;
gDirectory->GetObject("transMaxNch_b4",transMaxNch_b4);
PrintProfile(transMaxNch_b4,1,1,"text/DATA/transMaxNch_b4.txt");

TProfile *overallTotalNch_b4;
gDirectory->GetObject("overallTotalNch_b4",overallTotalNch_b4);
PrintProfile(overallTotalNch_b4,1,1,"text/DATA/overallTotalNch_b4.txt");

TProfile *overallAvg_b4;
gDirectory->GetObject("overallAvg_b4",overallAvg_b4);
PrintProfile(overallAvg_b4,1,1,"text/DATA/overallAvg_b4.txt");

TProfile *transDifNch_b4;
gDirectory->GetObject("transDifNch_b4",transDifNch_b4);
PrintProfile(transDifNch_b4,1,1,"text/DATA/transDifNch_b4.txt");

TProfile *transMax_b4;
gDirectory->GetObject("transMax_b4",transMax_b4);
PrintProfile(transMax_b4,1,1,"text/DATA/transMax_b4.txt");

TProfile *transMinNch_b4;
gDirectory->GetObject("transMinNch_b4",transMinNch_b4);
PrintProfile(transMinNch_b4,1,1,"text/DATA/transMinNch_b4.txt");

TProfile *ptMax_b4;
gDirectory->GetObject("ptMax_b4",ptMax_b4);
PrintProfile(ptMax_b4,1,1,"text/DATA/ptMax_b4.txt");

TProfile *towardAvg_b4;
gDirectory->GetObject("towardAvg_b4",towardAvg_b4);
PrintProfile(towardAvg_b4,1,1,"text/DATA/towardAvg_b4.txt");

TProfile *transDif_b4;
gDirectory->GetObject("transDif_b4",transDif_b4);
PrintProfile(transDif_b4,1,1,"text/DATA/transDif_b4.txt");

TProfile *transMin_b4;
gDirectory->GetObject("transMin_b4",transMin_b4);
PrintProfile(transMin_b4,1,1,"text/DATA/transMin_b4.txt");

TProfile *towardTotalNch_b4;
gDirectory->GetObject("towardTotalNch_b4",towardTotalNch_b4);
PrintProfile(towardTotalNch_b4,1,1,"text/DATA/towardTotalNch_b4.txt");

TProfile *overallNch_b4;
gDirectory->GetObject("overallNch_b4",overallNch_b4);
PrintProfile(overallNch_b4,1,1,"text/DATA/overallNch_b4.txt");

TProfile *transAvg_b4;
gDirectory->GetObject("transAvg_b4",transAvg_b4);
PrintProfile(transAvg_b4,1,1,"text/DATA/transAvg_b4.txt");

TProfile *overall_b4;
gDirectory->GetObject("overall_b4",overall_b4);
PrintProfile(overall_b4,1,1,"text/DATA/overall_b4.txt");

TProfile *transNch_b4;
gDirectory->GetObject("transNch_b4",transNch_b4);
PrintProfile(transNch_b4,1,1,"text/DATA/transNch_b4.txt");

TProfile *awayNch_b4;
gDirectory->GetObject("awayNch_b4",awayNch_b4);
PrintProfile(awayNch_b4,1,1,"text/DATA/awayNch_b4.txt");

TProfile *overallTotalAvg_b4;
gDirectory->GetObject("overallTotalAvg_b4",overallTotalAvg_b4);
PrintProfile(overallTotalAvg_b4,1,1,"text/DATA/overallTotalAvg_b4.txt");

TProfile *away_b4;
gDirectory->GetObject("away_b4",away_b4);
PrintProfile(away_b4,1,1,"text/DATA/away_b4.txt");

TProfile *awayAvg_b4;
gDirectory->GetObject("awayAvg_b4",awayAvg_b4);
PrintProfile(awayAvg_b4,1,1,"text/DATA/awayAvg_b4.txt");

TProfile *towardTotal_b4;
gDirectory->GetObject("towardTotal_b4",towardTotal_b4);
PrintProfile(towardTotal_b4,1,1,"text/DATA/towardTotal_b4.txt");





//No error for just this one:

TProfile *toward_b2;
gDirectory->GetObject("toward_b2",toward_b2);
PrintProfile(toward_b2,1,1,"text/DATA/toward_b2.txt");






TH1F *HIST_eta_ptH;
gDirectory->GetObject("HIST_eta_ptH",HIST_eta_ptH);
PrintHistogram(HIST_eta_ptH,1,1,"text/DATA/HIST_eta_ptH.txt");

TH1F *HIST_phi_etaptH;
gDirectory->GetObject("HIST_phi_etaptH",HIST_phi_etaptH);
PrintHistogram(HIST_phi_etaptH,1,1,"text/DATA/HIST_phi_etaptH.txt");



TH1F *HIST_CUT_FFF_eta;
gDirectory->GetObject("HIST_CUT_FFF_eta",HIST_CUT_FFF_eta);
PrintHistogram(HIST_CUT_FFF_eta,1,1,"text/DATA/HIST_CUT_FFF_eta.txt");

TH1F *HIST_CUT_TFF_eta;
gDirectory->GetObject("HIST_CUT_TFF_eta",HIST_CUT_TFF_eta);
PrintHistogram(HIST_CUT_TFF_eta,1,1,"text/DATA/HIST_CUT_TFF_eta.txt");

TH1F *HIST_CUT_TTF_eta;
gDirectory->GetObject("HIST_CUT_TTF_eta",HIST_CUT_TTF_eta);
PrintHistogram(HIST_CUT_TTF_eta,1,1,"text/DATA/HIST_CUT_TTF_eta.txt");

TH1F *HIST_CUT_TTT_eta;
gDirectory->GetObject("HIST_CUT_TTT_eta",HIST_CUT_TTT_eta);
PrintHistogram(HIST_CUT_TTT_eta,1,1,"text/DATA/HIST_CUT_TTT_eta.txt");

TH1F *HIST_CUT_TFT_eta;
gDirectory->GetObject("HIST_CUT_TFT_eta",HIST_CUT_TFT_eta);
PrintHistogram(HIST_CUT_TFT_eta,1,1,"text/DATA/HIST_CUT_TFT_eta.txt");

TH1F *HIST_CUT_FFF_phi;
gDirectory->GetObject("HIST_CUT_FFF_phi",HIST_CUT_FFF_phi);
PrintHistogram(HIST_CUT_FFF_phi,1,1,"text/DATA/HIST_CUT_FFF_phi.txt");

TH1F *HIST_CUT_TFF_phi;
gDirectory->GetObject("HIST_CUT_TFF_phi",HIST_CUT_TFF_phi);
PrintHistogram(HIST_CUT_TFF_phi,1,1,"text/DATA/HIST_CUT_TFF_phi.txt");

TH1F *HIST_CUT_TTF_phi;
gDirectory->GetObject("HIST_CUT_TTF_phi",HIST_CUT_TTF_phi);
PrintHistogram(HIST_CUT_TTF_phi,1,1,"text/DATA/HIST_CUT_TTF_phi.txt");

TH1F *HIST_CUT_TTT_phi;
gDirectory->GetObject("HIST_CUT_TTT_phi",HIST_CUT_TTT_phi);
PrintHistogram(HIST_CUT_TTT_phi,1,1,"text/DATA/HIST_CUT_TTT_phi.txt");

TH1F *HIST_CUT_TFT_phi;
gDirectory->GetObject("HIST_CUT_TFT_phi",HIST_CUT_TFT_phi);
PrintHistogram(HIST_CUT_TFT_phi,1,1,"text/DATA/HIST_CUT_TFT_phi.txt");

TH1F *HIST_CUT_FFF_PtErr;
gDirectory->GetObject("HIST_CUT_FFF_PtErr",HIST_CUT_FFF_PtErr);
PrintHistogram(HIST_CUT_FFF_PtErr,1,1,"text/DATA/HIST_CUT_FFF_PtErr.txt");

TH1F *HIST_CUT_TFF_PtErr;
gDirectory->GetObject("HIST_CUT_TFF_PtErr",HIST_CUT_TFF_PtErr);
PrintHistogram(HIST_CUT_TFF_PtErr,1,1,"text/DATA/HIST_CUT_TFF_PtErr.txt");

TH1F *HIST_CUT_TTF_PtErr;
gDirectory->GetObject("HIST_CUT_TTF_PtErr",HIST_CUT_TTF_PtErr);
PrintHistogram(HIST_CUT_TTF_PtErr,1,1,"text/DATA/HIST_CUT_TTF_PtErr.txt");

TH1F *HIST_CUT_TTT_PtErr;
gDirectory->GetObject("HIST_CUT_TTT_PtErr",HIST_CUT_TTT_PtErr);
PrintHistogram(HIST_CUT_TTT_PtErr,1,1,"text/DATA/HIST_CUT_TTT_PtErr.txt");

TH1F *HIST_CUT_TFT_PtErr;
gDirectory->GetObject("HIST_CUT_TFT_PtErr",HIST_CUT_TFT_PtErr);
PrintHistogram(HIST_CUT_TFT_PtErr,1,1,"text/DATA/HIST_CUT_TFT_PtErr.txt");

TH1F *HIST_CUT_TFT_NchMB;
gDirectory->GetObject("HIST_CUT_TFT_NchMB",HIST_CUT_TFT_NchMB);
PrintHistogram(HIST_CUT_TFT_NchMB,1,1,"text/DATA/HIST_CUT_TFT_NchMB.txt");

TH1F *HIST_CUT_TFT_d0;
gDirectory->GetObject("HIST_CUT_TFT_d0",HIST_CUT_TFT_d0);
PrintHistogram(HIST_CUT_TFT_d0,1,1,"text/DATA/HIST_CUT_TFT_d0.txt");

TH1F *HIST_CUT_TFT_dz;
gDirectory->GetObject("HIST_CUT_TFT_dz",HIST_CUT_TFT_dz);
PrintHistogram(HIST_CUT_TFT_dz,1,1,"text/DATA/HIST_CUT_TFT_dz.txt");

TH1F *HIST_CUT_TFT_d0dzMax;
gDirectory->GetObject("HIST_CUT_TFT_d0dzMax",HIST_CUT_TFT_d0dzMax);
PrintHistogram(HIST_CUT_TFT_d0dzMax,1,1,"text/DATA/HIST_CUT_TFT_d0dzMax.txt");

TH1F *HIST_CUT_FFF_NchMB;
gDirectory->GetObject("HIST_CUT_FFF_NchMB",HIST_CUT_FFF_NchMB);
PrintHistogram(HIST_CUT_FFF_NchMB,1,1,"text/DATA/HIST_CUT_FFF_NchMB.txt");

TH1F *HIST_CUT_FFF_d0;
gDirectory->GetObject("HIST_CUT_FFF_d0",HIST_CUT_FFF_d0);
PrintHistogram(HIST_CUT_FFF_d0,1,1,"text/DATA/HIST_CUT_FFF_d0.txt");

TH1F *HIST_CUT_FFF_dz;
gDirectory->GetObject("HIST_CUT_FFF_dz",HIST_CUT_FFF_dz);
PrintHistogram(HIST_CUT_FFF_dz,1,1,"text/DATA/HIST_CUT_FFF_dz.txt");

TH1F *HIST_CUT_FFF_d0dzMax;
gDirectory->GetObject("HIST_CUT_FFF_d0dzMax",HIST_CUT_FFF_d0dzMax);
PrintHistogram(HIST_CUT_FFF_d0dzMax,1,1,"text/DATA/HIST_CUT_FFF_d0dzMax.txt");

TH1F *HIST_VTX_nTrk;
gDirectory->GetObject("HIST_VTX_nTrk",HIST_VTX_nTrk);
PrintHistogram(HIST_VTX_nTrk,1,1,"text/DATA/HIST_VTX_nTrk.txt");

TH1F *HIST_VTX_ndof;
gDirectory->GetObject("HIST_VTX_ndof",HIST_VTX_ndof);
PrintHistogram(HIST_VTX_ndof,1,1,"text/DATA/HIST_VTX_ndof.txt");

TH1F *HIST_VTX_Zpos;
gDirectory->GetObject("HIST_VTX_Zpos",HIST_VTX_Zpos);
PrintHistogram(HIST_VTX_Zpos,1,1,"text/DATA/HIST_VTX_Zpos.txt");

TH1F *HIST_VTX_chi2;
gDirectory->GetObject("HIST_VTX_chi2",HIST_VTX_chi2);
PrintHistogram(HIST_VTX_chi2,1,1,"text/DATA/HIST_VTX_chi2.txt");

TH1F *HIST_TRK_PtErr;
gDirectory->GetObject("HIST_TRK_PtErr",HIST_TRK_PtErr);
PrintHistogram(HIST_TRK_PtErr,1,1,"text/DATA/HIST_TRK_PtErr.txt");


TH1F *HIST_CUT_TFF_NchMB;
gDirectory->GetObject("HIST_CUT_TFF_NchMB",HIST_CUT_TFF_NchMB);
PrintHistogram(HIST_CUT_TFF_NchMB,1,1,"text/DATA/HIST_CUT_TFF_NchMB.txt");

TH1F *HIST_CUT_TTF_NchMB;
gDirectory->GetObject("HIST_CUT_TTF_NchMB",HIST_CUT_TTF_NchMB);
PrintHistogram(HIST_CUT_TTF_NchMB,1,1,"text/DATA/HIST_CUT_TTF_NchMB.txt");

TH1F *HIST_CUT_TTT_NchMB;
gDirectory->GetObject("HIST_CUT_TTT_NchMB",HIST_CUT_TTT_NchMB);
PrintHistogram(HIST_CUT_TTT_NchMB,1,1,"text/DATA/HIST_CUT_TTT_NchMB.txt");

TH1F *HIST_CUT_TFF_d0;
gDirectory->GetObject("HIST_CUT_TFF_d0",HIST_CUT_TFF_d0);
PrintHistogram(HIST_CUT_TFF_d0,1,1,"text/DATA/HIST_CUT_TFF_d0.txt");

TH1F *HIST_CUT_TTF_d0;
gDirectory->GetObject("HIST_CUT_TTF_d0",HIST_CUT_TTF_d0);
PrintHistogram(HIST_CUT_TTF_d0,1,1,"text/DATA/HIST_CUT_TTF_d0.txt");

TH1F *HIST_CUT_TTT_d0;
gDirectory->GetObject("HIST_CUT_TTT_d0",HIST_CUT_TTT_d0);
PrintHistogram(HIST_CUT_TTT_d0,1,1,"text/DATA/HIST_CUT_TTT_d0.txt");

TH1F *HIST_CUT_TFF_dz;
gDirectory->GetObject("HIST_CUT_TFF_dz",HIST_CUT_TFF_dz);
PrintHistogram(HIST_CUT_TFF_dz,1,1,"text/DATA/HIST_CUT_TFF_dz.txt");

TH1F *HIST_CUT_TTF_dz;
gDirectory->GetObject("HIST_CUT_TTF_dz",HIST_CUT_TTF_dz);
PrintHistogram(HIST_CUT_TTF_dz,1,1,"text/DATA/HIST_CUT_TTF_dz.txt");

TH1F *HIST_CUT_TTT_dz;
gDirectory->GetObject("HIST_CUT_TTT_dz",HIST_CUT_TTT_dz);
PrintHistogram(HIST_CUT_TTT_dz,1,1,"text/DATA/HIST_CUT_TTT_dz.txt");

TH1F *HIST_CUT_TFF_d0dzMax;
gDirectory->GetObject("HIST_CUT_TFF_d0dzMax",HIST_CUT_TFF_d0dzMax);
PrintHistogram(HIST_CUT_TFF_d0dzMax,1,1,"text/DATA/HIST_CUT_TFF_d0dzMax.txt");

TH1F *HIST_CUT_TTF_d0dzMax;
gDirectory->GetObject("HIST_CUT_TTF_d0dzMax",HIST_CUT_TTF_d0dzMax);
PrintHistogram(HIST_CUT_TTF_d0dzMax,1,1,"text/DATA/HIST_CUT_TTF_d0dzMax.txt");

TH1F *HIST_CUT_TTT_d0dzMax;
gDirectory->GetObject("HIST_CUT_TTT_d0dzMax",HIST_CUT_TTT_d0dzMax);
PrintHistogram(HIST_CUT_TTT_d0dzMax,1,1,"text/DATA/HIST_CUT_TTT_d0dzMax.txt");






TProfile *towardTotalAvg_b1;
gDirectory->GetObject("towardTotalAvg_b1",towardTotalAvg_b1);
PrintProfile(towardTotalAvg_b1,1,1,"text/DATA/towardTotalAvg_b1.txt");

TProfile *towardTotalAvg_b2;
gDirectory->GetObject("towardTotalAvg_b2",towardTotalAvg_b2);
PrintProfile(towardTotalAvg_b2,1,1,"text/DATA/towardTotalAvg_b2.txt");

TProfile *transDifNch_b1;
gDirectory->GetObject("transDifNch_b1",transDifNch_b1);
PrintProfile(transDifNch_b1,1,1,"text/DATA/transDifNch_b1.txt");

TH1F *HIST_nchMB;
gDirectory->GetObject("HIST_nchMB",HIST_nchMB);
PrintHistogram(HIST_nchMB,1,1,"text/DATA/HIST_nchMB.txt");

TProfile *towardNch_b2;
gDirectory->GetObject("towardNch_b2",towardNch_b2);
PrintProfile(towardNch_b2,1,1,"text/DATA/towardNch_b2.txt");

TH1F *HIST_ptSumMB;
gDirectory->GetObject("HIST_ptSumMB",HIST_ptSumMB);
PrintHistogram(HIST_ptSumMB,1,1,"text/DATA/HIST_ptSumMB.txt");

TProfile *trans_b2;
gDirectory->GetObject("trans_b2",trans_b2);
PrintProfile(trans_b2,1,1,"text/DATA/trans_b2.txt");

TProfile *trans_b1;
gDirectory->GetObject("trans_b1",trans_b1);
PrintProfile(trans_b1,1,1,"text/DATA/trans_b1.txt");

TProfile *transMax_bh;
gDirectory->GetObject("transMax_bh",transMax_bh);
PrintProfile(transMax_bh,1,1,"text/DATA/transMax_bh.txt");

TProfile *overallAvg_bh;
gDirectory->GetObject("overallAvg_bh",overallAvg_bh);
PrintProfile(overallAvg_bh,1,1,"text/DATA/overallAvg_bh.txt");

TProfile *toward_b2;
gDirectory->GetObject("toward_b2",toward_b2);
PrintProfile(toward_b2,1,1,"text/DATA/toward_b2.txt");

TProfile *toward_b1;
gDirectory->GetObject("toward_b1",toward_b1);
PrintProfile(toward_b1,1,1,"text/DATA/toward_b1.txt");

TProfile *overallTotal_b2;
gDirectory->GetObject("overallTotal_b2",overallTotal_b2);
PrintProfile(overallTotal_b2,1,1,"text/DATA/overallTotal_b2.txt");

TProfile *overallTotal_b1;
gDirectory->GetObject("overallTotal_b1",overallTotal_b1);
PrintProfile(overallTotal_b1,1,1,"text/DATA/overallTotal_b1.txt");

TProfile *trans_bh;
gDirectory->GetObject("trans_bh",trans_bh);
PrintProfile(trans_bh,1,1,"text/DATA/trans_bh.txt");

TProfile *towardNch_bh;
gDirectory->GetObject("towardNch_bh",towardNch_bh);
PrintProfile(towardNch_bh,1,1,"text/DATA/towardNch_bh.txt");

TProfile *transMaxNch_b2;
gDirectory->GetObject("transMaxNch_b2",transMaxNch_b2);
PrintProfile(transMaxNch_b2,1,1,"text/DATA/transMaxNch_b2.txt");

TH1F *HIST_etaMB;
gDirectory->GetObject("HIST_etaMB",HIST_etaMB);
PrintHistogram(HIST_etaMB,1,1,"text/DATA/HIST_etaMB.txt");

TProfile *towardTotalAvg_bh;
gDirectory->GetObject("towardTotalAvg_bh",towardTotalAvg_bh);
PrintProfile(towardTotalAvg_bh,1,1,"text/DATA/towardTotalAvg_bh.txt");

TProfile *towardNch_b1;
gDirectory->GetObject("towardNch_b1",towardNch_b1);
PrintProfile(towardNch_b1,1,1,"text/DATA/towardNch_b1.txt");

TProfile *overallTotalNch_b2;
gDirectory->GetObject("overallTotalNch_b2",overallTotalNch_b2);
PrintProfile(overallTotalNch_b2,1,1,"text/DATA/overallTotalNch_b2.txt");

TProfile *overallAvg_b2;
gDirectory->GetObject("overallAvg_b2",overallAvg_b2);
PrintProfile(overallAvg_b2,1,1,"text/DATA/overallAvg_b2.txt");

TProfile *overallAvg_b1;
gDirectory->GetObject("overallAvg_b1",overallAvg_b1);
PrintProfile(overallAvg_b1,1,1,"text/DATA/overallAvg_b1.txt");

TProfile *toward_bh;
gDirectory->GetObject("toward_bh",toward_bh);
PrintProfile(toward_bh,1,1,"text/DATA/toward_bh.txt");

TProfile *transDifNch_b2;
gDirectory->GetObject("transDifNch_b2",transDifNch_b2);
PrintProfile(transDifNch_b2,1,1,"text/DATA/transDifNch_b2.txt");

TProfile *transMax_b2;
gDirectory->GetObject("transMax_b2",transMax_b2);
PrintProfile(transMax_b2,1,1,"text/DATA/transMax_b2.txt");

TProfile *transMax_b1;
gDirectory->GetObject("transMax_b1",transMax_b1);
PrintProfile(transMax_b1,1,1,"text/DATA/transMax_b1.txt");

TH1F *HIST_pt_pt5;
gDirectory->GetObject("HIST_pt_pt5",HIST_pt_pt5);
PrintHistogram(HIST_pt_pt5,1,1,"text/DATA/HIST_pt_pt5.txt");

TProfile *ptMax_bh;
gDirectory->GetObject("ptMax_bh",ptMax_bh);
PrintProfile(ptMax_bh,1,1,"text/DATA/ptMax_bh.txt");

TProfile *transMinNch_bh;
gDirectory->GetObject("transMinNch_bh",transMinNch_bh);
PrintProfile(transMinNch_bh,1,1,"text/DATA/transMinNch_bh.txt");

TH1F *HIST_delPhiPt_pt5;
gDirectory->GetObject("HIST_delPhiPt_pt5",HIST_delPhiPt_pt5);
PrintHistogram(HIST_delPhiPt_pt5,1,1,"text/DATA/HIST_delPhiPt_pt5.txt");

TH1F *HIST_nch_pt5;
gDirectory->GetObject("HIST_nch_pt5",HIST_nch_pt5);
PrintHistogram(HIST_nch_pt5,1,1,"text/DATA/HIST_nch_pt5.txt");

TProfile *overallTotalNch_b1;
gDirectory->GetObject("overallTotalNch_b1",overallTotalNch_b1);
PrintProfile(overallTotalNch_b1,1,1,"text/DATA/overallTotalNch_b1.txt");

TH1F *HIST_ptSum;
gDirectory->GetObject("HIST_ptSum",HIST_ptSum);
PrintHistogram(HIST_ptSum,1,1,"text/DATA/HIST_ptSum.txt");

TProfile *transMaxNch_b1;
gDirectory->GetObject("transMaxNch_b1",transMaxNch_b1);
PrintProfile(transMaxNch_b1,1,1,"text/DATA/transMaxNch_b1.txt");

TProfile *towardAvg_bh;
gDirectory->GetObject("towardAvg_bh",towardAvg_bh);
PrintProfile(towardAvg_bh,1,1,"text/DATA/towardAvg_bh.txt");

TH1F *HIST_ptMax;
gDirectory->GetObject("HIST_ptMax",HIST_ptMax);
PrintHistogram(HIST_ptMax,1,1,"text/DATA/HIST_ptMax.txt");

TH1F *HIST_transPtSum_pt5;
gDirectory->GetObject("HIST_transPtSum_pt5",HIST_transPtSum_pt5);
PrintHistogram(HIST_transPtSum_pt5,1,1,"text/DATA/HIST_transPtSum_pt5.txt");

TProfile *transMinNch_b1;
gDirectory->GetObject("transMinNch_b1",transMinNch_b1);
PrintProfile(transMinNch_b1,1,1,"text/DATA/transMinNch_b1.txt");

TProfile *transMinNch_b2;
gDirectory->GetObject("transMinNch_b2",transMinNch_b2);
PrintProfile(transMinNch_b2,1,1,"text/DATA/transMinNch_b2.txt");

TProfile *ptMax_b2;
gDirectory->GetObject("ptMax_b2",ptMax_b2);
PrintProfile(ptMax_b2,1,1,"text/DATA/ptMax_b2.txt");

TProfile *ptMax_b1;
gDirectory->GetObject("ptMax_b1",ptMax_b1);
PrintProfile(ptMax_b1,1,1,"text/DATA/ptMax_b1.txt");

TH1F *HIST_transPt;
gDirectory->GetObject("HIST_transPt",HIST_transPt);
PrintHistogram(HIST_transPt,1,1,"text/DATA/HIST_transPt.txt");

TProfile *overallTotalNch_bh;
gDirectory->GetObject("overallTotalNch_bh",overallTotalNch_bh);
PrintProfile(overallTotalNch_bh,1,1,"text/DATA/overallTotalNch_bh.txt");

TProfile *transMaxNch_bh;
gDirectory->GetObject("transMaxNch_bh",transMaxNch_bh);
PrintProfile(transMaxNch_bh,1,1,"text/DATA/transMaxNch_bh.txt");

TProfile *towardAvg_b1;
gDirectory->GetObject("towardAvg_b1",towardAvg_b1);
PrintProfile(towardAvg_b1,1,1,"text/DATA/towardAvg_b1.txt");

TProfile *towardAvg_b2;
gDirectory->GetObject("towardAvg_b2",towardAvg_b2);
PrintProfile(towardAvg_b2,1,1,"text/DATA/towardAvg_b2.txt");

TH1F *HIST_delPhiPt;
gDirectory->GetObject("HIST_delPhiPt",HIST_delPhiPt);
PrintHistogram(HIST_delPhiPt,1,1,"text/DATA/HIST_delPhiPt.txt");

TH1F *HIST_ptMB;
gDirectory->GetObject("HIST_ptMB",HIST_ptMB);
PrintHistogram(HIST_ptMB,1,1,"text/DATA/HIST_ptMB.txt");

TProfile *transDif_b2;
gDirectory->GetObject("transDif_b2",transDif_b2);
PrintProfile(transDif_b2,1,1,"text/DATA/transDif_b2.txt");

TProfile *transDif_b1;
gDirectory->GetObject("transDif_b1",transDif_b1);
PrintProfile(transDif_b1,1,1,"text/DATA/transDif_b1.txt");

TProfile *transMin_b1;
gDirectory->GetObject("transMin_b1",transMin_b1);
PrintProfile(transMin_b1,1,1,"text/DATA/transMin_b1.txt");

TProfile *transMin_b2;
gDirectory->GetObject("transMin_b2",transMin_b2);
PrintProfile(transMin_b2,1,1,"text/DATA/transMin_b2.txt");

TH1F *HIST_delPhi;
gDirectory->GetObject("HIST_delPhi",HIST_delPhi);
PrintHistogram(HIST_delPhi,1,1,"text/DATA/HIST_delPhi.txt");

TProfile *transNch_bh;
gDirectory->GetObject("transNch_bh",transNch_bh);
PrintProfile(transNch_bh,1,1,"text/DATA/transNch_bh.txt");

TProfile *overall_bh;
gDirectory->GetObject("overall_bh",overall_bh);
PrintProfile(overall_bh,1,1,"text/DATA/overall_bh.txt");

TProfile *towardTotalNch_b1;
gDirectory->GetObject("towardTotalNch_b1",towardTotalNch_b1);
PrintProfile(towardTotalNch_b1,1,1,"text/DATA/towardTotalNch_b1.txt");

TProfile *towardTotalNch_b2;
gDirectory->GetObject("towardTotalNch_b2",towardTotalNch_b2);
PrintProfile(towardTotalNch_b2,1,1,"text/DATA/towardTotalNch_b2.txt");

TProfile *overallNch_bh;
gDirectory->GetObject("overallNch_bh",overallNch_bh);
PrintProfile(overallNch_bh,1,1,"text/DATA/overallNch_bh.txt");

TProfile *transMin_bh;
gDirectory->GetObject("transMin_bh",transMin_bh);
PrintProfile(transMin_bh,1,1,"text/DATA/transMin_bh.txt");

TH1F *HIST_transPtSum;
gDirectory->GetObject("HIST_transPtSum",HIST_transPtSum);
PrintHistogram(HIST_transPtSum,1,1,"text/DATA/HIST_transPtSum.txt");

TH1F *HIST_eta_pt5;
gDirectory->GetObject("HIST_eta_pt5",HIST_eta_pt5);
PrintHistogram(HIST_eta_pt5,1,1,"text/DATA/HIST_eta_pt5.txt");

TH1F *HIST_delPhi_pt5;
gDirectory->GetObject("HIST_delPhi_pt5",HIST_delPhi_pt5);
PrintHistogram(HIST_delPhi_pt5,1,1,"text/DATA/HIST_delPhi_pt5.txt");

TProfile *transDif_bh;
gDirectory->GetObject("transDif_bh",transDif_bh);
PrintProfile(transDif_bh,1,1,"text/DATA/transDif_bh.txt");

TProfile *overallNch_b2;
gDirectory->GetObject("overallNch_b2",overallNch_b2);
PrintProfile(overallNch_b2,1,1,"text/DATA/overallNch_b2.txt");

TProfile *overallNch_b1;
gDirectory->GetObject("overallNch_b1",overallNch_b1);
PrintProfile(overallNch_b1,1,1,"text/DATA/overallNch_b1.txt");

TProfile *towardTotalNch_bh;
gDirectory->GetObject("towardTotalNch_bh",towardTotalNch_bh);
PrintProfile(towardTotalNch_bh,1,1,"text/DATA/towardTotalNch_bh.txt");

TProfile *transAvg_b2;
gDirectory->GetObject("transAvg_b2",transAvg_b2);
PrintProfile(transAvg_b2,1,1,"text/DATA/transAvg_b2.txt");

TProfile *overall_b2;
gDirectory->GetObject("overall_b2",overall_b2);
PrintProfile(overall_b2,1,1,"text/DATA/overall_b2.txt");

TProfile *overall_b1;
gDirectory->GetObject("overall_b1",overall_b1);
PrintProfile(overall_b1,1,1,"text/DATA/overall_b1.txt");

TProfile *transNch_b1;
gDirectory->GetObject("transNch_b1",transNch_b1);
PrintProfile(transNch_b1,1,1,"text/DATA/transNch_b1.txt");

TProfile *transNch_b2;
gDirectory->GetObject("transNch_b2",transNch_b2);
PrintProfile(transNch_b2,1,1,"text/DATA/transNch_b2.txt");

TProfile *transAvg_b1;
gDirectory->GetObject("transAvg_b1",transAvg_b1);
PrintProfile(transAvg_b1,1,1,"text/DATA/transAvg_b1.txt");

TH1F *HIST_ptSum_pt5;
gDirectory->GetObject("HIST_ptSum_pt5",HIST_ptSum_pt5);
PrintHistogram(HIST_ptSum_pt5,1,1,"text/DATA/HIST_ptSum_pt5.txt");

TH1F *HIST_transNch_pt5;
gDirectory->GetObject("HIST_transNch_pt5",HIST_transNch_pt5);
PrintHistogram(HIST_transNch_pt5,1,1,"text/DATA/HIST_transNch_pt5.txt");

TProfile *towardTotal_bh;
gDirectory->GetObject("towardTotal_bh",towardTotal_bh);
PrintProfile(towardTotal_bh,1,1,"text/DATA/towardTotal_bh.txt");

TH1F *HIST_nch;
gDirectory->GetObject("HIST_nch",HIST_nch);
PrintHistogram(HIST_nch,1,1,"text/DATA/HIST_nch.txt");

TProfile *awayNch_b1;
gDirectory->GetObject("awayNch_b1",awayNch_b1);
PrintProfile(awayNch_b1,1,1,"text/DATA/awayNch_b1.txt");

TProfile *awayNch_b2;
gDirectory->GetObject("awayNch_b2",awayNch_b2);
PrintProfile(awayNch_b2,1,1,"text/DATA/awayNch_b2.txt");

TH1F *HIST_transPt_pt5;
gDirectory->GetObject("HIST_transPt_pt5",HIST_transPt_pt5);
PrintHistogram(HIST_transPt_pt5,1,1,"text/DATA/HIST_transPt_pt5.txt");

TProfile *overallTotalAvg_b1;
gDirectory->GetObject("overallTotalAvg_b1",overallTotalAvg_b1);
PrintProfile(overallTotalAvg_b1,1,1,"text/DATA/overallTotalAvg_b1.txt");

TProfile *overallTotalAvg_b2;
gDirectory->GetObject("overallTotalAvg_b2",overallTotalAvg_b2);
PrintProfile(overallTotalAvg_b2,1,1,"text/DATA/overallTotalAvg_b2.txt");

TProfile *transDifNch_bh;
gDirectory->GetObject("transDifNch_bh",transDifNch_bh);
PrintProfile(transDifNch_bh,1,1,"text/DATA/transDifNch_bh.txt");

TProfile *away_bh;
gDirectory->GetObject("away_bh",away_bh);
PrintProfile(away_bh,1,1,"text/DATA/away_bh.txt");

TProfile *awayAvg_bh;
gDirectory->GetObject("awayAvg_bh",awayAvg_bh);
PrintProfile(awayAvg_bh,1,1,"text/DATA/awayAvg_bh.txt");

TProfile *transAvg_bh;
gDirectory->GetObject("transAvg_bh",transAvg_bh);
PrintProfile(transAvg_bh,1,1,"text/DATA/transAvg_bh.txt");

TProfile *awayAvg_b1;
gDirectory->GetObject("awayAvg_b1",awayAvg_b1);
PrintProfile(awayAvg_b1,1,1,"text/DATA/awayAvg_b1.txt");

TProfile *away_b1;
gDirectory->GetObject("away_b1",away_b1);
PrintProfile(away_b1,1,1,"text/DATA/away_b1.txt");

TProfile *away_b2;
gDirectory->GetObject("away_b2",away_b2);
PrintProfile(away_b2,1,1,"text/DATA/away_b2.txt");

TProfile *awayAvg_b2;
gDirectory->GetObject("awayAvg_b2",awayAvg_b2);
PrintProfile(awayAvg_b2,1,1,"text/DATA/awayAvg_b2.txt");

TH1F *HIST_transNch;
gDirectory->GetObject("HIST_transNch",HIST_transNch);
PrintHistogram(HIST_transNch,1,1,"text/DATA/HIST_transNch.txt");

TProfile *overallTotalAvg_bh;
gDirectory->GetObject("overallTotalAvg_bh",overallTotalAvg_bh);
PrintProfile(overallTotalAvg_bh,1,1,"text/DATA/overallTotalAvg_bh.txt");

TProfile *overallTotal_bh;
gDirectory->GetObject("overallTotal_bh",overallTotal_bh);
PrintProfile(overallTotal_bh,1,1,"text/DATA/overallTotal_bh.txt");

TProfile *awayNch_bh;
gDirectory->GetObject("awayNch_bh",awayNch_bh);
PrintProfile(awayNch_bh,1,1,"text/DATA/awayNch_bh.txt");

TProfile *towardTotal_b1;
gDirectory->GetObject("towardTotal_b1",towardTotal_b1);
PrintProfile(towardTotal_b1,1,1,"text/DATA/towardTotal_b1.txt");

TProfile *towardTotal_b2;
gDirectory->GetObject("towardTotal_b2",towardTotal_b2);
PrintProfile(towardTotal_b2,1,1,"text/DATA/towardTotal_b2.txt");





// (" (" (" (" (" (" (" (" ", ", ", ", ", ", ", 







	cout << "Out file written" << endl;

	//	f->Close();
	}















