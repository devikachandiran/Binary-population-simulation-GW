# Step 1: Imports & Constants
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G, c

# Create results folder
os.makedirs("results", exist_ok=True)

# Physical constants
YEAR = 365.25 * 24 * 3600        # seconds in a year
MSUN = 1.98847e30                # kg
RSUN = 6.957e8                   # meters

plt.rcParams.update({'figure.figsize': (7, 5), 'axes.grid': True})
print("Environment ready ✅")

# Step 2: Sample random binary systems
def sample_m1(size, mmin=5, mmax=40, alpha=2.35):
    """Draw primary masses from a simple Salpeter power law."""
    r = np.random.rand(size)
    a1 = 1 - alpha
    return ((r * (mmax**a1 - mmin**a1) + mmin**a1)) ** (1 / a1)

N = 5000
m1 = sample_m1(N)
q = np.random.uniform(0.3, 1.0, N)        # mass ratio
m2 = q * m1
a0 = np.exp(np.random.uniform(np.log(1), np.log(100), N))   # separation in R_sun

print(f"Generated {N} binaries ✅")
print("Example:", list(zip(m1[:3], m2[:3], a0[:3])))

# Step 3: Compute merger times using Peters (1964)
def merger_time_s(m1_msun, m2_msun, a0_rsun):
    """Merger time in seconds for circular binaries."""
    m1, m2, a0 = m1_msun * MSUN, m2_msun * MSUN, a0_rsun * RSUN
    num = 5 * c**5 * a0**4
    den = 256 * G**3 * m1 * m2 * (m1 + m2)
    return num / den

tmerge_s = merger_time_s(m1, m2, a0)
tmerge_yr = tmerge_s / YEAR

# Fraction merging within Hubble time
HUBBLE_TIME_YR = 13.8e9
fraction = np.mean(tmerge_yr < HUBBLE_TIME_YR)
merge_mask = tmerge_yr < HUBBLE_TIME_YR

print(f"Fraction merging within Hubble time: {fraction:.2%}")

# Step 4: Compute chirp masses
def chirp_mass(m1, m2):
    M = m1 + m2
    return (m1 * m2)**(3/5) / (M**(1/5))

chirp = chirp_mass(m1, m2)

# Step 5: Make plots
plt.figure()
plt.scatter(m1, m2, s=4, alpha=0.4)
plt.xlabel("m1 [Msun]")
plt.ylabel("m2 [Msun]")
plt.title("Component Masses (All Systems)")
plt.tight_layout()
plt.savefig("results/mass_scatter.png", dpi=160)
plt.show()

# 2️⃣ Merger-Time Distribution (within 13.8 Gyr) 
plt.figure()
plt.hist(np.log10(tmerge_yr[merge_mask]), bins=40)
plt.xlabel("log10 Merger Time [years]")
plt.ylabel("Count")
plt.title("Merger-Time Distribution (within 13.8 Gyr)")
plt.tight_layout()
plt.savefig("results/merger_times_hist.png", dpi=160)
plt.show()

# 3️⃣ Chirp Mass vs Merger Time (Mergers only) 
plt.figure()
plt.scatter(tmerge_yr[merge_mask], chirp[merge_mask], s=6, alpha=0.7)
plt.xscale("log")
plt.xlabel("Merger Time [years] (log scale)")
plt.ylabel("Chirp Mass [Msun]")
plt.title("Chirp Mass vs Merger Time (Mergers only)")
plt.tight_layout()
plt.savefig("results/chirp_vs_tmerge.png", dpi=160)
plt.show()

