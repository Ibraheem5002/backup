from ursina import *

h1 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(-3.75,2.75,0),
    enabled=False
)

h2 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(-3.25,2.75,0),
    enabled=False
)

h3 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(-2.75,2.75,0),
    enabled=False
)

h4 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(-2.25,2.75,0),
    enabled=False
)

h5 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(-1.75,2.75,0),
    enabled=False
)


h10 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(3.75,2.75,0),
    enabled=False
)

h9 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(3.25,2.75,0),
    enabled=False
)

h8 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(2.75,2.75,0),
    enabled=False
)

h7 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(2.25,2.75,0),
    enabled=False
)

h6 = Entity(
    model="quad",
    texture=r"assets\ui\hrt0.png",
    scale=0.5,
    position=(1.75,2.75,0),
    enabled=False
)

l1 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(-3.75,2.25,0),
    enabled=False
)

l2 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(-3.25,2.25,0),
    enabled=False
)

l3 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(-2.75,2.25,0),
    enabled=False
)

l4 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(-2.25,2.25,0),
    enabled=False
)

l5 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(-1.75,2.25,0),
    enabled=False
)

l10 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(3.75,2.25,0),
    enabled=False
)

l9 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(3.25,2.25,0),
    enabled=False
)

l8 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(2.75,2.25,0),
    enabled=False
)

l7 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(2.25,2.25,0),
    enabled=False
)

l6 = Entity(
    model="quad",
    texture=r"assets\ui\lgt0.png",
    scale=0.5,
    position=(1.75,2.25,0),
    enabled=False
)

pHealth = [h1,h2,h3,h4,h5]
cHealth = [h10,h9,h8,h7,h6]
pCharge = [l1,l2,l3,l4,l5]
cCharge = [l10,l9,l8,l7,l6]

def update(pH,cH,pC,cC):
    for i in range(5):
        pHealth[i].enabled = True
        cHealth[i].enabled = True
        pCharge[i].enabled = True
        cCharge[i].enabled = True
    
    update_pHealth(pH)
    update_cHealth(cH)
    update_pCharge(pC)
    update_cCharge(cC)

def hide():
    for i in range(5):
        pHealth[i].enabled = False
        cHealth[i].enabled = False
        pCharge[i].enabled = False
        cCharge[i].enabled = False

def update_pHealth(H):
    if H > 10: H = 10

    Q = int(H/2)
    R = H % 2

    for i in range(Q):
        pHealth[i].texture = r"assets\ui\hrt0.png"
        
    if Q < 5:
        if R == 1:
            pHealth[Q].texture = r"assets\ui\hrt1.png"
        else:
            pHealth[Q].texture = r"assets\ui\hrt2.png"
    
    for i in range(Q+1,5):
        pHealth[i].texture = r"assets\ui\hrt2.png"

def update_cHealth(H):
    if H > 10: H = 10

    Q = int(H/2)
    R = H % 2

    for i in range(Q):
        cHealth[i].texture = r"assets\ui\hrt0.png"
        
    if Q < 5:
        if R == 1:
            cHealth[Q].texture = r"assets\ui\hrt3.png"
        else:
            cHealth[Q].texture = r"assets\ui\hrt2.png"
    
    for i in range(Q+1,5):
        cHealth[i].texture = r"assets\ui\hrt2.png"

def update_pCharge(C):
    if C > 5: C = 5

    for i in range(C):
        pCharge[i].texture = r"assets\ui\lgt0.png"
    
    for i in range(C,5):
        pCharge[i].texture = r"assets\ui\lgt1.png"

def update_cCharge(C):
    if C > 5: C = 5
    
    for i in range(C):
        cCharge[i].texture = r"assets\ui\lgt0.png"
    
    for i in range(C,5):
        cCharge[i].texture = r"assets\ui\lgt1.png"