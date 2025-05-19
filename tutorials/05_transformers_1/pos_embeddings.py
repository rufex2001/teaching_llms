import numpy as np
import argparse


def getPositionEncoding(seq_len, d, n=10000):
    """
    Returns matrix of positional embeddings (PE) according to original work on
    transformers.
    Source: https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/

    Args:
        seq_len (int): input length sequence
        d (int): embedding size
        n (int, optional): hyperparameter. Defaults to 10000.

    Returns:
        _type_: PE matrix
    """

    rounding = 5
    P = np.zeros((seq_len, d))
    for k in range(seq_len):
        for i in np.arange(int(d/2)):
            denominator = np.power(n, 2*i/d)
            P[k, 2*i] = np.around(np.sin(k/denominator), rounding)
            P[k, 2*i+1] = np.around(np.cos(k/denominator), rounding)
    return P
 
# P = getPositionEncoding(seq_len=4, d=4, n=100)
# print(P)


if __name__ == "__main__":

    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--seq_len', 
        required=True, 
        type=int,
        help="input sequence length"
    )
    parser.add_argument(
        '--d', 
        required=True, 
        type=int,
        help="embedding size"
    )
    parser.add_argument(
        '--n', 
        required=False, 
        type=int,
        help="hyperparameter"
    )
    args, _ = parser.parse_known_args()

    # get args
    seq_len = args.seq_len
    d = args.d
    n = 10000
    if args.n:
        n = args.n

    P = getPositionEncoding(seq_len, d, n)
    print(P)
    print("SIZE:", P.shape)

    for i in range(4):
        freq = 1/(n**((2*i)/d))
        period = (2 * np.pi) / freq
        print("i:", i)
        print("FREQ:", freq)
        print("PERIOD:", period)
