#! /usr/bin/env python3


def create_phone_number(n):
    parfit      =""
    firstfit    =""
    secfit      =""

    par     = n[:3]
    for i in range(3):
        parfit+=str(par[i])

    first   = n[3:6]
    for i in range(3):
        firstfit+=str(first[i])

    sec     = n[6:10]
    for i in range(4):
        secfit+=str(sec[i])


    phone = "({0}) {1}-{2}".format(parfit, firstfit, secfit)
    return phone
