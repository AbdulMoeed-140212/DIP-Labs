import matplotlib.pyplot as plt

dt = 10**(-5)
k = 1
m= 7294.3
qau = 79
qa = 2
t=0
vx = 0
vy = 9.5925208
x_stat = x_init = 0.0
y_stat = y_init = -0.005
r0 = pow((x_init ** 2 + y_init ** 2),.5)

i=1
for i in range(10):
    x = []
    y = []
    r=0
    while(r <= 1.1*r0):
        ax = (k * qau * qa)/ (m * (x_init**2 + y_init**2))
        ay = (k * qau * qa)/ (m * (x_init ** 2 + y_init ** 2))

        vx = vx + ax * dt
        vy = vy + ay * dt
        x_init = x_init + vx * dt
        y_init = y_init + vy * dt
        r = x_init**2 + y_init**2
        t = t + dt
        x.append(x_init)
        y.append(y_init)
    dt = 10 ** (-5)
    x_stat= x_stat + 0.0001
    x_init = x_stat
    y_init = y_stat
    vx = 0
    vy = 9.5925208
    r0 = pow((x_init ** 2 + y_init ** 2),.5)

    plt.plot(x , y)

plt.show()


