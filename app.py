import streamlit as st
import requests
from streamlit_lottie import st_lottie

def click_button():
    st.session_state.clicked = True

st.set_page_config(page_title="God Father Gaming", page_icon=":video_game:", layout="wide")

def lottieurl(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)





lottie_file1 = lottieurl("https://lottie.host/3f3af8d7-0933-41f8-be57-6a4031c309bf/tn9qLNu6O7.json")
lottie_file2 = lottieurl("https://lottie.host/33711147-5b4d-403b-8ca1-19e9baf7349d/6TMOzF8AnA.json")
lottie_file3 = lottieurl("https://lottie.host/3f3af8d7-0933-41f8-be57-6a4031c309bf/tn9qLNu6O7.json")
lottie_file4 = lottieurl("https://lottie.host/d63a36fd-2a4d-445c-9c92-cde96faaefad/vuK17rflxL.json")


st.markdown("<h1 style='text-align: center; color: white;'>WELCOME TO GOD FATHER GAMING</h1>", unsafe_allow_html=True)

with st.container():
	col1 = st.columns(1)
	st.write("---")

with st.container():
	colu1, colu2, colu3 = st.columns(3)
	with colu1:
		st_lottie(lottie_file1)
		#st_lottie(lottie_file2)
	with colu2:
		st.link_button("Game Vault", "https://download.gamevault999.com")
		st.link_button("JUWA", "https://dl.juwa777.com/")
		st.link_button("Orion Stars", "http://start.orionstars.vip:8580/")
		st.link_button("High Stake", "https://dl.highstakesweeps.com/")
		st.link_button("Rising stars", "http://risingstar.vip:8580/index.html")
		st.link_button("Panda Master", "https://pandamaster.vip:8888/")
		st.link_button("Fire Kirin", "http://start.firekirin.xyz:8580/")
		st.link_button("Milky Way", "https://milkywayapp.xyz/")
		st.link_button("Vblink", "https://www.vblink777.club/")
		st.link_button("Ultra Panda", "https://www.ultrapanda.mobi/")
	with colu3:
		st_lottie(lottie_file3)
		#st_lottie(lottie_file4)

with st.container():
	colum1, colum2, colum3 = st.columns(3)
	with colum1:
		st.write("")
	with colum2:
		st.write("---")
		st.link_button("Follow our Facebook page GFG", "https://www.facebook.com/godfathergamingg/")
		st.write("---")
	with colum3:
		st.write("")	
		

st.write("---")
	

style = "<style>.row-widget.stLinkButton {text-align: center;}, MainMenu {visibility: hidden;}, fotter {visibility: hidden;}, header {visibility: hidden;}</style>"
st.markdown(style, unsafe_allow_html=True)
