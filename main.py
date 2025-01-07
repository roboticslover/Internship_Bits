import streamlit as st

# -----------------------
# DATA: 10 CLUSTERS + PROJECT IDEAS
# -----------------------
clusters = {
    "Cluster 1 – Text-Focused Detection": [
        "1. Clickbait vs. Trustworthy Title Detector",
        "2. Satirical vs. Real News Classifier",
        "3. Opinion vs. Fact Classifier",
        "4. AI-Generated Article Catcher",
        "5. Implicit Bias Detector",
        "6. Automated Ethical Scoring",
        "7. Content Credibility Label Generator",
        "8. News Headline Generator vs. Real",
        "9. Topic Modeling & Suspicious Clusters",
        "10. Fake News 'Hall of Shame'"
    ],
    "Cluster 2 – Image-Focused Tools": [
        "1. Text-Image Fake News Classifier",
        "2. Neural Style Transfer Fakes Detection",
        "3. Image Context Understanding",
        "4. Historical Image Verification",
        "5. Image Reverse Search Integration",
        "6. Adversarial Image Attacks Detection",
        "7. Image Watermark Detection",
        "8. Propaganda Poster Recognition",
        "9. GAN Fake Image Detector",
        "10. Image Forensic Layers Analysis"
    ],
    "Cluster 3 – Audio & Speech Tools": [
        "1. Emotion-Based Detector",
        "2. Audio 'Clip Splicing' Detector",
        "3. Audio-Text Synchronization Checker",
        "4. Audio Clone Detection",
        "5. Live Transcription + Fact Checking",
        "6. Speech-to-Text Mismatch Detection",
        "7. Voice Biometrics for News Anchors",
        "8. Audio Watermarking",
        "9. Audio Speed Alteration Detector",
        "10. Speech Semantics vs. Infographic Analysis"
    ],
    "Cluster 4 – Deepfake & Video Tools": [
        "1. Video Deepfake Analysis",
        "2. Political Debates Fact-Checker",
        "3. Live-Stream Deepfake Spotter",
        "4. Video Metadata Tampering Checker",
        "5. Deepfake Face Transfer Spotter",
        "6. Altered Video Frame Detector",
        "7. Keyframes and Title Consistency",
        "8. Green Screen / Background Check",
        "9. Text-Video Fact Matching",
        "10. Audio-Visual Opinion Bias Detector"
    ],
    "Cluster 5 – Social Media & Network Analysis": [
        "1. Multi-Social-Media Fake News Aggregator",
        "2. User Credibility Scorer",
        "3. Cross-Platform Bot Network Finder",
        "4. Crowdsourced Flagging Interface",
        "5. Social Graph Analysis",
        "6. User Comment Analysis",
        "7. Meme-Genealogy Tracer",
        "8. Fake News Game / Interactive App",
        "9. Influencer-Focused Misinformation Monitor",
        "10. Clickbait Image Detection"
    ],
    "Cluster 6 – Metadata & Geolocation Tools": [
        "1. Location-Based Fake News Filter",
        "2. Timestamp Consistency Model",
        "3. Satellite Image Misinformation Detection",
        "4. 'Before and After' Photo Checker",
        "5. Geotag Mismatch Finder",
        "6. Chain-of-Custody Tracking",
        "7. Temporal Sequence Modeling",
        "8. Multi-Factor Authentication for News",
        "9. Automated Press Kit Verifier",
        "10. Online Learning Fake News Detector"
    ],
    "Cluster 7 – Fact-Checking & Summarization Tools": [
        "1. Cross-Source Verification Engine",
        "2. Multimodal Fact-Checking Chatbot",
        "3. Contextual Summarizer",
        "4. Podcast Misinformation Analyzer",
        "5. Image-Text Paraphrase Consistency",
        "6. Cross-Modal Summarization",
        "7. Political Campaign Ad Checker",
        "8. User Review Authenticity Checker",
        "9. Facial Recognition for Person-of-Interest",
        "10. OCR + Text Analysis on Newspaper Scans"
    ],
    "Cluster 8 – Domain-Specific & Specialized": [
        "1. Medical Misinformation Detector",
        "2. Cyber Threat Misinformation Monitor",
        "3. Brand Logo Misinformation Checker",
        "4. Cultural Sensitivity Fake News Filter",
        "5. AI-Verified Press Release Platform",
        "6. Consistent Headline-Body Image Detector",
        "7. Cross-Lingual Rumor Detection",
        "8. Multi-Modal Sarcasm Detection",
        "9. Ad-Focused Fake News Detection",
        "10. Trending Topic Evolution Tracker"
    ],
    "Cluster 9 – Security, Adversarial & Advanced": [
        "1. AI Penetration Testing",
        "2. Text-Based Watermark on Images",
        "3. Multi-Source Data Fusion",
        "4. Photo Authentication Using Blockchain",
        "5. AI-Driven Moderation Assistant",
        "6. Human-In-The-Loop Verification",
        "7. Confidence Scoring for Visual+Text",
        "8. ML-Driven Editorial Assistance",
        "9. Symbolic vs. Neural Hybrid System",
        "10. Article-Linked Video Summaries"
    ],
    "Cluster 10 – Mixed Multimodal & Misc": [
        "1. Hashtag & Meme Consistency Checker",
        "2. Optical Character Recognition (OCR) Meme Analysis",
        "3. Multi-Language Fake News Detector",
        "4. Sentiment + Visual Tone Fusion",
        "5. Celebrity Fake News Tracker",
        "6. Facial Expression Analysis in Interviews",
        "7. Contextual Keyword Spotter",
        "8. Sentiment Evolution Tracker",
        "9. Political Propaganda Visual Classifier",
        "10. Photo Caption Mismatch"
    ],
}

