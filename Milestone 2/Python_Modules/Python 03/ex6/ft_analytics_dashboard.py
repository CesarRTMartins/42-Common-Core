print("=== Game Analytics Dashboard ===")
print()
players = ["alice", "bob", "charlie", "diana"]
scores = [2300, 1800, 2150, 2050]
active = [True, True, True, False]
regions = ["north", "east", "central", "east"]

achievements = {
    "alice": ["first_kill", "level_10", "boss_slayer", "speed_run",
              "collector"],
    "bob": ["first_kill", "level_10", "collector"],
    "charlie": ["first_kill", "level_10", "boss_slayer",
                "collector", "speed_run", "elite", "veteran"]
}

print("=== List Comprehension Examples ===")

high_scorers = [players[i] for i in range(len(players)) if scores[i] > 2000]

scores_doubled = [s * 2 for s in scores]

active_players = [players[i] for i in range(len(players)) if active[i]]

print("High scorers (>2000):", high_scorers)
print("Scores doubled:", scores_doubled)
print("Active players:", active_players)
print()

print("=== Dict Comprehension Examples ===")

player_scores = {players[i]: scores[i] for i in range(3)}

score_categories = {
    "high": len([s for s in scores if s >= 2100]),
    "medium": len([s for s in scores if 1900 <= s < 2100]),
    "low": len([s for s in scores if s < 1900])
}

achievement_counts = {p: len(a) for p, a in achievements.items()}

print("Player scores:", player_scores)
print("Score categories:", score_categories)
print("Achievement counts:", achievement_counts)
print()

print("=== Set Comprehension Examples ===")

unique_players = {p for p in players}

unique_achievements = {a for lst in achievements.values()
                       for a in lst}

active_regions = {regions[i] for i in range(len(regions)) if active[i]}


print("Unique players:", unique_players)
print("Unique achievements:", unique_achievements)
print("Active regions:", active_regions)
print()

print("=== Combined Analysis ===")

total_players = len(players)

all_achievements = {a for lst in achievements.values() for a in lst}

average_score = sum(scores) / len(scores)

player_scores_full = {players[i]: scores[i] for i in range(len(players))}
top_player = max(player_scores_full, key=player_scores_full.get)

print("Total players:", total_players)
print("Total unique achievements:", len(all_achievements))
print("Average score:", average_score)
print("Top performer:", top_player, "(", player_scores_full[top_player],
      "points,", len(achievements[top_player]), "achievements)")
