from memory import Memory

memory = Memory()

# After generating extended prompt
memory.add("prompt_expansion", extended_prompt)

# After generating image
memory.add("image_2d", image_path)

# After converting to 3D
memory.add("image_3d", image_3d_path)

# View history (optional)
st.markdown("### 📜 History")
for entry in memory.get_all():
    st.write(f"**{entry['stage']}**: {entry['content']}")
