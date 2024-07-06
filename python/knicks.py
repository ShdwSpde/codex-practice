# Write code below 💖
knicks = [
  {'name': 'Jalen Brunson', 'position':'PG', 'jersey':11, 'points':32.4},
  {'name': 'Mikal Bridges', 'position':'SG','jersey':1,'points':19.6},
  {'name':'OG Anunoby', 'position':'SF','jersey':8, 'points':15.1},
  {'name':'Julius Randle', 'position': 'PF', 'jersey':30, 'points':24.0},
  {'name':'Mitchell Robinson', 'position':'C', 'jersey':23, 'points':2.8},
  {'name':'Josh Hart', 'position':'SF', 'jersey':3, 'points':9.4},
  {'name':'Donte DiVincenzo', 'position':'SG', 'jersey':0, 'points':15.5}
]

print(knicks[0])

# Calculate the total points
total_points = sum(player['points'] for player in knicks)

# Calculate the average points
average_points = total_points / len(knicks)

print("Total Points:", total_points)
print("Average Points per Player:", average_points)

def run_wings(players):
    for player in players:
        if player['position'] in ['SF', 'SG']:
            print(player)

# Run the function to print players with position 'SF' or 'SG'
run_wings(knicks)


