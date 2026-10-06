import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import alpha, e, eV

class ResonantUniverseTheory:
    def __init__(self):
        # Фундаментальная постоянная тонкой структуры
        self.alpha = alpha  # ~ 1 / 137.035999
        
        # Вычисление Квантового Угла Стабильности Psi_p из тождества cos^2(Psi_p) = 2 * pi * alpha
        self.cos2_psi = 2 * np.pi * self.alpha
        self.psi_p_rad = np.arccos(np.sqrt(self.cos2_psi))
        self.psi_p_deg = np.degrees(self.psi_p_rad)
        
        # Базовые массы покоя (электрон в МэВ)
        self.m_e_MeV = 0.51099895

    def cascade_operator(self, n, sector='charged_leptons'):
        """
        Единый каскадный оператор RUT:
        m_n = C_n * m_0 * n * [1 / (2*pi*alpha)]^(n-1) * (1 - alpha / (pi * n))
        """
        if n > 3:
            raise ValueError("n >= 4 топологически запрещено в 6D пространстве RUT!")
            
        # Геометрические факторы C_n для разных секторов
        if sector == 'charged_leptons':
            C_n = {1: 1.0, 2: 1.5, 3: 2.5}[n]
            m_0 = self.m_e_MeV
            factor_damping = 1.0  # Есть поперечные ЭМ моды
        elif sector == 'neutrinos':
            C_n = {1: 0.5, 2: 0.75, 3: 1.25}[n]
            m_0 = self.m_e_MeV
            # Топологический seesaw-фактор для нейтральных частиц: cos^4(Psi_p) = (2*pi*alpha)^2
            factor_damping = self.cos2_psi**2  
        else:
            raise ValueError("Неизвестный сектор")

        # Базовое каскадное масштабирование
        scale = (1.0 / (2 * np.pi * self.alpha)) ** (n - 1)
        correction = 1.0 - (self.alpha / (np.pi * n))
        
        mass = C_n * m_0 * n * scale * correction * factor_damping
        return mass

    def plot_phase_portrait(self):
        """Построение фазового портрета аттрактора вакуумной стабильности"""
        psi = np.linspace(0, np.pi/2, 1000)
        # Потенциальная функция фазового резонатора V(Psi) = (cos^2(Psi) - 2*pi*alpha)^2
        V = (np.cos(psi)**2 - 2 * np.pi * self.alpha)**2
        dV_dpsi = -2 * (np.cos(psi)**2 - 2 * np.pi * self.alpha) * np.sin(2 * psi)

        plt.figure(figsize=(10, 5))
        plt.plot(np.degrees(psi), V, label=r'Потенциал фазового вакуума $V(\Psi)$', color='navy', lw=2)
        plt.axvline(self.psi_p_deg, color='red', linestyle='--', label=f'Аттрактор $\Psi_p \\approx {self.psi_p_deg:.3f}^\circ$')
        plt.title('Фазовый портрет устойчивости вакуумного резонатора RUT', fontsize=12)
        plt.xlabel('Фазовый угол $\Psi$ (градусы)', fontsize=11)
        plt.ylabel('Потенциальная энергия $V(\Psi)$', fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.show()

# Запуск расчета
rut = ResonantUniverseTheory()

print(f"--- Вычисленный угол стабильности Psi_p: {rut.psi_p_deg:.5f}° ---")
print(f"Мюон (n=2): {rut.cascade_operator(2, 'charged_leptons'):.4f} МэВ (PDG: 105.6584 МэВ)")
print(f"Тау-лептон (n=3): {rut.cascade_operator(3, 'charged_leptons'):.2f} МэВ (PDG: 1776.86 МэВ)")
print(f"Электронное нейтрино (n=1): {rut.cascade_operator(1, 'neutrinos') * 1e6:.4f} эВ (KATRIN bound: < 0.8 эВ)")

# Отрисовка фазового портрета
rut.plot_phase_portrait()
