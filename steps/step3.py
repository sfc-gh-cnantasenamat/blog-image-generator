# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import time as time
import random
import streamlit.components.v1 as components

import cairosvg
from io import BytesIO
from PIL import Image

def convert_svg_to_png(svg_content, output=None):
    if output:
        cairosvg.svg2png(bytestring=svg_content, write_to=output)
    else:
        return cairosvg.svg2png(bytestring=svg_content)
    

def display_output():
    st.write('''
    ## Step 3: Downloads
    ''')

    svg_images = st.session_state.images

    st.info("Done! We've generated some options for you 👇🏻")

    for i in range(len(svg_images)):

        # Convert and get bytes
        png_data = convert_svg_to_png(svg_images[i])
        png_img = Image.open(BytesIO(png_data))
        
        components.html(f'''
            <body style="margin: 0; padding: 0;">
                <svg viewBox="0 0 1480 700">{svg_images[i]}</svg>
            </body>
        ''', height=333)

        # st.image(png_img)

        col = st.columns(2)

        with col[0]:
            st.download_button(
                label="Download SVG image",
                data=svg_images[i],
                file_name=f'''{st.session_state.template_name}.svg''',
                mime="image/svg+xml",
                key= f"key_{str(random.randint(0, 100000000))}"
            )

        with col[1]:
            st.download_button(
                label="Download PNG image",
                data=png_data,
                file_name=f'''{st.session_state.template_name}.png''',
                mime="image/png",
                key= f"key_{str(random.randint(0, 100000000))}"
            )

        st.write('')
        st.write('')
