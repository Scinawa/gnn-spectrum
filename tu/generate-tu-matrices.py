import sys
import numpy as np
# from tqdm import tqdm
#import torch
#import torch.nn as nn

#from torch.utils.tensorboard import SummaryWriter

import dgl
from dgl.data import LegacyTUDataset
from tu_dataloader import TUDataLoader
from tqdm import tqdm
import sys
sys.path.append('..')
from model import Net
from utils.config import process_config, get_args
from utils.basis_transform import basis_transform
from utils.config import get_config_from_json

import networkx as nx
import pickle




def generate_skew(config):


    dataset = LegacyTUDataset(config.dataset_name, raw_dir='./dataset')

    # config = get_config_from_json("./configs/" + config.dataset_name + ".json")
    basis = config.basis
    epsilon = config.epsilon
    power = config.power
    identity = config.get('identity', 1)

    megadataset= []

    for i in tqdm(range(len(dataset)), desc="Generating matrices from dgl data structures"):
    #for i in range(len(dataset)):
        g = dataset.graph_lists[i]
        g = dgl.remove_self_loop(g)
        g = dgl.add_self_loop(g)
        dataset.graph_lists[i] = basis_transform(g, basis=basis, epsilon=epsilon, power=power, identity=identity)
        #from IPython import embed
        #embed() 
        megadataset.append(nx.to_numpy_matrix(dataset[i][0].to_networkx()))

    with open('./tu-dataset.pikle', 'wb') as handle:
        pickle.dump(megadataset, handle, protocol=pickle.HIGHEST_PROTOCOL)  
        print("Pickled numpy version of dataset")  



def main():
    args = get_args()
    config = process_config(args)
    print(config)



    for seed in config.seeds:
        config.seed = seed
        generate_skew(config)
    #     config.time_stamp = int(time.time())
    #     print(config)
    #     run_model(config)
    #     print("exited run model")
    # print("finished for seed in config")

if __name__ == "__main__":
    main()
