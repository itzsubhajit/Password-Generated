
import streamlit as st
import secrets
import string
import re

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="SecureForge | Password Security",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0b1020 0%, #11182b 55%, #151126 100%);
    color: #edf2ff;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 30px;
    border: 1px solid #293653;
    border-radius: 22px;
    background: linear-gradient(120deg, #17233c, #211638);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 8px;
}

.hero p {
    color: #aab8d6;
    font-size: 16px;
}

.eyebrow {
    color: #a78bfa;
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 12px;
}

.panel {
    padding: 24px;
    background: rgba(22, 31, 53, 0.92);
    border: 1px solid #2c3a59;
    border-radius: 18px;
    min-height: 210px;
}

.panel h3 {
    color: #f3f5ff;
}

.result {
    padding: 18px;
    background: #0b1325;
    border: 1px solid #3b4b70;
    border-radius: 12px;
    color: #a7f3d0;
    font-size: 19px;
    font-weight: 600;
    overflow-wrap: anywhere;
    margin: 12px 0;
}

.info {
    padding: 13px;
    border-radius: 10px;
    background: #172541;
    color: #bac8e6;
    font-size: 13px;
    margin-top: 12px;
}

div.stButton > button {
    width: 100%;
    border: 0;
    border-radius: 10px;
    background: linear-gradient(90deg, #7c3aed, #4f46e5);
    color: white;
    font-weight: 700;
    min-height: 45px;
}

div.stButton > button:hover {
    border: 1px solid #a78bfa;
    color: white;
}

h2, h3 {
    color: #f3f5ff;
}

footer {
    visibility: hidden;
}

[data-testid="stMetric"] {
    background: #151f36;
    border: 1px solid #2c3a59;
    padding: 15px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SECURITY FUNCTIONS ----------------

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate a password using cryptographically secure randomness."""

    pools = []

    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+?")

    if not pools:
        return None

    # Ensure at least one character from each selected category
    password_chars = [secrets.choice(pool) for pool in pools]

    # Fill the remaining positions from the combined character pool
    all_chars = "".join(pools)

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    # Securely shuffle the characters
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = (
            password_chars[j], password_chars[i]
        )

    return "".join(password_chars)


def strengthen_password(word, extra_length=3):
    """Create a stronger-looking variation of a word with random additions."""

    word = word.strip()

    if not word:
        return None

    substitutions = {
        "a": "@",
        "e": "3",
        "i": "!",
        "o": "0",
        "s": "$",
        "t": "7"
    }

    result = []

    for char in word:
        lower_char = char.lower()

        # Apply substitutions occasionally, not predictably every time
        if lower_char in substitutions and secrets.randbelow(2) == 0:
            result.append(substitutions[lower_char])
        elif char.isalpha() and secrets.randbelow(2) == 0:
            result.append(char.upper())
        else:
            result.append(char)

    # Add random digits and symbols
    additions = string.digits + "!@#$%&*"
    for _ in range(extra_length):
        result.append(secrets.choice(additions))

    # Shuffle the added characters only, preserving the base word's order
    return "".join(result)


def assess_strength(password):
    """Give a simple heuristic assessment, not a guarantee of security."""

    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1

    if score <= 2:
        return "Weak", "Add more length and character variety."
    elif score <= 4:
        return "Moderate", "Try a longer password with more character types."
    return "Strong", "Good character variety. Keep it unique to this account."


# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <div class="eyebrow">PERSONAL SECURITY TOOLKIT</div>
    <h1>SecureForge</h1>
    <p>Generate secure passwords. Improve password complexity.
    Keep your digital accounts better protected.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- TABS ----------------

tab1, tab2, tab3 = st.tabs([
    "🔑 Password Generator",
    "🛡️ Password Strengthener",
    "ℹ️ Security Guide"
])

# ---------------- GENERATOR TAB ----------------

with tab1:
    st.subheader("Create a random password")
    st.write("Customize the length and character types for your password.")

    left, right = st.columns([1, 1], gap="large")

    with left:
        length = st.slider(
            "Password length",
            min_value=8,
            max_value=64,
            value=16,
            step=1
        )

        st.caption(f"Selected length: {length} characters")

        col1, col2 = st.columns(2)

        with col1:
            use_lower = st.checkbox("Lowercase (a-z)", value=True)
            use_upper = st.checkbox("Uppercase (A-Z)", value=True)

        with col2:
            use_digits = st.checkbox("Numbers (0-9)", value=True)
            use_symbols = st.checkbox("Symbols (!@#$)", value=True)

        generate_clicked = st.button(
            "Generate Secure Password",
            key="generate_password",
            use_container_width=True
        )

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### Your generated password")

        if generate_clicked:
            generated = generate_password(
                length, use_upper, use_lower, use_digits, use_symbols
            )

            if generated is None:
                st.error("Select at least one character category.")
            else:
                st.session_state["generated_password"] = generated

        generated = st.session_state.get("generated_password", "")

        if generated:
            st.code(generated, language=None)
            st.caption(f"{len(generated)} characters")

            strength, advice = assess_strength(generated)

            st.metric("Estimated strength", strength)
            st.write(advice)

            st.text_input(
                "Copy your password",
                value=generated,
                key="copy_generated_password"
            )
            st.caption("Select the text above and copy it. Avoid sharing passwords.")

        else:
            st.info("Your password will appear here after generation.")

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- STRENGTHENER TAB ----------------

with tab2:
    st.subheader("Improve a password idea")
    st.write(
        "Enter a memorable word to create a modified variation. "
        "For better security, use a long, unique password rather than "
        "relying on predictable substitutions."
    )

    source_word = st.text_input(
        "Enter a word",
        placeholder="e.g. orange",
        max_chars=100
    )

    extra_length = st.slider(
        "Number of random characters to append",
        min_value=3,
        max_value=12,
        value=5
    )

    if st.button("Strengthen Password", key="strengthen"):
        if not source_word.strip():
            st.warning("Please enter a word first.")
        else:
            strengthened = strengthen_password(source_word, extra_length)
            st.session_state["strengthened_password"] = strengthened

    strengthened = st.session_state.get("strengthened_password", "")

    if strengthened:
        st.markdown("### Your modified password")
        st.code(strengthened, language=None)

        strength, advice = assess_strength(strengthened)

        st.metric("Estimated strength", strength)
        st.write(advice)

        st.info(
            "Security note: this feature starts with your original word, "
            "so it may remain guessable. For important accounts, generate "
            "a completely random password instead."
        )

# ---------------- SECURITY GUIDE TAB ----------------

with tab3:
    st.subheader("Password security checklist")

    st.markdown("""
    - **Use length:** Prefer passwords of 16 or more characters when possible.
    - **Be unique:** Never reuse a password across different accounts.
    - **Use a password manager:** Store randomly generated passwords safely.
    - **Enable MFA:** Multi-factor authentication adds another layer of protection.
    - **Avoid personal information:** Names, birthdays and familiar words can be guessed.
    - **Do not share secrets:** Never post passwords in screenshots or public repositories.
    """)

    st.markdown("---")
    st.subheader("How SecureForge works")

    st.write(
        "**Random generator:** Uses Python's `secrets` module for "
        "cryptographically secure random choices."
    )
    st.write(
        "**Strengthener:** Makes a randomized variation of a supplied word. "
        "It is a learning feature, not a guarantee that the result is secure."
    )
    st.write(
        "**Strength estimate:** Uses length and character diversity as "
        "simple indicators. It is not a formal password-strength measurement."
    )

# ---------------- FOOTER ----------------

st.markdown("---")
st.caption(
    "SecureForge | Educational security tool | "
    "Do not enter passwords currently used for important accounts."
)
