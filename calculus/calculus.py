from sympy import symbols, diff, integrate, Matrix, cos, sin, simplify, Interval, exp, sqrt, log, pi, series, limit, E, acos, asin, tan, atan
from sympy.plotting import plot, plot3d
#from mpl_toolkits import Axes3D
#the common operation of R and all the polinomial and non linear function are those of sympy
#the operation of dot and cross product are functions
#all the other operations related to integration and/or differentiation are attributes
#of the object(s) function and/or field based on the attributes offered by sympy
#x, y, z and ρ , θ, φ are of type Symbol

#function and vectorial field are object(s) carachterized by:
#function: function and dimension
#field: components(function) and dimension

#vectors and/or points are tuple objects

#sets are objects charachterized by:
#dimension, primw variable  and Interval object(s): 1 for set_1, 2 for set_2
#set_3 is characterized by dimension, prime variable and a set_2 object


#coordinate systems
x, y, z= symbols ('x, y, z')
cart=(x, y, z)
ρ, θ, φ= symbols ('ρ, θ, φ')
pol=(ρ, θ, φ)
pol_2=(ρ*cos(θ), ρ*sin(θ))
pol_3=(ρ*sin(θ)*cos(φ), ρ*sin(θ)*sin(φ), ρ*cos(θ))
#dot product
def dot(u, v):
    if len(u)!=len(v):
        print('dimensional error')
        return -1
    else:
        a=0
        for i in range(len(u)):
            a=a+u[i]*v[i]
        return a
