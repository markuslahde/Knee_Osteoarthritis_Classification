import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Knee OA Classification')
    parser.add_argument('--backbone', type=str, choices=['resnet18', 'se_resnet50'],
                                                                default='resnet18')
    
    parser.add_argument('--out', '--out_dir', type=str, default='session')
    parser.add_argument('csv', '--csv_dir', default='data/CSVs')

    parser.add_argument('bs', '--batch_size', default=16, type=int, choices=[16, 32, 64])
    
    args = parser.parse_args()

    return args
