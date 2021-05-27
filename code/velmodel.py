#==============================================================================
# Python Imports
#==============================================================================
import numpy                   as np
from   scipy.interpolate       import interp1d
from   devito                  import *
#==============================================================================

#==============================================================================
# GM Model 1
#==============================================================================
def GMVelModel(setup,vp,abc):

    compx = setup.compx
    compz = setup.compz
    nptx  = setup.nptx
    nptz  = setup.nptz
    x0    = setup.x1
    x1    = setup.x0
    z0    = setup.z0
    z1    = setup.z1

    nptxvel = 1407
    nptzvel = 311
    x0vel   = 0.        
    x1vel   = 70300.     
    z0vel   = 0.        
    z1vel   = 9920.

    Xvel    = np.linspace(x0vel,x1vel,nptxvel)
    Zvel    = np.linspace(z0vel,z1vel,nptzvel)

    vp = vp.reshape((nptxvel,nptzvel))
    
    fscale = 10**(-3) 
    vp = vp*fscale

    X0 = np.linspace(x0,x1,nptx)  
    Z0 = np.linspace(z0,z1,nptz)
    
    C0x = np.zeros((nptx,nptzvel))
    
    for j in range(nptzvel):
        x  = Xvel
        z  = vp[0:nptxvel,j]
        cs = interp1d(x,z,kind='linear')
        xs = X0
        C0x[0:nptx,j] = cs(xs)
        
    v0 = np.zeros((nptx,nptz))  
    
    for i in range(nptx):
        x  = Zvel
        z  = C0x[i,0:nptzvel]
        cs = interp1d(x,z,kind='linear')
        xs = Z0
        v0[i,0:nptz] = cs(xs)

    if(abc=='pml'):
      
        X1 = np.linspace((x0+0.5*setup.hx),(x1-0.5*setup.hx),nptx-1)
        Z1 = np.linspace((z0+0.5*setup.hz),(z1-0.5*setup.hz),nptz-1)
        
        C11x = np.zeros((nptx-1,nptzvel))
        
        v1 = np.zeros((nptx-1,nptz-1))
        
        for j in range(nptzvel):
            x  = Xvel
            z  = vp[0:nptxvel,j]
            cs = interp1d(x,z,kind='linear')
            xs = X1
            C11x[0:nptx-1,j] = cs(xs)
            
        for i in range(nptx-1):
            x  = Zvel
            z  = C11x[i,0:nptzvel]
            cs = interp1d(x,z,kind='linear')
            xs = Z1
            v1[i,0:nptz-1] = cs(xs)

        return v0, v1
    
    else:
    
        return v0
#==============================================================================   

#==============================================================================
def GMVelModelnew(setup,vp,abc):

    nptx  = setup.nptx
    nptz  = setup.nptz
    x0    = setup.x0
    x1    = setup.x1
    z0    = setup.z0
    z1    = setup.z1
    
    nptxvel = 758
    nptzvel = 282
    x0vel   = 0.        
    x1vel   = 9462.5    
    z0vel   = 0.        
    z1vel   = 8992

    Xvel    = np.linspace(x0vel,x1vel,nptxvel)
    Zvel    = np.linspace(z0vel,z1vel,nptzvel)
    
    X0 = np.linspace(x0,x1,nptx)  
    Z0 = np.linspace(z0,z1,nptz)
   
    C0x = np.zeros((nptx,nptzvel))
    
    for j in range(nptzvel):
        x  = Xvel
        z  = vp[0:nptxvel,j]
        cs = interp1d(x,z,kind='linear')
        xs = X0
        C0x[0:nptx,j] = cs(xs)
        
    v0 = np.zeros((nptx,nptz))  
    
    for i in range(nptx):
        x  = Zvel
        z  = C0x[i,0:nptzvel]
        cs = interp1d(x,z,kind='linear')
        xs = Z0
        v0[i,0:nptz] = cs(xs)

    if(abc=='pml'):
      
        X1 = np.linspace((x0+0.5*setup.hx),(x1-0.5*setup.hx),nptx-1)
        Z1 = np.linspace((z0+0.5*setup.hz),(z1-0.5*setup.hz),nptz-1)
        
        C11x = np.zeros((nptx-1,nptzvel))
        
        v1 = np.zeros((nptx-1,nptz-1))
        
        for j in range(nptzvel):
            x  = Xvel
            z  = vp[0:nptxvel,j]
            cs = interp1d(x,z,kind='linear')
            xs = X1
            C11x[0:nptx-1,j] = cs(xs)
            
        for i in range(nptx-1):
            x  = Zvel
            z  = C11x[i,0:nptzvel]
            cs = interp1d(x,z,kind='linear')
            xs = Z1
            v1[i,0:nptz-1] = cs(xs)

        return v0, v1
    
    else:
    
        return v0
