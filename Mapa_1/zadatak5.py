import matplotlib.pyplot as plt

def ploting(x1,y1,x2,y2):
    plt.plot([x1,x2], [y1,y2])
    plt.scatter([x1],[y1])
    plt.scatter([x2],[y2])
    pf=int(input("Ako zelis plotanu funkciju upisi broj 1, ako zelis u pdfu upisi 2:"))
    if pf==1:
        plt.show()       
    if pf==2:
        ime_grafa=input("Unesi ime grafa:")
        plt.savefig(ime_grafa, format="pdf", bbox_inches="tight")
ploting(1,1,0,0)