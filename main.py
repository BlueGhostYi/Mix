"""
PyTorch Implementation of MixRec
"""

import torch
import utility.parser
import utility.data_loader
import utility.tools
import os

print('\t Step 1: General parameter setting reading...')
print('-' * 80)

args = utility.parser.parse_args()

if args.cuda:
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu_id)
device = torch.device('cuda' if torch.cuda.is_available() else "cpu")

if args.seed_flag:
    utility.tools.set_seed(args.seed)

print('\t Step 2: Select model MixRec...')
print('-' * 80)

model_list = {1: "MixRec"}

print('\t Step 3.1: Loading configuration file...')

import_str = 'from models.' + model_list[1] + " import Trainer"
config_str = './configure/' + model_list[1] + ".txt"
exec(import_str)

config = utility.tools.read_configuration(config_str, model_list[1])


print('\t Step 3.2: Loading dataset file...')

dataset = utility.data_loader.Data(config['dataset_path'] + config['dataset'], config)

print('-' * 80)
print('\t Step 3.3: Init the Recommendation Model:')

recommener = None
model_str = 'recommener = Trainer(args, config, dataset, device)'

exec(model_str)

print('\t model: ', model_list[1])

for key in config:
    print("\t " + str(key) + " : " + str(config[key]))

print('-' * 80)
print("\t Step 4: Model training and testing process:")

recommener.train()


