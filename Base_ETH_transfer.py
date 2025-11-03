import streamlit as st
from web3 import Web3

# Streamlit setup
st.set_page_config(page_title="Base ETH Transfer", layout="centered")

st.title("💸 ETH Transfer - Base Network")

# Network selection
network = st.selectbox(
    "🌐 Select network",
    ["Base Mainnet", "Base Sepolia Testnet"]
)

# Network configuration
if network == "Base Mainnet":
    rpc_url = "https://mainnet.base.org"
    chain_id = 8453
    explorer_url = "https://basescan.org/tx/"
else:
    rpc_url = "https://sepolia.base.org"
    chain_id = 84532
    explorer_url = "https://sepolia.basescan.org/tx/"

# User inputs
private_key = st.text_input("🔑 Private key", type="password")
destination = st.text_input("🎯 Recipient address (0x...)")
amount_eth = st.number_input("💰 ETH amount", min_value=0.0001, value=0.01, step=0.001)
send_button = st.button("🚀 Send transaction")

# Transaction logic
if send_button:
    if not private_key.startswith("0x") or len(private_key) != 66:
        st.error("❌ Invalid private key.")
    elif not Web3.is_address(destination):
        st.error("❌ Invalid recipient address.")
    else:
        try:
            # Connect to selected network
            w3 = Web3(Web3.HTTPProvider(rpc_url))
            if not w3.is_connected():
                st.error(f"❌ Could not connect to {network}.")
            else:
                # Account & balance
                account = w3.eth.account.from_key(private_key)
                sender = account.address
                balance = w3.eth.get_balance(sender)
                balance_eth = w3.from_wei(balance, 'ether')

                st.write(f"📤 Sender address: `{sender}`")
                st.write(f"💼 Balance: `{balance_eth:.4f} ETH`")

                # Prepare transaction
                value = w3.to_wei(amount_eth, 'ether')
                gas = 21000
                gas_price = w3.eth.gas_price
                fee = gas * gas_price

                if balance < (value + fee):
                    st.error("❌ Insufficient funds to cover gas fees.")
                else:
                    tx = {
                        'nonce': w3.eth.get_transaction_count(sender),
                        'to': destination,
                        'value': value,
                        'gas': gas,
                        'gasPrice': gas_price,
                        'chainId': chain_id
                    }

                    # Sign and send transaction
                    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
                    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

                    st.success("✅ Transaction sent successfully!")
                    st.markdown(f"🔗 [View on BaseScan]({explorer_url}{tx_hash.hex()})")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
