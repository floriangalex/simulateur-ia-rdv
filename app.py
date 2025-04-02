import streamlit as st

st.set_page_config(page_title="Simulateur IA - RDV Beauté", page_icon="💬")

st.title("💬 Simulateur IA - Prise de rendez-vous beauté")
st.caption("Teste ici les réponses de l’assistante virtuelle, comme si tu étais une cliente sur WhatsApp 🌸")

def get_ai_response(message):
    message = message.lower()
    if "prix" in message or "tarif" in message:
        return "Voici les prestations disponibles 🌸:\n- Pose Classique – 50€\n- Pose Mixte – 60€\n- Dépose – 20€\n- Retouche – 30€"
    elif "réserver" in message or "dispo" in message or "rdv" in message:
        return "Trop bien que tu veuilles réserver ! 💖\nJ’ai des créneaux jeudi à 14h et vendredi à 16h. Tu préfères lequel ?"
    elif "paypal" in message:
        return "Voici le lien PayPal pour l’acompte : [paypal.me/lea](https://paypal.me/lea) ✨"
    elif "carte" in message or "cb" in message or "stripe" in message:
        return "Voici le lien Stripe sécurisé : [stripe.com/pay](https://stripe.com/pay) 💳"
    elif "merci" in message or "ok" in message:
        return "Avec plaisir ma belle ! N’hésite pas si tu as d’autres questions 💅"
    else:
        return "Coucou 🌸 Tu veux réserver une prestation ou poser une question ? Je suis là pour t’aider !"

with st.form("chat_form"):
    user_message = st.text_input("Message cliente (WhatsApp simulé)", placeholder="Ex: Je veux réserver une pose mixte vendredi")
    submitted = st.form_submit_button("Envoyer")

if submitted and user_message:
    st.markdown("**Réponse IA :**")
    st.success(get_ai_response(user_message))
