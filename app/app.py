import streamlit as st

# Page configuration
st.set_page_config(
    page_title="House Price Estimator!@",
    page_icon="",
    layout="centered"
)

# Modern CSS styling
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stHeader"] {
        background-color: transparent;
    }
    
    /* Main container */
    .main-container {
        background: white;
        padding: 3rem 2.5rem;
        border-radius: 24px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        margin: 2rem auto;
        max-width: 600px;
    }
    
    /* Header */
    .app-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #8B5E3C 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    .app-subtitle {
        text-align: center;
        color: grey;
        font-size: 1rem;
        margin-bottom: 2.5rem;
        font-weight: 500;
    }
    
    /* Slider styling */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Input labels */
    .stSlider label, .stSelectbox label {
        font-weight: 600;
        color: #1f2937;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        border-radius: 12px;
        border: 2px solid #e5e7eb;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #667eea;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.9rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
    }
    
    /* Result card */
    .result-card {
        background: linear-gradient(135deg, #f0f4ff 0%, #f5f0ff 100%);
        padding: 2rem;
        border-radius: 16px;
        margin-top: 2rem;
        text-align: center;
        border: 2px solid #e0e7ff;
    }
    
    .result-label {
        color: #6b7280;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .result-price {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .result-note {
        color: #9ca3af;
        font-size: 0.85rem;
        font-style: italic;
    }
    
    /* Feature cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin-top: 1.5rem;
    }
    
    .feature-card {
        background: #f9fafb;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #e5e7eb;
    }
    
    .feature-icon {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.2rem;
    }
    
    .feature-label {
        color: #6b7280;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    /* Spacing */
    .spacer {
        margin: 1.5rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='app-title'> House Price Estimator</h1>", unsafe_allow_html=True)
st.markdown("<p class='app-subtitle'>Get an instant price estimate based on your property details</p>", unsafe_allow_html=True)

# Main container
with st.container():
    # Property Area
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    area = st.slider("📏 Property Area (sq ft)", 300, 10000, 1500, step=50)
    
    # Bedrooms and Bathrooms in columns
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        bedrooms = st.selectbox("🛏️ Bedrooms", [1, 2, 3, 4, 5], index=2)
    
    with col2:
        bathrooms = st.selectbox("🚿 Bathrooms", [1, 2, 3, 4], index=1)
    
    # Feature summary cards
    st.markdown("""
    <div class='feature-grid'>
        <div class='feature-card'>
            <div class='feature-icon'>📏</div>
            <div class='feature-value'>{:,}</div>
            <div class='feature-label'>Square Feet</div>
        </div>
        <div class='feature-card'>
            <div class='feature-icon'>🏠</div>
            <div class='feature-value'>{} / {}</div>
            <div class='feature-label'>Bed / Bath</div>
        </div>
    </div>
    """.format(area, bedrooms, bathrooms), unsafe_allow_html=True)
    
    # Estimate button
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    if st.button("✨ Estimate Price", use_container_width=True):
        # Simple mock calculation (replace with your model)
        base_price = 5000
        estimated_price = (area * base_price) + (bedrooms * 500000) + (bathrooms * 300000)
        
        st.markdown(f"""
        <div class='result-card'>
            <div class='result-label'>Estimated Price</div>
            <div class='result-price'>₹ {estimated_price:,}</div>
            <div class='result-note'>💡 This is a preliminary estimate. Actual pricing model will be integrated shortly.</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional information
        st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
        st.info("💼 **Note:** This estimate is based on basic parameters. For accurate pricing, our ML model will consider location, amenities, age, and market trends.")

# Footer info
st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
st.caption("Built with ❤️ using Streamlit!")