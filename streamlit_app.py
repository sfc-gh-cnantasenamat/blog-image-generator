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
from steps.step1 import step1
from steps.step2 import step2
from steps.step3 import step3

# Presentational content

st.markdown('<div style="font-size: 4rem; margin-bottom: -3rem;">🎨</div>', unsafe_allow_html=True)

'''
# Blog image generator

An app to generate good-looking images for [our blog](https://blog.streamlit.io).
'''

'---'

def reset_images():
    if 'images' in st.session_state:
        del st.session_state.images

template = step1(on_template_changed=reset_images)

if not template:
    st.stop()

'---'

out = step2(template)

if not out:
    st.stop()

'---'

step3(out)
