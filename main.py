import os
import torch
import pandas as pd
from torch.utils.data import DataLoader
from args import get_args
from dataset import knee_Xray_Dataset


def main():
    # 1. We need arguments
    args = get_args()

    # 2. Iterate through the folds
    for fold in range(5):
        print('Fold: ', fold)
        train_set = pd.read_csv(os.path.join(args.csv_dir, f'fold_{fold}_train.csv'))
        val_set = pd.read_csv(os.path.join(args.csv_dir, f'fold_{fold}_val.csv'))

        # 3. Prepare datasets
        train_dataset = knee_Xray_Dataset(dataset=train_set)
        val_dataset = knee_Xray_Dataset(dataset=val_set)

        # 4. Create data loaders
        train_loader = DataLoader(dataset=train_dataset, batch_size=args.batch_size, shuffle=True) # batch_size affects model performance!
        val_loader = DataLoader(dataset=val_dataset, batch_size=args.batch_size, shuffle=False) # batch_size affects model performance!

        # 5. Initialize the model
        # train_model =

        # 6. Train the model


        # 7. Evaluate the model
        # evaluate_model



if __name__ == '__main__':
    main()