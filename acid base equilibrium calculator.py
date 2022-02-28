from __future__ import division
import math

type = input("please tell me which type you want: dissociation, titration : ")

if type == "titration":
    #input
    monoprotic = "monoprotic"
    diprotic = "diprotic"
    triprotic = "triportic"
    case1 = input("Please type one of the following: monoprotic, diprotic, triprotic :")

    if case1 == "monoprotic":
        kA1 = input("enter ka1 value: ")


        ka1 = float(kA1)


        #pka1 = input("Enter pKa1 value: ")
        #pka2 = input("Enter pKa2 value: ")
        #pka3 = input("Enter pKa3 value: ")

        #pKa1 = float(pka1)
        #pKa2 = float(pka2)
        #pKa3 = float(pka3)

        #HPos = input("Enter H+ value: ")
        #OHNeg = input("Enter OH- value: ")
        #HH2A = input("Enter H+ with H2A value")
        OHNegative = input("enter OH- [OH] value : ")
        LOh = input("Enter L of OH-: ")
        LH3A = input("Enter L of H3A: ")
        H3a = input("Enter [H3A] value: ")

        #Hpos = float(HPos)
        #OHneg = float(OHNeg)
        #HH2a = float(HH2A)
        OHnegative = float(OHNegative)
        LOH = float(LOh)
        LH3a = float(LH3A)
        H3A = float(H3a)

        #X10 = Hpos
        #Y10 = OHneg
        #X13 = HH2a

        # H3A
        AL3 = LH3a * H3A
        AJ3 = OHnegative * LOH
        AJ4 = AJ3 / (LOH + LH3a)
        AJ6 = LOH - LH3a
        AJ7 = AJ3 - AL3
        AJ8 = LOH + LH3a
        AJ9 = AJ7 / AJ8
        AM4 = AL3 - AJ3
        AM5 = AM4 / (LOH + LH3a)
        AF2 = AJ4

        # ae block
        AE6 = ka1 * AM5
        AE8 = 1
        AE10 = (-1) * AE6
        AE11 = AF2 + ka1
        AE12 = AE11 ** 2
        AE13 = AE12 - (4 * 1 * AE10)
        AE14 = math.sqrt(AE13)
        AE15 = (AE11 * -1) + AE14
        AE16 = AE15 / (2 * AE8)

        AE3 = AM5 - AE16

        # y-aa
        Y2 = ka1


        #AB3 = pKa1
        #AC3 = pKa2
        #AD3 = pKa3

        if Y2 == 0:
            AB2 = 0
        else:
            AB2 = (math.log10(Y2) * -1)



        #Y4 = 10 ** (-1 * AB3)
        #Z4 = 10 ** (-1 * AC3)
        #AA4 = 10 ** (-1 * AD3)
        if Y2 == 0:
            AB7 = 0
        else:
            AB7 = 0.000000000000001 / Y2



        # af block
        AF2 = AJ4
        AF3 = AE16

        AF9 = AE16




        # AG

        # AG7=X10*AH2
        AG9 = AE16

        # X block
        X9 = AE16 + 0.0000001 + 0
        X14 = X9

        if X9 <= 0:
            X3 = 0
        else:
            X3 = (math.log10(X9) * -1)
        pH = X3
        # if X10 <= 0:
        #   X4 = 0
        # else:
        #    X4 = (math.log10(X10) * -1)

        X18 = AE16 + 0.0000001
        if AE3==0:
            X19=0
        else:
            X19 = AF2 / AE3
        if X19 <= 0:
            X20 = 0
        else:
            X20 = math.log10(X19)

        X5 = AB2 + X20
        if AJ9 <= 0:
            X6 = 0
        else:
            X6 = (math.log10(AJ9) * -1)

        # misc block
        AF7 = X9 * 0
        Z9 = 14 - X3
        Y9 = (10 ** -Z9)
        Y11 = 10 ** (-X6)
        Z10 = 14 - X5
        Z11 = 14 - X6
        # X block pt 2
        HHE = X5
        EB = X6
        X7 = (AB2 + 0) / 2
        EP = X7
        NpH = 14 - (X3)
        NHHE = 14 - (X5)
        NEB = 14 - (X6)

        # final

        H3AF = AM5-AF3
        pKa1F = AB2

        H2AF = AE16

        if AM4 <= 0:
            H3a = AL3 / ((LOH + LH3a))

            pKa1 = 0
            pKa2 = 0
            pKa3 = 0
            # HplusH2A=float(HplusH2a)
            if AM4 == 0:
                ka1=0.00000000000001/ka1
            else:
                ka1=ka1

            A = ((ka1) * (H3a))
            B = 1
            C = 0
            D = ((-1) * A)
            E = ((ka1) * (ka1))
            F = ((E) - (4 * (B) * D))
            G = math.sqrt(F)
            H = (-ka1) + G
            I = (H) / (2 * (B))
            Hpos = I
            if I == 0:
                pH = 0
            else:
                pH = (math.log10(I) * -1)
            pOH = 14 - (pH)
            if I > 0:
                H2af = I
            else:
                H2af = 0
            log1 = 10 ** ((pKa1) * -1)
            log2 = 10 ** ((pKa2) * -1)
            log3 = 10 ** ((pKa3) * -1)
            if ka1 == 0:
                pKa1F = 0
            else:
                pKa1F = (math.log10(ka1) * -1)

            # part2

            I9 = I




            J9 = Hpos

            pKB1 = 14 - pKa1F

            if pKa1F == 0:
                pKB1 = 0
            else:
                pKB1 = pKB1

            PH = 14 - pH
            pOH = 14 - (PH)



            print("H2A- =", H2af)

            print("pH   =", PH)
            print("H+   =", Hpos)
            print("pOH  =", pOH)
            print("pKa1 =", pKa1F)

            print("pKB1 =", pKB1)



        else:
            # block 2 diprotic final outputs
            print("pKa1 = ", pKa1F)

            print("[H2A] = ", H3AF)
            print("[HA-] = ", H2AF)

            print("pH = ", pH)
            print("HHE = ", HHE)
            print("equivalence point = ", EP)
            print("excess base = ", EB)
            print("Non buffer excess base = ", NEB)
            print("pOH HHE = ", NHHE)
            print("pOH = ", NpH)
            # initialize sum and counter
        iteration = input("would you like to run iterations changing LOH")
        if iteration == "yes":
            Counter = input("How many iterations do you want to run")
            counter = float(Counter)
            loop = counter + (counter * -2)
            number = 0

            Value = input("how much you want to increase LOH by")
            value = float(Value)
            while loop < 0:
                # run code here
                number = number + 1

                loop = loop + 1
                LOH = LOH + value
                OHnegative = float(OHNegative)
                LOH = float(LOh)
                LH3a = float(LH3A)
                H3A = float(H3a)

                # X10 = Hpos
                # Y10 = OHneg
                # X13 = HH2a

                # H3A
                AL3 = LH3a * H3A
                AJ3 = OHnegative * LOH
                AJ4 = AJ3 / (LOH + LH3a)
                AJ6 = LOH - LH3a
                AJ7 = AJ3 - AL3
                AJ8 = LOH + LH3a
                AJ9 = AJ7 / AJ8
                AM4 = AL3 - AJ3
                AM5 = AM4 / (LOH + LH3a)
                AF2 = AJ4

                # ae block
                AE6 = ka1 * AM5
                AE8 = 1
                AE10 = (-1) * AE6
                AE11 = AF2 + ka1
                AE12 = AE11 ** 2
                AE13 = AE12 - (4 * 1 * AE10)
                AE14 = math.sqrt(AE13)
                AE15 = (AE11 * -1) + AE14
                AE16 = AE15 / (2 * AE8)

                AE3 = AM5 - AE16

                # y-aa
                Y2 = ka1

                # AB3 = pKa1
                # AC3 = pKa2
                # AD3 = pKa3

                if Y2 <= 0:
                    AB2 = 0
                else:
                    AB2 = (math.log10(Y2) * -1)

                    # Y4 = 10 ** (-1 * AB3)
                    # Z4 = 10 ** (-1 * AC3)
                    # AA4 = 10 ** (-1 * AD3)
                if Y2 == 0:
                    AB7 = 0
                else:
                    AB7 = 0.000000000000001 / Y2

                    # af block
                AF2 = AJ4
                AF3 = AE16

                AF9 = AE16

                if AF16 > 0:

                    AF16 = AF16
                    AG2 = AF16
                else:
                    AF16 = 0
                    AG2 = 0

                    # AG

                    # AG7=X10*AH2
                AG9 = AE16

                AF4 = (AJ4) - AG2

                # X block
                X9 = AE16 + 0.0000001 + AF16
                X14 = X9

                if X9 <= 0:
                    X3 = 0
                else:
                    X3 = (math.log10(X9) * -1)
                pH = X3
                # if X10 <= 0:
                #   X4 = 0
                # else:
                #    X4 = (math.log10(X10) * -1)

                X18 = AE16 + 0.0000001
                if AE3 == 0:
                    X19 = 0
                else:
                    X19 = AF2 / AE3
                if X19 <= 0:
                    X20 = 0
                else:
                    X20 = math.log10(X19)

                X5 = AB2 + X20
                if AJ9 <= 0:
                    X6 = 0
                else:
                    X6 = (math.log10(AJ9) * -1)

                    # misc block
                AF7 = X9 * AG2
                Z9 = 14 - X3
                Y9 = (10 ** -Z9)
                Y11 = 10 ** (-X6)
                Z10 = 14 - X5
                Z11 = 14 - X6
                # X block pt 2
                HHE = X5
                EB = 14 - X6

                EP = X7
                NpH = 14 - (X3)
                NHHE = 14 - (X5)
                NEB = 14 - (X6)

                # final

                H3AF = AM5 - AF3
                pKa1F = AB2

                H2AF = AE16
                HAneg2F = AF16

                # new code that takes block one
                if AM4 <= 0:
                    H3a = AL3 / ((LOH + LH3a))
                    pKa1 = 0
                    pKa2 = 0
                    pKa3 = 0
                    # HplusH2A=float(HplusH2a)
                    if AM4 == 0:
                        ka1 = 0.00000000000001 / ka1
                    else:
                        ka1 = ka1

                    A = ((ka1) * (H3a))
                    B = 1
                    C = 0
                    D = ((-1) * A)
                    E = ((ka1) * (ka1))
                    F = ((E) - (4 * (B) * D))
                    G = math.sqrt(F)
                    H = (-ka1) + G
                    I = (H) / (2 * (B))
                    Hpos = I
                    if I == 0:
                        pH = 0
                    else:
                        pH = (math.log10(I) * -1)
                    pOH = 14 - (pH)
                    if I > 0:
                        H2af = I
                    else:
                        H2af = 0
                    log1 = 10 ** ((pKa1) * -1)
                    log2 = 10 ** ((pKa2) * -1)
                    log3 = 10 ** ((pKa3) * -1)
                    if ka1 == 0:
                        pKa1F = 0
                    else:
                        pKa1F = (math.log10(ka1) * -1)

                    # part2

                    I9 = I

                    J9 = Hpos

                    pKB1 = 14 - pKa1F

                    if pKa1F == 0:
                        pKB1 = 0
                    else:
                        pKB1 = pKB1

                        pKB3 = 0

                    PH = 14 - pH
                    pOH = 14 - (PH)
                    print("H2A- =", H2af)

                    print("pH   =", PH)
                    print("H+   =", Hpos)
                    print("pOH  =", pOH)
                    print(number, "iterations completed")

                else:
                    # block 2 diprotic final outputs

                    print("[H2A] = ", H3AF)
                    print("[HA-] = ", H2AF)
                    print("[A-2] = ", HAneg2F)
                    print("pH = ", pH)
                    print("HHE = ", HHE)
                    print("equivalence point = ", EP)
                    print("excess base = ", EB)
                    print("Non buffer excess base = ", NEB)
                    print("pOH HHE = ", NHHE)
                    print("pOH = ", NpH)
                    print(number, "iterations completed")
            else:
                # print output here
                print(number, "iterations computed")



        # print("A-3 = ", Aneg3F)
    else:
        none = 2

    # input
    if case1 == "diprotic":
        kA1 = input("enter ka1 value: ")
        kA2 = input("enter ka2 value: ")


        ka1 = float(kA1)
        ka2 = float(kA2)


        #pka1 = input("Enter pKa1 value: ")
        #pka2 = input("Enter pKa2 value: ")
        #pka3 = input("Enter pKa3 value: ")

        #pKa1 = float(pka1)
        #pKa2 = float(pka2)
        #pKa3 = float(pka3)

        #HPos = input("Enter H+ value: ")
        #OHNeg = input("Enter OH- value: ")
        #HH2A = input("Enter H+ with H2A value")
        OHNegative = input("enter OH- [OH] value: ")
        LOh = input("Enter L of OH-: ")
        LH3A = input("Enter L of H3A: ")
        H3a = input("Enter [H3A] value: ")

        #Hpos = float(HPos)
        #OHneg = float(OHNeg)
        #HH2a = float(HH2A)
        OHnegative = float(OHNegative)
        LOH = float(LOh)
        LH3a = float(LH3A)
        H3A = float(H3a)

        #X10 = Hpos
        #Y10 = OHneg
        #X13 = HH2a

        # H3A
        AL3 = LH3a * H3A
        AJ3 = OHnegative * LOH
        AJ4 = AJ3 / (LOH + LH3a)
        AJ6 = LOH - LH3a
        AJ7 = AJ3-AL3
        AJ8 = LOH + LH3a
        AJ9 = AJ7 / AJ8
        AM4 = AL3 - AJ3
        AM5 = AM4 / (LOH + LH3a)
        AF2 = AJ4

        # ae block
        AE6 = ka1 * AM5
        AE8 = 1
        AE10 = (-1) * AE6
        AE11 = AF2 + ka1
        AE12 = AE11 ** 2
        AE13 = AE12 - (4 * 1 * AE10)
        AE14 = math.sqrt(AE13)
        AE15 = (AE11 * -1) + AE14
        AE16 = AE15 / (2 * AE8)

        AE3 = AM5 - AE16

        # y-aa
        Y2 = ka1
        Z2 = ka2


        #AB3 = pKa1
        #AC3 = pKa2
        #AD3 = pKa3

        if Y2 <= 0:
            AB2 = 0
        else:
            AB2 = (math.log10(Y2) * -1)

        if Z2 <= 0:
            AC2 = 0
        else:
            AC2 = (math.log10(Z2) * -1)



        #Y4 = 10 ** (-1 * AB3)
        #Z4 = 10 ** (-1 * AC3)
        #AA4 = 10 ** (-1 * AD3)
        if Y2 == 0:
            AB7 = 0
        else:
            AB7 = 0.000000000000001 / Y2



        if Z2 == 0:
            AD7 = 0
        else:
            AD7 = 0.00000000000001 / Z2



        # af block
        AF2 = AJ4
        AF3 = AE16
        AF6 = AF3 * Z2
        AF9 = AE16
        AF10 = Z2 + AF9
        AF11 = -1 * AF6
        AF12 = AF10 * AF10
        AF13 = AF12 - (4 * 1 * AF11)
        AF14 = math.sqrt(AF13)
        AF15 = -AF10 + AF14
        AF16 = AF15 / 2

        if AF16 > 0:

            AF16 = AF16
            AG2 = AF16
        else:
            AF16 = 0
            AG2 = 0

        # AG


        # AG7=X10*AH2
        AG9 = AE16
        AG17 = AF10 * AF10

        AF4 = (AJ4) - AG2

        # X block
        X9 = AE16 + 0.0000001 + AF16
        X14 = X9

        if X9 <= 0:
            X3 = 0
        else:
            X3 = (math.log10(X9) * -1)
        pH = X3
        # if X10 <= 0:
        #   X4 = 0
        # else:
        #    X4 = (math.log10(X10) * -1)

        X18 = AE16 + 0.0000001
        if AE3 == 0:
            X19 = 0
        else:
            X19 = AF2 / AE3
        if X19 <= 0:
            X20 = 0
        else:
            X20 = math.log10(X19)

        X5 = AB2 + X20
        if AJ9 <= 0:
            X6 = 0
        else:
            X6 = (math.log10(AJ9) * -1)

        # misc block
        AF7 = X9 * AG2
        Z9 = 14 - X3
        Y9 = (10 ** -Z9)
        Y11 = 10 ** (-X6)
        Z10 = 14 - X5
        Z11 = 14 - X6
        # X block pt 2
        HHE = X5
        EB = 14-X6
        X7 = (AB2 + AC2) / 2
        EP = X7
        NpH = 14 - (X3)
        NHHE = 14 - (X5)
        NEB = 14 - (X6)

        # final

        H3AF = AM5-AF3
        pKa1F = AB2
        pKa2F = AC2

        H2AF = AE16
        HAneg2F = AF16
        Aneg3F = AG17
        # new code that takes block one
        if AM4 <= 0:
            H3a = AL3 / ((LOH + LH3a))
            pKa1 = 0
            pKa2 = 0
            pKa3 = 0
            # HplusH2A=float(HplusH2a)
            if AM4 == 0:
                ka1 = 0.00000000000001 / ka1
            else:
                ka1 = ka1

            A = ((ka1) * (H3a))
            B = 1
            C = 0
            D = ((-1) * A)
            E = ((ka1) * (ka1))
            F = ((E) - (4 * (B) * D))
            G = math.sqrt(F)
            H = (-ka1) + G
            I = (H) / (2 * (B))
            Hpos = I
            if I == 0:
                pH = 0
            else:
                pH = (math.log10(I) * -1)
            pOH = 14 - (pH)
            if I > 0:
                H2af = I
            else:
                H2af = 0
            log1 = 10 ** ((pKa1) * -1)
            log2 = 10 ** ((pKa2) * -1)
            log3 = 10 ** ((pKa3) * -1)
            if ka1 == 0:
                pKa1F = 0
            else:
                pKa1F = (math.log10(ka1) * -1)
            if ka2 == 0:
                pKa2F = 0
            else:
                pKa2F = (math.log10(ka2) * -1)



            # part2
            I6 = ((I) * (ka2))
            I9 = I
            I10 = ((ka2) + (I9))
            I11 = -1 * I6

            I13 = (I10 * I10)
            I14 = I13 - (4 * B * I11)
            I15 = math.sqrt(I14)
            I12 = (-1 * I10) + I15
            I16 = I12 / (2 * B)
            if I16 == int:
                I16 = 0
            else:
                I16 = I16
            J2 = I16

            J9 = Hpos



            pKB1 = 14 - pKa1F
            pKB2 = 14 - pKa2F

            if pKa1F == 0:
                pKB1 = 0
            else:
                pKB1 = pKB1
            if pKa2F == 0:
                pKB2 = 0
            else:
                pKB2 = pKB2

                pKB3 = 0

            PH = 14 - pH
            pOH = 14 - (PH)
            print("H2A- =", H2af)
            print("HA-2 =", I16)
            print("pH   =", PH)
            print("H+   =", Hpos)
            print("pOH  =", pOH)
            print("pKa1 =", pKa1F)
            print("pKa2 =", pKa2F)
            print("pKB1 =", pKB1)
            print("pKB2 =", pKB2)
            print("pKB3 =", pKB3)

        else:
            # block 2 diprotic final outputs
            print("pKa1 = ", pKa1F)
            print("pKa2 = ", pKa2F)


            print("[H2A] = ", H3AF)
            print("[HA-] = ", H2AF)
            print("[A-2] = ", HAneg2F)
            print("pH = ", pH)
            print("HHE = ", HHE)
            print("equivalence point = ", EP)
            print("excess base = ", EB)
            print("Non buffer excess base = ", NEB)
            print("pOH HHE = ", NHHE)
            print("pOH = ", NpH)
    # initialize sum and counter
        iteration = input("would you like to run iterations changing LOH")
        if iteration == "yes":
            Counter = input("How many iterations do you want to run")
            counter = float(Counter)
            loop = counter + (counter * -2)
            number = 0

            Value = input("how much you want to increase LOH by")
            value = float(Value)
            while loop < 0:
             # run code here
                number = number + 1

                loop = loop + 1
                LOH = LOH + value
                OHnegative = float(OHNegative)
                LOH = float(LOh)
                LH3a = float(LH3A)
                H3A = float(H3a)

                    # X10 = Hpos
                    # Y10 = OHneg
                    # X13 = HH2a

                    # H3A
                AL3 = LH3a * H3A
                AJ3 = OHnegative * LOH
                AJ4 = AJ3 / (LOH + LH3a)
                AJ6 = LOH - LH3a
                AJ7 = AJ3 - AL3
                AJ8 = LOH + LH3a
                AJ9 = AJ7 / AJ8
                AM4 = AL3 - AJ3
                AM5 = AM4 / (LOH + LH3a)
                AF2 = AJ4

                # ae block
                AE6 = ka1 * AM5
                AE8 = 1
                AE10 = (-1) * AE6
                AE11 = AF2 + ka1
                AE12 = AE11 ** 2
                AE13 = AE12 - (4 * 1 * AE10)
                AE14 = math.sqrt(AE13)
                AE15 = (AE11 * -1) + AE14
                AE16 = AE15 / (2 * AE8)

                AE3 = AM5 - AE16

                    # y-aa
                Y2 = ka1
                Z2 = ka2

                    # AB3 = pKa1
                    # AC3 = pKa2
                    # AD3 = pKa3

                if Y2 <= 0:
                    AB2 = 0
                else:
                    AB2 = (math.log10(Y2) * -1)

                if Z2 <= 0:
                    AC2 = 0
                else:
                    AC2 = (math.log10(Z2) * -1)

                    # Y4 = 10 ** (-1 * AB3)
                    # Z4 = 10 ** (-1 * AC3)
                    # AA4 = 10 ** (-1 * AD3)
                if Y2 == 0:
                    AB7 = 0
                else:
                    AB7 = 0.000000000000001 / Y2

                if Z2 == 0:
                    AD7 = 0
                else:
                    AD7 = 0.00000000000001 / Z2

                    # af block
                AF2 = AJ4
                AF3 = AE16
                AF6 = AF3 * Z2
                AF9 = AE16
                AF10 = Z2 + AF9
                AF11 = -1 * AF6
                AF12 = AF10 * AF10
                AF13 = AF12 - (4 * 1 * AF11)
                AF14 = math.sqrt(AF13)
                AF15 = -AF10 + AF14
                AF16 = AF15 / 2

                if AF16 > 0:

                    AF16 = AF16
                    AG2 = AF16
                else:
                    AF16 = 0
                    AG2 = 0

                    # AG

                    # AG7=X10*AH2
                AG9 = AE16
                AG17 = AF10 * AF10

                AF4 = (AJ4) - AG2

                    # X block
                X9 = AE16 + 0.0000001 + AF16
                X14 = X9

                if X9 <= 0:
                    X3 = 0
                else:
                    X3 = (math.log10(X9) * -1)
                pH = X3
                    # if X10 <= 0:
                    #   X4 = 0
                    # else:
                    #    X4 = (math.log10(X10) * -1)

                X18 = AE16 + 0.0000001
                if AE3 == 0:
                    X19 = 0
                else:
                    X19 = AF2 / AE3
                if X19 <= 0:
                    X20 = 0
                else:
                    X20 = math.log10(X19)

                X5 = AB2 + X20
                if AJ9 <= 0:
                    X6 = 0
                else:
                    X6 = (math.log10(AJ9) * -1)

                    # misc block
                AF7 = X9 * AG2
                Z9 = 14 - X3
                Y9 = (10 ** -Z9)
                Y11 = 10 ** (-X6)
                Z10 = 14 - X5
                Z11 = 14 - X6
                # X block pt 2
                HHE = X5
                EB = 14 - X6
                X7 = (AB2 + AC2) / 2
                EP = X7
                NpH = 14 - (X3)
                NHHE = 14 - (X5)
                NEB = 14 - (X6)

                # final

                H3AF = AM5 - AF3
                pKa1F = AB2
                pKa2F = AC2

                H2AF = AE16
                HAneg2F = AF16
                Aneg3F = AG17
                # new code that takes block one
                if AM4 <= 0:
                    H3a = AL3 / ((LOH + LH3a))
                    pKa1 = 0
                    pKa2 = 0
                    pKa3 = 0
                    # HplusH2A=float(HplusH2a)
                    if AM4 == 0:
                        ka1 = 0.00000000000001 / ka1
                    else:
                        ka1 = ka1

                    A = ((ka1) * (H3a))
                    B = 1
                    C = 0
                    D = ((-1) * A)
                    E = ((ka1) * (ka1))
                    F = ((E) - (4 * (B) * D))
                    G = math.sqrt(F)
                    H = (-ka1) + G
                    I = (H) / (2 * (B))
                    Hpos = I
                    if I == 0:
                        pH = 0
                    else:
                        pH = (math.log10(I) * -1)
                    pOH = 14 - (pH)
                    if I > 0:
                        H2af = I
                    else:
                        H2af = 0
                    log1 = 10 ** ((pKa1) * -1)
                    log2 = 10 ** ((pKa2) * -1)
                    log3 = 10 ** ((pKa3) * -1)
                    if ka1 == 0:
                        pKa1F = 0
                    else:
                        pKa1F = (math.log10(ka1) * -1)
                    if ka2 == 0:
                        pKa2F = 0
                    else:
                        pKa2F = (math.log10(ka2) * -1)

                    # part2
                    I6 = ((I) * (ka2))
                    I9 = I
                    I10 = ((ka2) + (I9))
                    I11 = -1 * I6

                    I13 = (I10 * I10)
                    I14 = I13 - (4 * B * I11)
                    I15 = math.sqrt(I14)
                    I12 = (-1 * I10) + I15
                    I16 = I12 / (2 * B)
                    if I16 == int:
                        I16 = 0
                    else:
                        I16 = I16
                    J2 = I16

                    J9 = Hpos

                    pKB1 = 14 - pKa1F
                    pKB2 = 14 - pKa2F

                    if pKa1F == 0:
                        pKB1 = 0
                    else:
                        pKB1 = pKB1
                    if pKa2F == 0:
                        pKB2 = 0
                    else:
                        pKB2 = pKB2

                        pKB3 = 0

                    PH = 14 - pH
                    pOH = 14 - (PH)
                    print("H2A- =", H2af)
                    print("HA-2 =", I16)
                    print("pH   =", PH)
                    print("H+   =", Hpos)
                    print("pOH  =", pOH)
                    print(number, "iterations completed")

                else:
                    # block 2 diprotic final outputs


                    print("[H2A] = ", H3AF)
                    print("[HA-] = ", H2AF)
                    print("[A-2] = ", HAneg2F)
                    print("pH = ", pH)
                    print("HHE = ", HHE)
                    print("equivalence point = ", EP)
                    print("excess base = ", EB)
                    print("Non buffer excess base = ", NEB)
                    print("pOH HHE = ", NHHE)
                    print("pOH = ", NpH)
                    print(number, "iterations completed")
            else:
                # print output here
                print(number, "iterations computed")

        kms = 1
    else:
        none = 1
    #triprotic
    if case1 == "triprotic":
    # input
        kA1 = input("enter ka1 value: ")
        kA2 = input("enter ka2 value: ")
        kA3 = input("enter ka3 value: ")

        ka1 = float(kA1)
        ka2 = float(kA2)
        ka3 = float(kA3)

        #pka1 = input("Enter pKa1 value: ")
        #pka2 = input("Enter pKa2 value: ")
        #pka3 = input("Enter pKa3 value: ")

        #pKa1 = float(pka1)
        #pKa2 = float(pka2)
        #pKa3 = float(pka3)

        #HPos = input("Enter H+ value: ")
        #OHNeg = input("Enter OH- value: ")
        #HH2A = input("Enter H+ with H2A value")
        OHNegative = input("enter OH- [OH] value: ")
        LOh = input("Enter L of OH- : ")
        LH3A = input("Enter L of H3A: ")
        H3a = input("Enter [H3A] value: ")

        #Hpos = float(HPos)
        #OHneg = float(OHNeg)
        #HH2a = float(HH2A)
        OHnegative = float(OHNegative)
        LOH = float(LOh)
        LH3a = float(LH3A)
        H3A = float(H3a)

        #X10 = Hpos
        #Y10 = OHneg
        #X13 = HH2a

        # H3A
        AL3 = LH3a * H3A
        AJ3 = OHnegative * LOH
        AJ4 = AJ3 / (LOH + LH3a)
        AJ6 = LOH - LH3a
        AJ7 = AJ3-AL3
        AJ8 = LOH + LH3a
        AJ9 = AJ7 / AJ8
        AM4 = AL3 - AJ3
        AM5 = AM4 / (LOH + LH3a)
        AF2 = AJ4

        # ae block
        AE6 = ka1 * AM5
        AE8 = 1
        AE10 = (-1) * AE6
        AE11 = AF2 + ka1
        AE12 = AE11 ** 2
        AE13 = AE12 - (4 * 1 * AE10)
        AE14 = math.sqrt(AE13)
        AE15 = (AE11 * -1) + AE14
        AE16 = AE15 / (2 * AE8)
        if AE16 > 0:

            AE16 = AE16
            AF3 = AE16
        else:
            AE16 = 0
            AF3 = 0

        AE3 = AM5 - AE16

        # y-aa
        Y2 = ka1
        Z2 = ka2
        AA2 = ka3

        #AB3 = pKa1
        #AC3 = pKa2
        #AD3 = pKa3

        if Y2 <= 0:
            AB2 = 0
        else:
            AB2 = (math.log10(Y2) * -1)

        if Z2 <= 0:
            AC2 = 0
        else:
            AC2 = (math.log10(Z2) * -1)

        if AA2 <= 0:
            AD2 = 0
        else:
            AD2 = (math.log10(AA2) * -1)

        #Y4 = 10 ** (-1 * AB3)
        #Z4 = 10 ** (-1 * AC3)
        #AA4 = 10 ** (-1 * AD3)
        if Y2 == 0:
            AB7 = 0
        else:
            AB7 = 0.00000000000001 / Y2

        if AA2 == 0:
            AC7 = 0
        else:
            AC7 = 0.00000000000001 / AA2
        if Z2 == 0:
            AD7 = 0
        else:
            AD7 = 0.00000000000001 / Z2



        # af block
        AF2 = AJ4
        AF3 = AE16
        AF6 = AF3 * Z2
        AF9 = AE16
        AF10 = Z2 + AF9
        AF11 = -1 * AF6
        AF12 = AF10 * AF10
        AF13 = AF12 - (4 * 1 * AF11)
        AF14 = math.sqrt(AF13)
        AF15 = -AF10 + AF14
        AF16 = AF15 / 2

        AG2=AF16
        # AG

        AG6 = AG2 * AA2
        # AG7=X10*AH2
        AG9 = AE16
        AG10 = AA2 + AG9


        AF4 = (AJ4) - AG2

        # X block
        X9 = AE16 + 0.0000001 + AF16
        X14 = X9

        if X9 <= 0:
            X3 = 0
        else:
            X3 = (math.log10(X9) * -1)
        pH=X3
        #if X10 <= 0:
         #   X4 = 0
        #else:
        #    X4 = (math.log10(X10) * -1)

        X18 = AE16 + 0.0000001
        if AE3 == 0:
            X19 = 0
        else:
            X19 = AF2 / AE3
        if X19 <= 0:
            X20 = 0
        else:
            X20 = math.log10(X19)

        X5 = AB2 + X20
        if AJ9 <= 0:
            X6 = 0
        else:
            X6 = (math.log10(AJ9) * -1)


        # misc block
        AF7 = X9 * AG2
        Z9 = 14 - X3
        Y9 = (10 ** -Z9)
        Y11 = 10 ** (-X6)
        Z10 = 14 - X5
        Z11 = 14 - X6
        #X block pt 2
        HHE=X5
        EB=14-X6
        X7=(AB2+AC2)/2
        EP=X7
        NpH=14-(X3)
        NHHE=14-(X5)
        NEB=14-(X6)
        AG17=4.38E-04
        AG3=(AG2)-(AG17)
        if AG3 > 0:

            AF16 = AF16
            AG2 = AF16
            AG17 = AF10 * AF10
        else:
            AG3=AF16
            AG17=0
        #new code that takes block one
        if AM4 <= 0:
            H3a=AL3/((LOH+LH3a))
            pKa1 = 0
            pKa2 = 0
            pKa3 = 0
            # HplusH2A=float(HplusH2a)
            if AM4 == 0:
                ka1 = 0.00000000000001 / ka1
            else:
                ka1 = ka1

            A = ((ka1) * (H3a))
            B = 1
            C = 0
            D = ((-1) * A)
            E = ((ka1) * (ka1))
            F = ((E) - (4 * (B) * D))
            G = math.sqrt(F)
            H = (-ka1) + G
            I = (H) / (2 * (B))
            Hpos = I
            if I == 0:
                pH = 0
            else:
                pH = (math.log10(I) * -1)
            pOH = 14 - (pH)
            if I > 0:
                H2af = I
            else:
                H2af = 0
            log1 = 10 ** ((pKa1) * -1)
            log2 = 10 ** ((pKa2) * -1)
            log3 = 10 ** ((pKa3) * -1)
            if ka1 == 0:
                pKa1F = 0
            else:
                pKa1F = (math.log10(ka1) * -1)
            if ka2 == 0:
                pKa2F = 0
            else:
                pKa2F = (math.log10(ka2) * -1)
            if ka3 == 0:
                pKa3F = 0
            else:
                pKa3F = (math.log10(ka3) * -1)

            # part2
            I6 = ((I) * (ka2))
            I9 = I
            I10 = ((ka2) + (I9))
            I11 = -1 * I6

            I13 = (I10 * I10)
            I14 = I13 - (4 * B * I11)
            I15 = math.sqrt(I14)
            I12 = (-1 * I10) + I15
            I16 = I12 / (2 * B)
            if I16 == int:
                I16 = 0
            else:
                I16 = I16
            J2 = I16
            J6 = J2 * ka3
            J9 = Hpos
            J10 = ka3 + J9
            J11 = -1 * J6
            J12 = J10 * J10
            J13 = J12 - (4 * B * J11)
            J14 = math.sqrt(J13)
            J15 = (-1 * I10) + J14
            J16 = J15 / (2 * B)
            if J16 > 0:

                J16 = J16
                A3 = J16
            else:
                J16 = 0
                A3 = 0
            if ka3 == 0:
                I16 = I16
            else:
                I16 = I16 - A3

            pKB1 = 14 - pKa1F
            pKB2 = 14 - pKa2F
            pKB3 = 14 - pKa3F
            if pKa1F == 0:
                pKB1 = 0
            else:
                pKB1 = pKB1
            if pKa2F == 0:
                pKB2 = 0
            else:
                pKB2 = pKB2
            if pKa3F == 0:
                pKB3 = 0
            else:
                pKB3 = pKB3
            PH=14-pH
            pOH=14 - (PH)
            print("[H3A]=", 0)
            print("[H2A-] =", H2af)
            print("[HA-2] =", I16)
            print("[A-3]  =", A3)
            print("pH   =", PH)
            print("[H+]   =", Hpos)
            print("pOH  =", pOH)
            print("pKa1 =", pKa1F)
            print("pKa2 =", pKa2F)
            print("pKa3 =", pKa3F)
            print("pKB1 =", pKB1)
            print("pKB2 =", pKB2)
            print("pKB3 =", pKB3)

        else:



            H3AF = AM5-(AF3)
            pKa1F = AB2
            pKa2F = AC2
            pKa3F = AD2
            H2AF = AE16
            HAneg2F = AG3
            Aneg3F = AG17

            #block 2 triprotic final outputs
            print("pKa1 = ", pKa1F)
            print("pKa2 = ", pKa2F)
            print("pKa1 = ", pKa3F)

            print("[H3A] = ", H3AF)
            print("[H2A]- = ", H2AF)
            print("[HA-2] = ", HAneg2F)
            print("[A-3] = ", Aneg3F)
            print("pH = ", pH)
            print("HHE  = ", HHE)
            print("equivalence point = ", EP)
            print("excess base pH = ", EB)
            print("excess base pOH = ", NEB)
            print("pOH HHE = ", NHHE)
            print("pOH = ", NpH)
            # initialize sum and counter
        iteration = input("would you like to run iterations changing LOH")
        if iteration == "yes":
            Counter = input("How many iterations do you want to run")
            counter = float(Counter)
            loop = counter + (counter * -2)
            number = 0

            Value = input("how much you want to increase LOH by")
            value = float(Value)
            while loop < 0:
                number = number + 1

                loop = loop + 1
                LOH = LOH + value
                OHnegative = float(OHNegative)
                LOH = float(LOh)
                LH3a = float(LH3A)
                H3A = float(H3a)

                # X10 = Hpos
                # Y10 = OHneg
                # X13 = HH2a

                # H3A
                AL3 = LH3a * H3A
                AJ3 = OHnegative * LOH
                AJ4 = AJ3 / (LOH + LH3a)
                AJ6 = LOH - LH3a
                AJ7 = AJ3 - AL3
                AJ8 = LOH + LH3a
                AJ9 = AJ7 / AJ8
                AM4 = AL3 - AJ3
                AM5 = AM4 / (LOH + LH3a)
                AF2 = AJ4

                # ae block
                AE6 = ka1 * AM5
                AE8 = 1
                AE10 = (-1) * AE6
                AE11 = AF2 + ka1
                AE12 = AE11 ** 2
                AE13 = AE12 - (4 * 1 * AE10)
                AE14 = math.sqrt(AE13)
                AE15 = (AE11 * -1) + AE14
                AE16 = AE15 / (2 * AE8)
                if AE16 > 0:

                    AE16 = AE16
                    AF3 = AE16
                else:
                    AE16 = 0
                    AF3 = 0

                AE3 = AM5 - AE16

                # y-aa
                Y2 = ka1
                Z2 = ka2
                AA2 = ka3

                # AB3 = pKa1
                # AC3 = pKa2
                # AD3 = pKa3

                if Y2 <= 0:
                    AB2 = 0
                else:
                    AB2 = (math.log10(Y2) * -1)

                if Z2 <= 0:
                    AC2 = 0
                else:
                    AC2 = (math.log10(Z2) * -1)

                if AA2 <= 0:
                    AD2 = 0
                else:
                    AD2 = (math.log10(AA2) * -1)

                # Y4 = 10 ** (-1 * AB3)
                # Z4 = 10 ** (-1 * AC3)
                # AA4 = 10 ** (-1 * AD3)
                if Y2 == 0:
                    AB7 = 0
                else:
                    AB7 = 0.00000000000001 / Y2

                if AA2 == 0:
                    AC7 = 0
                else:
                    AC7 = 0.00000000000001 / AA2
                if Z2 == 0:
                    AD7 = 0
                else:
                    AD7 = 0.00000000000001 / Z2

                # af block
                AF2 = AJ4
                AF3 = AE16
                AF6 = AF3 * Z2
                AF9 = AE16
                AF10 = Z2 + AF9
                AF11 = -1 * AF6
                AF12 = AF10 * AF10
                AF13 = AF12 - (4 * 1 * AF11)
                AF14 = math.sqrt(AF13)
                AF15 = -AF10 + AF14
                AF16 = AF15 / 2

                AG2 = AF16
                # AG

                AG6 = AG2 * AA2
                # AG7=X10*AH2
                AG9 = AE16
                AG10 = AA2 + AG9

                AF4 = (AJ4) - AG2

                # X block
                X9 = AE16 + 0.0000001 + AF16
                X14 = X9

                if X9 <= 0:
                    X3 = 0
                else:
                    X3 = (math.log10(X9) * -1)
                pH = X3
                # if X10 <= 0:
                #   X4 = 0
                # else:
                #    X4 = (math.log10(X10) * -1)

                X18 = AE16 + 0.0000001
                if AE3 == 0:
                    X19 = 0
                else:
                    X19 = AF2 / AE3

                if X19 <= 0:
                    X20 = 0
                else:
                    X20 = math.log10(X19)

                X5 = AB2 + X20
                if AJ9 <= 0:
                    X6 = 0
                else:
                    X6 = (math.log10(AJ9) * -1)

                # misc block
                AF7 = X9 * AG2
                Z9 = 14 - X3
                Y9 = (10 ** -Z9)
                Y11 = 10 ** (-X6)
                Z10 = 14 - X5
                Z11 = 14 - X6
                # X block pt 2
                HHE = X5
                EB = 14 - X6
                X7 = (AB2 + AC2) / 2
                EP = X7
                NpH = 14 - (X3)
                NHHE = 14 - (X5)
                NEB = 14 - (X6)
                AG17 = 4.38E-04
                AG3 = (AG2) - (AG17)
                if AG3 > 0:

                    AF16 = AF16
                    AG2 = AF16
                    AG17 = AF10 * AF10
                else:
                    AG3 = AF16
                    AG17 = 0
                # new code that takes block one
                if AM4 <= 0:
                    H3a = AL3 / ((LOH + LH3a))
                    pKa1 = 0
                    pKa2 = 0
                    pKa3 = 0
                    # HplusH2A=float(HplusH2a)
                    if AM4 == 0:
                        ka1 = 0.00000000000001 / ka1
                    else:
                        ka1 = ka1

                    A = ((ka1) * (H3a))
                    B = 1
                    C = 0
                    D = ((-1) * A)
                    E = ((ka1) * (ka1))
                    F = ((E) - (4 * (B) * D))
                    G = math.sqrt(F)
                    H = (-ka1) + G
                    I = (H) / (2 * (B))
                    Hpos = I
                    if I == 0:
                        pH = 0
                    else:
                        pH = (math.log10(I) * -1)
                    pOH = 14 - (pH)
                    if I > 0:
                        H2af = I
                    else:
                        H2af = 0
                    log1 = 10 ** ((pKa1) * -1)
                    log2 = 10 ** ((pKa2) * -1)
                    log3 = 10 ** ((pKa3) * -1)
                    if ka1 == 0:
                        pKa1F = 0
                    else:
                        pKa1F = (math.log10(ka1) * -1)
                    if ka2 == 0:
                        pKa2F = 0
                    else:
                        pKa2F = (math.log10(ka2) * -1)
                    if ka3 == 0:
                        pKa3F = 0
                    else:
                        pKa3F = (math.log10(ka3) * -1)

                    # part2
                    I6 = ((I) * (ka2))
                    I9 = I
                    I10 = ((ka2) + (I9))
                    I11 = -1 * I6

                    I13 = (I10 * I10)
                    I14 = I13 - (4 * B * I11)
                    I15 = math.sqrt(I14)
                    I12 = (-1 * I10) + I15
                    I16 = I12 / (2 * B)
                    if I16 == int:
                        I16 = 0
                    else:
                        I16 = I16
                    J2 = I16
                    J6 = J2 * ka3
                    J9 = Hpos
                    J10 = ka3 + J9
                    J11 = -1 * J6
                    J12 = J10 * J10
                    J13 = J12 - (4 * B * J11)
                    J14 = math.sqrt(J13)
                    J15 = (-1 * I10) + J14
                    J16 = J15 / (2 * B)
                    if J16 > 0:

                        J16 = J16
                        A3 = J16
                    else:
                        J16 = 0
                        A3 = 0
                    if ka3 == 0:
                        I16 = I16
                    else:
                        I16 = I16 - A3

                    pKB1 = 14 - pKa1F
                    pKB2 = 14 - pKa2F
                    pKB3 = 14 - pKa3F
                    if pKa1F == 0:
                        pKB1 = 0
                    else:
                        pKB1 = pKB1
                    if pKa2F == 0:
                        pKB2 = 0
                    else:
                        pKB2 = pKB2
                    if pKa3F == 0:
                        pKB3 = 0
                    else:
                        pKB3 = pKB3
                    PH = 14 - pH
                    pOH = 14 - (PH)
                    print("[H3A]=", 0)
                    print("[H2A-] =", H2af)
                    print("[HA-2] =", I16)
                    print("[A-3]  =", A3)
                    print("pH   =", PH)
                    print("[H+]   =", Hpos)
                    print("pOH  =", pOH)
                    print("pKa1 =", pKa1F)
                    print("pKa2 =", pKa2F)
                    print("pKa3 =", pKa3F)
                    print("pKB1 =", pKB1)
                    print("pKB2 =", pKB2)
                    print("pKB3 =", pKB3)
                    print(number, "iterations completed")

                else:

                    H3AF = AM5 - (AF3)
                    pKa1F = AB2
                    pKa2F = AC2
                    pKa3F = AD2
                    H2AF = AE16
                    HAneg2F = AG3
                    Aneg3F = AG17

                    # block 2 triprotic final outputs
                    print("pKa1 = ", pKa1F)
                    print("pKa2 = ", pKa2F)
                    print("pKa1 = ", pKa3F)

                    print("[H3A] = ", H3AF)
                    print("[H2A]- = ", H2AF)
                    print("[HA-2] = ", HAneg2F)
                    print("[A-3] = ", Aneg3F)
                    print("pH = ", pH)
                    print("HHE  = ", HHE)
                    print("equivalence point = ", EP)
                    print("excess base pH = ", EB)
                    print("excess base pOH = ", NEB)
                    print("pOH HHE = ", NHHE)
                    print("pOH = ", NpH)
                    print(number, "iterations completed")
            else:
                # print output here
                print(number, "iterations computed")


    else:
        if case1 == "diprotic":
            none = 1
        else:
            if case1 == "monoprotic":
                nothinghappens = 0
            else:
                print("please try to use your brain for once")
