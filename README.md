# Picross Principle of Inclusion Exclusion
Picross/Nonograms is a puzzle game involving m x n grids where the player must fill in tiles based on a list of clues. These clues dictate the order and number of tiles that must be filled in, but leaves out information on how big gaps of no color are. This principle of giving some information but not all of it makes for a fun game, but presents many mathmatical questions. For a more detailed explanation on picross, I recommend https://webpbn.com/ as a first resource. For the use of explanations (mostly for myself) I refer to a solvable grid as unique if there exists exactly one grid that fits the provided clues. A grid is not-unique if the provided instructions can lead to more than one version of the grid. A grid is not-solvable if the provided instructions do not produce any grids. I am focusing on the former two with this program.

I noticed a simple pattern in the 2x2 grid that is not-unique; it looks like a tiny checkerboard. There exists two out of sixteen combinations that are not uniquely solvable. But what about 3x3 grids? That's a little harder to brute force, so that's where programming comes in. To start I aim at counting possible grids and then expanding to this question of "uniqueness" with averages and stuff (that I currently don't know enough about to accurate access how big a sample size I need, but thats a future me problem).

Another element of this game is color. If a puzzle has more than one color, those two colors don't need a blank gap to seperate them. This alters some solving techniques from the simple single color grid. It also presents more questions about uniqueness. To start, I want to calculate the number of possible grids of several colors and several sizes. Turns out this is a fantastic place to use the Principle of Inclusion Exclusion (PIE). I want to take these findings and export them into an excel file to notice trends, specifically at how many colors do fewer grids become possible. I believe adding more colors makes grids more solvable, but I'm also curious about the ratio of possible grids to unique ones. 

Line logic is the term used to describe using the clues from a single row or colmun to solve that line. This can include finding tiles that must be filled a certain color or must be white, along with solving the whole line. Edge logic is when solving a line along the edge of the border helps determine more squares in other lines. These two strategies can get you pretty far, but advanced puzzles make use of other techniques. Snaking is a version of this, that has only one solution but line logic won't get you there. (somehow i need to include an example here) For the simplcity of my program, I plan on marking these cases as ambiguous and re-evaluating how to handle them later. 

Further questions can be asked about Picross, such as how many boards exist that require more than line and edge logic to be solved. 

I am using Github to track my progress and log issues, and using the README as a log of when issues arrise and how I solve them. I will move text to a serperate file once the project is completed for a more polished look, but for now I think it's interesting to make clear my thoughts on my incomplete program.

# 7/2/2024 and 7/3/2024

Today wrote the background of the README file, configured this project with GitHub, and wrote the basic skeleton of the program. More detailed notes on specific aspects can be found in the commit of the corresponding date.

# 7/15/2024

Today I added the main logic in for PIE, with alternating between adding and subtracting elements based on the modulo of the number of colors currently being tested. Scattered print statements to test the correct output of the code still remain. The binomial coefficents work as intended, but I realize I need to add recursion to avoid repeat cases. I noted in the code where this should happen. I'm going to brainstorm the best way to go about this, for now I'm unsure if I should rewrite the bulk of the code to make it more compatable with recursion, or if it's possible to keep this the same.

I also realized that some of my numbers may get to large to be stored as integers. This would be fine, but I still need to do calculations with these. I believe Python can handle this with long integers, but yet again with recursion my calls might take too long. As of now I only plan on calculating for 20x20 boards as a maximum, but 2^400 is too large for my calculator to handle, and 2^325 is already a 98 digit number... I am just now realizing a 20x20 board might even not be feasible. I suppose there's a reason no one else has done this! I think I'll be okay for the meantime; I'll finish the code, get the data I can, and I can work on another solution if I deem it necessary. 

# 7/16/2024

I need to come back with a fresh mind and rethink the layout of the program. For the recursion, is the base case c==i? I think it should be i==2, but based on how I set up the program I need to start with i=c and i-- rather than i=2 and i++. I've been messing with the code for about 2 hours but I'll get nowhere if I don't even know what the plan of attack is. I'll do some thinking on the side and come back to this.

# 7/17/2024

I had an epiphany last night and realized my error is with how I count the blank board. There are 16 ways to fill a 2x2 board with each square being blank or black, 2^4. But this also counts the board where none of the squares are colored, which we don't count as a valid board. In all other cases, take 3^4, each board must contain 2 different colors. So by defintion, the blank board doesn't hit the requirements for the base case. How I play with this idea is what is causing the error to be too large. I also noticed a few more bugs, but I can't really test and work those out until I fix this issue. I need to rework the base case and confirm that the binomial coefficents are calculated correctly. After that the bulk of the program should be done, and I just need to format how I want exports to the terminal in order to plan for integration with Excel. As always, notes are in the files with the corresponding date. I made distint notes of where I went wrong last time.
