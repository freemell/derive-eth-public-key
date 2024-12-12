from web3 import Web3

# well, this is where I Connected to an Ethereum node. i used infura
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/use yours'))


def check_address(address):
    try:
        
        checksum_address = w3.toChecksumAddress(address)
        
        
        balance = w3.eth.get_balance(checksum_address)
        
      
        if balance is not None:
            print(f"Address {checksum_address} exists on the Ethereum network.")
        else:
            print(f"Address {checksum_address} does not exist on the Ethereum network.")
    
    except Exception as e:
        print(f"Error checking address {address}: {e}")


generated_addresses = [
    "0x691ee59cf0882625001956e82532f5ffca0282f5",
    "0x86b0f4ead1d91ff74ec801d574449e910ccc5f39",
    "0x90aae089cf62f29b2fb3191411038cbf653a8fdb",
    "0x7d701741e9fd6e76e879ee6521e958a1d23856b5",
    "0xbe98976ca32e1afe9d3dc15d6bdaf8e8bb86e60e",
    "0x425e65e3a544251e2d41d6faedf8f2340ae3f89e",
    "0xa8dbc60a768d60d7130a3041698c566c0e34168b",
    "0x87f24895ce04a7ff1c14c0bed88bfd38f9d66b1d",
    "0x81d3e130f6d1ab15689569d09853b2286e7ef398",
    "0x73b5588b3f61e70f110d375bf23863818eed6f4f",
    # You can add more addresses under
]


for address in generated_addresses:
    check_address(address)