else:
    none=3
if type == "dissociation":

    # input
    diprotic = "diprotic"
    monoprotic = "monoprotic"
    triprotic = "triprotic"

    case = input("Please type one of the following: monoprotic, diprotic, triprotic :")
    # mono
    if case == "monoprotic":
        kA1 = input("Enter ka1 value :")
        H3a = input("Enter H3A vaule :")
        # Ph=input("Enter PH vaule :")

        # pKA1=input("Enter pKa1 vaule :")
        # pKA2=input("Enter pKa2 vaule :")
        # pKA3=input("Enter pKa3 vaule :")
        # HplusH2a=input("Enter H2A+ vaule :")

        # converting to int
        ka1 = float(kA1)
        H3A = float(H3a)
        # pH=float(Ph)
        pKa1 = 0
        # HplusH2A=float(HplusH2a)

        A = ((ka1) * (H3A))
        B = 1
        C = 0
        D = ((-1) * A)
        E = ((ka1) * (ka1))
        F = ((E) - (4 * (B) * D))
        G = math.sqrt(F)
        H = (-ka1) + G
        I = (H) / (2 * (B))
        Hpos = I
        if I == 0:
            pH = 0
        else:
            pH = (math.log10(I) * -1)
        pOH = 14 - (pH)
        if I > 0:
            H2af = I
        else:
            H2af = 0
        log1 = 10 ** ((pKa1) * -1)
        if ka1 == 0:
            pKa1F = 0
        else:
            pKa1F = (math.log10(ka1) * -1)
        pKB1 = 14 - pKa1F
        # part2

        print("[H2A-] =", H2af)

        print("pH   =", pH)
        print("H+   =", Hpos)
        print("pOH  =", pOH)
        print("pKa1 =", pKa1F)
        print("pKB1 =", pKB1)
    else:
        nothinghap = 2
    # diprotic
    if case == "diprotic":
        kA1 = input("Enter ka1 value :")
        kA2 = input("Enter ka2 vaule :")
        H3a = input("Enter H3A vaule :")
        # Ph=input("Enter PH vaule :")

        # pKA1=input("Enter pKa1 vaule :")
        # pKA2=input("Enter pKa2 vaule :")
        # pKA3=input("Enter pKa3 vaule :")
        # HplusH2a=input("Enter H2A+ vaule :")

        # converting to int
        ka1 = float(kA1)
        ka2 = float(kA2)
        H3A = float(H3a)
        # pH=float(Ph)
        pKa1 = 0
        pKa2 = 0
        # HplusH2A=float(HplusH2a)

        A = ((ka1) * (H3A))
        B = 1
        C = 0
        D = ((-1) * A)
        E = ((ka1) * (ka1))
        F = ((E) - (4 * (B) * D))
        G = math.sqrt(F)
        H = (-ka1) + G
        I = (H) / (2 * (B))
        Hpos = I
        if I == 0:
            pH = 0
        else:
            pH = (math.log10(I) * -1)
        pOH = 14 - (pH)
        if I > 0:
            H2af = I
        else:
            H2af = 0
        log1 = 10 ** ((pKa1) * -1)
        log2 = 10 ** ((pKa2) * -1)
        if ka1 == 0:
            pKa1F = 0
        else:
            pKa1F = (math.log10(ka1) * -1)
        if ka2 == 0:
            pKa2F = 0
        else:
            pKa2F = (math.log10(ka2) * -1)

        # part2
        I6 = ((I) * (ka2))
        I9 = I
        I10 = ((ka2) + (I9))
        I11 = -1 * I6

        I13 = (I10 * I10)
        I14 = I13 - (4 * B * I11)
        I15 = math.sqrt(I14)
        I12 = (-1 * I10) + I15
        I16 = I12 / (2 * B)

        if I16 == int:
            I16 = 0
        else:
            I16 = I16
        pKB1 = 14 - pKa1F
        pKB2 = 14 - pKa2F
        if pKa1F == 0:
            pKB1 = 0
        else:
            pKB1 = pKB1
        if pKa2F == 0:
            pKB2 = 0
        else:
            pKB2 = pKB2

        print("H2A- =", H2af)
        print("HA-2 =", I16)
        print("pH   =", pH)
        print("H+   =", Hpos)
        print("pOH  =", pOH)
        print("pKa1 =", pKa1F)
        print("pKa2 =", pKa2F)
        print("pKB1 =", pKB1)
        print("pKB2 =", pKB2)

    else:
        nothinghappens = 1

    # triprotic
    if case == "triprotic":
        kA1 = input("Enter ka1 value :")
        kA2 = input("Enter ka2 vaule :")
        kA3 = input("Enter ka3 vaule :")
        H3a = input("Enter H3A vaule :")
        # Ph=input("Enter PH vaule :")

        # pKA1=input("Enter pKa1 vaule :")
        # pKA2=input("Enter pKa2 vaule :")
        # pKA3=input("Enter pKa3 vaule :")
        # HplusH2a=input("Enter H2A+ vaule :")

        # converting to int
        ka1 = float(kA1)
        ka2 = float(kA2)
        ka3 = float(kA3)
        H3A = float(H3a)
        # pH=float(Ph)
        pKa1 = 0
        pKa2 = 0
        pKa3 = 0
        # HplusH2A=float(HplusH2a)

        A = ((ka1) * (H3A))
        B = 1
        C = 0
        D = ((-1) * A)
        E = ((ka1) * (ka1))
        F = ((E) - (4 * (B) * D))
        G = math.sqrt(F)
        H = (-ka1) + G
        I = (H) / (2 * (B))
        Hpos = I
        if I == 0:
            pH = 0
        else:
            pH = (math.log10(I) * -1)
        pOH = 14 - (pH)
        if I > 0:
            H2af = I
        else:
            H2af = 0
        log1 = 10 ** ((pKa1) * -1)
        log2 = 10 ** ((pKa2) * -1)
        log3 = 10 ** ((pKa3) * -1)
        if ka1 == 0:
            pKa1F = 0
        else:
            pKa1F = (math.log10(ka1) * -1)
        if ka2 == 0:
            pKa2F = 0
        else:
            pKa2F = (math.log10(ka2) * -1)
        if ka3 == 0:
            pKa3F = 0
        else:
            pKa3F = (math.log10(ka3) * -1)

        # part2
        I6 = ((I) * (ka2))
        I9 = I
        I10 = ((ka2) + (I9))
        I11 = -1 * I6

        I13 = (I10 * I10)
        I14 = I13 - (4 * B * I11)
        I15 = math.sqrt(I14)
        I12 = (-1 * I10) + I15
        I16 = I12 / (2 * B)
        if I16 == int:
            I16 = 0
        else:
            I16 = I16
        J2 = I16
        J6 = J2 * ka3
        J9 = Hpos
        J10 = ka3 + J9
        J11 = -1 * J6
        J12 = J10 * J10
        J13 = J12 - (4 * B * J11)
        J14 = math.sqrt(J13)
        J15 = (-1 * I10) + J14
        J16 = J15 / (2 * B)
        if J16 > 0:

            J16 = J16
            A3 = J16
        else:
            J16 = 0
            A3 = 0
        if ka3 == 0:
            I16 = I16
        else:
            I16 = I16 - A3

        pKB1 = 14 - pKa1F
        pKB2 = 14 - pKa2F
        pKB3 = 14 - pKa3F
        if pKa1F == 0:
            pKB1 = 0
        else:
            pKB1 = pKB1
        if pKa2F == 0:
            pKB2 = 0
        else:
            pKB2 = pKB2
        if pKa3F == 0:
            pKB3 = 0
        else:
            pKB3 = pKB3

        print("[H2A-] =", H2af)
        print("[HA-2] =", I16)
        print("[A-3]  =", A3)
        print("pH   =", pH)
        print("[H+]   =", Hpos)
        print("pOH  =", pOH)
        print("pKa1 =", pKa1F)
        print("pKa2 =", pKa2F)
        print("pKa3 =", pKa3F)
        print("pKB1 =", pKB1)
        print("pKB2 =", pKB2)
        print("pKB3 =", pKB3)
    else:
        if case == "diprotic":
            non = 1
        else:
            if case == "monoprotic":
                nothinghap = 0
            else:
                print("u dum, you must enter monoprotic diprotic or triprotic effing idiot")

else: print("remember to use lower case and to not misspell anything")