import argparse
from simulator import generate_user_data
from db import insert_experiment

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
parser.add_argument("--num_users", type=int, required=True)
parser.add_argument("--p_A", type=float, required=True)
parser.add_argument("--p_B", type=float, required=True)

args = parser.parse_args()

data = generate_user_data(args.num_users, args.p_A, args.p_B)
insert_experiment(args.name, data)
