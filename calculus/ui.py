from os import system
f_op=('1. evaluation', '2. gradiens', '3. tangent plane', '4. integral', '5. linear integral', '6. surface integral', '7. indefinite integral', '8. limit', '9. Taylor series', '10. max or min', '11. plot', '0. exit')
F_op=('1. evaluation', '2. divergence', '3. curl', '4. path integral', '5. flux integral', '6. green theorem', '7. stokes theorem', '8. gauss theorem', '0. exit')

cart = ('x', 'y', 'z')

print('Hello there!\nThis is a user interface for the calculus module.\n')
#returns an array in Rn
def get_array(n):
    print('insert the value of x0')
    x0 = [] 
    for i in range(n):
        b=float(input(f'{cart[i]} = '))
        x0.append(b)
    return tuple(x0)

#handles the recursive menu and the loop escape
def r_menu():
    c = int(input('press 0 to exit or 9 to return to main menu\n'))
    if c == 0:
        print('Bye')
        return -1
    if c == 9:
        menu()


#menu 
def menu():
    print('Chose an option:')
    print('1. salar function')
    print('2. vectorial field')
    a = int(input())
    fp=open('exe.py', 'w')    
    fp.write('from calculus import*\n')
    
    if a == 1:
        print('which operation do you wish to execute?')
        for i in f_op:
            print(i)
        b = int(input())
        
        
        g=input('function=')
        n=int(input('n='))
        fp.write(f'f = function({g}, {n})\n')

        if b == 1:
           x0=get_array(n)
           fp.write(f'x0={x0}\nf.eval(x0).prnt() \n') 
        if b == 2:
            fp.write('f.grad().prnt()')
        if b == 3:
            if n != 2:
                print('invalid option')
                r_menu()
            if n == 2:
                x0=get_array(n)
                fp.write(f'x0={x0}\nf.t_pl(x0).prnt()\n')
        if b == 4:
            if n == 1:
                print('insert interval')
                inf=int(input('a='))
                sup=int(input('b='))
                fp.write(f's=set_1(Interval({inf}, {sup}))\nprint(f.integral(s))')
            if n == 2:
                t=input('is the set y or x simple?')
                pol=input('is the set in polar coordinates?')
                infx=input('f(x) inf=')
                supx=input('f(x) sup=')
                inf=input('a=')
                sup=input('b=')
                fp.write(f's=set_2({t}, Interval({infx}, {supx}), Interval({inf}, {sup}), 2, {pol})\n')
                fp.write('f.integral(s)')
            if n == 3:
                t=input('what is the axis of reference?')
                pol=input('is the set in polar coordinates?')
                infz=input('f(z)=')
                supz=input('f(z)=')
                print('insert the 2-dimensional set')
                t1=input('is the set y or x simple?')
                pol1=input('is the set in polar coordinates?')
                infx=input('f(x)=')
                supx=input('f(x)=')
                inf=input('a=')
                sup=input('b=')
                fp.write(f'set=set_2({t1}, Interval({infx}, {supx}), Interval({inf}, {sup}), 2, {pol1})\ns=set_3({t}, Interval({infz}, {supz}), set, 3, {pol})\nprint(f.integral(s))')
        if b == 5:
            print('insert gamma function')
            if n == 2:
                f1=input('f1(x)=')
                f2=input('f2(x)=')
                inf=input('lower bound=')
                sup=input('upper bound=')
                fp.write(f'gamma=field_2(function({f1}, 1), function({f2}, 1), 2, set_1(Interval({inf}, {sup})))\nprint(f.l_integral(gamma))')
            if n == 3:
                f1=input('f1(x)=')
                f2=input('f2(x)=')
                f3=input('f3(x)=')
                inf=input('lower bound=')
                sup=input('upper bound=')
                fp.write(f'gamma=field(function({f1}, 1), function({f2}, 1), function({f3}, 1), 3, set_1(Interval({inf}, {sup})))\nprint(simplify(f.l_integral(gamma)))')
            
            else :
                print('invalid option')
                r_menu()
        if b == 6:
            print('insert sigma function')
            t=input('axis of reference=')
            s=input('function g(x, y)=')
            print('insert set')
            t1=input('is the set x or y simple?')
            pol=input('is the set in polar coordinates?')
            infx=input('f1(x)=')
            supx=input('f2(x)=')
            inf=input('a=')
            sup=input('b=')
            vec=input('is the normal vector positive or negative?')
            fp.write(f"sigma=sigma({t}, {s}, set_2({t1}, Interval({infx}, {supx}), Interval({inf}, {sup}), 2, {pol}), False, '{vec}')\nprint(simplify(f.s_integral(sigma)))")
        if b == 7:
            var=input('insert variable')
            fp.write(f'i=f.i_integral({var})\nprint(i.f)')
        if b == 8:
            var=input('variable=')
            x0=input('x0=')
            fp.write(f'print(f.lim({var}, {x0}))')
        if b == 9:
            var=input('variable=')
            x0=input('x0=')
            degr=input('degree=')
            fp.write(f't=f.taylor({var}, {x0}, {degr})\nprint(t.f)')
        if b == 10:
            x0=get_array(n)
            fp.write(f'f.max_min({x0})')
        if b == 11:
            print('insert interval')
            l=input('lower bound=')
            u=input('uppper bound=')
            fp.write(f'f.plot(set_1(Interval({l}, {u})))')
        if b == 0:
            r_menu()

    if a == 2:
        for i in F_op:
            print(i)
        b = int(input())

        n=int(input('dimension='))
        if n == 2:
            f1=input('f1=')
            f2=input('f2=')
            fp.write(f'F=field_2(function({f1}, 2), function({f2}, 2))\n')
        if n == 3:
            f1=input('f1=')
            f2=input('f2=')
            f3=input('f3=')
            fp.write(f'F=field(function({f1}, 3), function({f2}, 3), function({f3}, 3))\n')

        if b == 1:
            x0=get_array(n)
            fp.write(f'F.eval({x0}).prnt()')
        if b == 2:
            if n == 2:
                print('invalid option')
                r_menu()
            if n == 3:
                fp.write(f'F.div().prnt()')
        if b == 3:
            if n == 2:
                print('invalid option')
                r_menu()
            if n == 3:
                fp.write(f'F.curl().prnt()')
        if b == 4:
            print('insert gamma function')
            if n == 2:
                g1=input('g1=')
                g2=input('g2=')
                inf=input('lower bound=')
                sup=input('upper bound=')
                fp.write(f'gamma=field_2(function({g1}, 2), function({g2}, 2), 2, set_1(Interval({inf}, {sup})))\n')
            if n == 3:
                g1=input('g1=')
                g2=input('g2=')
                g3=input('g3=')
                inf=input('lower bound=')
                sup=input('upper bound=')
                fp.write(f'gamma=field(function({g1}, 3), function({g2}, 3), function({g3}, 3), 3, set_1(Interval({inf}, {sup})))\n')
            fp.write('print(F.p_integral(gamma))')
        if b == 5:
            if n == 3:
                print('insert sigma function')
                t=input('axis of reference=')
                s=input('function g(x, y)=')
                print('insert set')
                t1=input('is the set x or y simple?')
                pol=input('is the set in polar coordinates?')
                infx=input('f1(x)=')
                supx=input('f2(x)=')
                inf=input('a=')
                sup=input('b=')
                vec=input('is the normal vector positive or negative?')
                fp.write(f"sigma=sigma({t}, {s}, set_2({t1}, Interval({infx}, {supx}), Interval({inf}, {sup})), {pol},'{vec}')\n")
                fp.write(f'print(F.flux(sigma))')
            else:
                print('invalid option')
                r_menu()
        if b == 6:
            if n == 2:
                print('insert set')
                t=input('is the set x or y simple?')
                pol=input('is the set in polar coordinates?')
                infx=input('f1(x)=')
                supx=input('f2(x)=')
                inf=input('a=')
                sup=input('b=')
                fp.write(f'set=set_2({t}, Interval({infx}, {supx}), Interval({inf}, {sup}), 2, {pol})\n')
                fp.write('print(F.green(set))')
            else :
                print('invalid option')
                r_menu()
        if b == 7:
            if n == 3:
                print('insert sigma function')
                t=input('axis of reference=')
                s=input('function g(x, y)=')
                print('insert set')
                t1=input('is the set x or y simple?')
                pol=input('is the set in polar coordinates?')
                infx=input('f1(x)=')
                supx=input('f2(x)=')
                inf=input('a=')
                sup=input('b=')
                vec=input('is the normal vector positive or negative?')
                fp.write(f"sigma=sigma({t}, {s}, set_2({t1}, Interval({infx}, {supx}), Interval({inf}, {sup})), {pol},'{vec}')\n")
                fp.write(f'print(F.stokes(sigma))')
            else:
                print('invalid option')
                r_menu()
        if b == 8:
            if n == 3:
                print('insert set\n')
                t=input('what is the axis of reference?')
                pol=input('is the set in polar coordinates?')
                infz=input('f(z)=')
                supz=input('f(z)=')
                print('insert the 2-dimensional set')
                t1=input('is the set y or x simple?')
                pol1=input('is the set in polar coordinates?')
                infx=input('f(x)=')
                supx=input('f(x)=')
                inf=input('a=')
                sup=input('b=')
                fp.write(f'set2=set_2({t1}, Interval({infx}, {supx}), Interval({inf}, {sup}), 2, {pol1})\ns=set_3({t}, Interval({infz}, {supz}), set2, 3, {pol})\n')
                fp.write('print(F.gauss(s))')
            else :
                print('invalid option')
                r_menu()
        if b == 9:
            system('python plotting.py')
        if b == 0:
            r_menu()

    if a != 1 and a != 2:
        r_menu()


    fp.close()
    system('python3 ~/Desktop/python/calculus/exe.py')
    r_menu()

menu() 
