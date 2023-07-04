#!/usr/bin/python3

from ChessLogic.HelperFunctions import *
from ChessLogic.ChessBase       import ChessGame, vm_list

def test_points_on_line():
    a = points_on_line((3, 3), (0, 6))
    print(a)
    print(str_b(visp((3, 3), a)))

def test_check():
    test_str  = "k-------\n"
    test_str += "pppppppp\n"
    test_str += "--------\n"
    test_str += "--------\n"
    test_str += "--------\n"
    test_str += "-q------\n"
    test_str += "--PP----\n"
    test_str += "-qKB----"
    ############ ABCDEFGH ############
    a = ChessGame(start_string=test_str, to_move='white')
    #print(a.g('a1'))
    #print(a.move('c2b1'))
    print(a.str_board())
    print(a.move('c2b1'))
    print(a.str_board())
    #print('is_check', a.is_check('black'))
    print('is_mate', a.is_mate())
    #print('is_stalemate', a.is_stalemate())
    ##print('a_move', a.move((7, 2), (7, 1)))
    #print(a.str_board())

def test_game():
    a = ChessGame()
    moves = ['e2e4', 'e7e5', 'f1d3', 'a7a6']
    for i in moves:
        print("\n\n")
        print(a.move(i))
        print(a.str_board())

def lineprint():
    print("\n\n\n\n")

def test_read_pgn():
    example_string = """[Event "F/S Return Match"]
[Site "Belgrade, Serbia JUG"]
[Date "1992.11.04"]
[Round "29"]
[White "Fischer, Robert J."]
[Black "Spassky, Boris V."]
[Result "1/2-1/2"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 {This opening is called the Ruy Lopez.}
4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7
11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15. Nb1 h6 16. Bh4 c5 17. dxe5
Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. Nc4 Nxc4 22. Bxc4 Nb6
23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7 27. Qe3 Qg5 28. Qxg5
hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33. f3 Bc8 34. Kf2 Bf5
35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5 40. Rd6 Kc5 41. Ra6
Nf2 42. g4 Bd3 43. Re6 1/2-1/2"""
    print(example_string)

if __name__ == "__main__":
    #pos = (3, 3)
    #x = vm_list('k', pos)
    #print(x)
    #print(str_b(visp(pos, x)))
    #print()
    #a = ChessGame()
    #print(a.str_board())
    #print(a.g((0, 0)))
    #test_points_on_line()
    #lineprint()
    #test_game()
    #test_check()
    #test_read_pgn()
    test_case()

