import numpy as np

G = 6.67430e-11
S = 8.74e-10
M_SUN = 1.989e30
KPC = 3.086e19


def calculate_galactic_v(distance, mass):
    # Geometrijski faktor za S-OS Informacioni Horizont (4*pi)
    # Ovo je površina sfere procesorskog manifolda
    S_eff = S / (4 * np.pi)

    # Newton (Logic 1.0)
    v_n = np.sqrt((G * mass) / distance)

    # S-OS Flat Velocity (Logic 0.5)
    # Formula izvedena iz Appendixa K: v = (G * M * S_eff)^0.25
    v_flat = (G * mass * S_eff) ** 0.25

    # Ukupna S-OS brzina
    v_total = np.sqrt(v_n ** 2 + v_flat ** 2)

    return v_n / 1000, v_total / 1000


# Test za M33 (15 kpc, masa ~1.2e10 M_sun)
v_newton, v_sos = calculate_galactic_v(15 * KPC, 1.2e10 * M_SUN)

print(f"--- M33 GALAXY ROTATION (S-OS v1.9.2 FINAL) ---")
print(f"Newtonian (No Dark Matter): {v_newton:.2f} km/s")
print(f"S-OS Predicted (Logic 0.5): {v_sos:.2f} km/s (Target: ~105-115 km/s)")