#==============================================================================   
          
#==============================================================================
# Homogenous Model - Daiane
#==============================================================================      
def HomogVelModel(setup,abcs,vel=1.5):

    nptx  = setup.nptx
    nptz  = setup.nptz
    
    v0 = np.zeros((nptx,nptz))  
    v0[:,:] = vel
    
    if(abcs=='pml'):
        
        v1 = np.zeros((nptx-1,nptz-1))
        
        v1[:,:] = vel

        return v0, v1
    
    else:
        
        return v0
#==============================================================================

#==============================================================================
# Homogenous Model - Felipe
#==============================================================================      
def HomogVelModel2(setup, abcs):

    nptx  = setup.nptx
    nptz  = setup.nptz
    x0    = setup.x0
    x1    = setup.x1
    z0    = setup.z0
    z1    = setup.z1
    x0pml = setup.x0pml
    x1pml = setup.x1pml
    z0pml = setup.z0pml
    z1pml = setup.z1pml
  
    X0   = np.linspace(x0,x1,nptx)
    Z0   = np.linspace(z0,z1,nptz)

    v0   = np.zeros((nptx,nptz))                     

    xmpml = 0.5*(x0pml+x1pml)
    zmpml = 0.5*(z0pml+z1pml)
        
    pxm = 0
    pzm = 0
        
    for i in range(0,nptx):
        
        if(X0[i]==xmpml): pxm = i
            
    for j in range(0,nptz):
        
        if(Z0[j]==zmpml): pzm = j
            
    p0 = 0    
    p2 = pzm
    p4 = nptz
        
    v0[0:nptx,p0:p2] = 1.5
    v0[0:nptx,p2:p4] = 1.5
    
    if(abcs=='pml'):
       
        v1 = np.zeros((nptx-1,nptz-1))
 
        p0 = 0    
        p2 = pzm
        p4 = nptz-1
                
        v1[0:nptx-1,p0:p2] = 1.5
        v1[0:nptx-1,p2:p4] = 1.5
        
        return v0,v1
    
    else:
    
        return v0
#==============================================================================

#==============================================================================
# Heterogeneous Model - Felipe
#==============================================================================      
def HetVelModel2(setup,abcs):

    nptx  = setup.nptx
    nptz  = setup.nptz
    x0    = setup.x0
    x1    = setup.x1
    z0    = setup.z0
    z1    = setup.z1
    x0pml = setup.x0pml
    x1pml = setup.x1pml
    z0pml = setup.z0pml
    z1pml = setup.z1pml
  
    X0   = np.linspace(x0,x1,nptx)
    Z0   = np.linspace(z0,z1,nptz)

    v0   = np.zeros((nptx,nptz))                     

    xmpml = 0.5*(x0pml+x1pml)
    zmpml = 0.5*(z0pml+z1pml)
        
    pxm = 0
    pzm = 0
        
    for i in range(0,nptx):
        
        if(X0[i]==xmpml): pxm = i
            
    for j in range(0,nptz):
        
        if(Z0[j]==zmpml): pzm = j

    p0 = 0    
    p2 = pzm
    p4 = nptz
            
    v0[0:nptx,p0:p2] = 1.5
    v0[0:nptx,p2:p4] = 2.5
        
    if(abcs=='pml'):
       
        v1 = np.zeros((nptx-1,nptz-1))
 
        p0 = 0    
        p2 = pzm
        p4 = nptz-1
                
        v1[0:nptx-1,p0:p2] = 1.5
        v1[0:nptx-1,p2:p4] = 2.5
        
        return v0,v1
    
    else:
    
        return v0
#==============================================================================

