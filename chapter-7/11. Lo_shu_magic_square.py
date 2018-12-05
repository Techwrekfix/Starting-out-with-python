#This program is a Lo Shu Magic Square
ROWS = 3
COLS = 3
def main():
    lo_shu_list = [[4,9,2],
                   [3,5,7],
                   [8,1,6]]
    
    #filling the list with values
    for r in(lo_shu_list):
        for c in range(COLS):
            if sum(r) == sum (lo_shu_list[c][c] for c in range(COLS)):
                if sum(r)== sum(r[c] for r in lo_shu_list):
                    answer_output = str('a Lo Shu Magic Square')
            else:
                answer_output = str('not a Lo Shu Magic Square')

    print("The inputs are", answer_output)
    
main()
