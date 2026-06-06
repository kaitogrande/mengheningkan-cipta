import streamlit as st

with open("thisis.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


st.title ("FaSHioN: Show ur Fits!")
st.write("Let's learn about fashion styles together")


# Mengubah input angka menjadi pilihan dropdown web
pilihan = st.selectbox(
    "I pick.. (Silahkan pilih gaya fashion):",
    ["Pilih gaya...", "Casual", "Vintage", "Emo", "Streetwear", "Gyaru"]
)

if pilihan == "Casual":
    st.subheader("Casual Style")
    # Link gambar 
    st.image("casual.png")

elif pilihan == "Vintage":
    st.subheader("Vintage Style")
  
    st.image("vintage.png")

elif pilihan == "Emo":
    st.subheader("Emo Style")
    st.image("emo.png")


elif pilihan == "Streetwear":
    st.subheader("Streetwear Style")
    st.image("streetwear.png")


elif pilihan == "Gyaru":
    st.subheader("Gyaru Style")
    st.image("gyaru.png")

st.markdown("""
<a href="file:///C:/Users/kayra/OneDrive/Desktop/PROJECT%20INFOR/product.html">
    <button>← Back to Home</button>
</a>
""", unsafe_allow_html=True)

