x1 = int(input('a1 noktasındaki degeri  x1 girin'))
y1 = int(input('a1 noktasındaki degeri  y1girin'))
x2 = int(input('b1 noktasındaki degeri x2 girin'))
y2 = int(input('b1 noktasındaki degeri y2 girin'))
def koordinat(x1,y1,x2,y2):
    formul = (((x2-x1)**2+(y2-y1))**2)**1/2
    print('iki nokta arasındaki uzaklık', formul)
    
koordinat(x1,y1,x2,y2)