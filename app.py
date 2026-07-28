import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="ขับขี่จักรยานยนต์อย่างปลอดภัย",
    page_icon="🏍️",
    layout="wide",
)

# ---------- Style ----------
st.markdown(
    """
    <style>
    .block-container {
        max-width: 1100px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }
    .main-title {
        text-align: center;
        color: #0B3B75;
        font-size: 2.1rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
    }
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 1.05rem;
        margin-bottom: 1.2rem;
    }
    .safety-box {
        background: #EEF6FF;
        border-left: 6px solid #1464B4;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        margin-bottom: 1rem;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        font-weight: 700;
        min-height: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

IMAGE_DIR = Path(__file__).parent / "images"

POSTERS = {
    "1. การล้มอย่างปลอดภัย": {
        "file": IMAGE_DIR / "safe_fall.png",
        "caption": "แนวทางลดการบาดเจ็บเมื่อเกิดอุบัติเหตุจักรยานยนต์",
    },
    "2. Helmet Fitting": {
        "file": IMAGE_DIR / "helmet_fitting.png",
        "caption": "การเลือกขนาดและสวมหมวกกันน็อกให้กระชับพอดี",
    },
    "3. การผ่านเนินสะดุด": {
        "file": IMAGE_DIR / "speed_hump.png",
        "caption": "ชะลอก่อนถึงเนิน ปล่อยเบรกขณะผ่านเนิน และระวังถนนเปียก",
    },
    "4. การดูแลแผลถลอกหลังรถล้ม": {
        "file": IMAGE_DIR / "abrasion_care.png",
        "caption": "ล้างแผลให้สะอาด ปิดแผลอย่างเหมาะสม และสังเกตอาการติดเชื้อ",
    },
}

st.markdown(
    '<div class="main-title">🏍️ ขับขี่จักรยานยนต์อย่างปลอดภัย</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-title">สถานพยาบาล มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="safety-box">
    เลือกหัวข้อด้านล่างเพื่อดูโปสเตอร์ และสามารถบันทึกภาพไว้ในโทรศัพท์ได้
    </div>
    """,
    unsafe_allow_html=True,
)

menu = st.radio(
    "เลือกหัวข้อ",
    list(POSTERS.keys()),
    horizontal=True,
    label_visibility="collapsed",
)

item = POSTERS[menu]
image_path = item["file"]

st.subheader(menu)
st.caption(item["caption"])

if image_path.exists():
    st.image(str(image_path), use_container_width=True)

    with open(image_path, "rb") as f:
        st.download_button(
            label="📥 ดาวน์โหลดภาพนี้",
            data=f.read(),
            file_name=image_path.name,
            mime="image/png",
            use_container_width=True,
        )
else:
    st.error(
        f"ไม่พบไฟล์ภาพ: {image_path.name}\n\n"
        "โปรดตรวจสอบว่าได้วางไฟล์ไว้ในโฟลเดอร์ images และใช้ชื่อไฟล์ให้ตรงกับโค้ด"
    )

st.divider()

with st.expander("ดูภาพทั้งหมด"):
    for title, data in POSTERS.items():
        st.markdown(f"### {title}")
        if data["file"].exists():
            st.image(str(data["file"]), use_container_width=True)
        else:
            st.warning(f"ไม่พบไฟล์ {data['file'].name}")

st.info(
    "คำแนะนำนี้ใช้เพื่อส่งเสริมความปลอดภัยทั่วไป "
    "หากเกิดอุบัติเหตุ มีเลือดออกมาก หมดสติ ปวดศีรษะรุนแรง "
    "หายใจลำบาก แขนขาผิดรูป หรือขยับไม่ได้ ควรไปโรงพยาบาลทันที"
)
