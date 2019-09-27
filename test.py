import os

from umbral import keys, utils
from umbral.curvebn import CurveBN

def share_secret(secret, threshold, n):
    coeff = [secret] + [CurveBN.gen_rand() for _ in range(threshold - 1)]
    xs = [CurveBN.gen_rand() for _ in range(n)]
    points = [(x, utils.poly_eval(coeff, x)) for x in xs]
    return points

def recover_secret(shares):
    points = [share[0] for share in shares]
    summands = []
    for point, value in shares:
        lambda_i = utils.lambda_coeff(point, points)
        summands.append(lambda_i * point)

    return sum(summands[1:], summands[0])

def main():
    secret = CurveBN.gen_rand()
    shares = share_secret(secret, 3, 6)
    print(secret)

    print(recover_secret(shares[:3]))

if __name__ == '__main__':
    main()
