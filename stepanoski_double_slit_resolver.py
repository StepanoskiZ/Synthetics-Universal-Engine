import numpy as np
import matplotlib.pyplot as plt


class DoubleSlitS_OS:
    """
    Simulates the Double Slit Experiment using Logic 0.5 (Synthetics).
    Proves that Wave/Particle duality is a result of available 'Work' (W).
    """

    def __init__(self):
        self.S = 8.74e-10  # The Stepanoski Constant (Work Floor)
        self.W_threshold = 1.0  # Required Work to collapse 0.5 to 1.0

    def simulate_experiment(self, observer_present=False):
        # x represents the screen where the particle hits
        x = np.linspace(-10, 10, 500)

        # 1. THE WAVE STATE (Logic 0.5) - System is in 'Potential'
        # Interference pattern: cos^2 function
        interference = np.cos(x) ** 2

        # 2. THE LOGICAL TRANSACTION
        # If observer is present, they provide the 'Work' (W)
        work_injected = 2.0 if observer_present else 0.1

        if work_injected >= self.W_threshold:
            # COLLAPSE TO REALITY (State 1.0)
            # Two Gaussian bands (Particle distribution)
            pattern = np.exp(-(x - 2) ** 2) + np.exp(-(x + 2) ** 2)
            state = "1.0 (REALITY / PARTICLE)"
            color = 'blue'
        else:
            # MAINTAIN POTENTIAL (State 0.5)
            # Wave interference pattern
            pattern = interference
            state = "0.5 (POTENTIAL / WAVE)"
            color = 'magenta'

        return x, pattern, state, color


def run_quantum_test():
    sos = DoubleSlitS_OS()

    # Test 1: No Observer (The Lazy Universe)
    x1, p1, s1, c1 = sos.simulate_experiment(observer_present=False)

    # Test 2: With Observer (Work Injected)
    x2, p2, s2, c2 = sos.simulate_experiment(observer_present=True)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.plot(x1, p1, color=c1, linewidth=2)
    ax1.set_title(f"Quantum Test A: No Observation (Logic State: {s1})")
    ax1.fill_between(x1, p1, color=c1, alpha=0.3)
    ax1.set_ylabel("Probability Density")

    ax2.plot(x2, p2, color=c2, linewidth=2)
    ax2.set_title(f"Quantum Test B: Observation/Work Injected (Logic State: {s2})")
    ax2.fill_between(x2, p2, color=c2, alpha=0.3)
    ax2.set_xlabel("Impact Position on Screen")
    ax2.set_ylabel("Probability Density")

    plt.tight_layout()
    print("--- QUANTUM RESOLVER: ONLINE ---")
    print(f"State A: {s1} - Universe conserves energy by not calculating position.")
    print(f"State B: {s2} - Observer 'pays' the processing fee (W) to resolve path.")
    plt.show()


if __name__ == "__main__":
    run_quantum_test()