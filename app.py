import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Tradutor Multilíngue", page_icon="🌍", layout="wide")

st.title("🗺️Tradutor Multilíngue🗺️")

#Área de textos
texto = st.text_area(" Digite sua frase em português:", 
                     "Olá! Estou aprendendo a programar em Python e a usar modelos de inteligência artificial.")

# Seleção de idiomas
linguas = {
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it",
    "Coreano": "kr"
}

idiomas_escolhidos = st.multiselect("Selecione os idiomas de destino:", list(linguas.keys()), ["Inglês", "Espanhol"])

#traduzir
if st.button("Traduzir"):
    if texto.strip() == "":
        st.warning("Digite uma frase para traduzir!")
    else:
        for nome in idiomas_escolhidos:
            codigo = linguas[nome]
            traducao = GoogleTranslator(source='pt', target=codigo).translate(texto)
            st.subheader(f'➡ Tradução para {nome} ({codigo})')
            st.write(f'**Original:** {texto}')
            st.write(f'**Traduzido:** {traducao}')
            st.write("---")

st.markdown(
    """
    <style>
        .card {
            background-color: #DFF6E4;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 15px;
        }
        .card h3 {
            color: #00796b;  /* Teal color for heading */
        }
        .card p {
            font-size: 1.1em;
            color: #424242;
        }
    </style>
    """, unsafe_allow_html=True
)

if texto.strip() != "":
    for nome in idiomas_escolhidos:
        codigo = linguas[nome]
        traducao = GoogleTranslator(source='pt', target=codigo).translate(texto)
        st.markdown(f'<div class="card"><h3>➡ Tradução para {nome}</h3><p><strong>Original:</strong> {texto}</p><p><strong>Traduzido:</strong> {traducao}</p></div>', unsafe_allow_html=True)



