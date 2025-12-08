

### Examples 12/8/25 
If $S$ is the graph of $z=g(x,y)$. 
$$\iint_{S}F\cdot d S= \iint_{D}F\cdot \langle -g_{x},-g_{y},1 \rangle $$
Let $D$ be the rectangle in the $\phi, \theta$ plan with a constant $\rho=1$, find, where $r$ is the position [[Vector Field]]
$$dS=r\cdot R \sin(\phi) \cos(\theta)$$
$$\iint_{S}r\cdot dS=\int_{0}^{2\pi} \int_{0}^{\pi} r \cdot r \cdot R\sin(\phi)d \phi d \theta =$$
$$\int_{0}^{2\pi}\int_{0}^{\pi} \|r\|^2 \cdot R\sin(\phi)d \phi d \theta $$
$$\int_{0}^{2\pi}\int_{0}^{\pi}  \sin(\phi)d \phi d \theta =2\pi \cdot 2=4\pi$$
#### Ex 2.) $z=12,x^2+y^2\leq 25$ describe a disk of radius $5$ lying in the plane $z=12$ oriented upward. Compute $\iint_{S} r \cdot dS$ where $r$ is the position vector 

The function generated is the disk $x^2 +y^2 \leq 25$ at $z=12$ with a domain situated at the same but for $z=12$. We can use:
$$\implies g(x,y)=12 \implies \nabla g(x,y)=\langle 0,0,1 \rangle $$
$$dS=\langle -g_{x},-g_{y},1 \rangle dxdy= \hat{k}$$
Let $r$ be the position vector field:
$$\iint_{S}r\cdot dS= \iint_{D}r\cdot \hat{k} \cdot dx dy =\iint_{x^2+y^2 \leq 25} z\cdot dxdy=12\iint_{x^2+y^2\leq 25}dxdy$$
$$=\boxed{\therefore 25\cdot 12 \cdot \pi}$$

### Ex 3.)
Let $S$ be the sphere $x^2+y^2+z^2=R^2$, compute the following surface integral:
$$\iint_{S}\frac{\vec{r}}{r^3}\cdot dS$$
We know that $r=\|\vec{r}\|=R$
This particular problem is known as the [[3 Dimensional Gauss Law]]. Let $\vec{r}= \langle x,y,z \rangle$. 
We can use spherical coordinates with a fixed $r$ to find $dS$. $D$ is the rectangular region on the $d\phi,d\theta$ plane where $0 \leq \phi \leq \pi$ and  $0 \leq \theta \leq 2\pi$ 
$$dS=\vec{r}R \sin(\phi) d\phi d\theta$$
$$\iint_{S}\frac{\vec{r}}{r^3}\cdot dS=\iint_{D}\frac{\vec{r}}{r^3} \cdot \iint_{S}\vec{r}R=\frac{r^3}{r^3} d\phi d\theta=\iint_{s}dS=4 \pi$$
The integral here is completely independent of the radius and is always $4\pi$ despite any change in $R$. 

### Ex 4.) Let $S$ be the part of the Cylinder of radius $2$ centered on the z-axis with $x>0, y>0, 0 \leq z \leq 3$ oriented outward. Let $F=\langle 0,y,0 \rangle$. Compute:
$$\iint_{S}F \cdot dS$$

$$X(\theta, z )= \langle 2\cos(\theta),2\sin(\theta),z \rangle$$
$$D= 0 \leq \leq \pi/2, 0 \leq z \leq 3$$
$$dS=\langle \cos(\theta),\sin(\theta),0 \rangle\cdot 2 d \theta dz$$
$$\iint_{S}F\cdot dS = \iint_{S}\langle 0,y,0 \rangle \cdot \langle cos(\theta),\sin(\theta,0) \rangle $$
$$=\int_{0}^3 \int_{0}^{\pi/2}4\sin(\theta)^2d\theta dz=12 \int_{0}^{\pi/2}\sin^2(\theta)d\theta=12\int_{0}^{\pi/2}\frac{1-\cos(2\theta)}{2}d\theta$$
$$=\boxed{\therefore 3\pi}$$
### Ex 5.) Let $F = \langle 0,0,z \rangle$. Compute $\iint_{S}F \cdot dS$ where $S$ is the upper hemisphere of radius $2$, centered at the origin oriented outward 
$$X_{(\theta,\phi)}=\langle \rangle $$
$$dS=\vec{r} \cdot R\sin(\phi)d\phi d\theta  $$
$$\iint_{S}F\cdot dS=\iint_{D}z^2R\sin(\phi)d\theta d\phi=\iint_{D}R^3\cos(\phi)^2\sin(\phi)d\theta d\phi$$
$$=8\cdot\int_{0}^{2\pi} \int_{0}^{\pi/2} \cos^2(\phi)\sin(\phi) $$
$$=16\pi \cdot -\frac{\cos^3(\phi)}{3}\bigg|_{0}^{\pi/2}=\frac{16\pi}{3}$$
$$=\boxed{\therefore \frac{16\pi}{3}}$$

---
# Additional 

Let $S$ be a closed upper hemisphere made out of $S_{1}$ which is an upper hemisphere with no bottom, and $S_{2}$ is the disc on the bottom. The unit normal for $S_{2}$ in the positive direction points towards the bottom

We the bottom disc can be though of as a graph of a 2 variable function, $z=g(x,y)=0$. 
If we are to use the formula for the surface element, then we need to multiply it by $-1$ in order to force the unit normal to it using $\langle -g_{x},-g_{y},1 \rangle$ to obtain $\langle g_{x},g_{y},-1 \rangle$


























