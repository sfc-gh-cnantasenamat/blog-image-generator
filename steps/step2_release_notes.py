import streamlit as st
import re
from .lib.generate_images import generate_gradients, get_gradient_direction

def render():
    emoji = st.text_input('Emoji', value='🚀')

    showCategory = st.checkbox('Show category text and icon?')

    direction = st.selectbox(
        'Gradient direction',
        ['0 degrees (left-to-right)',
        '45 degrees (diagonal top-left-to-bottom-right)',
        '90 degrees (top-to-bottom)',
        '135 degrees (diagonal top-right-to-bottom-left)',
        '315 degrees (diagonal bottom-left-top-top-right)'
        ],
    )

    return [emoji, showCategory, direction]

def generate(emoji, category, gradient_direction):
    verify_arguments(emoji)


    generated_images = []
    gradients = generate_gradients()
    coordinates = get_gradient_direction(gradient_direction)

    for i in range(len(gradients) - 1):
        categoryContent = ''

        if category:
            categoryContent = '<g transform="translate(32, 74)"><path fill-rule="evenodd" clip-rule="evenodd" d="M0 42C0 18.804 18.804 0 42 0H233C256.196 0 275 18.804 275 42C275 65.196 256.196 84 233 84H42C18.804 84 0 65.196 0 42ZM85.7216 50.5V33.0455H92.267C93.608 33.0455 94.733 33.2784 95.642 33.7443C96.5568 34.2102 97.2472 34.8636 97.7131 35.7045C98.1847 36.5398 98.4205 37.5142 98.4205 38.6278C98.4205 39.7472 98.1818 40.7188 97.7045 41.5426C97.233 42.3608 96.5369 42.9943 95.6165 43.4432C95.5087 43.4951 95.398 43.544 95.2844 43.5898L99.0597 50.5H95.5312L92.101 44.108H88.8835V50.5H85.7216ZM91.7983 41.483H88.8835V35.6875H91.7812C92.571 35.6875 93.2159 35.804 93.7159 36.0369C94.2159 36.2642 94.5881 36.5994 94.8324 37.0426C95.0767 37.4801 95.1989 38.0085 95.1989 38.6278C95.1989 39.2472 95.0767 39.7699 94.8324 40.196C94.5938 40.6165 94.2244 40.9375 93.7244 41.1591C93.2244 41.375 92.5824 41.483 91.7983 41.483ZM107.043 50.7557C105.73 50.7557 104.597 50.483 103.642 49.9375C102.693 49.3864 101.963 48.608 101.452 47.6023C100.94 46.5909 100.685 45.4006 100.685 44.0312C100.685 42.6847 100.94 41.5028 101.452 40.4858C101.969 39.4631 102.69 38.6676 103.616 38.0994C104.543 37.5256 105.631 37.2386 106.881 37.2386C107.687 37.2386 108.449 37.3693 109.165 37.6307C109.886 37.8864 110.523 38.2841 111.074 38.8239C111.631 39.3636 112.068 40.0511 112.386 40.8864C112.704 41.7159 112.864 42.7045 112.864 43.8523V44.7983H103.745C103.754 45.5269 103.893 46.1548 104.162 46.6818C104.44 47.2216 104.829 47.6364 105.329 47.9261C105.829 48.2102 106.415 48.3523 107.085 48.3523C107.534 48.3523 107.94 48.2898 108.304 48.1648C108.668 48.0341 108.983 47.8438 109.25 47.5938C109.517 47.3438 109.719 47.0341 109.855 46.6648L112.736 46.9886C112.554 47.75 112.207 48.4148 111.696 48.983C111.19 49.5455 110.543 49.983 109.753 50.2955C108.963 50.6023 108.06 50.7557 107.043 50.7557ZM104.145 41.2955C103.912 41.7314 103.78 42.2059 103.751 42.7188H109.906C109.901 42.1278 109.773 41.6023 109.523 41.142C109.273 40.6761 108.923 40.3097 108.474 40.0426C108.031 39.7756 107.514 39.642 106.923 39.642C106.293 39.642 105.739 39.7955 105.261 40.1023C104.784 40.4034 104.412 40.8011 104.145 41.2955ZM118.799 33.0455V50.5H115.714V33.0455H118.799ZM128.007 50.7557C126.694 50.7557 125.561 50.483 124.606 49.9375C123.658 49.3864 122.927 48.608 122.416 47.6023C121.905 46.5909 121.649 45.4006 121.649 44.0312C121.649 42.6847 121.905 41.5028 122.416 40.4858C122.933 39.4631 123.655 38.6676 124.581 38.0994C125.507 37.5256 126.595 37.2386 127.845 37.2386C128.652 37.2386 129.413 37.3693 130.129 37.6307C130.851 37.8864 131.487 38.2841 132.038 38.8239C132.595 39.3636 133.033 40.0511 133.351 40.8864C133.669 41.7159 133.828 42.7045 133.828 43.8523V44.7983H124.709C124.718 45.5269 124.857 46.1548 125.126 46.6818C125.405 47.2216 125.794 47.6364 126.294 47.9261C126.794 48.2102 127.379 48.3523 128.05 48.3523C128.498 48.3523 128.905 48.2898 129.268 48.1648C129.632 48.0341 129.947 47.8438 130.214 47.5938C130.481 47.3438 130.683 47.0341 130.819 46.6648L133.7 46.9886C133.518 47.75 133.172 48.4148 132.66 48.983C132.155 49.5455 131.507 49.983 130.717 50.2955C129.927 50.6023 129.024 50.7557 128.007 50.7557ZM125.109 41.2955C124.876 41.7314 124.745 42.2059 124.715 42.7188H130.871C130.865 42.1278 130.737 41.6023 130.487 41.142C130.237 40.6761 129.888 40.3097 129.439 40.0426C128.996 39.7756 128.479 39.642 127.888 39.642C127.257 39.642 126.703 39.7955 126.226 40.1023C125.748 40.4034 125.376 40.8011 125.109 41.2955ZM140.445 50.7642C139.616 50.7642 138.868 50.6165 138.204 50.321C137.545 50.0199 137.022 49.5767 136.635 48.9915C136.255 48.4062 136.064 47.6847 136.064 46.8267C136.064 46.0881 136.201 45.4773 136.473 44.9943C136.746 44.5114 137.118 44.125 137.59 43.8352C138.062 43.5455 138.593 43.3267 139.184 43.179C139.78 43.0256 140.397 42.9148 141.033 42.8466C141.8 42.767 142.422 42.696 142.9 42.6335C143.377 42.5653 143.723 42.4631 143.939 42.3267C144.161 42.1847 144.272 41.9659 144.272 41.6705V41.6193C144.272 40.9773 144.081 40.4801 143.701 40.1278C143.32 39.7756 142.772 39.5994 142.056 39.5994C141.3 39.5994 140.701 39.7642 140.258 40.0938C139.82 40.4233 139.525 40.8125 139.371 41.2614L136.491 40.8523C136.718 40.0568 137.093 39.392 137.616 38.858C138.138 38.3182 138.777 37.9148 139.533 37.6477C140.289 37.375 141.124 37.2386 142.039 37.2386C142.67 37.2386 143.297 37.3125 143.922 37.4602C144.547 37.608 145.118 37.8523 145.635 38.1932C146.152 38.5284 146.567 38.9858 146.88 39.5653C147.198 40.1449 147.357 40.8693 147.357 41.7386V50.5H144.391V48.7017H144.289C144.101 49.0653 143.837 49.4062 143.496 49.7244C143.161 50.0369 142.738 50.2898 142.226 50.483C141.721 50.6705 141.127 50.7642 140.445 50.7642ZM141.246 48.4972C141.866 48.4972 142.402 48.375 142.857 48.1307C143.312 47.8807 143.661 47.5511 143.905 47.142C144.155 46.733 144.28 46.2869 144.28 45.804V44.2614C144.184 44.3409 144.019 44.4148 143.786 44.483C143.559 44.5511 143.303 44.6108 143.019 44.6619C142.735 44.7131 142.454 44.7585 142.175 44.7983C141.897 44.8381 141.655 44.8722 141.451 44.9006C140.991 44.9631 140.579 45.0653 140.215 45.2074C139.851 45.3494 139.564 45.5483 139.354 45.804C139.144 46.054 139.039 46.3778 139.039 46.7756C139.039 47.3438 139.246 47.7727 139.661 48.0625C140.076 48.3523 140.604 48.4972 141.246 48.4972ZM161.046 40.8693L158.233 41.1761C158.154 40.892 158.015 40.625 157.816 40.375C157.623 40.125 157.361 39.9233 157.032 39.7699C156.702 39.6165 156.299 39.5398 155.821 39.5398C155.179 39.5398 154.64 39.679 154.202 39.9574C153.77 40.2358 153.557 40.5966 153.563 41.0398C153.557 41.4205 153.696 41.7301 153.981 41.9688C154.27 42.2074 154.748 42.4034 155.412 42.5568L157.645 43.0341C158.884 43.3011 159.804 43.7244 160.407 44.304C161.015 44.8835 161.321 45.642 161.327 46.5795C161.321 47.4034 161.08 48.1307 160.603 48.7614C160.131 49.3864 159.475 49.875 158.634 50.2273C157.793 50.5795 156.827 50.7557 155.736 50.7557C154.134 50.7557 152.844 50.4205 151.867 49.75C150.89 49.0739 150.307 48.1335 150.12 46.929L153.128 46.6392C153.265 47.2301 153.554 47.6761 153.998 47.9773C154.441 48.2784 155.017 48.429 155.728 48.429C156.461 48.429 157.049 48.2784 157.492 47.9773C157.941 47.6761 158.165 47.304 158.165 46.8608C158.165 46.4858 158.02 46.1761 157.731 45.9318C157.446 45.6875 157.003 45.5 156.401 45.3693L154.168 44.9006C152.912 44.6392 151.983 44.1989 151.381 43.5795C150.779 42.9545 150.481 42.1648 150.486 41.2102C150.481 40.4034 150.699 39.7045 151.142 39.1136C151.591 38.517 152.213 38.0568 153.009 37.733C153.81 37.4034 154.733 37.2386 155.779 37.2386C157.313 37.2386 158.52 37.5653 159.401 38.2188C160.287 38.8722 160.836 39.7557 161.046 40.8693ZM169.907 50.7557C168.594 50.7557 167.461 50.483 166.506 49.9375C165.557 49.3864 164.827 48.608 164.316 47.6023C163.804 46.5909 163.549 45.4006 163.549 44.0312C163.549 42.6847 163.804 41.5028 164.316 40.4858C164.833 39.4631 165.554 38.6676 166.48 38.0994C167.407 37.5256 168.495 37.2386 169.745 37.2386C170.552 37.2386 171.313 37.3693 172.029 37.6307C172.75 37.8864 173.387 38.2841 173.938 38.8239C174.495 39.3636 174.932 40.0511 175.25 40.8864C175.569 41.7159 175.728 42.7045 175.728 43.8523V44.7983H166.609C166.618 45.5269 166.757 46.1548 167.026 46.6818C167.304 47.2216 167.694 47.6364 168.194 47.9261C168.694 48.2102 169.279 48.3523 169.949 48.3523C170.398 48.3523 170.804 48.2898 171.168 48.1648C171.532 48.0341 171.847 47.8438 172.114 47.5938C172.381 47.3438 172.583 47.0341 172.719 46.6648L175.6 46.9886C175.418 47.75 175.071 48.4148 174.56 48.983C174.054 49.5455 173.407 49.983 172.617 50.2955C171.827 50.6023 170.924 50.7557 169.907 50.7557ZM167.009 41.2955C166.776 41.7314 166.644 42.2059 166.615 42.7188H172.77C172.765 42.1278 172.637 41.6023 172.387 41.142C172.137 40.6761 171.787 40.3097 171.338 40.0426C170.895 39.7756 170.378 39.642 169.787 39.642C169.157 39.642 168.603 39.7955 168.125 40.1023C167.648 40.4034 167.276 40.8011 167.009 41.2955ZM187.856 50.5H184.771V37.4091H187.72V39.6335H187.873C188.174 38.9006 188.654 38.3182 189.313 37.8864C189.978 37.4545 190.799 37.2386 191.777 37.2386C192.68 37.2386 193.467 37.4318 194.137 37.8182C194.813 38.2045 195.336 38.7642 195.706 39.4972C196.081 40.2301 196.265 41.1193 196.259 42.1648V50.5H193.174V42.642C193.174 41.767 192.947 41.0824 192.492 40.5881C192.044 40.0938 191.421 39.8466 190.626 39.8466C190.086 39.8466 189.606 39.9659 189.186 40.2045C188.771 40.4375 188.444 40.7756 188.206 41.2188C187.973 41.6619 187.856 42.1989 187.856 42.8295V50.5ZM205.346 50.7557C204.068 50.7557 202.96 50.4744 202.022 49.9119C201.085 49.3494 200.357 48.5625 199.84 47.5511C199.329 46.5398 199.073 45.358 199.073 44.0057C199.073 42.6534 199.329 41.4688 199.84 40.4517C200.357 39.4347 201.085 38.6449 202.022 38.0824C202.96 37.5199 204.068 37.2386 205.346 37.2386C206.624 37.2386 207.732 37.5199 208.67 38.0824C209.607 38.6449 210.332 39.4347 210.843 40.4517C211.36 41.4688 211.619 42.6534 211.619 44.0057C211.619 45.358 211.36 46.5398 210.843 47.5511C210.332 48.5625 209.607 49.3494 208.67 49.9119C207.732 50.4744 206.624 50.7557 205.346 50.7557ZM205.363 48.2841C206.056 48.2841 206.636 48.0938 207.102 47.7131C207.568 47.3267 207.914 46.8097 208.142 46.1619C208.374 45.5142 208.491 44.7926 208.491 43.9972C208.491 43.196 208.374 42.4716 208.142 41.8239C207.914 41.1705 207.568 40.6506 207.102 40.2642C206.636 39.8778 206.056 39.6847 205.363 39.6847C204.653 39.6847 204.062 39.8778 203.59 40.2642C203.124 40.6506 202.775 41.1705 202.542 41.8239C202.315 42.4716 202.201 43.196 202.201 43.9972C202.201 44.7926 202.315 45.5142 202.542 46.1619C202.775 46.8097 203.124 47.3267 203.59 47.7131C204.062 48.0938 204.653 48.2841 205.363 48.2841ZM221.014 37.4091V39.7955H218.432V46.5625C218.432 46.9773 218.494 47.2955 218.619 47.517C218.75 47.733 218.921 47.8807 219.131 47.9602C219.341 48.0398 219.574 48.0795 219.83 48.0795C220.023 48.0795 220.199 48.0653 220.358 48.0369C220.523 48.0085 220.648 47.983 220.733 47.9602L221.253 50.3722C221.088 50.429 220.852 50.4915 220.546 50.5597C220.244 50.6278 219.875 50.6676 219.438 50.679C218.665 50.7017 217.969 50.5852 217.35 50.3295C216.73 50.0682 216.239 49.6648 215.875 49.1193C215.517 48.5739 215.341 47.892 215.347 47.0739V39.7955H213.489V37.4091H215.347V34.2727H218.432V37.4091H221.014ZM229.489 50.7557C228.177 50.7557 227.043 50.483 226.089 49.9375C225.14 49.3864 224.41 48.608 223.899 47.6023C223.387 46.5909 223.131 45.4006 223.131 44.0312C223.131 42.6847 223.387 41.5028 223.899 40.4858C224.416 39.4631 225.137 38.6676 226.063 38.0994C226.989 37.5256 228.077 37.2386 229.327 37.2386C230.134 37.2386 230.896 37.3693 231.612 37.6307C232.333 37.8864 232.97 38.2841 233.521 38.8239C234.077 39.3636 234.515 40.0511 234.833 40.8864C235.151 41.7159 235.31 42.7045 235.31 43.8523V44.7983H226.192C226.201 45.5269 226.34 46.1548 226.609 46.6818C226.887 47.2216 227.276 47.6364 227.776 47.9261C228.276 48.2102 228.862 48.3523 229.532 48.3523C229.981 48.3523 230.387 48.2898 230.751 48.1648C231.114 48.0341 231.43 47.8438 231.697 47.5938C231.964 47.3438 232.166 47.0341 232.302 46.6648L235.183 46.9886C235.001 47.75 234.654 48.4148 234.143 48.983C233.637 49.5455 232.989 49.983 232.2 50.2955C231.41 50.6023 230.506 50.7557 229.489 50.7557ZM226.592 41.2955C226.359 41.7314 226.227 42.2059 226.197 42.7188H232.353C232.347 42.1278 232.22 41.6023 231.97 41.142C231.72 40.6761 231.37 40.3097 230.921 40.0426C230.478 39.7756 229.961 39.642 229.37 39.642C228.739 39.642 228.185 39.7955 227.708 40.1023C227.231 40.4034 226.859 40.8011 226.592 41.2955ZM248.507 40.8693L245.695 41.1761C245.615 40.892 245.476 40.625 245.277 40.375C245.084 40.125 244.822 39.9233 244.493 39.7699C244.163 39.6165 243.76 39.5398 243.283 39.5398C242.641 39.5398 242.101 39.679 241.663 39.9574C241.232 40.2358 241.018 40.5966 241.024 41.0398C241.018 41.4205 241.158 41.7301 241.442 41.9688C241.732 42.2074 242.209 42.4034 242.874 42.5568L245.107 43.0341C246.345 43.3011 247.266 43.7244 247.868 44.304C248.476 44.8835 248.783 45.642 248.788 46.5795C248.783 47.4034 248.541 48.1307 248.064 48.7614C247.592 49.3864 246.936 49.875 246.095 50.2273C245.254 50.5795 244.288 50.7557 243.197 50.7557C241.595 50.7557 240.305 50.4205 239.328 49.75C238.351 49.0739 237.768 48.1335 237.581 46.929L240.59 46.6392C240.726 47.2301 241.016 47.6761 241.459 47.9773C241.902 48.2784 242.479 48.429 243.189 48.429C243.922 48.429 244.51 48.2784 244.953 47.9773C245.402 47.6761 245.626 47.304 245.626 46.8608C245.626 46.4858 245.482 46.1761 245.192 45.9318C244.908 45.6875 244.465 45.5 243.862 45.3693L241.629 44.9006C240.374 44.6392 239.445 44.1989 238.842 43.5795C238.24 42.9545 237.942 42.1648 237.947 41.2102C237.942 40.4034 238.161 39.7045 238.604 39.1136C239.053 38.517 239.675 38.0568 240.47 37.733C241.271 37.4034 242.195 37.2386 243.24 37.2386C244.774 37.2386 245.982 37.5653 246.862 38.2188C247.749 38.8722 248.297 39.7557 248.507 40.8693ZM42 72C58.5685 72 72 58.5685 72 42C72 25.4315 58.5685 12 42 12C25.4315 12 12 25.4315 12 42C12 58.5685 25.4315 72 42 72Z" fill="white"/><path d="M39.4526 52.4826C39.1657 52.4826 38.8907 52.3687 38.6878 52.1658L31.8336 45.3122C31.6989 45.1775 31.602 45.0096 31.553 44.8254C31.504 44.6414 31.5045 44.4475 31.5545 44.2637C32.933 40.0544 35.3378 36.2548 38.5527 33.2078C45.0169 26.7436 55.498 26.9921 55.948 27.0039C56.2233 27.0126 56.4848 27.1258 56.6797 27.3204C56.8743 27.5151 56.9873 27.7768 56.996 28.0519C57.0085 28.4954 57.257 38.9811 50.7914 45.4459V45.4461C47.745 48.6606 43.9458 51.0659 39.7367 52.4444C39.644 52.4697 39.5486 52.4825 39.4525 52.4823L39.4526 52.4826ZM33.8185 44.2375L39.7621 50.1807C43.3629 48.8405 46.6114 46.6984 49.2615 43.9161C53.9415 39.2357 54.699 31.9107 54.8141 29.1858C52.0874 29.3049 44.7516 30.0679 40.0819 34.737C37.3002 37.3877 35.1584 40.6367 33.818 44.2376L33.8185 44.2375Z" fill="white"/><path d="M44.4392 43.8845C43.0947 43.8833 41.8272 43.2569 41.0098 42.1896C40.1921 41.1223 39.9174 39.7355 40.2666 38.4371C40.6155 37.1387 41.5483 36.0765 42.7909 35.5629C44.0333 35.0493 45.444 35.1427 46.6081 35.8157C47.772 36.4887 48.5566 37.6646 48.7314 38.9976C48.906 40.3307 48.4508 41.6693 47.4996 42.6195C46.6883 43.4313 45.587 43.8867 44.4392 43.8845V43.8845ZM44.4402 37.3973V37.3975C43.7682 37.398 43.1343 37.7112 42.7255 38.2449C42.3167 38.7785 42.1795 39.4721 42.3539 40.1211C42.5285 40.7705 42.995 41.3015 43.6163 41.5581C44.2374 41.815 44.9427 41.7682 45.5247 41.4316C46.1066 41.095 46.499 40.507 46.5862 39.8406C46.6733 39.1741 46.4456 38.5048 45.9699 38.0298C45.5643 37.6241 45.0139 37.3966 44.4402 37.3976L44.4402 37.3973Z" fill="white"/><path d="M54.3841 38.3463C54.097 38.3468 53.8217 38.2329 53.6191 38.0295L45.9693 30.3803C45.7029 30.1055 45.6015 29.7107 45.7024 29.3417C45.8031 28.9728 46.0914 28.6844 46.4607 28.5835C46.8296 28.4826 47.2244 28.5842 47.499 28.8506L55.1488 36.4998H55.1491C55.3519 36.7026 55.4659 36.9779 55.4656 37.2648C55.4656 37.5514 55.3519 37.8267 55.1491 38.0295C54.9462 38.2323 54.671 38.3463 54.3841 38.3463L54.3841 38.3463Z" fill="white"/><path d="M36.026 54.2791C35.1644 54.2815 34.3377 53.9388 33.7303 53.3276L30.6709 50.2687C30.0629 49.6597 29.7217 48.8344 29.7217 47.974C29.7217 47.1134 30.0629 46.2881 30.6709 45.6791L32.2006 44.1493C32.4034 43.9465 32.6785 43.8328 32.9653 43.8328C33.2522 43.8328 33.5275 43.9465 33.7303 44.1493L39.8502 50.2687C40.053 50.4718 40.167 50.7468 40.167 51.0337C40.167 51.3206 40.053 51.5956 39.8502 51.7987L38.3205 53.3284V53.3281C37.7134 53.9388 36.8871 54.2812 36.026 54.2791V54.2791ZM32.9651 46.4438L32.2001 47.2085C31.9978 47.4118 31.884 47.6869 31.884 47.9738C31.884 48.2606 31.9977 48.5357 32.2001 48.7387L35.2605 51.7982H35.2615L35.2617 51.7984C35.4675 51.9952 35.7413 52.1048 36.026 52.1048C36.3109 52.1048 36.5845 51.9952 36.7905 51.7984L37.5552 51.0334L32.9651 46.4438Z" fill="white"/><path d="M32.2013 46.761C32.1127 46.7613 32.0243 46.7504 31.9381 46.7287L25.8195 45.199C25.5708 45.1367 25.3523 44.9882 25.2028 44.7798C25.0533 44.5716 24.9828 44.3169 25.0036 44.0614C25.0246 43.8059 25.1354 43.5661 25.3165 43.3848L27.7327 40.9684V40.9682C28.3467 40.3471 29.1878 40.0037 30.0612 40.0172L33.9711 40.0595H33.9709C34.258 40.0626 34.5318 40.1795 34.7325 40.3847C34.9334 40.5898 35.0442 40.8662 35.0411 41.1531C35.0459 41.4424 34.9314 41.7208 34.7245 41.9232C34.5178 42.1255 34.237 42.234 33.9479 42.2231L30.0388 42.1806C29.7497 42.1847 29.4728 42.2977 29.2634 42.4972L28.1973 43.5633L32.4622 44.6296H32.4624C32.8065 44.7158 33.0864 44.9652 33.2117 45.2973C33.3368 45.6293 33.2911 46.0014 33.0895 46.2933C32.8881 46.5855 32.5561 46.7601 32.2014 46.7606L32.2013 46.761Z" fill="white"/><path d="M39.8499 58.9999C39.6086 58.9999 39.3742 58.9195 39.1841 58.771C38.9938 58.6225 38.8588 58.4146 38.8004 58.1806L37.2707 52.0612V52.061C37.1963 51.7811 37.2371 51.4829 37.3844 51.2334C37.5315 50.984 37.7727 50.8039 38.0535 50.7336C38.3346 50.6633 38.6321 50.7085 38.8796 50.8594C39.1269 51.0103 39.3034 51.254 39.3693 51.536L40.4364 55.8018L41.5013 54.7369V54.7372C41.7068 54.531 41.821 54.2511 41.8183 53.9601L41.7761 50.0519V50.0517C41.7729 49.7648 41.884 49.4885 42.0847 49.2835C42.2853 49.0783 42.5592 48.9614 42.846 48.9583C43.1319 48.9587 43.4062 49.0708 43.6108 49.2707C43.815 49.4707 43.9329 49.7426 43.9396 50.0285L43.9819 53.9367C43.9894 54.8096 43.6467 55.649 43.031 56.2674L40.6148 58.6828C40.412 58.8857 40.1367 58.9996 39.8498 58.9999L39.8499 58.9999Z" fill="white"/></g>'

        generated_images.append(f"""
            <svg viewBox="0 0 1480 700" width="100%" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                # Gradient Background
                <rect width="100%" height="100%" fill="url(#gradient)"/>

                # Emoji
                <text fill="black" xml:space="preserve" style="white-space: pre" font-family="Inter" font-size="240" font-weight="600" letter-spacing="0.01em"><tspan x="653.047" y="437.273">{emoji}</tspan></text>

                # Category name and icon
                {categoryContent}

                <defs>
                    # Gradient
                    <linearGradient id="gradient" x1="0" y1="0" x2="1" y2="0" gradientTransform="rotate({coordinates[0]})">{gradients[i]}</linearGradient>
                </defs>
            </svg>
        """.strip())
    
    return generated_images


def verify_arguments(emoji):
    # Check if emoji is not empty
    if emoji == '':
        st.error("Please add an emoji")
        st.stop()

    # Check if emoji is actually an emoji
    MATCH_EMOJI = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        "]+",
        flags=re.UNICODE,
    )
    
    for i in range(len(emoji)):
        extracted_emoji = MATCH_EMOJI.match(emoji[i])

        if extracted_emoji == None:
            st.error("Hmmm, that doesn't look like a valid emoji. Please try using a different one!")
            st.stop()