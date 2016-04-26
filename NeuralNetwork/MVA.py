"""
###############################################
MVA implementation with Neural Networks
                       by Mauro Dinardo
###############################################
Before running double-check:
  - number of perceptrons & neurons
  - learn rate
  - regulator
  - scramble
To-do:
  - mini-batch learning
  - porting in pyCUDA
###############################################
e.g.: python MVA.py -nv 2 -np 6 -nn 2 3 4 3 2 1
###############################################
"""
from argparse  import ArgumentParser
from random    import seed, random, gauss

from ROOT      import gROOT, gStyle, TCanvas, TGraph, TH1D, TGaxis, TLegend

from NeuralNet import NeuralNet


def ArgParser():
    """
    ###############
    Argument parser
    ###############
    """
    parser = ArgumentParser()
    parser.add_argument("-nv", "--Nvars",        dest = "Nvars",        type = int,  help = "Number of variables",              required=True)
    parser.add_argument("-np", "--Nperceptrons", dest = "Nperceptrons", type = int,  help = "Number of perceptrons",            required=True)
    parser.add_argument("-nn", "--Nneurons",     dest = "Nneurons",     type = int,  help = "Number of neurons per perceptron", required=True,  nargs='*')
    parser.add_argument("-sc", "--Scramble",     dest = "doScramble",   type = bool, help = "Perform NN scrambling",            required=False, default=False)

    options = parser.parse_args()

    print ""
    if options.Nvars:
        print "--> I'm reading the variable number: ", options.Nvars

    if options.Nperceptrons:
        print "--> I'm reading the perceptron number: ", options.Nperceptrons

    if options.Nneurons:
        print "--> I'm reading the neuron number per perceptron: ", options.Nneurons

    if options.doScramble:
        print "--> I'm reading the option scramble: ", options.doScramble

    return options


def SetStyle():
    """
    ###################
    ROOT style settings
    ###################
    """
    gROOT.SetStyle("Plain")
    gROOT.ForceStyle()
    gStyle.SetTextFont(42)
    
    gStyle.SetOptTitle(0)
    gStyle.SetOptFit(0)
    gStyle.SetOptStat(1111)
    
    gStyle.SetPadRightMargin(0.08)
    gStyle.SetPadTopMargin(0.11)
    gStyle.SetPadBottomMargin(0.12)
    
    gStyle.SetTitleFont(42,"x")
    gStyle.SetTitleFont(42,"y")
    gStyle.SetTitleFont(42,"z")
    
    gStyle.SetTitleOffset(1.05,"x")
    gStyle.SetTitleOffset(0.95,"y")
    
    gStyle.SetTitleSize(0.05,"x")
    gStyle.SetTitleSize(0.05,"y")
    gStyle.SetTitleSize(0.05,"z")
    
    gStyle.SetLabelFont(42,"x")
    gStyle.SetLabelFont(42,"y")
    gStyle.SetLabelFont(42,"z")
    
    gStyle.SetLabelSize(0.05,"x")
    gStyle.SetLabelSize(0.05,"y")
    gStyle.SetLabelSize(0.05,"z")
    
    TGaxis.SetMaxDigits(3)
    gStyle.SetStatY(0.9)


    

"""
############
Main program
############
"""
cmd = ArgParser()


"""
##########################
Neural net: initialization
##########################
"""
seed(0)
NN = NeuralNet(cmd.Nvars,cmd.Nperceptrons,cmd.Nneurons)
NN.printParams()


"""
###################
Internal parameters
###################
"""
seed(0)
nRuns     = 100000
scrStart  =   1000
scrLen    =   1000
saveEvery =    100
xRange    = 3.
xOffset   = 0.
yRange    = 3.
yOffset   = 0.
noiseBand = 0.1
loR       = 0.5
hiR       = 0.
NNoutMin  = NN.outputMin(cmd.Nperceptrons-1)
NNoutMax  = NN.outputMax(cmd.Nperceptrons-1)
NNthr     = (NNoutMin+NNoutMax) / 2.
#xyCorr    = lambda x,y: ((x-xOffset)*(x-xOffset)+(y-yOffset)*(y-yOffset))
xyCorr    = lambda x,y: (6*(x-xOffset)*(x-xOffset)*(x-xOffset) - (y-yOffset))


"""
#########################
Graphics layout and plots
#########################
"""
gROOT.Reset()
SetStyle()

