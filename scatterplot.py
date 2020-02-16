#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
created on Jan.,2020

@Author:
'''

from def_import import *


def readCsv(file_name):
    with open(file_name,'r') as f:
      rander=csv.reader(f)
    return rander

def drawArrow(A, B):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.arrow(A[0], A[1], B[0]-A[0], B[1]-A[1],
             length_includes_head=True,
             head_width=0.25, head_length=0.5, fc='r', ec='b')
    ax.grid()
    ax.set_aspect('equal')
    plt.tight_layout()
    
    plt.savefig('arrow.png', transparent = True, bbox_inches = 'tight', pad_inches = 0.25) 
    # plt.show()


def drawscatter():
	plt.scatter(x[:,7], x[:,5], s=x[:,2], alpha=0.5, color=c)




'''
def cut_img(img, x, y):

    x_center = img.size[0] / 2
    y_center = img.size[1] / 2
    new_x1 = x_center - x//2
    new_y1 = y_center - y//2
    new_x2 = x_center + x//2
    new_y2 = y_center + y//2
    new_img = img.crop((new_x1, new_y1, new_x2, new_y2))
    return new_img

    img1 = Image.open('1.jpg')
    img2 = Image.open('2.jpg')
    #print(img1.size, img2.size)

    new_x = min(img1.size, img2.size)[0]  
    new_y = min(img1.size, img2.size)[1]

    new_img1 = cut_img(img1, new_x, new_y)
    new_img2 = cut_img(img2, new_x, new_y)
    #print(new_img1.size, new_img2.size)


    final_img2 = Image.blend(new_img1, new_img2,)

    final_img2.show()
'''


if __name__ == '__main__':
	file_name = 'csvdata/fullevents.csv'
	csv_data = readCsv(file_name)
	n = 150
	x = np.random.rand(n,3)
	c = np.random.rand(n,3)
    print(x.shape)
	plt.scatter(x[:,0], x[:,1], s=x[:,2]*500, alpha=0.5, color=c)
	# pitch.createPitch()
	plt.show()