#==============================================================================
# Marmosi Model
#==============================================================================
def MarmoVelModel(setup,vp,abc):

    compx = setup.compx
    compz = setup.compz
    nptx  = setup.nptx
    nptz  = setup.nptz
    x0    = setup.x0
    x1    = setup.x1
    z0    = setup.z0
    z1    = setup.z1

    nptxvel =  len(vp[:])
    nptzvel =  len(vp[0,:])
    
    x0vel   =  0        
    x1vel   =  17000     
    z0vel   =  0       
    z1vel   =  3500.

    Xvel    = np.linspace(x0vel,x1vel,nptxvel)
    Zvel    = np.linspace(z0vel,z1vel,nptzvel)

    fscale = 10**(-3) 
    vp     = vp*fscale

    X0 = np.linspace(x0,x1,nptx)  
    Z0 = np.linspace(z0,z1,nptz)
    
    C0x = np.zeros((nptx,nptzvel))
    
    for j in range(nptzvel):
        x  = Xvel
        z  = vp[0:nptxvel,j]
        cs = interp1d(x,z,kind='linear',fill_value="extrapolate")
        xs = X0
        C0x[0:nptx,j] = cs(xs)
    
    v0 = np.zeros((nptx,nptz))  
    
    for i in range(nptx):
        x  = Zvel
        z  = C0x[i,0:nptzvel]
        cs = interp1d(x,z,kind='linear',fill_value="extrapolate")
        xs = Z0
        v0[i,0:nptz] = cs(xs)

    if(abc=='pml'):
      
        X1 = np.linspace((x0+0.5*setup.hx),(x1-0.5*setup.hx),nptx-1)
        Z1 = np.linspace((z0+0.5*setup.hz),(z1-0.5*setup.hz),nptz-1)
        
        C11x = np.zeros((nptx-1,nptzvel))
        
        v1 = np.zeros((nptx-1,nptz-1))
        
        for j in range(nptzvel):
            x = Xvel
            z = vp[0:nptxvel,j]
            cs = interp1d(x,z,kind='linear',fill_value="extrapolate")

            xs = X1
            C11x[0:nptx-1,j] = cs(xs)
            
        for i in range(nptx-1):
            x  = Zvel
            z  = C11x[i,0:nptzvel]
            cs = interp1d(x,z,kind='linear', fill_value="extrapolate")
            xs = Z1
            v1[i,0:nptz-1] = cs(xs)

        return v0, v1
    
    else:
    
        return v0
#==============================================================================

#==============================================================================
# Circle - Isotropic
#==============================================================================      
def CircleIsot(setup,abcs,r,vp_circle=3.0,vp_background=2.5):

    nptx = setup.nptx
    nptz = setup.nptz
    x0    = setup.x0
    x1    = setup.x1
    z0    = setup.z0
    z1    = setup.z1
    x0pml = setup.x0pml
    x1pml = setup.x1pml
    z0pml = setup.z0pml
    z1pml = setup.z1pml
    hx    = setup.hx
    hz    = setup.hz
    npmlx = setup.npmlx
    npmlz = setup.npmlz
    
    xc    = (x1pml-x0pml)/2    
    zc    = (z1pml-z0pml)/2 

    X0   = np.linspace(x0,x1,nptx)
    Z0   = np.linspace(z0,z1,nptz)
    v0   = np.zeros((nptx,nptz))                     
  
    for i in range(nptx):
        for j in range(nptz):
            val = (X0[i]-xc)**2 + (Z0[j]-zc)**2
            if (val<=r**2): 
                v0[i,j] = vp_circle
            else:        
                v0[i,j] = vp_background
    
    if(abcs=='pml'):
       
        v1  = np.zeros((nptx-1,nptz-1))
        X1  = np.linspace((x0+0.5*hx),(x1-0.5*hx),nptx-1)
        Z1  = np.linspace((z0+0.5*hz),(z1-0.5*hz),nptz-1)
     
        for i in range(nptx-1):    
            for j in range(nptz-1):
                val = (X1[i]-xc)**2 + (Z1[j]-zc)**2
                if (val<=r**2): 
                    v1[i,j] = vp_circle
                else:
                    v1[i,j] = vp_background
    
        return v0,v1
    
    else:
    
        return v0                
#==============================================================================

#==============================================================================
# Homogenous Density Model
#==============================================================================      
def HomogDenModel(setup):

    nptx  = setup.nptx
    nptz  = setup.nptz
    x0    = setup.x0
    x1    = setup.x1
    z0    = setup.z0
    z1    = setup.z1
    x0pml = setup.x0pml
    x1pml = setup.x1pml
    z0pml = setup.z0pml
    z1pml = setup.z1pml
  
    X0   = np.linspace(x0,x1,nptx)
    Z0   = np.linspace(z0,z1,nptz)

    d0      = np.zeros((nptx,nptz))                     
    d0[:,:] = 1.0
    
    return d0
