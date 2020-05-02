

class Ship():


    length = 1
    status_map = []
    coord_map = []
    around_map = []
    death = 0
    prefix = ""
    ship_correct = 1


    def __init__(self,length,rasp,keypoint):
        self.status_map = []
        self.around_map = []
        self.coord_map = []
        self.death = 0
        self.ship_correct = 1
        self.length = length
        self.prefix = keypoint.split("_")[0]
        stroka = int(keypoint.split("_")[1])
        stolb = int(keypoint.split("_")[2])
        for i in range(length):
            self.status_map.append(0)
            if stolb + i > 9 or stroka + i > 9:
                self.ship_correct = 0
            if rasp == 0:
                self.coord_map.append(self.prefix+"_"+str(stroka)+"_"+str(stolb+i))
            else:
                self.coord_map.append(self.prefix+"_"+str(stroka+i)+"_"+str(stolb))
        for point in self.coord_map:
            ti = int(point.split("_")[1])
            tj = int(point.split("_")[2])
            for ri in range(ti-1,ti+2):
                for rj in range(tj-1,tj+2):
                    if ri>=0 and ri<=9 and rj>=0 and rj<=9:
                        if not(self.prefix+"_"+str(ri)+"_"+str(rj) in self.around_map) and not(self.prefix+"_"+str(ri)+"_"+str(rj) in self.coord_map):
                            self.around_map.append(self.prefix+"_"+str(ri)+"_"+str(rj))


    def shoot(self,shootpoint):
        status = 0
        for point in range(len(self.coord_map)):
            if self.coord_map[point] == shootpoint:
                self.status_map[point] = 1
                status = 1
                break
        if not(0 in self.status_map):
            status = 2
            self.death = 1
        return status