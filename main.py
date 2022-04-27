from web3.auto import w3
import pandas as pd
import time
import os


def create_wallet(count):
    wallet_list = []
    for _ in range(0, count):
        wallet = w3.eth.account.create()
        wallet_list.append({
            'Address':wallet.address,
            'PrivateKey':wallet.privateKey.hex()
        })
    print(f'\nSuccesfully generated {count} wallets\n')
    df = pd.DataFrame(data=wallet_list)
    df.index += 1
    return df


if __name__ == '__main__':
    print(f'Made by @freakcollections\n')
    time.sleep(1)

    while True:
        try:
            count = int(input(f'Input the required number of wallets:\n'))
            break
        except:
            print(f'ERROR | Input an integer value!\n')

    df = create_wallet(count)

    cur_dir = f'{os.getcwd()}\wallets.xlsx'
    if os.path.exists(cur_dir):
        with pd.ExcelWriter('wallets.xlsx', mode='a', if_sheet_exists='overlay') as writer:  
            start_row = writer.sheets['Wallets'].max_row
            df.index += start_row - 1
            df.to_excel(writer, sheet_name='Wallets', startrow=start_row, header=False)
    else:
        df.to_excel('wallets.xlsx', sheet_name='Wallets')

    print(f'Added {count} rows to {cur_dir}')