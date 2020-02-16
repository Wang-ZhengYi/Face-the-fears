

from def_import import *


def colorset(tex):
    if tex == "Simple pass":
        return 'blue'
    if tex ==  'Head pass':
        return 'black'
    if tex == 'High pass':
        return 'yellow'
    if tex == 'Launch':
        return 'green'
    if tex == 'Cross':
        return 'red'
    if tex == 'Smart pass':
        return 'oringe'
    if tex == 'Hand pass':
        return 'pink'
    else:
        return 'blue'



def createPitch(O_P,D_P,tex1,tex2,tex3):
    scaler = np.mat([[1.3,0.],
        [0.,0.9]])
    O_P = np.dot(O_P,scaler)
    D_P = np.dot(D_P,scaler)
    #Create figure
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,90], color="black")
    plt.plot([0,130],[90,90], color="black")
    plt.plot([130,130],[90,0], color="black")
    plt.plot([130,0],[0,0], color="black")
    plt.plot([65,65],[0,90], color="black")
    
    #Left Penalty Area
    plt.plot([16.5,16.5],[65,25],color="black")
    plt.plot([0,16.5],[65,65],color="black")
    plt.plot([16.5,0],[25,25],color="black")
    
    #Right Penalty Area
    plt.plot([130,113.5],[65,65],color="black")
    plt.plot([113.5,113.5],[65,25],color="black")
    plt.plot([113.5,130],[25,25],color="black")
    
    #Left 6-yard Box
    plt.plot([0,5.5],[54,54],color="black")
    plt.plot([5.5,5.5],[54,36],color="black")
    plt.plot([5.5,0.5],[36,36],color="black")
    
    #Right 6-yard Box
    plt.plot([130,124.5],[54,54],color="black")
    plt.plot([124.5,124.5],[54,36],color="black")
    plt.plot([124.5,130],[36,36],color="black")
    
    #Prepare Circles
    centreCircle = plt.Circle((65,45),9.15,
                        color="black",fill=False)
    centreSpot = plt.Circle((65,45),0.8,color="black")
    leftPenSpot = plt.Circle((11,45),0.8,color="black")
    rightPenSpot = plt.Circle((119,45),0.8,color="black")
    
    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)
    
    #Prepare Arcs
    leftArc = Arc((11,45),height=18.3,width=18.3,
        angle=0,theta1=310,theta2=50,color="black")
    rightArc = Arc((119,45),height=18.3,width=18.3,
        angle=0,theta1=130,theta2=230,color="black")

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)
    
    c1 = colorset(tex1)
    c2 = colorset(tex2)
    c3 = colorset(tex3)

    # for i in range(O_P.shape[1]):
    i = 2
    ax.arrow(O_P[i:0], O_P[i:1], D_P[i:0]-O_P[i,0], D_P[i:1]-O_P[i,1],
                 length_includes_head=True,
                 head_width=0.25, head_length=0.5, 
                 fc='r', ec='b',
                 color=c1
                 )
    
    plt.scatter(O_P[:,0].tolist(),O_P[:,1].tolist(),s=50,color=c2)
    plt.scatter(D_P[:,0].tolist(),D_P[:,1].tolist(),s=50,color=c3)



    #Tidy Axes
    plt.axis('on')
    plt.grid("on")
    





    


if __name__ == '__main__':
    file_name = './csvdata/passingevents0.dat'
    data = np.loadtxt(file_name)
    lenth1 = 4
    A = np.zeros(shape=(lenth1,2),dtype='float')
    B = np.zeros(shape=(lenth1,2),dtype='float')

    A[:,0] = data[0:lenth1,1]
    A[:,1] = data[0:lenth1,2]
    B[:,0] = data[0:lenth1,3]
    B[:,1] = data[0:lenth1,4]
    print(A)
    print(B)
    t1 = ''
    t2 = ''
    t3 = ''
    createPitch(A,B,t1,t2,t3)
    plt.savefig('pass.png',dpi=600, transparent = False, bbox_inches = 'tight', pad_inches = 0.25)
    plt.show()
