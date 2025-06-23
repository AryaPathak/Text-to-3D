
import os
import sys

# Add the project root to sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print("PROJECT ROOT:", PROJECT_ROOT)
sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

# Now import after sys.path is updated
from llm.local_llm import LocalLLM
from pipeline.text_to_image import generate_image
from pipeline.image_to_3d import convert_to_3d

st.set_page_config(page_title="AI Creative Partner", layout="centered")
st.title("🧠 AI Creative Partner")
st.markdown("### Generate creative content in multiple stages using AI")

llm = LocalLLM()

prompt = st.text_area("Enter your base prompt:", height=150)

if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Stage 1: Extending your prompt..."):
            extended_prompt = llm.expand_prompt(prompt)
        st.success("Stage 1 Complete ✅")
        st.markdown("**Extended Prompt:**")
        st.info(extended_prompt)

        with st.spinner("Stage 2: Generating 2D image..."):
            image_path = generate_image(extended_prompt)
        st.success("Stage 2 Complete ✅")
        st.image(image_path, caption="Generated 2D Image", use_column_width=True)

        with st.spinner("Stage 3: Converting to 3D..."):
            image_3d_path = convert_to_3d(image_path)
        st.success("Stage 3 Complete ✅")
        st.image(image_3d_path, caption="Converted 3D Image", use_column_width=True)
    else:
        st.warning("Please enter a prompt to proceed.")