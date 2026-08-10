#!/usr/bin/env python3
"""
SERP Intelligence
A research focused framework for analyzing search results, search intent,
ranking patterns, competitor visibility, SERP features, and content
opportunities. It helps organize search data into meaningful insights for
SEO research, content planning, and organic search strategy.
https://serpchecker.fyi
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "serp_visibility": "SERP Visibility",
        "search_intent": "Search Intent",
        "ranking_pattern": "Ranking Pattern",
        "competitor_visibility": "Competitor Visibility",
        "serp_feature": "SERP Feature",
        "content_opportunity": "Content Opportunity",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_serp_channels(visibility: int, feature: int, intent: int, competitor: int) -> dict:
    return {
        "Organic Results": min(100, round(visibility * 1.0)),
        "Featured Snippets": min(100, round(feature * 1.0)),
        "People Also Ask": min(100, round(intent * 1.0)),
        "Local Pack": min(100, round(competitor * 1.0)),
    }


def analyze_serp_intelligence(
    keyword: str,
    search_intent: str = "informational",
    serp_visibility: int = 88,
    search_intent_score: int = 82,
    ranking_pattern: int = 85,
    competitor_visibility: int = 78,
    serp_feature: int = 90,
    content_opportunity: int = 84,
) -> dict:
    """
    Analyze SERP intelligence signals for SEO research and content strategy.

    Args:
        keyword: Target keyword or query
        search_intent: Type of search intent
        serp_visibility: SERP visibility score (0-100)
        search_intent_score: Search intent score (0-100)
        ranking_pattern: Ranking pattern score (0-100)
        competitor_visibility: Competitor visibility score (0-100)
        serp_feature: SERP feature score (0-100)
        content_opportunity: Content opportunity score (0-100)

    Returns:
        dict with individual signal scores, overall SERP intelligence index,
        and SERP channel breakdown
    """
    scores = {
        "serp_visibility": serp_visibility,
        "search_intent": search_intent_score,
        "ranking_pattern": ranking_pattern,
        "competitor_visibility": competitor_visibility,
        "serp_feature": serp_feature,
        "content_opportunity": content_opportunity,
    }
    overall_serp_intelligence_index = round(sum(scores.values()) / 6)

    return {
        "keyword": keyword,
        "search_intent": search_intent.capitalize(),
        "serp_visibility_score": serp_visibility,
        "search_intent_score": search_intent_score,
        "ranking_pattern_score": ranking_pattern,
        "competitor_visibility_score": competitor_visibility,
        "serp_feature_score": serp_feature,
        "content_opportunity_score": content_opportunity,
        "overall_serp_intelligence_index": overall_serp_intelligence_index,
        "priority_action": get_priority_action(scores),
        "serp_channels": get_serp_channels(serp_visibility, serp_feature, search_intent_score, competitor_visibility),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    keyword = args[0] if len(args) > 0 else "target-keyword"
    search_intent = args[1] if len(args) > 1 else "informational"
    serp_visibility = int(args[2]) if len(args) > 2 else 88
    search_intent_score = int(args[3]) if len(args) > 3 else 82
    ranking_pattern = int(args[4]) if len(args) > 4 else 85
    competitor_visibility = int(args[5]) if len(args) > 5 else 78
    serp_feature = int(args[6]) if len(args) > 6 else 90
    content_opportunity = int(args[7]) if len(args) > 7 else 84

    result = analyze_serp_intelligence(
        keyword, search_intent, serp_visibility, search_intent_score,
        ranking_pattern, competitor_visibility, serp_feature, content_opportunity
    )

    print(f"Keyword: {result['keyword']}")
    print(f"Search Intent: {result['search_intent']}")
    print("=" * 45)
    print(f"SERP Visibility Score:         {result['serp_visibility_score']}/100  [{get_status(result['serp_visibility_score'])}]")
    print(f"Search Intent Score:           {result['search_intent_score']}/100  [{get_status(result['search_intent_score'])}]")
    print(f"Ranking Pattern Score:         {result['ranking_pattern_score']}/100  [{get_status(result['ranking_pattern_score'])}]")
    print(f"Competitor Visibility Score:   {result['competitor_visibility_score']}/100  [{get_status(result['competitor_visibility_score'])}]")
    print(f"SERP Feature Score:            {result['serp_feature_score']}/100  [{get_status(result['serp_feature_score'])}]")
    print(f"Content Opportunity Score:     {result['content_opportunity_score']}/100  [{get_status(result['content_opportunity_score'])}]")
    print("=" * 45)
    print(f"Overall SERP Intelligence Index: {result['overall_serp_intelligence_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nSERP Channels:")
    for channel, score in result['serp_channels'].items():
        print(f"  {channel:<24} {score}/100")


if __name__ == "__main__":
    main()
