import streamlit as st
import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd
from io import StringIO


def app():

    st.title('Heatmaps')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

    # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
    filepath = dataframe 
    m = leafmap.Map(tiles="stamentoner")
    m.add_heatmap(
        filepath,
        latitude="Lat",
        longitude="Long",
        value="Dummy",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(width=700, height=500)
