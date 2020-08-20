categories = [
    'Porn',
    'Science: Life Sciences',
    'Religion',
    'Science: Other Science',
    'Sport',
    'Science: Engineering and Technology',
    'Public Services',
    'Science: Social Sciences',
    'Healthcare',
    'Non-Governmental Organization',
    'Business',
    'Art',
    'Media: Scientific News and Communication',
    'Outspoken Political Supporter',
    'Government and Politics',
    'Media: Other Media',
    'Media: News',
    'Other'
]

categories_coarse = [
    'Art',
    'Business',
    'Government and Politics',
    'Healthcare',
    'Media',
    'Non-Governmental Organization',
    'Outspoken Political Supporter',
    'Porn',
    'Public Services',
    'Religion',
    'Science',
    'Sport',
    'Other'
]

categories_final = {
    'Art': "Arts and Entertainment",
    'Business': "Business",
    'Government and Politics': 'Government and Politics',
    'Healthcare': "Healthcare",
    'Media': "News Media",
    'Non-Governmental Organization': "NGO",
    'Outspoken Political Supporter': 'Political Supporter',
    'Porn': "Adult",
    'Public Services': "Public Services",
    'Religion': "Religion",
    'Science': "Science",
    'Sport': "Sports",
    'Other': "Other"
}

types = [
    'Individual:Male',
    'Institution',
    'Individual: Other gender or unclear',
    'Unclear',
    'Individual:Female'
]

langs = ['en', 'ja', 'es', 'pt', 'ar', 'fr', 'de', 'it']

lang_names = {
    'ar': "Arabic",
    'de': "German",
    'en': "English",
    'es': "Spanish",
    'fr': "French",
    'it': "Italian",
    'ja': "Japanese",
    'pt': "Portuguese"
}

lang_colors = {
    'ar': "#66c2a5",
    'de': "#fc8d62",
    'en': "#8da0cb",
    'es': "#e78ac3",
    'fr': "#a6d854",
    'it': "#ffd92f",
    'ja': "#e5c494",
    'pt': "#b3b3b3"
}

quint = {

    "en": {
        "followers": [0.0, 679.2000000000007, 2802.0, 8539.0, 30881.40000000001, 117399818.0],
        "retweets": [10.0, 12.0, 17.0, 28.0, 63.0, 256410.0]
    },
    "ja": {
        "followers": [0.0, 251.0, 1063.0, 3012.0, 9850.0, 46532655.0],
        "retweets": [10.0, 13.0, 18.0, 29.0, 67.40000000000146, 183857.0]
    },

    "es": {
        "followers": [0.0, 614.0, 2408.0, 6951.0, 23952.80000000003, 28020637.0],
        "retweets": [10.0, 12.0, 17.0, 28.0, 64.0, 35009.0]
    },

    "pt": {
        "followers": [0.0, 413.0, 1288.8000000000002, 4215.599999999997, 19235.200000000004, 27989186.0],
        "retweets": [10.0, 12.0, 17.0, 28.0, 72.0, 46605.0]
    },

    "in": {
        "followers": [0.0, 298.0, 2062.0, 8261.0, 39730.0, 21910623.0],
        "retweets": [10.0, 12.0, 18.0, 31.0, 80.0, 21927.0]
    },

    "hi": {
        "followers": [0.0, 53.0, 443.0, 2353.0, 11332.800000000007, 35309296.0],
        "retweets": [10.0, 13.0, 18.0, 28.0, 52.0, 14569.0]
    },

    "fr": {
        "followers": [0.0, 875.0, 3182.000000000001, 8141.200000000003, 26447.000000000036, 21918353.0],
        "retweets": [10.0, 12.0, 16.0, 25.0, 54.0, 12469.0]
    },

    "de": {
        "followers": [0.0, 930.2, 2631.0, 5986.4, 18791.2, 4860892.0],
        "retweets": [10.0, 12.0, 16.600000000000023, 27.0, 56.0, 7074.0]
    },

    "it": {
        "followers": [0.0, 1300.0, 3549.4, 8534.799999999997, 31766.200000000004, 12910331.0],
        "retweets": [10.0, 12.400000000000034, 17.0, 27.0, 56.0, 12969.0]
    },

    "ar": {
        "followers": [0.0, 2192.0, 9515.6, 26217.799999999996, 103688.80000000005, 19436193.0],
        "retweets": [10.0, 13.0, 18.0, 30.0, 67.0, 6697.0]
    }
}


def nicer_words(category):
    """ This changes some of the names of the categories for plotting! """
    return category.replace("Science: ", "") \
        .replace("Media: ", "") \
        .replace(" and Communication", "") \
        .replace("Non-Governmental Organization", "Non-Govt. Org.") \
        .replace("Political", "Pol.") \
        .replace("Government", "Govt.") \
        .replace("Engineering", "Eng.") \
        .replace(" Other gender or u", "U")


def coarsify_category(name):
    if 'Science' in name:
        return 'Science'
    elif 'Media' in name:
        return 'Media'
    elif 'Not in English' in name:
        return 'Other'
    else:
        return name


def remove_not_in_english(name):
    if 'Not in English' in name:
        return 'Other'
    else:
        return name