#==============================================================================

#==============================================================================
# Marmosi Density Model
#==============================================================================
def MarmoDenModel(setup,den):

    compx = setup.compx
    compz = setup.compz
    nptx  = setup.nptx
    nptz  = setup.nptz
    x0    = setup.x0
    x1    = setup.x1
    z0    = setup.z0
    z1    = setup.z1

    nptxvel =  len(den[:])
    nptzvel =  len(den[0,:])
    
    x0vel   =  0        
    x1vel   =  17000     
    z0vel   =  0       
    z1vel   =  3500.

    Xvel    = np.linspace(x0vel,x1vel,nptxvel)
    Zvel    = np.linspace(z0vel,z1vel,nptzvel)

    fscale = 10**(-3) 
    den     = den*fscale

    X0 = np.linspace(x0,x1,nptx)  
    Z0 = np.linspace(z0,z1,nptz)
    
    D0x = np.zeros((nptx,nptzvel))
    
    for j in range(nptzvel):
        
        x  = Xvel
        z  = den[0:nptxvel,j]
        cs = interp1d(x,z,kind='linear',fill_value="extrapolate")
        xs = X0
        D0x[0:nptx,j] = cs(xs)
    
    d0 = np.zeros((nptx,nptz))  
    
    for i in range(nptx):
        
        x  = Zvel
        z  = D0x[i,0:nptzvel]
        cs = interp1d(x,z,kind='linear',fill_value="extrapolate")
        xs = Z0
        d0[i,0:nptz] = cs(xs)
    
    return d0
#==============================================================================

#==============================================================================
# Velocity Model
#==============================================================================
def SetVel(model,setup,setting,grid, **kwargs):
    
    (x, z)  = grid.dimensions
    
    if(model['vp']=='Circle'):
    
        vp_circle      = kwargs.get('vp_circle')
        vp_background  = kwargs.get('vp_background')
        r              = kwargs.get('r')
        v0             = CircleIsot(setup,setting["Abcs"],r,vp_circle,vp_background)
        d0m            = HomogDenModel(setup)
        
    elif(model['vp']=='Marmousi'):
        
        vp_file  = kwargs.get('vp_file')
        den_file = kwargs.get('den_file')
        v0       = MarmoVelModel(setup, vp_file, setting["Abcs"])
        d0m      = MarmoDenModel(setup, den_file)

    elif(model['vp']=='GM'):
        
        vp_file = kwargs.get('vp_file')
        v0      = GMVelModel(setup, vp_file, setting["Abcs"])
        d0m     = HomogDenModel(setup)
    
    elif(model['vp']=='GMnew'):  
    
        vp_file = kwargs.get('vp_file')
        v0      = GMVelModelnew(setup, vp_file, setting["Abcs"])
        d0m     = HomogDenModel(setup)

    if(setting["Abcs"]=='pml'):
        
        vel0 = Function(name="vel0",grid=grid,space_order=setup.sou,staggered=NODE,dtype=np.float64)
        vel0.data[:,:]  = v0[0]
        vel1 = Function(name="vel1", grid=grid,space_order=setup.sou,staggered=(x,z),dtype=np.float64)
        vel1.data[0:setup.nptx-1,0:setup.nptz-1]  = v0[1]
        vel1.data[setup.nptx-1,0:setup.nptz-1]    = vel1.data[setup.nptx-2,0:setup.nptz-1]
        vel1.data[0:setup.nptx,setup.nptz-1]      = vel1.data[0:setup.nptx,setup.nptz-2]

        d0 = Function(name="d0",grid=grid,space_order=setup.sou,staggered=NODE,dtype=np.float64)
        d0.data[:,:] = d0m
        
        return [vel0, vel1], v0[0], d0
    
    else:
        
        vel0 = Function(name="vel0",grid=grid,space_order=setup.sou,staggered=NODE,dtype=np.float64)
        vel0.data[:,:] = v0
        d0 = Function(name="d0",grid=grid,space_order=setup.sou,staggered=NODE,dtype=np.float64)
        d0.data[:,:] = d0m
        
        return vel0, v0, d0
#==============================================================================