python train_MVA_Top_vs_TTG.py --mva mlp --variables varlist1 --NLayers 7 --LearningRate 0.03 --Sampling 0.3 --SamplingEpoch 0.8

python train_MVA_Top_vs_TTG.py --mva bdt --variables varlist1 --NTrees 100 --maxdepth 3 --ncuts 50



python train_MVA_Top_vs_TTG.py –plotname MVA_selection1 --variables selection1 --NTrees 100 --maxdepth 3 --ncuts 50 --NLayers 7

python train_MVA_Top_vs_TTG.py –plotname MVA_selection2 --variables selection2 --NTrees 100 --maxdepth 3 --ncuts 50 --NLayers 7

python train_MVA_Top_vs_TTG.py –plotname MVA_selection3 --variables selection3 --NTrees 100 --maxdepth 3 --ncuts 50 --NLayers 7



python train_MVA_Top_vs_TTG.py –plotname MVA_selection1 --variables selection1 --NTrees 800 --maxdepth 3 --ncuts 20 --NLayers 7