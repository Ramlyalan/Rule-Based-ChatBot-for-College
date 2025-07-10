import re

# Keyword-based quick responses
keyword_responses = {
    "hostel": {
        "text": "Karunya hostels are clean, secure, and equipped with Wi-Fi and modern amenities.",
        "image": "/static/images/hostel.jpeg"
    },
    "faculty": {
        "text": "Our faculty members are experienced, highly qualified, and committed to excellence.",
        "image": "/static/images/faculty.png"
    },
    "campus": {
        "text": "Karunya University has a lush green 700-acre campus with state-of-the-art infrastructure.",
        "image": "/static/images/campus1.jpg"
    }
}

# Regex-based flexible patterns
pattern_responses = [
    {
        "pattern": r"(facility|infrastructure|campus|amenities)",
        "text": "Our lush green campus features cutting-edge labs, auditoriums, sports grounds, and food courts. All buildings are Wi-Fi enabled and designed for holistic education.",
        "image": "static/images/facilities.jpeg"
    },
    {
        "pattern": r"(library|reading|books)",
        "text": "The central library has over 1.5 lakh books and journals. It offers digital access, peaceful reading zones, and group study spaces.",
        "image": "/static/images/library.jpg"
    },
    {
        "pattern": r"(lab|labs|laboratory|computer|electronics)",
        "text": "There are over 50 labs across departments including AI, IoT, Embedded Systems, Civil Engineering, and Biotechnology.",
        "image": "/static/images/labs.jpg"
    },
    {
        "pattern": r"(sports|ground|basketball|football|cricket|gym)",
        "text": "Students enjoy a cricket ground, football field, basketball courts, indoor stadium, gym, and even yoga centers.",
        "image": "/static/images/sports.jpg"
    },
    {
        "pattern": r"(faculty|teachers|staff)",
        "text": "Karunya has highly qualified faculty with international exposure. Professors are approachable and focused on both academic and personal growth.",
        "image": "/static/images/faculty.jpg"
    }
]

# Chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Step 1: Check keyword-based answers
    for keyword in keyword_responses:
        if keyword in user_input:
            return keyword_responses[keyword]

    # Step 2: Pattern-based match
    for item in pattern_responses:
        if re.search(item["pattern"], user_input):
            return {
                "text": item["text"],
                "image": item["image"]
            }

    # Step 3: Default fallback
    return {
        "text": "I'm trained to answer only Karunya-related academic queries. 😊",
        "image": ""
    }
