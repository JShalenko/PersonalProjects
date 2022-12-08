# bruteForceSudoku

'''
This Python project was inspired by my love and hate for harder sudoku games. I've always enjoyed the puzzling experience, but the methods of the 'evil' or 'extreme'
sudoku puzzles were ridiculous and I found myself less interested in the challenge over time.

Essentially, this program follows three primary steps as outlined by the funcitons developed.

1. The Import and Board Setup Phase
2. The Reduction Phase
and finally 3. The Forcing Phase

Phase 1 is self explantatory: based on the file being formatted properly, the function takes in all data from the text file and puts it into a 2D list in the python 
language, each of the nine elements containing a sublist of nine more elements. A __str__ function is defined to output the 'board' to the command line, where this 
file has to be run.

Phase 2 is a little bit of a simplistic preliminary run through of all the elements, going row by row and column by column. It goes into each element of the list and
determines if a 'simple solution' exists, i.e. there is only one(1) possible answer for the given space. If it finds one, without complication, the Block element will
have it's preliminary value updated and the stored list element emptied accordingly. Another important part of this phase is that it also reduces the values that each
left over empty box cannot be.

The third and final phase is the most complex and hardest to explain. In coding terms, it acts as a Depth-First Search algorithm that recursively calls upon itself to
try and finalize the puzzle, back-tracking and re-iterating as necessary for runtime completion. To break it down, essentially, the algorithm goes through each of the 
still emptied boxes and tries to determine via the remaining elements of the list property if the elements can be input properly and will fall back on itself if it runs
into any major errors.

Take the following example for instance(let's assume that phase one and two have been executed):

The Best value for the second box would be to see if 3 works, where it would then go from all the possible elements to a point that it might run into a conflicting 
result (in this case it will as 3 is not the correct value associated with the location) at which point it will undo all the prior steps it committed and try the next
value possible                                                                 

                                                                                    (second to last item couldn't be any value)   (tries 8 next to see if it's fixed)
4 _ 9 | 2 7 _ | _ _ _                 4 3 9 | 2 7 _ | _ _ _                                    4 3 9 | 2 7 5 | 6 x _                   4 3 9 | 2 7 5 | 8 _ _
_ _ _ | 4 _ _ | _ 3 _                 _ _ _ | 4 _ _ | _ 3 _                                    _ _ _ | 4 _ _ | _ 3 _                   _ _ _ | 4 _ _ | _ 3 _
_ 1 6 | _ 8 _ | _ _ 7                 _ 1 6 | _ 8 _ | _ _ 7                                    _ 1 6 | _ 8 _ | _ _ 7                   _ 1 6 | _ 8 _ | _ _ 7
― ― ― + ― ― ― + ― ― ―                 ― ― ― + ― ― ― + ― ― ―                                    ― ― ― + ― ― ― + ― ― ―                   ― ― ― + ― ― ― + ― ― ―
_ _ _ | 6 _ 9 | _ 2 _                 _ _ _ | 6 _ 9 | _ 2 _                                    _ _ _ | 6 _ 9 | _ 2 _                   _ _ _ | 6 _ 9 | _ 2 _
8 _ 4 | 5 _ 1 | 7 6 3 - - - - - - - > 8 _ 4 | 5 _ 1 | 7 6 3 - - - - - - - > (continued until)  8 _ 4 | 5 _ 1 | 7 6 3 - - (undo) - - >  8 _ 4 | 5 _ 1 | 7 6 3
2 6 5 | 7 _ 8 | 4 _ 9                 2 6 5 | 7 _ 8 | 4 _ 9                                    2 6 5 | 7 _ 8 | 4 _ 9                   2 6 5 | 7 _ 8 | 4 _ 9 
― ― ― + ― ― ― + ― ― ―                 ― ― ― + ― ― ― + ― ― ―                                    ― ― ― + ― ― ― + ― ― ―                   ― ― ― + ― ― ― + ― ― ―
1 _ _ | _ 6 _ | _ _ _                 1 _ _ | _ 6 _ | _ _ _                                    1 _ _ | _ 6 _ | _ _ _                   1 _ _ | _ 6 _ | _ _ _
_ 4 2 | _ _ _ | 3 8 _                 _ 4 2 | _ _ _ | 3 8 _                                    _ 4 2 | _ _ _ | 3 8 _                   _ 4 2 | _ _ _ | 3 8 _
_ _ _ | 8 _ _ | 1 _ 4                 _ _ _ | 8 _ _ | 1 _ 4                                    _ _ _ | 8 _ _ | 1 _ 4                   _ _ _ | 8 _ _ | 1 _ 4


Eventually it will spit out the correct answer:
4 8 9 | 2 7 3 | 6 5 1 
5 2 7 | 4 1 6 | 9 3 8 
3 1 6 | 9 8 5 | 2 4 7 
― ― ― + ― ― ― + ― ― ―
7 3 1 | 6 4 9 | 8 2 5 
8 9 4 | 5 2 1 | 7 6 3 
2 6 5 | 7 3 8 | 4 1 9 
― ― ― + ― ― ― + ― ― ―
1 7 8 | 3 6 4 | 5 9 2 
9 4 2 | 1 5 7 | 3 8 6 
6 5 3 | 8 9 2 | 1 7 4 

Some notes:
1. By no means is this the most effecient algorithm. I made this about half way through my Data Structures course and while it does get the answer every single time
(tested approximately 40 different games of various difficulties), it is rather slow at times.
2. Even though this might seem impressive, if you've read the comments in the main file, you know this was done out of sheer boredom and served no real purpose besides
me wanting to be entertained.
'''
