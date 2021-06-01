import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Get arguments for active learning.")

    parser.add_argument('--method', '-m', type=str, default="random", choices=['coreset'],
                        required=True, help="active learning query strategy")
    parser.add_argument('--init_num', type=int, default=1000, required=True, help="init label number")
    parser.add_argument('--query_num', type=int, default=1000, required=True, help="query budget for each cycle")
    parser.add_argument('--cycle_num', type=int, default=10, required=True, help="query cycle number")
    parser.add_argument('--epoch_num', type=int, default=200, required=True, help="training epochs per cycle")
    parser.add_argument('--dataset', type=str, default="CIFAR10", required=True, help='dataset for training',
                        choices=["CIFAR10", "MNIST", "CIFAR100", "FashionMNIST", "SVHN"])
    parser.add_argument('--save', '-s', type=bool, default=True, required=True, help='save datasets and task models')
    parser.add_argument('--task_model_type', type=str, default="pytorch", choices=["tensorflow", "pytorch"])
    args = parser.parse_args()

    return args