#Simulering av sjukdomsspridning i en vaccinerad population

import matplotlib.pyplot as plt
from math import *
from random import random, randint


# generera population
rader = 10
kolumner = 10
popAntal = rader * kolumner
pop = []
for i in range(rader):
    rad = []
    for j in range(0, kolumner):
        rad.append(1)
    pop.append(rad)

# Andelen vaccinerade
vacc = 0.50

# antalet ej vaccinerade
antal = int(ceil((popAntal*(1 - vacc))))

# sannolikheten for smittspridnining
smitta = 0.9

# Slumpa ut ickevaccinerade
for i in range(antal):
    t = 0
    while t == 0:
        n = randint(0, rader - 1)
        m = randint(0, kolumner - 1)
        if pop[n][m] == 1:
            pop[n][m] = 0
            t = 1

# Initialsmitta
s = 0
i = 1
while s == 0 and i < 5:
    n = randint(0, rader-1)
    m = randint(0, kolumner-1)
    if pop[n][m] == 0:
        pop[n][m] = 2
        s = 1
    i = i + 1

# Smittspridning
while s == 1:
    for n in range(rader):
        for m in range(kolumner):
            if pop[n][m] == 2:
                # rutan till hoger
                if m != kolumner - 1:
                    if pop[n][m+1] == 0:
                        p = random()
                        if p <= smitta:
                            pop[n][m + 1] = 3
                # rutan till vanster
                if m != 0:
                    if pop[n][m-1] == 0:
                        p = random()
                        if p <= smitta:
                            pop[n][m - 1] = 3
                # rutan nedanfor
                if n != 1:
                    if pop[n-1][m] == 0:
                        p = random()
                        if p <= smitta:
                            pop[n - 1][m] = 3
                # rutan ovanfor
                if n != rader - 1:
                    if pop[n + 1][m] == 0:
                        p = random()
                        if p <= smitta:
                            pop[n + 1][m] = 3
                # rutan ovanfor till hoger
                if (n != rader - 1) and (m != kolumner - 1):
                    if pop[n + 1][m + 1] == 0:
                        p = random()
                        if p <= smitta:
                            pop[n + 1][m + 1] = 3
                # rutan ovanfor till vonster
                if (n != rader - 1) and (m != 0):
                    if pop[n + 1][m - 1] == 0:
                        p = random()
                        if p <= smitta:
                            pop[n + 1][m - 1] = 3
                # rutan nedanfor till hoger
                if (n != 0) and (m != kolumner - 1):
                    if pop[n - 1][m + 1] == 0:
                        p = random()
                        if p <= smitta:
                            pop[n - 1][m + 1] = 3
                # rutan nedanfor till vonster
                if (n != 0) and (m != 0):
                    if pop[n - 1][m - 1] == 0:
                        p = random()
                        if p <= smitta:
                            pop[n - 1][m - 1] = 3

    # generationens smittspridare blir inaktiva
    for n in range(rader):
        for m in range(kolumner):
            if pop[n][m] == 2:
                pop[n][m] = 4

    # de smittade blir smittspridare
    for n in range(rader):
        for m in range(kolumner):
            if pop[n][m] == 3:
                pop[n][m] = 2

    # Kontroll om det fortfarande finns smittspridare
    s = 0
    for n in range(rader):
        for m in range(kolumner):
            if pop[n][m] == 2:
                s = 1

# grafisk output
# Skapar listor med koordinater
xi = []
yi = []
xv = []
yv = []
xm = []
ym = []
a = 0
b = 0
c = 0
for i in range(rader):
    for j in range(kolumner):
        if pop[i][j] == 4:
            xi.append(j)
            yi.append(i)
            a = a + 1
        if pop[i][j] == 1:
            xv.append(j)
            yv.append(i)
            b = b + 1
        if pop[i][j] == 0:
            xm.append(j)
            ym.append(i)
            c = c + 1

# Plottar resultatet
size = 400
fig = plt.figure()
fig.add_axes([0.1, 0.2, 0.6, 0.7])
plt.title("Smittspridning i vaccinerad population")
plt.scatter(xi, yi, s=size, c="red", label="Infekterade")
plt.scatter(xv, yv, s=size, c="blue", label="Vaccinerade")
plt.scatter(xm, ym, s=size, c="yellow", label="Mottagliga")
plt.xlabel("Andelen vaccinerade: " + str(b/(a+b+c)) + "\n Andelen smittade totalt: " + str(a/(a+b+c)) + "\n Andelen smittade av mottagliga:" + str(a/(a+c)))
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
#Sjukdomsspridning_i_vaccinerad_population.py
#Visar Sjukdomsspridning_i_vaccinerad_population.py.
