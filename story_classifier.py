def classify_story(headline):

    headline = headline.lower()

    if "world cup" in headline:
        return "world_cup"

    elif "champions league" in headline:
        return "champions_league"

    elif "transfer" in headline or "sign" in headline:
        return "transfer"

    elif "injury" in headline:
        return "injury"

    elif "manager" in headline or "coach" in headline:
        return "manager"

    elif "sacked" in headline:
        return "manager"

    elif "premier league" in headline:
        return "premier_league"

    else:
        return "general"
