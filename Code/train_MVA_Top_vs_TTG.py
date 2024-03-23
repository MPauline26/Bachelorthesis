#!/usr/bin/env python

import os

# Analysis
from Analysis.TMVA.Trainer	 import Trainer
from Analysis.TMVA.Reader        import Reader
from Analysis.TMVA.defaults	 import default_methods, default_factory_settings

import Analysis.Tools.syncer

from RootTools.plot.helpers    import copyIndexPHP

# TTGammaEFT
from TTGammaEFT.Tools.user           import plot_directory, mva_directory
from TTGammaEFT.Tools.cutInterpreter import cutInterpreter

# MVA configuration
from TTGammaEFT.MVA.MVA_Top_vs_TTG import mlp, bdt, sequence, read_variables, mva_variables

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--plot_directory',     action='store',             default=None)
argParser.add_argument('--selection',          action='store', type=str,   default='nLepTight1-nLepVeto1-nJet3p-nBTag1p-nPhoton1')
argParser.add_argument('--trainingFraction',   action='store', type=float, default=0.5)
argParser.add_argument('--small',              action='store_true')
argParser.add_argument('--overwrite',          action='store_true')

argParser.add_argument('--variables',          action='store', type=str,   default='orig')
argParser.add_argument('--NTrees',             action='store', type=float, default=250)
argParser.add_argument('--maxdepth',           action='store', type=float, default=1)
argParser.add_argument('--ncuts',              action='store', type=float, default=50)
argParser.add_argument('--NLayers',            action='store', type=float, default=7)
argParser.add_argument('--plotname',            action='store', type=str, default='MVA')





args = argParser.parse_args()

#Logger
import Analysis.Tools.logger as logger
logger = logger.get_logger("INFO", logFile = None )

if args.plot_directory == None:
    args.plot_directory = plot_directory

if args.variables:
   plot_directory = os.path.join( plot_directory, str(args.variables) )

if args.selection == None:
    selectionString = "(1)"
else:
    selectionString = cutInterpreter.cutString( args.selection )

# Samples
from TTGammaEFT.Samples.nanoTuples_RunII_postProcessed import TTG, Top

signal = TTG_incl

# TTZ
backgrounds = [ Top ]

samples = backgrounds + [signal]
for sample in samples:
    sample.setSelectionString( selectionString )
    if args.small:
        sample.reduceFiles(to = 1)

mvas = [ bdt, mlp]

## TMVA Trainer instance
trainer = Trainer(
    signal = signal,
    backgrounds = backgrounds,
    output_directory = mva_directory,
    plot_directory   = plot_directory,
    mva_variables    = mva_variables,
    label            = str(plotname),   /* umschreiben, damit variabel */
    fractionTraining = args.trainingFraction,
    )

weightString = "(1)"
trainer.createTestAndTrainingSample(
    read_variables   = read_variables,
    sequence         = sequence,
    weightString     = weightString,
    overwrite        = args.overwrite,
    )

for mva in mvas:
    trainer.addMethod(method = mva)

trainer.trainMVA( factory_settings = default_factory_settings )
trainer.plotEvaluation()
copyIndexPHP(plot_directory)