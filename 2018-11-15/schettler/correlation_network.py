#!/usr/bin/env python
#
# Matt Schettler
# Nov 2018
# 
# https://github.com/ccomings/hft-coding-challenges/blob/master/2018-11-15/word-search.md
# 
import sys
import itertools

try:
    import pandas as pd
except ImportError:
    print('[ImportError] you probably need to run:   pip install pandas')
    sys.exit(1)


SMALL_BOARD = [
    ['A', 'B'],
    ['C', 'D'],
]


LARGE_BOARD = [ 
    ['C', 'A', 'T', 'D', 'O'],
    ['Y', 'Z', 'X', 'V', 'G'],
    ['R', 'P', 'N', 'J', 'U'],
    ['S', 'L', 'E', 'I', 'Q'],
]


class CorrelationNetwork:

    @classmethod
    def compile_links(cls, board):
        """ returns a pandas dataframe network like object ie
               C  A  T  D  O  Y  Z  X  V  G  R  P  N  J  U  S  L  E  I  Q
            C  0  1  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0
            A  1  0  1  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0
            T  0  1  0  1  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0
            D  0  0  1  0  1  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0
            O  0  0  0  1  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0
            Y  1  0  0  0  0  0  1  0  0  0  1  0  0  0  0  0  0  0  0  0
            Z  0  1  0  0  0  1  0  1  0  0  0  1  0  0  0  0  0  0  0  0
            X  0  0  1  0  0  0  1  0  1  0  0  0  1  0  0  0  0  0  0  0
            V  0  0  0  1  0  0  0  1  0  1  0  0  0  1  0  0  0  0  0  0
            G  0  0  0  0  1  0  0  0  1  0  0  0  0  0  1  0  0  0  0  0
            R  0  0  0  0  0  1  0  0  0  0  0  1  0  0  0  1  0  0  0  0
            P  0  0  0  0  0  0  1  0  0  0  1  0  1  0  0  0  1  0  0  0
            N  0  0  0  0  0  0  0  1  0  0  0  1  0  1  0  0  0  1  0  0
            J  0  0  0  0  0  0  0  0  1  0  0  0  1  0  1  0  0  0  1  0
            U  0  0  0  0  0  0  0  0  0  1  0  0  0  1  0  0  0  0  0  1
            S  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0  1  0  0  0
            L  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  0  1  0  0
            E  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  0  1  0
            I  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  0  1
            Q  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  1  0
        """

        # compute 1 row width
        width = len(board[0])

        # flatten board to a 1d list
        flat_board = list(itertools.chain(*board))

        # compute total board length
        board_width = len(flat_board)

        # allocate a frame of 0s with proper columns and index
        df = pd.DataFrame(0, columns=flat_board, index=flat_board)

        # form links, one full loop of the board
        for y in range(board_width - 1):

            # 2 main skipping chains
            df.ix[y][y + 1] = df.ix[y + 1][y] = (y + 1) % width

            try:
                # 2 solid side chains
                df.ix[y][y + width] = df.ix[y + width][y] = y + width < board_width
            except IndexError:
                pass
            
        # make sure we cast any ints to bool on exit
        return df.astype(bool)

    @classmethod
    def does_network_have_substring(cls, df, substr):

        # track the used nodes
        used = set()

        # track position in the substring
        itr = iter(substr.upper())

        # starting point
        node = itr.next()

        while 1:

            try:
                # match a letter to a index/row, raises KeyError if no jumpoff points found
                jumpoff_points = df.loc[node]
            
                possible_landings = {t for t in jumpoff_points[jumpoff_points].index.values if t not in used}
                if not possible_landings:
                    # no valid landing; tick iterator to make sure we arent at the end
                    # if we are at the end, we passed, if not, we failed
                    itr.next()
                    raise KeyError

                # it's a valid target, record it
                used.add(node)

                # iterate to next node, may raise StopIteration
                node = itr.next()
                
                if node not in possible_landings:
                    # cant map next destination at all
                    raise KeyError

            except KeyError:
                # failed to find a jump target
                return False

            except StopIteration:
                # we were able to form a path through the entire string
                return True

    @classmethod
    def main(cls):

        # build networks
        network_small = CorrelationNetwork.compile_links(SMALL_BOARD)
        network_big = CorrelationNetwork.compile_links(LARGE_BOARD)

        # shortcut
        f = CorrelationNetwork.does_network_have_substring

        #########
        # tests #
        #########
        assert not f(network_small, 'AD')
    
        assert not f(network_small, 'DA')
        assert not f(network_small, 'BC')
        assert not f(network_small, 'CB')
        assert not f(network_small, '123')

        assert f(network_small, 'AB')
        assert f(network_small, 'BD')
        assert f(network_small, 'DC')
        assert f(network_small, 'CA')
        assert f(network_small, 'BA')
        assert f(network_small, 'DB')
        assert f(network_small, 'CD')
        assert f(network_small, 'AC')

        assert f(network_small, 'ABD')
        assert f(network_small, 'ABDC')
        assert f(network_small, 'ACD')
        assert f(network_small, 'ACDB')

        assert not f(network_big, 'XP')
        assert not f(network_big, 'XzzdasdasdsadP')
        assert not f(network_big, 'XP1')
        assert not f(network_big, 'XP2')
        assert not f(network_big, 'XP3')
        assert not f(network_big, 'XP4')
        assert not f(network_big, 'XP')
        assert not f(network_big, 'AB')

        assert f(network_big, 'CY')
        assert f(network_big, 'CA')
        assert f(network_big, 'CAT')
        assert f(network_big, 'CAZX')
        assert f(network_big, 'CAT')
        assert f(network_big, 'CATDOG')
        assert f(network_big, 'catdog')  # lowercase
        assert not f(network_big, 'CATDGO')
        assert not f(network_big, 'CYRSLTE')
        assert not f(network_big, 'CYRSLTZATXNEOIADOGUX')
        assert f(network_big, 'CYRSLPZATXNEIJVDOGUQ')

        # ones with repeats
        assert not f(network_small, 'ABDCA')
        assert not f(network_small, 'ABCDA')
        assert not f(network_small, 'AA')
        assert not f(network_small, 'BB')
        assert not f(network_small, 'BB')
        assert not f(network_small, 'CDD')
        assert not f(network_small, 'CDAA')
        assert not f(network_small, 'AADC')
        
        assert not f(network_big, 'YCY')
        assert not f(network_big, 'CAC')
        assert not f(network_big, 'CATT')
        assert not f(network_big, 'GODTACC')
        
        print "well, it worked!\n"

        print "here's the network we used"
        print network_big.astype(int)  # ints look nicer than "True" "False"


if __name__ == '__main__':
   CorrelationNetwork.main()
