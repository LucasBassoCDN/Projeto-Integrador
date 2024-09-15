print(f"P | Q | R | S |  P -> Q | R -> S | P V R | (P -> Q)^(R -> S)^(P V R) | Q V S | ((P -> Q)^(R -> S)^(P V R)) -> (Q V S)"
for a in range(0, 2, 1):
    for b in range(0, 2, 1):
        for c in range(0, 2, 1):
            if a==0:
                P="V"
            else:
                P="F"
            if b==0:
                Q="V"
            else:
                Q="F"
            if c==0:
                R="V"
            else:
                R="F"
            if P=="V" and Q=="F":
                PQ="F"
            else:
                PQ="V"
            if R=="V" and S=="F":
                RS="F"
            else:
                RS="V"
            if P=="F" and R=="F":
                PR="F"
            else:
                PR="V"
            if PQ=="V" and RS=="V" and PR=="V":
                PQRS="V"
            else:
                PQRS="F"
            if Q=="F" and S=="F":
                QR="F"
            else:
                QR="V"
            if PQRS=="V" and QR=="F":
                print(f"{P} | {Q} | {R} | {S} |  {PQ} | {RS} | {PR} | {PQRS} | {QS} | F"
            else:
                print(f"{P} | {Q} | {R} | {S} |  {PQ} | {RS} | {PR} | {PQRS} | {QS} | V"
