💸 Base ETH Transfer

A simple Streamlit web app for transferring ETH on the Base Network, supporting both Base Mainnet and Base Sepolia Testnet.
It provides a minimal, secure, and user-friendly interface to send ETH and view the transaction on BaseScan.


🚀 Features

- Choose between Base Mainnet or Base Sepolia Testnet

- Secure private key input

- Automatic gas estimation and transaction signing

- Live balance display

- Direct BaseScan transaction link after sending


🧩 Requirements

Make sure you have Python 3.9+ installed, then install dependencies:

pip install streamlit web3


▶️ Run the app

streamlit run Base_ETH_transfer.py


⚙️ Configuration

By default, the app connects to:

Base Mainnet: https://mainnet.base.org or Base Sepolia Testnet: https://sepolia.base.org

You can easily switch networks using the dropdown menu in the interface.


🔒 Security note

Your private key is never stored or transmitted — it only exists locally in your browser session.

For testing, always use a fresh test wallet on the Base Sepolia Testnet before using your main wallet.


🧠 Author

Developed with ❤️ by dnapog.base.eth for the Base Network.
