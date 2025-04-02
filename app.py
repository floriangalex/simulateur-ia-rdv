import streamlit as st
import openai

# Configuration de la clé API depuis les secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Simulateur IA - RDV Beauté", page_icon="💬")
st.title("💬 Simulateur IA - Prise de rendez-vous beauté")
st.caption("Teste ici les réponses de l’assistante virtuelle, comme si tu étais une cliente sur WhatsApp 🌸")

def get_ai_response(message):
    system_prompt = (
        "Tu es l’assistante virtuelle de Léa, une prestataire beauté. "
        "Tu réponds à ses clientes sur WhatsApp. "
        "Tu es douce, naturelle, rassurante et très professionnelle. "
        "Voici les prestations disponibles : "
        "- Pose Classique (50€, acompte 10€) "
        "- Pose Mixte (60€, acompte 10€) "
        "- Dépose (20€, acompte 5€) "
        "- Retouche (30€, acompte 5€) "
        "Elle est dispo jeudi à 14h ou vendredi à 16h. "
        "Propose toujours des réponses utiles, bienveillantes et simples. "
        "Ne dis jamais que tu es une IA."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        temperature=0.7,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

# UI
with st.form("chat_form"):
    user_message = st.text_input("Message cliente (WhatsApp simulé)", placeholder="Ex: Je veux réserver une pose mixte vendredi")
    submitted = st.form_submit_button("Envoyer")

if submitted and user_message:
    st.markdown("**Réponse IA :**")
    with st.spinner("L'assistante répond..."):
        st.success(get_ai_response(user_message))
