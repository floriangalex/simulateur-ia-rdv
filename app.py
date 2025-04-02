import streamlit as st
from openai import OpenAI

# Configuration de la clé via les secrets Streamlit
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Configuration de la page
st.set_page_config(page_title="Simulateur IA - RDV Beauté", page_icon="💬")
st.title("💬 Simulateur IA - Prise de rendez-vous beauté")
st.caption("Teste ici les réponses de l’assistante virtuelle, comme si tu étais une cliente sur WhatsApp 🌸")

# Fonction IA (GPT)
def get_ai_response(message):
    system_prompt = (
        "Tu es l’assistante virtuelle de Léa, une prestataire beauté spécialisée dans les poses de cils. "
        "Tu réponds à ses clientes sur WhatsApp. "
        "Tu es douce, chaleureuse, rassurante, et tu t’exprimes toujours comme une vraie personne. "
        "Voici les prestations proposées :\n"
        "- Pose Classique (50€, acompte 10€)\n"
        "- Pose Mixte (60€, acompte 10€)\n"
        "- Dépose (20€, acompte 5€)\n"
        "- Retouche (30€, acompte 5€)\n"
        "Elle est disponible jeudi à 14h ou vendredi à 16h. "
        "Si la cliente veut réserver, propose un créneau et explique le système d’acompte. "
        "N'envoie le lien de paiement que si elle dit 'carte' ou 'paypal'. "
        "Ne dis jamais que tu es une IA."
    )

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

# Interface utilisateur (formulaire)
with st.form("chat_form"):
    user_message = st.text_input(
        "Message cliente (WhatsApp simulé)", 
        placeholder="Ex: Je veux réserver une pose mixte vendredi"
    )
    submitted = st.form_submit_button("Envoyer")

# Réponse IA affichée
if submitted and user_message:
    st.markdown("**Réponse IA :**")
    with st.spinner("L'assistante répond..."):
        try:
            st.success(get_ai_response(user_message))
        except Exception as e:
            st.error(f"Erreur : {str(e)}")
