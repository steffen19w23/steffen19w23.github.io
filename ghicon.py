import numpy as np
import matplotlib.pyplot as plt

gh=[[1,0,1,0,1],[0]*5,[1,1,0,1,1],[0,1,1,1,0],[0,0,1,0,0]]
gh=[[1,0,1,0,1],[1]*5,[1,0,0,0,1],[1,0,1,0,1],[0,1,0,1,0]]
gih=[[0]*12]+[[0]+[c for c in row for j in range(2)]+[0] for row in gh for i in range(2)]+[[0]*12]
giih=[[0]*7]+[[0]+row+[0] for row in gh]+[[0]*7]
egh=sum(sum(row) for row in gh)/25
egih=sum(sum(row) for row in gih)/144
egiih=sum(sum(row) for row in giih)/49
ghh=[[cell+0*egh+0.25*(scell-egih) for cell in row for scell in srow] for row in gih for srow in gh]
ghhh=[[cell+0.13*(scell-egiih) for cell in row for scell in srow] for row in ghh for srow in giih]
ghhh=[[egiih+(cell-egiih)*(1+.3*((scell-egiih)*1+1.2*(sscell-egh))) for cell in row for scell in srow for sscell in ssrow] \
     for row in giih for srow in giih for ssrow in gh]


(xscale,yscale)=(2,2)
(xres,yres)=(xscale*6*7*5,yscale*6*7*5)
z=np.zeros((xscale*len(ghhh[0]),yscale*len(ghhh)))
for i,row in enumerate(ghhh):
  for ii in range(i*yscale,(i+1)*yscale):
    for j,cell in enumerate(row):
      for jj in range(j*xscale,(j+1)*xscale):
        z[ii,jj]=cell
fig=plt.figure()
fig.set_size_inches(xres/fig.get_dpi(),yres/fig.get_dpi())
fig.add_axes(plt.Axes(fig, [0., 0., 1., 1.]))
fig.gca().set_axis_off()
green=(0x5b/255,0xcc/255,0x8c/255)
purple=(0x7c/255,0x74/255,0xce/255)
gray=0xf0/255
ipol=lambda idx,lam: gray+lam*(purple[idx]-gray)
p=plt.imshow([[[ipol(i,x) for i in range(3)] for x in y[35:-35]] for y in z[35:-35]])
print(yres,len(z)-70)
plt.gcf().savefig('ghicon_528.png',dpi=fig.get_dpi())
plt.show()

'''
gh=[[1,0,1,0,1],[0]*5,[1,1,0,1,1],[0,1,1,1,0],[0,0,1,0,0]]
gih=[[0]*12]+[[0]+[c for c in row for j in range(2)]+[0] for row in gh for i in range(2)]+[[0]*12]
giih=[[0]*7]+[[0]+row+[0] for row in gh]+[[0]*7]
egh=sum(sum(row) for row in gh)/25
egih=sum(sum(row) for row in gih)/144
egiih=sum(sum(row) for row in giih)/49
ghh=[[cell+0*egh+0.25*(scell-egih) for cell in row for scell in srow] for row in gih for srow in gh]
ghhh=[[cell+0.13*(scell-egiih) for cell in row for scell in srow] for row in ghh for srow in giih]
ghhh=[[egh+(cell-egh)*(1+.25*(scell-egih)*(1+.3*(sscell-egiih))) for cell in row for scell in srow for sscell in ssrow] \
     for row in gih for srow in giih for ssrow in gh]

for i,row in enumerate(ghhh):
  for ii in range(i*yscale,(i+1)*yscale):
    for j,cell in enumerate(row):
      for jj in range(j*xscale,(j+1)*xscale):
        z[ii,jj]=cell
fig=plt.figure()
fig.set_size_inches(xres/fig.get_dpi(),yres/fig.get_dpi())
fig.gca().set_axis_off()
green=(0x5b/255,0xcc/255,0x8c/255)
gray=0xf0/255
ipol=lambda idx,lam: gray+lam*(green[idx]-gray)
p=plt.imshow([[[ipol(i,x) for i in range(3)] for x in y] for y in z])
plt.gcf().savefig('ghicon_c57.png',dpi=fig.get_dpi(),bbox_inches='tight')
plt.show()
'''
