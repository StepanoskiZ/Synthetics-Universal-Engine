import numpy as np


def gaia_wide_binary_test():
    r = 10000 * 1.496e11
    M_total = 2 * 1.989e30
    G = 6.67430e-11
    S = 8.74e-10

    # Newton
    a_n = (G * M_total) / (r ** 2)

    # S-OS Interpolation (Spherical Horizon Correction)
    a_sos = a_n * np.sqrt(1 + (S / (4 * np.pi)) / a_n)

    v_n = np.sqrt(a_n * r)
    v_sos = np.sqrt(a_sos * r)

    boost = (v_sos / v_n - 1) * 100

    print(f"--- GAIA WIDE-BINARY TEST (10,000 AU) ---")
    print(f"Newtonian Velocity: {v_n:.2f} m/s")
    print(f"S-OS Velocity:      {v_sos:.2f} m/s")
    print(f"Velocity Boost:     {boost:.1f}%")


gaia_wide_binary_test()
