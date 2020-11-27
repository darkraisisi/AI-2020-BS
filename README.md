# AI-2020-BS
HBO ICT AI 2020: Behaviour-based Simulation

# Working with sub tree
<a href='https://medium.com/@thoferon/git-subtrees-for-fun-and-profit-a18eef31ef3e'>Source</a><br>

git remote add game_of_life git@github.com:USERNAME/game_of_life.git

git fetch game_of_life

git subtree pull --prefix='Test-driven development' game_of_life master

git subtree push --prefix='Test-driven development' game_of_life master