cCost  = TCanvas('cCost',  'NN Cost Function', 0, 0, 700, 500)
cAccu  = TCanvas('cAccu',  'NN Accuracy',      0, 0, 700, 500)
cNNin  = TCanvas('cNNin',  'NN Input',         0, 0, 700, 500)
cNNout = TCanvas('cNNout', 'NN Output',        0, 0, 700, 500)
cNNval = TCanvas('cNNval', 'NN Values',        0, 0, 700, 500)
cDeriv = TCanvas('cDeriv', 'NN Derivatives',   0, 0, 700, 500)
cDelta = TCanvas('cDelta', 'NN Deltas',        0, 0, 700, 500)

graphNNcost = TGraph()
graphNNcost.SetTitle('NN cost function;Epoch [#];Cost Function')

graphNNaccuracy = TGraph()
graphNNaccuracy.SetTitle('NN accuracy;Epoch [#];Accuracy [%]')

graphSin = TGraph()
graphSin.SetTitle('NN input;x;y')
graphSin.SetMarkerStyle(20)
graphSin.SetMarkerSize(0.5)
graphSin.SetMarkerColor(4)

graphBin = TGraph()
graphBin.SetTitle('NN input;x;y')
graphBin.SetMarkerStyle(20)
graphBin.SetMarkerSize(0.5)
graphBin.SetMarkerColor(2)

graphSout = TGraph()
graphSout.SetTitle('NN output;x;y')
graphSout.SetMarkerStyle(20)
graphSout.SetMarkerSize(0.5)
graphSout.SetMarkerColor(4)

graphBout = TGraph()
graphBout.SetTitle('NN output;x;y')
graphBout.SetMarkerStyle(20)
graphBout.SetMarkerSize(0.5)
graphBout.SetMarkerColor(2)

graphNNerr = TGraph()
graphNNerr.SetTitle('NN output;x;y')
graphNNerr.SetMarkerStyle(20)
graphNNerr.SetMarkerSize(0.5)
graphNNerr.SetMarkerColor(3)

histoNNS = TH1D('histoNNS','histoNNS',100,NNoutMin,NNoutMax)
histoNNS.SetTitle('NN signal output;NN output;Entries [#]')
histoNNS.SetLineColor(4)

histoNNB = TH1D('histoNNB','histoNNB',100,NNoutMin,NNoutMax)
histoNNB.SetTitle('NN background output;NN output;Entries [#]')
histoNNB.SetLineColor(2)

histoNNE = TH1D('histoNNE','histoNNE',100,NNoutMin,NNoutMax)
histoNNE.SetTitle('NN error output;NN output;Entries [#]')
histoNNE.SetLineColor(3)

legNNderiv = TLegend(0.88, 0.17, 1.0, 1.0, "")
legNNderiv.SetTextSize(0.03)
legNNderiv.SetFillStyle(1001)

legNNdelta = TLegend(0.88, 0.17, 1.0, 1.0, "")
legNNdelta.SetTextSize(0.03)
legNNdelta.SetFillStyle(1001)

graphNNderiv = []
graphNNdelta = []


"""
####################
Neural net: training
####################
"""
print "\n=== Training neural netowrk ==="
NNcost = 0.
count  = 0.
for n in xrange(nRuns):
    """
    ####################
    Neural net: training
    ####################
    """
    x = random() * xRange + xOffset - xRange/2
    y = random() * yRange + yOffset - yRange/2

#    if gauss(loR,noiseBand) <= xyCorr(x,y) < gauss(hiR,noiseBand):
    if xyCorr(x,y) > hiR:
        target = NNoutMax
        if n % saveEvery == 0:
            graphSin.SetPoint(n/saveEvery,x,y)
    else:
        target = NNoutMin
        if n % saveEvery == 0:
            graphBin.SetPoint(n/saveEvery,x,y)


    """
    ######################
    Neural net: scrambling
    ######################
    """
    indx = (n-scrStart)/scrLen-1
    if cmd.doScramble and n > scrStart and (n-scrStart) % scrLen == 0 and indx < cmd.Nperceptrons:
        indx = cmd.Nperceptrons - 1 - indx
        print "=== Scrambling perceptron [", indx, "] ==="
        NN.scramble({indx:[-1]})


    NNcost += NN.learn([x,y],[target])
    
    
    if n % saveEvery == 0:
        graphNNcost.SetPoint(n/saveEvery,n,NNcost/saveEvery)
        NNcost = 0.

        
        """
        #################################################
        Neural net: saving activation function derivative
        #################################################
        """
        k = 0
        for j,P in enumerate(NN.FFperceptrons):
            for i,N in enumerate(P.neurons):
                if n == 0:
                    graphNNderiv.append(TGraph())
                    leg = "P:" + str(j) +  "; N:" + str(i)
                    legNNderiv.AddEntry(graphNNderiv[k],leg,"L");
                graphNNderiv[k].SetPoint(n/saveEvery,n,N.dafundz)
                k += 1

                
        """
        #################################
        Neural net: saving delta function
        #################################
        """
        k = 0
        for j,P in enumerate(NN.BPperceptrons):
            for i,N in enumerate(P.neurons):
                if n == 0:
                    graphNNdelta.append(TGraph())
                    leg = "P:" + str(j) +  "; N:" + str(i)
                    legNNdelta.AddEntry(graphNNdelta[k],leg,"L");
                graphNNdelta[k].SetPoint(n/saveEvery,n,N.afun)
                k += 1


    """
    ################
    Neural net: test
    ################
    """
    x = random() * xRange + xOffset - xRange/2
    y = random() * yRange + yOffset - yRange/2

    
    NNout = NN.eval([x,y])
     

