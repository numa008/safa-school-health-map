def classify_risk(score):
    """
    Classify school exposure risk based on total vulnerability score.
    """
    if score >= 75:
        return "Critical"
    elif score >= 55:
        return "High"
    elif score >= 30:
        return "Medium"
    else:
        return "Low"


def calculate_risk_score(
    distance_to_landfill_km,
    open_burning_reports,
    visible_waste_score,
    collection_gap_score
):
    """
    Simple prototype scoring model.

    Lower distance to landfill increases risk.
    More open-burning reports increase risk.
    Visible waste and collection gaps increase risk.
    """

    score = 0

    if distance_to_landfill_km <= 2:
        score += 35
    elif distance_to_landfill_km <= 5:
        score += 25
    elif distance_to_landfill_km <= 10:
        score += 10

    score += min(open_burning_reports * 5, 25)
    score += visible_waste_score
    score += collection_gap_score

    return min(score, 100)


if __name__ == "__main__":
    sample_score = calculate_risk_score(
        distance_to_landfill_km=1.2,
        open_burning_reports=5,
        visible_waste_score=12,
        collection_gap_score=10
    )

    print("Risk score:", sample_score)
    print("Risk category:", classify_risk(sample_score))
