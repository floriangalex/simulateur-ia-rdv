{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
\
st.set_page_config(page_title="Simulateur IA - RDV Beaut\'e9", page_icon="\uc0\u55357 \u56492 ")\
\
st.title("\uc0\u55357 \u56492  Simulateur IA - Prise de rendez-vous beaut\'e9")\
st.caption("Teste ici les r\'e9ponses de l\'92assistante virtuelle, comme si tu \'e9tais une cliente sur WhatsApp \uc0\u55356 \u57144 ")\
\
def get_ai_response(message):\
    message = message.lower()\
    if "prix" in message or "tarif" in message:\
        return "Voici les prestations disponibles \uc0\u55356 \u57144 :\\n- Pose Classique \'96 50\'80\\n- Pose Mixte \'96 60\'80\\n- D\'e9pose \'96 20\'80\\n- Retouche \'96 30\'80"\
    elif "r\'e9server" in message or "dispo" in message or "rdv" in message:\
        return "Trop bien que tu veuilles r\'e9server ! \uc0\u55357 \u56470 \\nJ\'92ai des cr\'e9neaux jeudi \'e0 14h et vendredi \'e0 16h. Tu pr\'e9f\'e8res lequel ?"\
    elif "paypal" in message:\
        return "Voici le lien PayPal pour l\'92acompte : [paypal.me/lea](https://paypal.me/lea) \uc0\u10024 "\
    elif "carte" in message or "cb" in message or "stripe" in message:\
        return "Voici le lien Stripe s\'e9curis\'e9 : [stripe.com/pay](https://stripe.com/pay) \uc0\u55357 \u56499 "\
    elif "merci" in message or "ok" in message:\
        return "Avec plaisir ma belle ! N\'92h\'e9site pas si tu as d\'92autres questions \uc0\u55357 \u56453 "\
    else:\
        return "Coucou \uc0\u55356 \u57144  Tu veux r\'e9server une prestation ou poser une question ? Je suis l\'e0 pour t\'92aider !"\
\
with st.form("chat_form"):\
    user_message = st.text_input("Message cliente (WhatsApp simul\'e9)", placeholder="Ex: Je veux r\'e9server une pose mixte vendredi")\
    submitted = st.form_submit_button("Envoyer")\
\
if submitted and user_message:\
    st.markdown("**R\'e9ponse IA :**")\
    st.success(get_ai_response(user_message))\
}