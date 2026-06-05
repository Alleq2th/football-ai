def score_story(headline):

    headline = headline.lower()

    score = 0

    keywords = {

        # World Cup
        "world cup": 25,
        "fifa world cup": 25,
        "world cup qualifier": 20,
        "world cup fixture": 20,

        # European competitions
        "champions league": 20,
        "uefa champions league": 20,
        "europa league": 15,
        "conference league": 12,

        # Major stages
        "final": 18,
        "semi-final": 15,
        "quarter-final": 12,

        # Transfers
        "transfer": 10,
        "sign": 10,
        "deal": 10,

        # Management
        "manager": 10,
        "coach": 10,
        "sacked": 20,

        # Injuries
        "injury": 8,

        # Major leagues
        "premier league": 10,
        "la liga": 10,
        "serie a": 10,
        "bundesliga": 10,

        # Big players
        "messi": 15,
        "ronaldo": 15,
        "mbappe": 15,
        "haaland": 15,
        "bellingham": 12,

        # Big clubs
        "arsenal": 8,
        "manchester united": 8,
        "man city": 8,
        "liverpool": 8,
        "chelsea": 8,
        "barcelona": 8,
        "real madrid": 8,
        "bayern": 8
    }

    for word, points in keywords.items():

        if word in headline:
            score += points

    return score