#cross product
def cross(u, v):
    if len(u)==3 and len(u)==len(v):
        return (u[1]*v[2]-u[1]*v[2], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
    else :
        print('dimensional error')
        return -1
#return the geometric norm of a vector
def norm(u):
    return simplify(sqrt(dot(u, u)))
#determines wheter or not a function is in cartesian coordinate system
def pol_check(f):
    g=f.f
    #returns the gradiens in cartesian coordinates
    a=0
    for i in range(f.n):
        if g.has(pol[i])==True:
            a=1
        else :
            continue
    if a==1:
        return True
    if a==0:
        return False
#asses the value of a matrix for a x0 point
def eval_m(m, x0):
    if len(m)==9:
        return m.subs({x:x0[0], y:x0[1], z:x0[2]})
    if len(m)==4:
        return m.subs({x:x0[0], y:x0[1]})

#set in R (interval)
class set_1:
    def __init__(self, a=Interval(0, 1), n=1):
        self.a=a
        self.n=n
#set in R2
class set_2:
    def __init__(self, t=x, a=Interval(0, x), b=Interval(0, 1), n=2, s=False):
        self.t=t
        self.a=a
        self.b=b
        self.n=n
        self.s=s  #indicates wheter or not the set is in polar coordinates
#set in R3
class set_3:
    def __init__(self, t=z, a=Interval(0, 1), s2=set_2(), n=3, pol=False):
        self.t=t
        self.a=a
        self.s2=s2
        self.n=n
        self.pol=pol
#surface
class sigma:
    def __init__(self, t=z, s=1, i=set_2(), p=False, a='+'):
        self.t=t
        self.s=s  #function g(x, y)
        self.i=i
        self.p=p  #p must be True if polar coordinates must be used
        self.a=a  #a indicates if the normal vector must be oriented as self.t or opposed
    #returns a parametrization of the surface
    def sigmap(self):
        if self.t==z:
            return (x, y, self.s)
        if self.t==x:
            return (self.s, y, z)
        if self.t==y:
            return (x, self.s, z)
    #returns the ortogonal vector to the surface in a generic (x, y) point
    def n(self):
        if self.t==z:
            if self.a=='+':
                return (-diff(self.s, x), -diff(self.s, y), 1)
            if self.a=='-':
                return (diff(self.s, x), diff(self.s, y), -1)
        if self.t==x:
            if self.a=='+':
                return (1, -diff(self.s, y), -diff(self.s, z))
            if self.a=='-':
                return (-1, diff(self.s, y), diff(self.s, z))
        if self.t==y:
            if self.a=='+':
                return (-diff(self.s, x), 1, -diff(self.s, z))
            if self.a=='-':
                return (diff(self.s, x), -1, diff(self.s, z))
#scalar function
class function:
    def __init__(self, f=1, n=1, var=(x)):
        self.f=f
        self.n=n
        self.var=var
    #assess the function f in x0
    def eval(self, x0):
        if self.n==1:
            return function(simplify(self.f.subs({x:x0})))
        if self.n==3:
            return function(simplify(self.f.subs({x:x0[0], y:x0[1], z:x0[2]})), 3)
        if self.n==2:
            if self.f.has(z)==False:
                return function(simplify(self.f.subs({x:x0[0], y:x0[1]})), 2)
            if self.f.has(y)==False:
                return function(simplify(self.f.subs({x:x0[0], z:x0[1]})), 2)
            if self.f.has(x)==False:
                return function(simplify(self.f.subs({z:x0[0], y:x0[1]})), 2)
    #returns the derivative N.B.: ONLY VALID FOR MONO-VARIABLE FUNCTIONS
    def der(self):
        return function(simplify(diff(self.f, x)), 1)
    #return the function in the polar coordinate system
    def pol(self):
        if self.n==2:
            return self.eval(pol_2)
        if self.n==3:
            return self.eval(pol_3)
    #return gradiens of f
    def grad(self):
        f=self.f
        if pol_check(self)==False:
            if self.n==2:
                return field_2(function(simplify(diff(f, x)), 2), function(simplify(diff(f, y)), 2), 2)
            if self.n==3:
                return field(function(simplify(diff(f, x)), 3), function(simplify(diff(f, y)), 3), function(simplify(diff(f, z)), 3))
            if self.n==1:
                return function(simplify(diff(f, x)), 1)
        #returns the gradiens in polar coordinates
        if pol_check(self)==True:
            if self.n==1:
                return False
            if self.n==2:
                return field_2(function(simplify(diff(f, ρ)), 2), function(simplify(diff(f, θ)), 2))
            if self.n==3:
                return field(function(simplify(diff(f, ρ)), 3), function(simplify(diff(f, θ)), 3), function(simplify(diff(f, φ)), 3))
    #return the plane tangent z(x, y) in x0=(x0, y0)
    def t_pl(self, x0):
        if self.n!=2:
             print('dimensional error')
             return -1
        else:
            h=self.eval(x0)
            g=self.grad().eval(x0).vec()
            s=(x-x0[0], y-x0[0])
            d_=simplify(dot(g, s))
            d=function(d_, 2)
            return function(simplify(h.f+d.f), 2)
    #prints the function
    def prnt(self):
        if pol_check(self)==True:
            if self.n==2:
                print('f(ρ, θ)=', self.f)
            if self.n==3:
                print('f(ρ, θ, φ)=', self.f)
        if pol_check(self)==False:
            if self.n==2:
                print('f(x, y)=', self.f)
            if self.n==3:
                print('f(x, y, z)=', self.f)
    #returns the value of the integral calculated over the set
    def integral(self, s):
        if pol_check(self)==False:
            if self.n==2 and s.n==2:
                if s.s==True:
                    return self.pol().integral(s)
                if self.var==(x, y):
                    if s.t==x:
                        return integrate(self.f, (x, s.a.inf, s.a.sup), (y, s.b.inf, s.b.sup))
                    if s.t==y:
                        return integrate(self.f, (y, s.a.inf, s.a.sup), (x, s.b.inf, s.b.sup))
                if self.var==(z, y):
                    if s.t==z:
                        return integrate(self.f, (z, s.a.inf, s.a.sup), (y, s.b.inf, s.b.sup))
                    if s.t==y:
                        return integrate(self.f, (y, s.a.inf, s.a.sup), (z, s.b.inf, s.b.sup))
                if self.var==(x, z):
                    if s.t==x:
                        return integrate(self.f, (x, s.a.inf, s.a.sup), (z, s.b.inf, s.b.sup))
                    if s.t==z:
                        return integrate(self.f, (z, s.a.inf, s.a.sup), (x, s.b.inf, s.b.sup))
            if self.n==3 and s.n==3:
                if s.pol==True:
                    return self.pol().integral(s)
                if s.t==z:
                    fi=function(integrate(self.f, (z, s.a.inf, s.a.sup)), 2)
                    return fi.integral(s.s2)
                if s.t==y:
                    fi=function(integrate(self.f, (y, s.a.inf, s.a.sup)), 2)
                    return fi.integral(s.s2)
                if s.t==x:
                    fi=function(integrate(self.f, (z, s.a.inf, s.a.sup)), 2)
                    return fi.integral(s.s2)
            if self.n==1:
                if self.f.has(x)!=True:
                    return integrate(self.f.subs({y:x, z:x}), (x, s.a.inf, s.a.sup))
                else :
                    return integrate(self.f, (x, s.a.inf, s.a.sup))
        if pol_check(self)==True:
            if self.n==2 and s.n==2:
                if s.t==x:              #assess if Ω is θ-simple
                    return integrate(self.f*ρ, (θ, s.a.inf, s.a.sup), (ρ, s.b.inf, s.b.sup))
                if s.t==y:              #assess if Ω is x-simple
                    return integrate(self.f*ρ, (ρ, s.a.inf, s.a.sup), (θ, s.b.inf, s.b.sup))
            if self.n==3 and s.n==3:
                fi=function(integrate(simplify(self.f*ρ**2*sin(θ)), (φ, s.a.inf, s.a.sup)), 2)
                return fi.integral(s.s2)
            else :
                    return integrate(self.f, (x, s.a.inf, s.a.sup))
        elif self.n!=s.n:
            print('dimensional error: set and function are non compatible')
            return False
    #return the line integral of the function  the gamma function is a field(field_2) object
    def l_integral(self, g):
        if self.n==g.n:
            f=self.eval(g.vec())
            g_=g.der()
            n=simplify(norm(g_.vec()))
            fi=function(simplify(f.f*n), 1)
            return fi.integral(g.dom)
        else :
            print('dimensional error: function and gamma are non compaible')
            return False
    #returns the surface integral of the function
    def s_integral(self, s):
        f1=self.eval(s.sigmap())
        n=norm(s.n())
        fi=function(simplify(f1.f*n), 2)
        if s.p==True:
            f=fi.pol()
            return f.integral(s.i)
        if s.p==False:
            return fi.integral(s.i)
    #returns the indefinite integral
    def i_integral(self, x):
        return function(simplify(integrate(self.f, x)), self.n)
    #returns the limit
    def lim(self, var, x0):
        return limit(self.f, var, x0)
    #returns the limit for x0+
    def limdx(self, var, x0):
        return self.lim(var, x0)
    #returns the limit for xo+
    def limsx(self, var, x0):
        return limit(self.f, var, x0, '-')
    #returns the Taylor series function centered in 'x0', of oreder 'ord' from the variable 'x'
    def taylor(self, var, x0, degr):
        return function(series(self.f, var, x0, degr), self.n)
    #assess if x0 is a maximum, minimum or saddle point
    def max_min(self, x0):
        f=self.f
        if self.n==2:
            h1=Matrix(([diff(f, x, 2), diff(f, x, y)], [diff(f, x, y), diff(f, y, 2)]))
        if self.n==3:
            h1=Matrix(([diff(f, x, 2), diff(f, x, y), diff(f, x, z)], [diff(f, x, y), diff(f, y, 2), diff(f, y, z)],
                    [diff(f, x, z), diff(f, z, y), diff(f, z, 2)]))
        h=eval_m(h1, x0)
        if self.n==2:
            d=h.det()
            if d>0 and h[0, 0]>0:
                print('x0 is a minimum point for f')
            if d>0 and h[0, 0]<0:
                print('x0 is a maximum point for f')
            if d<0:
                print('x0 is a saddle point for f ')
            if d==0:
                print('NSPCN')
        if self.n==3:
            d=(h[0, 0], h[1, 1], h[2, 2])
            f=0
            s=0
            for i in d:
                if i>0:
                    f=1
                    for i in d:
                        if i>0:
                            f=-1
                        else :
                            if i<0:
                                f=0
                                s=0
                                break
                            if i==0:
                                s=1

                if i<0:
                    for i in d:
                        if i<0:
                            f=1
                        else:
                            f=0
                            break
                break
            if f==1:
                print('x0 is a maximum point for f')
            if f==-1:
                print('x0 is a minimum point for f')
            if f==0:
                print('NSPCN')
            if s==1:
                print('x0 is a saddle point for f')



#vectorial field
class field:
    def __init__(self, f1=function(), f2=function(), f3=function(), n=3, dom=set_1()):
        self.f1=f1
        self.f2=f2
        self.f3=f3
        self.n=n
        self.dom=dom
    #asses the value of the field in x0
    def eval(self, x0):
        return field(self.f1.eval(x0), self.f2.eval(x0), self.f3.eval(x0), self.n, self.dom)
    #prints the field
    def prnt(self):
        print(self.vec())
    #return the divergence of the field
    def div(self):
        return function(simplify(diff(self.f1.f, x)+diff(self.f2.f, y)+diff(self.f3.f, z)), 3)
    #return the curl of the field
    def curl(self):
        f1=function((diff(self.f3.f, y)-diff(self.f2.f, z)), 3)
        f2=function((diff(self.f1.f, z)-diff(self.f3.f, x)), 3)
        f3=function((diff(self.f2.f, x)-diff(self.f1.f, y)), 3)
        return field(f1, f2, f3, 3)
    #returns a vector (tuple object)
    def vec(self):
        return (self.f1.f, self.f2.f, self.f3.f)
    #returns the path integral
    def p_integral(self, gamma):
        F=self.eval(gamma.vec())
        g=gamma.der().vec()
        fi=function(dot(F.vec(), g))
        return fi.integral(gamma.dom)
    #returns the derivative of the field N.B.: ONLY VALID FOR MONO-VARIABLE FIELDS
    def der(self):
        return field(self.f1.der(), self.f2.der(), self.f3.der(), 3, self.dom)
    #returns the flux of F given a surface
    def flux(self, s):
        F=self.eval(s.sigmap()).vec()
        n=s.n()
        d=dot(F, n)
        f=function(d, 2)
        if s.p==False:
            return f.integral(s.i)
        if s.p==True:
            return f.pol().integral(s.i)
    #Stokes theorem
    def stokes(self, s):
        r=self.curl()
        return r.flux(s)
    #Gauss theorem
    def gauss(self, s):
        return self.div().integral(s)

#vectorial field in R2
class field_2:
    def __init__(self, f1=function(), f2=function(), n=2, dom=set_1()):
        self.f1=f1
        self.f2=f2
        self.n=n
        self.dom=dom
    def eval(self, x0):
        return field_2(self.f1.eval(x0), self.f2.eval(x0), 2)
    #returns a vector of R2
    def vec(self):
        return (self.f1.f, self.f2.f)
    #prints the vector
    def prnt(self):
        print(self.vec())
    #returns the derivative of the field N.B.: ONLY VALID FOR MONO-VARIABLE FIELDS
    def der(self):
        return field_2(self.f1.der(), self.f2.der(), 2, self.dom)
    #returns the path integral
    def p_integral(self, gamma):
        F=self.eval(gamma.vec())
        g=gamma.der().vec()
        F1=F.vec()
        fi=function(dot(F1, g))
        return fi.integral(gamma.dom)
    #Green theorem
    def green(self, s):
        f=function(diff(self.f2.f, x)-diff(self.f1.f, y), 2)
        return f.integral(s)
