# O(n) time | O(k) space

HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}
    print('Keeping track of scores', scores)
    
    for idx, competition in enumerate(competitions):
        print('Checking idx, competition', idx, competition)
        result = results[idx]
        print('What does result do???????', result)
        homeTeam, awayTeam = competition
        print('##### hometeam and away', homeTeam, awayTeam)
        
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        print('$$$$ checking the boolean', winningTeam)
        
        updateScores(winningTeam, 3, scores)
        if scores[winningTeam] > scores[currentBestTeam]:
            print('How are we comparing on the data structure?', scores[winningTeam], scores[currentBestTeam])
            currentBestTeam = winningTeam
    return currentBestTeam

def updateScores(team, points, scores):
    print('This is what we send to updateScores', team, points, scores)
    if team not in scores:
        scores[team] = 0
    scores[team] += points
    
print(tournamentWinner([['HTML', 'C#'], ['C#', 'PYTHON'], ['PYTHON', 'HTML']], [0,0,1]))