# Create two sets
cricket_players = {"Virat Kohli", "Rohit Sharma", "MS Dhoni", "Jasprit Bumrah", "Hardik Pandya"}
football_players = {"Cristiano Ronaldo", "Lionel Messi", "Neymar", "Rohit Sharma", "Virat Kohli"}

# Players playing both sports
both_sports = cricket_players & football_players
print(f"Players playing both sports: {both_sports}")

# Players playing only cricket
only_cricket = cricket_players - football_players
print(f"Players playing only cricket: {only_cricket}")

# Players playing only football
only_football = football_players - cricket_players
print(f"Players playing only football: {only_football}")

# Total unique players
total_unique = cricket_players | football_players
print(f"Total unique players: {total_unique}")
print(f"Total count: {len(total_unique)}")
