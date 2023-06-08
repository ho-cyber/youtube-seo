import streamlit as st

def add_google_analytics_tracking_code(tracking_id):
    """Add Google Analytics tracking code to the Streamlit app."""
    script = """
    <script async src="https://www.googletagmanager.com/gtag/js?id={tracking_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{tracking_id}');
    </script>
    """.format(tracking_id=tracking_id)
    st.markdown(script, unsafe_allow_html=True)

def send_analytics_event(category, action):
    """Send an analytics event to Google Analytics."""
    script = """
    <script>
      if (typeof gtag !== 'undefined') {{
        gtag('event', '{action}', {{
          'event_category': '{category}',
          'event_label': 'Button Click'
        }});
      }}
    </script>
    """.format(category=category, action=action)
    st.markdown(script, unsafe_allow_html=True)

# Usage example
tracking_id = "G-M26G6BJJT0"
add_google_analytics_tracking_code(tracking_id)

# Add a button that sends an analytics event when clicked
if st.button("Hello"):
    send_analytics_event("Button", "Hello")
    st.write("Button clicked!")
