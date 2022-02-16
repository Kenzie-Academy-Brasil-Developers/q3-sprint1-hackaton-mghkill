# Seu código aqui
hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_score(team_name, teams):
    for str in enumerate(teams):
        if team_name == str[1]:
            return f"A {str[1]} ficou classificada em {str[0] + 1}"
            

get_score("Team Ateliware", hackathon_1)

