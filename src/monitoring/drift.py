<<<<<<< HEAD

=======
>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
from scipy.stats import ks_2samp

def detect_drift(df_old, df_new):
    drift_report = {}

    for col in df_old.select_dtypes(include='number').columns:
        stat, p_value = ks_2samp(df_old[col].dropna(), df_new[col].dropna())

        drift_report[col] = {
            "p_value": p_value,
            "drift_detected": p_value < 0.05
        }

    return drift_report
<<<<<<< HEAD

=======
>>>>>>> c4b2cc020bf3aed33d1cb5d33b4d0aec10260f6a
