teams = [
    {"name":"Berekum Chelsea", "points":25},
    {"name":"Dreams F.C", "points":23},
    {"name":"Hearts", "points":18}
]

print("League table")
for team in teams:
    print(team)

update = input("\nWhich team's points do you want to update: ").title()
new_points = int(input("What is the new points for the team: "))
if update == 'Berekum Chelsea':
    teams[0]['points']= new_points
elif update == 'Dreams F.C':
    teams[1]['points']= new_points
elif update == 'Hearts':
    teams[2]['points']= new_points
else:
    print("Such team does not exist in the league")

print("\n New league table")
for team in teams:
    print(team)