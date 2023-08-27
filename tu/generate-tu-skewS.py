import sys
import numpy as np

from tqdm import tqdm
import sys
sys.path.append('..')
#from model import Net
from utils.config import process_config, get_args
from utils.basis_transform import basis_transform
from utils.config import get_config_from_json
import random
import time
import pickle

# from IPython import embed; embed()


sys.path.append('/Users/scinawa/workspace/grouptheoretical/new-experiments/multi-orbit-bispectrum')
from spectrum_utils import * 
from utils import *





def generate_skew():

    skew_spectrums = {}


    with open("./tu-dataset.pikle", 'rb') as f:
        graphs = pickle.load(f)



    for i in tqdm(range(len(graphs)), desc="Generating skew spectrums"):
        
        for k in range(2,6):
            new_kcor1orb = []
            new_kcor2orb = []
            print("Creating {}-th correlation".format(k))
            for i in range(len(graphs)):
                #import Ipython
                #ipython.embed()
                import pdb
                pdb.set_trace()
                func_1o = create_func_on_group_from_matrix_1orbit(graphs[i])
                func_2o = create_func_on_group_from_matrix_2orbits(np.array(graphs[i]))

                new_kcor1orb.append(reduced_k_correlation(func_1o, k=k, method="extremedyn", vector=False))     
                new_kcor2orb.append(reduced_k_correlation(func_2o, k=k, method="extremedyn", vector=False))

            skew_spectrums["1orbit-{}-corre-dict".format(k)] = new_kcor1orb
            skew_spectrums["2orbit-{}-corre-dict".format(k)] = new_kcor2orb





    ############ USE WITH CARE!!!!!! IT WILL OVERWRITE THE PERVIOUSLY COMPUTED FEATURES FILE
    with open('megadump-all-features.pickle', 'wb') as handle:
        pickle.dump(megadataset, handle, protocol=pickle.HIGHEST_PROTOCOL)    



# def main():
#     args = get_args()
#     config = process_config(args)
#     print(config)



#     for seed in config.seeds:
#         config.seed = seed
#         generate_skew(config)
#     #     config.time_stamp = int(time.time())
#     #     print(config)
#     #     run_model(config)
#     #     print("exited run model")
#     # print("finished for seed in config")

if __name__ == "__main__":
    print("generating the skew-spectra from matrices")
    generate_skew()
