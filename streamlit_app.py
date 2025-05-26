import streamlit as st
import openai

openai.api_key = st.secrets["openai"]["api_key"]

# System messages
creator_sys_msg = "You are the Content Creator Agent. Your role is to draft content on topics involving Generative AI. Ensure the content is clear, concise, and technically accurate."
critic_sys_msg = "You are the Content Critic Agent. Your role is to evaluate the content drafted by the Content Creator Agent. Provide feedback on language and technical correctness, and suggest improvements."

st.title("🧠 Smart Content Creation Agent Simulation")

topic = st.text_input("Enter a content topic:", "Agentic AI")

if st.button("Start Agent Conversation"):
    with st.spinner("Generating content..."):
        # Step 1: Content Creator drafts
        draft = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": creator_sys_msg},
                {"role": "user", "content": f"Draft a paragraph on: {topic}"}
            ]
        )["choices"][0]["message"]["content"]

        st.markdown("### 📝 Draft by Content Creator")
        st.write(draft)

        # Step 2: Content Critic gives feedback
        feedback = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": critic_sys_msg},
                {"role": "user", "content": f"Evaluate and suggest improvements to the following:\n\n{draft}"}
            ]
        )["choices"][0]["message"]["content"]

        st.markdown("### 🧠 Feedback by Content Critic")
        st.write(feedback)

        # Step 3: Content Creator revises
        revised = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": creator_sys_msg},
                {"role": "user", "content": f"Revise the original based on this feedback:\n\n{feedback}"}
            ]
        )["choices"][0]["message"]["content"]

        st.markdown("### ✅ Final Refined Content")
        st.markdown(revised)
