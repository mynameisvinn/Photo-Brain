mkdir -p ~/.streamlit/
echo "[general]
email = "vin.tang@gmail.com"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml