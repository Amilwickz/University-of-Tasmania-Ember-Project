#Main code to calputure the data of .prt5 files.
#Changes to when you run it for a new case:
        # for fileCtr in range(13,28): these 13, and 28 are mesh numbers. Select the mesh numbers you want to process according to the simulation
        # NPC is the number of particle classes defined by PART ID. According to the order of PART IDs in the FDS, you can filter the relevant particles by changing the portion of (NPC < 3) everywhere. It coud be (NPC < 9), (NPC < 1), (2< NPC < 4) etc:
        #The output files are prt5_output_All (all the particle info (X, Y, Z, T, ID) through out the time) and prt5_params_All (only the filtered particles info at the selected time interval and selected region)
import struct
import numpy as np
import matplotlib.pyplot as plt
import os

w = open('prt5_output_All.txt', 'w')
z = open('prt5_params_All.txt', 'w')

XP = []
YP = []
ZP = []
QP = []
PC = []
TP = []  # TP=Time
newLen = 0
TA = []  # TA=Tag (unique particle ID)

for fileCtr in range(13,28):
    fileCtrP1 = fileCtr + 1
    if fileCtrP1 < 10:

        f = open(os.path.abspath(
            'C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/FDS prt5 files/Ember_Project_test_4_000' + '%d' % fileCtrP1 + '.prt5'), 'rb')
    else:
        f = open(os.path.abspath(
            'C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/FDS prt5 files/Ember_Project_test_4_00' + '%d' % fileCtrP1 + '.prt5'), 'rb')

    print(fileCtrP1)

    f.read(4)
    test_int = int.from_bytes(f.read(4), 'little')
    f.read(4)

    f.read(4)
    version = int.from_bytes(f.read(4), 'little')
    f.read(4)

    f.read(4)
    N_PART = int.from_bytes(f.read(4), 'little')
    f.read(4)
    #print(N_PART)
    PC = [0, 0]
    N_QUANTITIES = []
    SMV_LABEL = []
    UNITS = []
    for NPC in range(N_PART):
        f.read(4)
        PC[0] = int.from_bytes(f.read(4), 'little')
        PC[1] = int.from_bytes(f.read(4), 'little')
        N_QUANTITIES.append(PC[0])
        #print(PC[0])
        f.read(4)

        for NQ in range(N_QUANTITIES[NPC]):
            f.read(4)
            SMV_LABEL.append(struct.unpack('30s', (f.read(30))))
            #print(SMV_LABEL[NQ])
            f.read(4)

            f.read(4)
            UNITS.append(struct.unpack('30s', (f.read(30))))
            #print(UNITS[NQ])
            f.read(4)

    STIME_N = []
    n = 0
    NPLIM = 0
    maxNPLIM = 0
    while 1 == 1:

        n = n + 1
        # f.read(4)
        stime_tmp = f.read(8)
        if not stime_tmp:
            break
        stime_tmp = struct.unpack('xxxxf', stime_tmp)
        f.read(4)
        #print(stime_tmp[0])
        # NPC = Number of Particle Class, i.e. what kind of particle it is
        # NPLIM = Number of Particles Limit, i.e. how many particles of species NPC are in the domain
        # TA = Integer tag for each particle, not currently used but may be in future
        for NPC in range(N_PART):
            f.read(4)
            NPLIM = int.from_bytes(f.read(4), 'little')

            f.read(4)

            f.read(4)

            # for i in range(NPLIM):
            for i in range(NPLIM):
                xps = struct.unpack('<f', f.read(4))  # xps = x position single
                if (NPC < 3):
                    XP.append(xps[0])
                    TP.append(stime_tmp)

            for i in range(NPLIM):
                yps = struct.unpack('<f', f.read(4))  # xps = x position single
                if (NPC < 3):
                    YP.append(yps[0])

            for i in range(NPLIM):
                zps = struct.unpack('<f', f.read(4))  # xps = x position single
                if (NPC < 3):
                    ZP.append(zps[0])

            f.read(4)

            # for NP in range(NPLIM):

            f.read(4)
            for tagID in range(NPLIM):
                ta = f.read(4)
                if (NPC < 3):
                    TA.append(struct.unpack('i', ta))
            # ta=f.read(4*NPLIM)  #Integer tag for each particle
            # TA.append(struct.unpack('i'*NPLIM, ta)  )
            f.read(4)

            if N_QUANTITIES[NPC] > 0:
                f.read(4)
                for NQ in range(N_QUANTITIES[NPC]):
                    qp = f.read(4 * NPLIM)
                    qp = struct.unpack('<' + 'f' * NPLIM, qp)
                    QP.append(qp)
                    # print(qp)

            f.read(4)


    f.close()

    #plt.plot(XP[x],YP[x])
    # TP_MAX=max(TP)
    TP_MAX = 100
    for x in range(len(XP)):
        w.write('%f' % XP[x] + ',')
        w.write('%f' % YP[x] + ',')
        w.write('%f' % ZP[x] + ',')
        w.write('%f' % TP[x] + ',')
        w.write('%f' % TA[x] + ',\n')
        if ((ZP[x] < 1.0) and (TP[x][0] > 98.5) and (TP[x][0] < 100)):  # (x > 0*len(ZP))
            z.write('%f' % XP[x] + ',')
            z.write('%f' % YP[x] + ',')
            z.write('%f' % ZP[x] + ',')
            z.write('%f' % TP[x] + ',')
            z.write('%i' % TA[x] + ',\n')
w.close()
z.close()












