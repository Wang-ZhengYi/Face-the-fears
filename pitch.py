

from def_import import *

fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")
prop = fm.FontProperties(fname=fpath)

def border(x,N):
    less = (x<=N)
    return x-less*(x-N)

def colorset1(tex):
    if tex == "Simple pass":
        return 'blue'
    if tex ==  'Head pass':
        return 'black'
    if tex == 'High pass':
        return 'orange'
    if tex == 'Launch':
        return 'green'
    if tex == 'Cross':
        return 'red'
    if tex == 'Smart pass':
        return 'olive'
    if tex == 'Hand pass':
        return 'pink'
    else:
        return 'blue'

def colorset2(tex):
    if tex == "Huskies":
        return 'red'
    else:
        return 'cyan'

def colorset1(tex):
    if tex == "Simple pass":
        return 'blue'
    if tex ==  'Head pass':
        return 'black'
    if tex == 'High pass':
        return 'orange'
    if tex == 'Launch':
        return 'green'
    if tex == 'Cross':
        return 'red'
    if tex == 'Smart pass':
        return 'olive'
    if tex == 'Hand pass':
        return 'pink'
    else:
        return 'blue'



def pass_stats0(file_name):
    dataSet=[] 
    with open(file_name,'r') as file: 
        csvReader=csv.reader(file) 
        data0 = list(csvReader)
        file.close()
    return data0

def data_row(file_name,nrow):
	#read csv files in row.
    dataSet=[] 
    with open(file_name,'r') as file: 
        csvReader=csv.reader(file) 
        data1 = list([row[nrow] for row in csvReader])
        file.close()
    return data1

def holding(file_name,MatchID):
	#holding time calculations, 0 means intercepting.
	MatchID_list = data_row(file_name,0)
	idid = data_row(file_name,1)
	time0 = data_row(file_name,5)
	N = MatchID_list.count('{}'.format(MatchID))

	hold = np.zeros(N,dtype='float')
	for i in range(1,N):
		if idid[i] == idid[i-1]:
			hold[i] = float(time0[i]) - float(time0[i-1])
		else:
			hold[i] = 0
	return hold




def pitchmker(file_name,MatchID):
    ##---------------------------------clear the file folder---------------------------------##
    delList = []
    delDir = './figures'
    delList = os.listdir(delDir )

    for f in delList:
        filePath = os.path.join( delDir, f )
        if os.path.isfile(filePath):
            os.remove(filePath)
        elif os.path.isdir(filePath):
            shutil.rmtree(filePath,True)
    # print(O_P)
    #Create figure
    fig=plt.figure()
    ax=fig.add_subplot(111)
    '''
    data format:
    |MatchID--0
    |TeamID--1
    |OriginPlayerID--2
    |DestinationPlayerID--3
    |MatchPeriod--4
    |EventTime--5
    |EventSubType--6
    |EventOrigin_x--7
    |EventOrigin_y--8
    |EventDestination_x--9
    |EventDestination_y--10
    ''' 
    data,data1 = pass_stats0(file_name),data_row(file_name,0)
    
    MatchID_list = data_row(file_name,0)
    N = MatchID_list.count('{}'.format(MatchID))

    print(N)

    # while True:
    for k in range(1,N):
        plt.title('{}{}'.format('MatchID:',MatchID))
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
        for i in range(border(k-10,1),k):
                a = 1.3*float(data[i][7])
                b = 0.9*float(data[i][8])
                c = 1.3*float(data[i][9])
                d = 0.9*float(data[i][10])

                c1 = colorset1(data[i][6])
                c2 = colorset2(data[i][1])
                # c3 = colorset2(data[i][3])

                ax.arrow(a,b, c-a,d-b,
                         length_includes_head=True,
                         head_width=2.5, head_length=4,shape="full",
                         fc=c1, ec=c1,overhang=0.5,alpha=0.9,
                         # color=c1
                         )
                rotations = np.arctan((d-b)/((c-a)+(c-a==0)*0.01))*180/np.pi

                plt.text((a+c)/2,(b+d)/2,data[i][6],color=c1,fontproperties=prop,fontsize=8,rotation=rotations)
                # plt.text(a,b,i,color="black",fontproperties=prop,fontsize=8,rotation=rotations)
                # plt.text(c,d,i,color="black",fontproperties=prop,fontsize=8,rotation=rotations)

                ax.scatter(a,b,s=50,color=c2)
                ax.scatter(c,d,s=50,color=c2) 
        ax.scatter(0,-100,s=50,color='cyan',label='Opponent1')
        ax.scatter(0,-100,s=50,color='red',label='Huskies')
        ax.set_xlim(-5,135)
        ax.set_ylim(-10,95)
        plt.axis('on')
        plt.grid('on')
        ax.legend(loc='upper left',fontsize=8)
        plt.savefig('./figures/pass{}.png'.format(k),
        	dpi=300,
        	transparent = False,bbox_inches = 'tight',
        	pad_inches = 0.,
        	)
        ax.cla()
    #Tidy Axes
    
    


if __name__ == '__main__':
    file_name = 'csvdata/passingevents.csv'
    # pitchmker(file_name,1)
   
    # plt.savefig('pass.png',dpi=600, transparent = False, bbox_inches = 'tight', pad_inches = 0.25)
    # plt.show()
