import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sindaca Generator 🏛️", page_icon="🏛️")

st.title("🏛️ Generatore di Post Istituzionali")
st.subheader("della Sindaca di Montefiascone")
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
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            model = genai.GenerativeModel("gemini-1.5-flash")

            prompt = f"""Agisci come un generatore di post per Facebook per Giulia De Santis, la Sindaca di Montefiascone. Il tuo obiettivo è scrivere post pubblici altamente retorici, emotivi, istituzionali e focalizzati sul senso di comunità.
Regole di stile: Usa parole che evocano forti sentimenti civici; usa metafore classiche sulla cura e la crescita ('la democrazia è una pianta da curare'); usa un tono materno verso i giovani; dedica una parte enorme del post a ringraziare ossessivamente ogni istituzione, associazione o figura coinvolta.
Struttura: 1. Apertura ad effetto. 2. Il cuore dell'evento descritto in modo profondo. 3. Una lezione di vita/morale sul senso civico. 4. Una lista estesa e puntuale di ringraziamenti. 5. Chiusura ad effetto con un incoraggiamento per la città.

Evento: {evento}
Presenti e da ringraziare: {presenti if presenti else 'non specificato'}
Dettaglio specifico: {dettaglio if dettaglio else 'nessuno'}"""

            response = model.generate_content(prompt)
            post = response.text

        st.success("Post generato con successo!")
        st.markdown("### 📋 Il tuo post istituzionale:")
        st.markdown(post)
        st.code(post, language=None)
        st.caption("Copia il testo qui sopra e incollalo su Facebook. Buona pubblicazione, Sindaca! 🏛️")