# -----------------------
# RESEARCH PROPOSAL CONTENT
# -----------------------
proposal_text = """
# **Multimodal Fake News Detection: Research Proposal** 📜

**1. Introduction**  
Fake news poses a huge challenge today, especially as it spans **multiple media types** (text, images, audio, video). A **multimodal** approach, therefore, is essential to detect and counter misinformation effectively.

**2. Problem Statement**  
- Many fake news items pair sensational text with **misleading images** or heavily edited **audio/video**.  
- With **deepfakes** and AI-generated content, it’s increasingly tough for average users (and even experts) to tell real from fake.

**3. Objectives**  
1. **Data Fusion**: Combine advanced **NLP** for text, **CNNs**/Vision Transformers for images, and relevant methods for audio/video.  
2. **Real-Time Detection**: Analyze social media or live content quickly.  
3. **Adversarial Robustness**: Ensure the system can handle deliberate attempts to bypass detection.  
4. **Scalability**: Make it easy to deploy at scale, supporting journalists, researchers, and platforms.

**4. Literature Review**  
- **NLP**: Transformer-based methods (BERT, GPT) for misinformation classification.  
- **Computer Vision**: CNN-based or Vision Transformer models for deepfake detection.  
- **Speech Processing**: Voice cloning detection, transcript mismatches.  
- **Multimodal Fusion**: Combining text + image or text + audio can significantly boost performance (Ref: Wang et al., 2021).

**5. Methodology**  
1. **Data Collection**: Gather labeled real vs. fake items from diverse platforms.  
2. **Preprocessing**: Clean and tokenize text, resize/augment images, extract audio/video features.  
3. **Model Building**:  
   - NLP + CNN (or Vision Transformer) + audio/video models.  
   - **Fusion**: Combine embeddings (late fusion) or build a multi-branch network (early fusion).  
4. **Evaluation**: Measure accuracy, precision, recall, and F1. Test with adversarial samples.

**6. Proposed Timeline**  
- **Month 1-2**: Collect data, initial text-based prototype.  
- **Month 3-4**: Integrate image/video detection.  
- **Month 5**: Evaluate, refine, adversarial testing.  
- **Month 6**: Finalize, document, and present findings.

**7. Expected Outcomes**  
- A robust **multimodal system** detecting fake news across different content types.  
- Better accuracy than single-modal approaches.  
- A reference architecture for future research.

**References**  
- Wang, X. et al. (2021). _Multimodal Deepfake Detection via Cross-Modal Consistency_.  
- Nguyen, T. et al. (2022). _Advanced Fusion Techniques for Misinformation Detection_.  
- (Add more as needed)

---

"""

# -----------------------
# STREAMLIT APP
# -----------------------
def main():
    st.set_page_config(page_title="Multimodal Fake News Detection", layout="centered")
    
    st.title("🤖 Multimodal Fake News Detection")
    st.write("Welcome to our **interactive showcase** on detecting fake news using multiple data types!")
    
    # Side navigation
    st.sidebar.title("🔎 Easy Navigation")
    menu_options = ["🏠 Home", "📜 Research Proposal", "💡 Project Clusters"]
    choice = st.sidebar.radio("Go to:", menu_options)

    if choice == "🏠 Home":
        st.markdown("""
        ### Welcome Home! 🏠
        - This app demonstrates how **multimodal** approaches can enhance **fake news detection**.
        - Explore our **Research Proposal** to dive deeper into the **objectives, methodology,** and **timeline**.
        - Or jump to **Project Clusters** for a list of **100 different project ideas**, neatly grouped into 10 thematic clusters.
        """)
        st.image("https://cdn.pixabay.com/photo/2017/08/24/13/28/fakenews-2671921_1280.jpg", 
                 caption="Misinformation can be hidden in text, images, audio, or video. A multimodal approach helps detect it all.")
        
    elif choice == "📜 Research Proposal":
        st.markdown(proposal_text)

    else:  # "💡 Project Clusters"
        st.subheader("💡 Project Clusters")
        st.write("Below are **10 clusters** of project ideas, each focusing on different aspects or modalities of fake news detection.")
        
        selected_cluster = st.selectbox("Choose a Cluster 📂:", list(clusters.keys()))
        
        st.write(f"### {selected_cluster}")
        project_list = clusters[selected_cluster]
        for idx, project in enumerate(project_list, start=1):
            st.write(f"- **{idx}.** {project}")

        st.success("Tip: Use the dropdown above to navigate between clusters!")

if __name__ == "__main__":
    main()
