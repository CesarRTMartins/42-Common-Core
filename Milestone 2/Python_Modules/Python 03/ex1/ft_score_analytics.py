import sys

print("=== Player Score Analytics ===")

argc = len(sys.argv)


scores = []
i = 1
nb = 0
if argc == 1:
    print("No scores provided. Usage: python3"
          " ft_score_analytics.py <score1> <score2> ...")
if argc > 1:
    while i < argc:
        try:
            nb = int(sys.argv[i])
            scores += [nb]
        except ValueError:
            print("Invalid Value")
        i += 1

    print("Scores processed:", scores)
    print("Total players:", argc)
    # Total Score
    tscore = sum(scores)
    print("Total score:", tscore)
    # Average Score
    ascore = sum(scores) / (argc - 1)
    print("Average score:", ascore)
    # High Score
    hscore = max(scores)
    print("High score:", hscore)
    # Min Score
    mscore = min(scores)
    print("Low score:", mscore)
    # Range Score
    rscore = max(scores) - min(scores)
    print("Score range:", rscore)