#    if ((NNout[0] > NNthr and loR <= xyCorr(x,y) < hiR) or (NNout[0] <= NNthr and (xyCorr(x,y) < loR or hiR <= xyCorr(x,y)))):
    if ((NNout[0] > NNthr and xyCorr(x,y) > hiR) or (NNout[0] <= NNthr and xyCorr(x,y) <= hiR)):
        count += 1
    else:
        count -= 1

    if n % saveEvery == 0:
        graphNNaccuracy.SetPoint(n/saveEvery,n,count / saveEvery * 100)
        count = 0.
NN.printParams()
NN.save("NeuralNet.txt")


"""
################
Neural net: test
################
"""
print "\n=== Testing neural netowrk ==="
for n in xrange(nRuns/saveEvery):
    x = random() * xRange + xOffset - xRange/2
    y = random() * yRange + yOffset - yRange/2

    
    NNout = NN.eval([x,y])
     

#    if (NNout[0] > NNthr and loR <= xyCorr(x,y) < hiR):
    if (NNout[0] > NNthr and xyCorr(x,y) > hiR):
        graphSout.SetPoint(n,x,y)
        histoNNS.Fill(NNout[0])
#    elif (NNout[0] <= NNthr and (xyCorr(x,y) < loR or hiR <= xyCorr(x,y))):
    elif (NNout[0] <= NNthr and xyCorr(x,y) <= hiR):
        graphBout.SetPoint(n,x,y)
        histoNNB.Fill(NNout[0])
    else:
        graphNNerr.SetPoint(n,x,y)
        histoNNE.Fill(NNout[0])


"""
#########################
Neural net: control plots
#########################
"""
cCost.cd()
graphNNcost.Draw('AL')
cCost.Modified()
cCost.Update()

cAccu.cd()
cAccu.SetGrid()
graphNNaccuracy.Draw('AL')
cAccu.Modified()
cAccu.Update()

cNNin.cd()
cNNin.DrawFrame(xOffset - xRange/2 - xRange/20,yOffset - yRange/2 - xRange/20,xOffset + xRange/2 + xRange/20,yOffset + yRange/2 + xRange/20)
graphSin.Draw('P')
graphBin.Draw('P same')
cNNin.Modified()
cNNin.Update()

cNNout.cd()
cNNout.DrawFrame(xOffset - xRange/2 - xRange/20,yOffset - yRange/2 - xRange/20,xOffset + xRange/2 + xRange/20,yOffset + yRange/2 + xRange/20)
graphSout.Draw('P')
graphBout.Draw('P same')
graphNNerr.Draw('P same')
cNNout.Modified()
cNNout.Update()

cNNval.cd()
histoNNS.Draw()
histoNNB.Draw('sames')
histoNNE.Draw('sames')
cNNval.Modified()
cNNval.Update()

cDeriv.cd()
graphNNderiv[0].Draw('AL')
graphNNderiv[0].SetTitle('NN activation function derivative;Epoch [#];Activation Function Derivative')
graphNNderiv[0].SetLineColor(1)
for k in xrange(1,len(graphNNderiv[:])):
    graphNNderiv[k].SetLineColor(k+1)
    graphNNderiv[k].Draw('L same')
legNNderiv.Draw("same")
cDeriv.Modified()
cDeriv.Update()

cDelta.cd()
graphNNdelta[0].Draw('AL')
graphNNdelta[0].SetTitle('NN delta function;Epoch [#];Delta Function')
graphNNdelta[0].SetLineColor(1)
for k in xrange(1,len(graphNNdelta[:])):
    graphNNdelta[k].SetLineColor(k+1)
    graphNNdelta[k].Draw('L same')
legNNdelta.Draw("same")
cDelta.Modified()
cDelta.Update()


"""
########################
Wait for keyborad stroke
########################
"""
raw_input("\n---press enter---")
