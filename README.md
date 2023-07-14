# PIPPack
Implementation of Protein Invariant Point Packer (PIPPack)

## Getting started
To build the environment from scratch:
```
# Create and activate the pippack environment
conda create -n pippack
conda activate pippack

# Install PyTorch (see https://pytorch.org/get-started/locally/)
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# Install Lightning (see https://lightning.ai/docs/pytorch/stable/starter/installation.html)
conda install lightning=2.0.1 -c conda-forge

# Pip installs:
#  - PyTorch Geometric (see https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html) 
#  - BioPython (see https://biopython.org/wiki/Download)
#  - Hydra (see https://hydra.cc/docs/intro/#installation)
python -m pip install torch-geometric biopython hydra-core -U
```

Alternatively, you can use the environment file `env/pippack_env.yaml` to build the environment:
```
# Build pippack environment from yaml file
conda env create -f env/pippack_env.yaml
```