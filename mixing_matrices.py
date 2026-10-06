import numpy as np

class RUTMixingMatrices:
    def __init__(self, psi_p_deg=77.638):
        self.alpha = 1.0 / 137.035999
        self.cos2_psi = 2 * np.pi * self.alpha
        self.psi_p = np.radians(psi_p_deg)
        
        # Массы RUT (МэВ)
        self.m_u, self.m_c = 2.16, 1270.0
        self.m_d, self.m_s = 4.67, 93.4

    def calculate_ckm_cabibbo(self):
        """Угол Кабиббо theta_12 из фазовой разности d/s и u/c секторов"""
        # Фазовый угол взаимодействия down-сектора и up-сектора
        phi_d_s = np.arcsin(np.sqrt(self.m_d / self.m_s))
        phi_u_c = np.arcsin(np.sqrt(self.m_u / self.m_c))
        
        # Полный угол Кабиббо как разность/сумма фазовых проекций
        theta_C_rad = phi_d_s - phi_u_c * np.cos(self.psi_p)
        theta_C_deg = np.degrees(theta_C_rad)
        sin_theta_C = np.sin(theta_C_rad)
        
        return theta_C_deg, sin_theta_C

    def calculate_pmns_matrix(self):
        """Полная матрица PMNS с учетом 6D фазовой намотки"""
        theta_12 = np.degrees(np.arcsin(np.sqrt(1/3))) # ~ 35.3°
        theta_23 = 45.0                                 # 45.0°
        
        # Проекция n=1 -> n=3 через диагональное сечение гиперкуба sqrt(pi * alpha)
        theta_13 = np.degrees(np.arcsin(np.sqrt(np.pi * self.alpha))) # ~ 8.71°
        return theta_12, theta_23, theta_13

    def display_results(self):
        theta_C, sin_C = self.calculate_ckm_cabibbo()
        t12_p, t23_p, t13_p = self.calculate_pmns_matrix()

        print("=" * 65)
        print("    УТОЧНЕННЫЙ РАСЧЕТ УГЛОВ СМЕШИВАНИЯ CKM / PMNS (RUT 5.3)")
        print("=" * 65)
        print(f"1. КВАРКОВЫЙ СЕКТОР (Угол Кабиббо theta_12):")
        print(f"   RUT расчет:  {theta_C:.2f}°  (sin theta_12 = {sin_C:.4f})")
        print(f"   Эксперимент: ~ 13.04° (sin theta_12 = 0.2257)")
        print("-" * 65)
        print(f"2. НЕЙТРИННЫЙ СЕКТОР (Матрица PMNS):")
        print(f"   theta_12 (Солнечный):   RUT = {t12_p:.1f}° | Эксперимент = 33.4° ± 0.8°")
        print(f"   theta_23 (Атмосферный): RUT = {t23_p:.1f}° | Эксперимент = 45.0° ± 1.5°")
        print(f"   theta_13 (Реакторный):  RUT = {t13_p:.2f}° | Эксперимент = 8.57° ± 0.12°")
        print("=" * 65)

if __name__ == "__main__":
    rut_mix = RUTMixingMatrices()
    rut_mix.display_results()
