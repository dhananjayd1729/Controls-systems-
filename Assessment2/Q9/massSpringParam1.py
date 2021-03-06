# Mass Spring Damper System Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory

import massSpringParam as P

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative gain
tau_max = P.tau_max  # limit on control signal

#  tuning parameters
tr = 1.5 # part (a)
#tr = 0.4  # tuned to get fastest possible rise time before saturation.
zeta = 0.7
ki = 0.2 #integrator gain

# desired natural frequency
wn = 2.2/tr
alpha1 = 2.0*zeta*wn
alpha0 = wn**2

# compute PD gains
kp = P.m*(alpha0 - (P.k/P.m))
kd = P.m*(alpha1 - (P.b/P.m))

print('kp: ', kp)
print('kd: ', kd)
print('ki: ', ki)