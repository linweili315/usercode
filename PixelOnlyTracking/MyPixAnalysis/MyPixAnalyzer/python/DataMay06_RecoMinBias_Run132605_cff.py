# Dataset: /MinimumBias/Commissioning10-May6thReReco-v1/RECO
# Global Tag: GR_R_35X_V8B::All

import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/FA81A4DC-7C59-DF11-8054-002618FDA277.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/F8B6DF84-5759-DF11-B800-001A92971B12.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/F89DD0A7-7A59-DF11-AAF6-001A92971B16.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/F84915CA-7B59-DF11-A555-00304867BECC.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/F8428290-5E59-DF11-9FBA-003048678B08.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/E012F79C-6659-DF11-B7D1-0018F3D096A0.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/DA845DDD-4E59-DF11-B7A5-001A92810AD6.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/D46B0DF7-7B59-DF11-849E-0018F3D096B6.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/D0CB7702-5F59-DF11-ACC0-00261894383C.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/C6739FF7-4E59-DF11-AB5D-0018F3D0962A.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/BEDE4110-8159-DF11-935D-001A928116D8.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/BE5626A6-5759-DF11-9AB2-00304867BFA8.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/B87CB235-8A59-DF11-AC32-001A92810A98.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/B86CD5DD-5159-DF11-98B1-00261894391C.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/B275769D-7F59-DF11-B99B-001BFCDBD15E.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/B0CACA4E-5959-DF11-8699-001A9281172A.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/B062963D-8959-DF11-8AFA-002618943863.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/B04DD0E4-4E59-DF11-990D-001A92811744.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/AE1BB77A-8359-DF11-A392-00248C0BE018.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/AAD7C040-5159-DF11-B9A0-001A92971B3C.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/AA9CD745-8459-DF11-B5F9-001A928116BE.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/AA778F10-4F59-DF11-98E6-002618943973.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/AA4F0BEF-4E59-DF11-8740-0026189438F6.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/AA4CD313-5659-DF11-91C5-0018F3D09692.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/A8A3301D-4F59-DF11-BAEF-001A92971B88.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/A89F9B8C-8759-DF11-949F-003048678E24.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/A69612A7-7E59-DF11-985E-0018F3D095FE.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/A45E3DEB-8059-DF11-8FB2-003048678B36.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/A2640BC0-8459-DF11-B14F-00261894397F.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/A250E16F-8159-DF11-AFA6-00304867C1BA.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/A047FD0E-8659-DF11-8897-00304867C1B0.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/A0403891-7A59-DF11-8285-002618FDA204.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/9ED63BA7-8B59-DF11-BA37-003048678DD6.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/9EB99287-5859-DF11-AE48-001BFCDBD182.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/9E40EA2B-8A59-DF11-A46B-00261894392D.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/9C7A522E-8359-DF11-B6F0-003048678AC0.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/9C061C1C-5E59-DF11-A8B2-003048678B12.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/9A162E6A-4F59-DF11-8682-001A92971B9A.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/981F5657-7459-DF11-8972-003048678F8A.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/9628B38B-6D59-DF11-B272-002618943920.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/9017EC1A-6C59-DF11-8679-002618943836.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/8E3EBEB7-7D59-DF11-A88E-0030486790FE.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/8E30C0D7-7859-DF11-A339-002354EF3BDC.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/8636B4CC-7D59-DF11-9956-002618FDA265.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/86343EE1-5459-DF11-AEFC-001A92810ABA.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/8257EC7C-8259-DF11-93A1-001A9281170C.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/8236B8CE-7B59-DF11-A28F-00261894393C.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/7E89910B-6C59-DF11-94ED-00261894395C.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/7CF0A18A-8B59-DF11-B788-001A928116EC.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/7A6D15EC-6359-DF11-8920-002618943950.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/7A2A0987-8659-DF11-84C6-0018F3D0965C.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/76744DF1-6959-DF11-B976-002618943861.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/76579533-7059-DF11-B687-00261894393C.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/7273BF2E-6559-DF11-9CF1-003048678B0E.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/70E43BB7-5559-DF11-AFDA-001A92810AE4.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/70932CE7-7B59-DF11-A076-002618943951.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/6EC0EBAB-8659-DF11-9F2B-002618943926.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/6E21437B-6859-DF11-8B9C-002354EF3BDC.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/6CDD1E35-7D59-DF11-BCDC-00304867BEE4.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/6839AD66-8359-DF11-A3B0-001A92811744.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/6495EAD3-4E59-DF11-97E8-003048678B88.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/64360B98-7D59-DF11-AFEB-0018F3D096DE.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/62817DF2-4E59-DF11-921F-0018F3D09708.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/6048E6EC-6C59-DF11-BA8B-003048678FE4.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/5EA4565B-5C59-DF11-83A7-0030486792AC.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/5CD44F88-6759-DF11-901C-001A92971BB2.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/5CC598A0-7E59-DF11-8203-0018F3D09642.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/5C913050-8459-DF11-8EA6-003048679162.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/5C7B58BC-5159-DF11-B779-003048678AC8.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/54256493-8659-DF11-B4C8-0018F3D09696.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/529614E7-8B59-DF11-B9DF-003048D42DC8.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/50469CBD-6159-DF11-AEE0-0026189437E8.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/4ECBC22F-8259-DF11-8F4E-002618943902.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/489D8F7E-8659-DF11-BB89-0026189438D8.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/46633EF7-8159-DF11-A43E-0026189438EA.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/4400F208-8159-DF11-A918-0026189438AE.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/42DC4260-7C59-DF11-BB61-001A928116D8.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/3C9C3B88-5159-DF11-8EA7-002618FDA277.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/3C9B03C0-5259-DF11-ACD8-0018F3D096FE.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/3C705E57-6359-DF11-81A2-0018F3D095EE.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/32735C36-5159-DF11-9018-003048679076.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/321853A5-6459-DF11-8461-00261894387C.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/30984B7E-6059-DF11-A109-003048679080.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/2AF5F46B-4F59-DF11-BE7F-001A92971BBE.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/2816D8C7-8759-DF11-90B2-002618943857.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/26A4BF9B-6859-DF11-9DC9-002618FDA28E.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/220B5AD1-7B59-DF11-9E7F-00261894394F.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/20BD2A11-7A59-DF11-855C-001A92811718.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/1C81AFF9-6559-DF11-AC50-0026189438AF.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/1A27A5DA-8659-DF11-9FE1-00261894393B.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/1282CEB4-7659-DF11-8ADF-002618943833.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/0CAFBE3B-5B59-DF11-8EC0-003048678B88.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/0CADC12F-6659-DF11-A936-002618FDA21D.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/04ADCFA2-8859-DF11-8BCB-003048678D78.root",
"/store/data/Commissioning10/MinimumBias/RECO/May6thReReco-v1/0007/000E1558-8B59-DF11-B753-00304867BFB0.root" ] );

secFiles.extend( [
               ] );
