import argparse
from simulator import generate_user_data
from db import insert_data

def main():
    # Pass arguments from CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--num_users", type=int, required=True)
    parser.add_argument("--p_A", type=float, required=True)
    parser.add_argument("--p_B", type=float, required=True)

    args = parser.parse_args()

    # Assign CLI inputs to variables
    experiment_name = args.name
    num_users = args.num_users
    p_A = args.p_A
    p_B = args.p_B

    # Generate and insert data into database
    data = generate_user_data(num_users, p_A, p_B)
    insert_data(experiment_name, data)

main()
