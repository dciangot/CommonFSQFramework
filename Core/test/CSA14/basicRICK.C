#include "Riostream.h"
#include "string.h"
#include <stdio.h>
void basicRICK() {
//  Read data from an ascii file and create a root file with an histogram and an ntuple.
//   see a variant of this macro in basic2.C
//Author: Rene Brun
      

   TString dir = gSystem->UnixPathName(gInterpreter->GetCurrentMacroName());
   dir.ReplaceAll("basicRICK.C","");
   dir.ReplaceAll("/./","/");
   ifstream in;
   in.open(Form("%s13-10-23-52072-Corrected_Data_PTmax_Eta20_7-27-15.prn",dir.Data()));
   std::string line;

   //Skip title lines.  Make sure this matches the number of lines in the input file!
   for(unsigned int i = 0; i < 7; i++)
   {
      getline(in, line);
   }
   Double_t low, high, center, MAXnch, MAXerr, MINnch, MINerr, AVEnch, AVEerr, DIFnch, DIFerr;
   Int_t nlines = 0;
   TFile *f = new TFile("basic.root","RECREATE");
   //TH1F *h1 = new TH1F("h1","x distribution",100,-4,4);
   //TNtuple *ntuple = new TNtuple("ntuple","data from ascii file","x:y:z");

   //For now the low sides of bins have to be entered manually.
   Float_t binLows[18] = {0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5, 6, 7, 8, 10, 12, 16, 20, 24};


   //We use TH1 instead of TProfile because SetBinContent does not work with TProfile
   TH1D *transMAX_Nch = new TH1D("transMAX_nch", "Transverse MAX (Nch)", 17, binLows);
   TH1D *transMIN_Nch = new TH1D("transMIN_nch", "Transverse MIN (Nch)", 17, binLows);
   TH1D *transAVE_Nch = new TH1D("transAVE_nch", "Transverse AVE (Nch)", 17, binLows);
   TH1D *transDIF_Nch = new TH1D("transDIF_nch", "Transverse DIF (Nch)", 17, binLows);


   std::cout << "Make sure the array binLows matches your data!" << std::endl;
   std::cout << "The input read from your data file is: " << std::endl;
   while (1) {

      in >> low >> high >> center >> MAXnch >> MAXerr >> MINnch >> MINerr >> AVEnch >> AVEerr >> DIFnch >> DIFerr;

      if (!in.good()) break;

      std::cout << " " << low << " " << high << " " << center << " " << MAXnch << " " << MAXerr << " " << MINnch << " " << MINerr << " " << AVEnch << " " << AVEerr << " " << DIFnch << " " << DIFerr << std::endl;

      transMAX_Nch->SetBinContent(nlines+1, MAXnch);
      transMAX_Nch->SetBinError(nlines+1, MAXerr);

      transMIN_Nch->SetBinContent(nlines+1, MINnch);
      transMIN_Nch->SetBinError(nlines+1, MINerr);

      transAVE_Nch->SetBinContent(nlines+1, AVEnch);
      transAVE_Nch->SetBinError(nlines+1, AVEerr);

      transDIF_Nch->SetBinContent(nlines+1, DIFnch);
      transDIF_Nch->SetBinError(nlines+1, DIFerr);






      //std::cout << "Wrote " << MAXnch << " to histogram at " << nlines+1 << std::endl;
      //std::cout << "Bin content is now " << transMAX_Nch->GetBinContent(nlines+1) << std::endl;

      nlines++;
   }
   //printf(" found %d points\n",nlines);

   in.close();

   f->Write();
}
