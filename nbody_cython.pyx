"""
    Auther: Zewei Liu
    Data: 02/19/2017
    N-body simulation.
    all the optimization included
    Original runtime: 109.012778997
    This program runtime: 34.3830599785
    Relative Speedup: 2.701859625021585
    Cython version running time: 8.29397201538086
    Relative Speedup: 13.143615483008611
"""

from itertools import combinations
import time



cdef advance(dt,int iterations,BODIES_keys,BODIES_keys_pair,bodies_local):
    '''
        advance the system one timestep
    '''
    cdef float x1, y1, z1, m1, x2, y2, z2, m2, dx, dy, dz, mag, vx, vy, vz, m
    cdef list v1, v2, r 
    for _ in range(iterations):
        for body1,body2 in BODIES_keys_pair:
            ([x1, y1, z1], v1, m1) = bodies_local[body1]
            ([x2, y2, z2], v2, m2) = bodies_local[body2]
            (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
            # update vs

            mag = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
            v1[0] -= dx * m2 * mag
            v1[1] -= dy * m2 * mag
            v1[2] -= dz * m2 * mag
            v2[0] += dx * m1 * mag
            v2[1] += dy * m1 * mag
            v2[2] += dz * m1 * mag
            
        for body in BODIES_keys:
            (r, [vx, vy, vz], m) = bodies_local[body]
            r[0] += dt * vx
            r[1] += dt * vy
            r[2] += dt * vz

cdef report_energy(BODIES_keys,BODIES_keys_pair,bodies_local,float e=0.0):
    '''
        compute the energy and return it so that it can be printed
    '''
    cdef float x1, y1, z1, m1, x2, y2, z2, m2, dx, dy, dz, vx, vy, vz, m
    cdef list v1, v2, r 

    for body1,body2 in BODIES_keys_pair:
        ((x1, y1, z1), v1, m1) = bodies_local[body1]
        ((x2, y2, z2), v2, m2) = bodies_local[body2]
        (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
        
    for body in BODIES_keys:
        (r, [vx, vy, vz], m) = bodies_local[body]
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
        
    return e

cdef offset_momentum(ref, BODIES_keys, bodies_local,float px=0.0, float py=0.0, float pz=0.0):
    '''
        ref is the body in the center of the system
        offset values from this reference
    '''
    cdef float vx, vy, vz, m 
    cdef list r, v 
    for body in BODIES_keys:
        (r, [vx, vy, vz], m) = bodies_local[body]
        px -= vx * m
        py -= vy * m
        pz -= vz * m
        
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m

cdef nbody(int loops, reference,int iterations,BODIES):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''

    BODIES_keys = BODIES.keys()
    # bodies key pair represen different combination of bodies keys 
    BODIES_keys_pair = list(combinations(BODIES_keys,2))
    bodies_local = BODIES
    # Set up global state
    offset_momentum(BODIES[reference], BODIES_keys, bodies_local)

    for _ in range(loops):
        # report_energy()
        advance(0.01,iterations,BODIES_keys,BODIES_keys_pair,bodies_local)
        print(report_energy(BODIES_keys,BODIES_keys_pair,bodies_local))
def main():
    cdef float PI = 3.14159265358979323
    cdef float SOLAR_MASS = 4 * PI * PI
    cdef float DAYS_PER_YEAR = 365.24
    cdef dict BODIES = {
    'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),
    'jupiter': ([4.84143144246472090e+00,
                 -1.16032004402742839e+00,
                 -1.03622044471123109e-01],
                [1.66007664274403694e-03 * DAYS_PER_YEAR,
                 7.69901118419740425e-03 * DAYS_PER_YEAR,
                 -6.90460016972063023e-05 * DAYS_PER_YEAR],
                9.54791938424326609e-04 * SOLAR_MASS),
    'saturn': ([8.34336671824457987e+00,
                4.12479856412430479e+00,
                -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                4.99852801234917238e-03 * DAYS_PER_YEAR,
                2.30417297573763929e-05 * DAYS_PER_YEAR],
               2.85885980666130812e-04 * SOLAR_MASS),
    'uranus': ([1.28943695621391310e+01,
                -1.51111514016986312e+01,
                -2.23307578892655734e-01],
               [2.96460137564761618e-03 * DAYS_PER_YEAR,
                2.37847173959480950e-03 * DAYS_PER_YEAR,
                -2.96589568540237556e-05 * DAYS_PER_YEAR],
               4.36624404335156298e-05 * SOLAR_MASS),
    'neptune': ([1.53796971148509165e+01,
                 -2.59193146099879641e+01,
                 1.79258772950371181e-01],
                [2.68067772490389322e-03 * DAYS_PER_YEAR,
                 1.62824170038242295e-03 * DAYS_PER_YEAR,
                 -9.51592254519715870e-05 * DAYS_PER_YEAR],
                5.15138902046611451e-05 * SOLAR_MASS)}
    temp_time = time.time()
    nbody(100,'sun',20000,BODIES)
    print("time is ",time.time()-temp_time)