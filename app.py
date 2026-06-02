import streamlit as st
import requests

st.set_page_config(page_title="Sindaca Generator 🏛️", page_icon="🏛️")

st.title("🏛️ Generatore di post per Facebook")
st.subheader("Comune di Montefiascone - Ufficio Sindaca e Assessori vari ed eventuali")
st.markdown(
    "_Perché scrivere un post quando puoi generarne uno con il giusto peso istituzionale, "
    "la giusta dose di pathos civico e un numero adeguato di ringraziamenti?_"
)
st.divider()

evento = st.text_input("📅 Qual è l'evento o la festività di oggi?", placeholder="es. Festa della Repubblica, inaugurazione del parco...")
presenti = st.text_input("🤝 Chi era presente? (Chi dobbiamo ringraziare?)", placeholder="es. Il Prefetto, l'Associazione Proloco, i ragazzi delle scuole...")
dettaglio = st.text_input("✨ C'è un dettaglio specifico da citare?", placeholder="es. È stata piantata una quercia, è stato consegnato un premio...")

st.divider()

if st.button("✍️ Genera Post Istituzionale", use_container_width=True, type="primary"):
    if not evento:
        st.warning("Inserisci almeno l'evento per procedere!")
    else:
        with st.spinner("Elaborazione del pathos civico in corso..."):
            prompt = f"""Agisci come un generatore di post per Facebook per Giulia De Santis, la Sindaca di Montefiascone. Il tuo obiettivo è scrivere post pubblici altamente retorici, emotivi, istituzionali e focalizzati sul senso di comunità.
Regole di stile: Usa parole che evocano forti sentimenti civici; usa metafore classiche sulla cura e la crescita ('la democrazia è una pianta da curare'); usa un tono materno verso i giovani anche se non è madre, è single e ha meno di 40 anni ma di aprime come una boomer; dedica una parte enorme del post a ringraziare ossessivamente ogni istituzione, associazione o figura coinvolta.
Struttura: 1. Apertura ad effetto. 2. Il cuore dell'evento descritto in modo profondo. 3. Una lezione di vita/morale sul senso civico. 4. Una lista estesa e puntuale di ringraziamenti. 5. Chiusura ad effetto con un incoraggiamento per la città.

Evento: {evento}
Presenti e da ringraziare: {presenti if presenti else 'non specificato'}
Dettaglio specifico: {dettaglio if dettaglio else 'nessuno'}"""

            api_key = st.secrets["GEMINI_API_KEY"]
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
            payload = {"contents": [{"parts": [{"text": prompt}]}]}
            response = requests.post(url, json=payload, timeout=30)
            result = response.json()

            if response.status_code != 200:
                st.error(f"Errore API: {result}")
            else:
                post = result["candidates"][0]["content"]["parts"][0]["text"]
                st.success("Post generato con successo!")
                st.markdown("### 📋 Il tuo post istituzionale:")
                st.markdown(post)
                st.code(post, language=None)
                st.caption("Copia il testo qui sopra e incollalo su Facebook. Buona pubblicazione, Sindaca! 🏛️")
