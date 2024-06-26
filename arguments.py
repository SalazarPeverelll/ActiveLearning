import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Get arguments for active learning.")

    parser.add_argument('--method', '-m', type=str, choices=['random', 'LeastConfidence', 'coreset', "LL4AL"],
                        help="active learning query strategy")
    parser.add_argument('--init_num', type=int, default=1000, help="init label number")
    parser.add_argument('--query_num', type=int, default=1000, help="query budget for each cycle")
    parser.add_argument('--cycle_num', type=int, default=10, help="query cycle number")
    parser.add_argument('--epoch_num', type=int, default=200, help="training epochs per cycle")
    parser.add_argument('--dataset', type=str, default="CIFAR10", help='dataset for training',
                        choices=["CIFAR10", "MNIST", "CIFAR100", "FashionMNIST", "SVHN"])
    parser.add_argument('--save', '-s', type=bool, default=True, help='save datasets and task models')
    parser.add_argument('--task_model_type', type=str, default="pytorch", choices=["tensorflow", "pytorch"])
    parser.add_argument("--gpu",'-g', default="0", choices=[None, "0", "1", "2", "3"])
    parser.add_argument("--resume", '-r', type=int, default=1, help="resume from checkpoints")
    parser.add_argument("--resume_path", default="/home/yifan/projects/phD/datasets/AL_dataset/Model/Epoch_1", type=str, help="path to where ckpt is saved")
    args = parser.parse_args()

    return args