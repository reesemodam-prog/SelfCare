import streamlit as st

st.set_page_config(page_title="Self-Care Assessment", layout="centered")

# -----------------------------
# SESSION STATE
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "responses" not in st.session_state:
    st.session_state.responses = {}

# -----------------------------
# STYLING
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #C8F7E5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# TITLE + INTRO
# -----------------------------
st.title("🌿 Self-Care Assessment Tool 🌿")

st.markdown("""
Self-assessment is an important reflective process that helps individuals understand their strengths and areas for improvement and supports self-directed learning.  

This tool aims to:

1. Promote self-awareness and reflection  
2. Support holistic wellbeing  
3. Encourage individuals to identify areas for growth in self-care  
4. Align with holistic approaches to wellbeing in education and professional practice  

This self-care assessment is adapted from:  
https://rise.articulate.com/share/i3RuAxAmlt3AIEi5QS1Fyasu-JYib9LT  

### Scale
- 1 = It has never occurred to me  
- 2 = Never  
- 3 = Sometimes  
- 4 = Fairly Often  
- 5 = Frequently  
""")

# -----------------------------
# QUESTION SET
# -----------------------------
categories = {

"Physical Self-Care": [
"Eat regularly (e.g. breakfast & lunch)",
"Eat a well balanced, healthy diet",
"Exercise at home or go to the gym",
"Lift weights",
"Practice martial arts",
"Get regular medical care for prevention of health problems",
"Get medical care when needed",
"Take time off when you're sick",
"Get massages to help reduce muscle tension",
"Do physical activity that is fun for you",
"Take time to be sexually intimate",
"Get enough sleep",
"Wear clothes you like",
"Take vacations",
"Take day trips or mini-vacations",
"Get away from stressful technology"
],

"Psychological Self-Care": [
"Make time for self-reflection",
"Go to see a psychotherapist or counsellor for yourself",
"Keep a journal",
"Read literature unrelated to work",
"Do something at which you are a beginner",
"Take a step to decrease stress in your life",
"Notice your inner experience (dreams, thoughts, feelings)",
"Let others know different aspects of you",
"Engage your intelligence in a new area, cultural activity, sports event, etc",
"Be curious",
"Say no to extra responsibilities sometimes",
"Spend time outdoors"
],

"Emotional Self-Care": [
"Spend time with others whose company you enjoy",
"Stay in contact with important people in your life",
"Treat yourself kindly (supportive inner dialogue or self-talk)",
"Feel proud of yourself",
"Reread favourite books or re-watch favourite movies",
"Seek comforting activities, people, places",
"Allow yourself to cry",
"Find things that make you laugh",
"Express your outrage constructively",
"Play with children"
],

"Spiritual Self-Care": [
"Make time for prayer, meditation, reflection",
"Spend time in nature",
"Participate in a spiritual gathering, community or group",
"Be open to inspiration",
"Cherish optimism and hope",
"Be aware of intangible aspects of life",
"Be open to mystery",
"Identify what is meaningful to you",
"Sing",
"Express gratitude",
"Celebrate milestones meaningfully",
"Remember loved ones who passed away",
"Nurture others",
"Have 'awesome' experiences",
"Participate in causes you believe in",
"Read inspirational literature",
"Listen to inspiring music"
],

"Workplace / Professional Self-Care": [
"Take time to eat lunch",
"Take time to chat with co-workers",
"Make time to complete tasks",
"Identify tasks that are exciting and rewarding and promote growth",
"Set limits with clients and colleagues",
"Balance workload",
"Arrange your workplace so it is comfortable and comforting",
"Get regular supervision and consultation",
"Negotiate for your needs",
"Have a peer support group"
]

}

categories_list = list(categories.keys())

# -----------------------------
# PROGRESS BAR
# -----------------------------
progress = st.session_state.step / len(categories_list)
st.progress(min(progress, 1.0))

st.write(f"Step {min(st.session_state.step + 1, len(categories_list))} of {len(categories_list)}")

# -----------------------------
# NAVIGATION FUNCTIONS
# -----------------------------
def next_step():
    st.session_state.step += 1

def prev_step():
    if st.session_state.step > 0:
        st.session_state.step -= 1

def restart():
    st.session_state.step = 0
    st.session_state.responses = {}

# -----------------------------
# TXT REPORT FUNCTION
# -----------------------------
def create_txt_report():
    responses = st.session_state.responses

    total_score = sum(responses.values())
    max_score = len(responses) * 5
    percentage = (total_score / max_score) * 100

    report = []
    report.append("SELF-CARE ASSESSMENT REPORT\n")
    report.append("=" * 40 + "\n")

    report.append(f"Total Score: {total_score} / {max_score}")
    report.append(f"Overall Percentage: {percentage:.1f}%\n")

    if percentage < 40:
        report.append("Level: Low self-care (risk of burnout)\n")
    elif percentage < 70:
        report.append("Level: Moderate self-care\n")
    else:
        report.append("Level: Strong self-care\n")

    report.append("\nCATEGORY BREAKDOWN\n")
    report.append("-" * 40 + "\n")

    for category, questions in categories.items():
        cat_score = sum(responses[q] for q in questions)
        cat_max = len(questions) * 5
        cat_percent = (cat_score / cat_max) * 100

        report.append(f"{category}")
        report.append(f"Score: {cat_score}/{cat_max} ({cat_percent:.1f}%)\n")

    report.append("\nDISCLAIMER\n")
    report.append("This tool is for educational and reflective purposes only.\n")

    return "\n".join(report)

# -----------------------------
# RESULTS SCREEN
# -----------------------------
if st.session_state.step >= len(categories_list):

    responses = st.session_state.responses

    total_score = sum(responses.values())
    max_score = len(responses) * 5
    percentage = (total_score / max_score) * 100

    st.subheader("📊 Your Results")
    st.write(f"**Total Score:** {total_score} / {max_score}")
    st.write(f"**Overall Self-Care Level:** {percentage:.1f}%")

    if percentage < 40:
        st.error("⚠️ Low self-care: Risk of burnout.")
    elif percentage < 70:
        st.warning("🟡 Moderate self-care: Some balance, room to grow.")
    else:
        st.success("🟢 Strong self-care: Healthy self-care habits.")

    st.subheader("📌 Category Breakdown")

    for category, questions in categories.items():
        cat_score = sum(responses[q] for q in questions)
        cat_max = len(questions) * 5
        cat_percent = (cat_score / cat_max) * 100

        st.write(f"**{category}:** {cat_score}/{cat_max} ({cat_percent:.1f}%)")

    # DOWNLOAD TXT
    st.download_button(
        label="📄 Download TXT Report",
        data=create_txt_report(),
        file_name="self_care_assessment.txt",
        mime="text/plain"
    )

    st.button("🔄 Restart Assessment", on_click=restart)

# -----------------------------
# QUESTION FLOW
# -----------------------------
else:

    current_category = categories_list[st.session_state.step]

    st.subheader(current_category)

    for q in categories[current_category]:
        st.session_state.responses[q] = st.radio(
            q,
            [1, 2, 3, 4, 5],
            horizontal=True,
            key=q
        )

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.step > 0:
            st.button("⬅ Back", on_click=prev_step)

    with col2:
        st.button("Next ➡", on_click=next_step)
